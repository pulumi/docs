#!/bin/bash

set -o errexit -o pipefail

source ./scripts/programs/common.sh

# The directory containing the example code programs to test.
programs_dir="static/programs"

# Directories that need to be tested
dirs_to_test=( $(find "${programs_dir}" -maxdepth 1 -type d -not -path '*/\.*' -not -path "${programs_dir}") )
# Track projects that failed tests
failed_projects=()
# Track projects that passed tests
passing_projects=()

# Get the list of changed directories in the static/programs directory. 
if [[ "$TEST_MODE" == "pull_request" ]]; then

    # Clear the dirs_to_test array  
    dirs_to_test=()
    # Get the list of changed directories in the static/programs directory.
    git_changes="$(git diff --name-only master)"
    # Filter out only the static/programs directories from the git diff output.
    # Use or true to ignore grep errors when grep comes up empty.
    grep_result="$(echo "$git_changes" | grep "^static/programs/" || true)"
    # Extract only the program directory from the git diff output.
    dirs="$(echo "$grep_result" | cut -d'/' -f3)"
    # Pipe to sort and uniq to deduplicate the list of directories.
    programs="$(echo "$dirs" | sort | uniq)"
    
    # If there are programs to test, add them to the dirs_to_test array.
    if [[ -n "$programs" ]]; then
        while IFS= read -r line; do
            dirs_to_test+=("$line")
        done <<< "$programs"
    fi

    echo "Number of programs to test: ${#dirs_to_test[@]}"

    # Check if the array is empty and if it is exit.
    if [[ ${#dirs_to_test[@]} -eq 0 ]]; then
        echo "No new programs to test in static/programs directories."
        exit 0
    fi
fi

# Delete install artifacts.
git clean -fdX "${programs_dir}/*"

# Fix up go.mod files.
clean_gomods

# By default, only run previews.
mode="${1:-preview}"

# If we're only running previews, just use local mode -- it's faster.
if [[ "$mode" == "preview" ]]; then
    org="organization"
    export PULUMI_CONFIG_PASSPHRASE="foo"
    pulumi login --local
else
    org="$(pulumi whoami -v --json | jq -r .user)"
fi

# The ignore file contains a list of programs to skip.
ignore_file="$(pwd)/scripts/programs/ignore.txt"

pushd "$programs_dir"
    found_first_program=false

    # Iterate over the dirs_to_test array and test each program.
    for dir in "${dirs_to_test[@]}"; do
        project="$(basename $dir)"

        # Skip programs listed in the ignore.txt file
        if [ -f "${ignore_file}" ]; then
            # yes this is a nested loop, but in practice it accounts for a negligible amount of time
            # compared to the rest of the overall test process.
            while IFS= read -r pattern; do
                # Skips empty lines and comments to allow for comments in the ignore.txt file.
                [[ -z "$pattern" || "$pattern" =~ ^[[:space:]]*# ]] && continue
                
                if [[ "$project" =~ ^${pattern}$ ]]; then
                    echo "Skipping ${project} (matches '${pattern}' in ignore.txt file)"
                    # continue 2 means exit this loop as well as the outer loop.
                    continue 2
                fi
            done < "${ignore_file}"
        fi

        # Optionally test only selected examples by setting an ONLY_TEST="<example-path>"
        # environment variable (e.g., ONLY_TEST="awsx-ecr-repository").
        if [[ ! -z "$ONLY_TEST" && "$project" != "$ONLY_TEST"* ]]; then
            continue
        fi

        # Optionally test only from the specified example forward by setting ONLY_TEST_FROM="<example-path>".
        if [[ ! -z "$ONLY_TEST_FROM" ]]; then
            if [[ "$project" == "$ONLY_TEST_FROM"* && "$found_first_program" == false ]]; then
                found_first_program=true
            fi

            if [ "$found_first_program" == false ]; then
                continue
            fi
        fi

        echo
        echo "***"
        echo "* $project"
        echo "***"
        echo

        # Check for a Makefile. If one exists, run `make test`, otherwise,
        # try to run as a Pulumi program
        makefile="${project}/Makefile"
        if [ -f "${makefile}" ]; then
            echo "File ${makefile} exists. Running 'make test' in ${dir} "
            if ! make -C ${project} test; then
                failed_projects+=("$project")
                continue
            fi

            passing_projects+=("$project")
            continue
        fi

        stack="dev"
        fqsn="${org}/${project}/${stack}"

        # Install dependencies.
        if ! pulumi -C "$project" install; then
            failed_projects+=("$project")
            continue
        fi

        # Destroy any existing stacks.
        pulumi -C "$project" cancel --stack $fqsn --yes || true
        pulumi -C "$project" destroy --stack $fqsn --yes --refresh --remove || true

        # Create a new stack.
        pulumi -C "$project" stack select $fqsn || pulumi -C "$project" stack init $fqsn
        pulumi -C "$project" config set aws:region us-west-2 || true
        pulumi -C "$project" config set azure:location eastus || true
        pulumi -C "$project" config set azure-native:location eastus || true
        pulumi -C "$project" config set resourceGroupName pulumi-tutorials || true
        pulumi -C "$project" config set gcp:region us-central1 || true
        pulumi -C "$project" config set gcp:zone us-central1-a || true
        pulumi -C "$project" config set gcp:project pulumi-devrel || true

        # Preview or deploy.
        if [[ "$mode" == "update" ]]; then

            # Skip programs we know don't successfully update.

            # Error converting 'java.util.Collections$UnmodifiableRandomAccessList' to 'TypeShape{type=interface java.util.List, parameters=[TypeShape{type=class com.pulumi.aws.lb.outputs.TargetGroupTargetHealthState, parameters=[]}]}'.
            # https://github.com/pulumi/pulumi-java/issues/1276
            if [[ "$project" == "awsx-elb-web-listener-java" ]]; then
                continue
            elif [[ "$project" == "awsx-elb-multi-listener-redirect-java" ]]; then
                continue
            elif [[ "$project" == "awsx-load-balanced-ec2-instances-java" ]]; then
                continue
            fi

            if ! pulumi -C "$project" up --yes; then
                failed_projects+=("$project")
                continue
            fi
        else
            if ! pulumi -C "$project" preview; then
                failed_projects+=("$project")
                continue
            fi
        fi

        # Destroy and remove.
        pulumi -C "$project" destroy --yes --remove

        passing_projects+=("$project")
        
        # Clean up artifacts.
        git clean -fdX .
    done
popd

clean_gomods

# Log out of local mode.
if [[ "$mode" == "preview" ]]; then
    unset PULUMI_CONFIG_PASSPHRASE
    pulumi logout --local
fi

# Report passing and failing projects.
if [ ${#failed_projects[@]} -ne 0 ]; then
    echo -e "\n\nThe following projects passed:"
    for project in "${passing_projects[@]}"; do
        echo "- $project"
    done
    echo -e "\n\nThe following projects failed:"
    for project in "${failed_projects[@]}"; do
        echo "- $project"
    done
    exit 1
else
    echo "All projects passed successfully :)"
fi
