#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

pulumi whoami -v

#
# Run program tests.
#

# Delete install artifacts (but leave any existing go.mod files in place so we can use them.)
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "node_modules" | xargs rm -rf
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "venv" | xargs rm -rf
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "__pycache__" | xargs rm -rf
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "bin" | xargs rm -rf
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "obj" | xargs rm -rf
find ./themes/default/static/programs/* -type d -maxdepth 1 -name "target" | xargs rm -rf
find ./themes/default/static/programs/* -type f -maxdepth 1 -name "go.sum" | xargs rm -f

# Fix up go.mod files.
clean_gomods
unsuffix_gomods

pushd themes/default/static/programs
    for dir in */; do
        project="$(basename $dir)"

        # Optionally test only selected examples by setting an ONLY_TEST="<example-path>"
        # environment variable (e.g., ONLY_TEST="awsx-ecr-repository").
        if [[ ! -z "$ONLY_TEST" && "$dir" != "$ONLY_TEST"* ]]; then
            continue
        fi

        echo "***"
        echo "* $project"
        echo "***"

        org="$(pulumi whoami -v --json | jq -r .user)"
        stack="dev"
        fqsn="${org}/${project}/${stack}"

        # Install dependencies.
        pulumi -C "$project" install

        # Skip previews known not to work.

        # Java examples of FargateService erroneously complain about missing container declarations.
        # https://github.com/pulumi/pulumi-awsx/issues/820
        if [[ "$project" == "awsx-vpc-fargate-service-java" ]]; then
            continue
        elif [[ "$project" == "awsx-load-balanced-fargate-ecr-java" ]]; then
            continue
        elif [[ "$project" == "awsx-load-balanced-fargate-nginx-java" ]]; then
            continue
        fi

        # Destroy any existing stacks.
        pulumi -C "$project" cancel --stack $fqsn --yes || true
        pulumi -C "$project" destroy --stack $fqsn --yes --refresh --remove || true

        # Create a new stack.
        pulumi -C "$project" stack select $fqsn || pulumi -C "$project" stack init $fqsn
        pulumi -C "$project" config set aws:region us-west-2 || true

        # Preview or deploy.
        if [[ "$1" == "update" ]]; then

            # Skip updates known not to work.

            # Error converting 'java.util.Collections$UnmodifiableRandomAccessList' to 'TypeShape{type=interface java.util.List, parameters=[TypeShape{type=class com.pulumi.aws.lb.outputs.TargetGroupTargetHealthState, parameters=[]}]}'.
            # https://github.com/pulumi/pulumi-java/issues/1276
            # if [[ "$project" == "awsx-elb-web-listener-java" ]]; then
            #     continue
            # elif [[ "$project" == "awsx-elb-multi-listener-redirect-java" ]]; then
            #     continue
            # elif [[ "$project" == "awsx-load-balanced-ec2-instances-java" ]]; then
            #     continue
            # fi

            pulumi -C "$project" up --yes
        else
            pulumi -C "$project" preview
        fi

        # Destroy and remove.
        pulumi -C "$project" destroy --yes --remove

    done
popd

clean_gomods
suffix_gomods
