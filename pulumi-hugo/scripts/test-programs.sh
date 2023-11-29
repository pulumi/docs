#!/bin/bash

set -euo pipefail

pulumi whoami -v

# Delete build/test artifacts.
git clean -fdX themes/default/static/programs

pushd themes/default/static/programs
    for dir in */; do
        project="$(basename $dir)"


        echo "***"
        echo "* $project"
        echo "***"

        org="$(pulumi whoami -v --json | jq -r .user)"
        stack="dev"
        fqsn="${org}/${project}/${stack}"

        # Install dependencies.
        pulumi -C "$project" install

        # Skip certain programs known not to work.

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

        # Delete any existing Docker images.
        # docker rmi -f "$(docker images -aq)" || true

        # Create a new stack.
        pulumi -C "$project" stack select $fqsn || pulumi -C "$project" stack init $fqsn
        pulumi -C "$project" config set aws:region us-west-2 || true

        # Preview or deploy.
        if [[ "$1" == "update" ]]; then
            pulumi -C "$project" up --yes
        else
            pulumi -C "$project" preview
        fi

        # Destroy and remove.
        pulumi -C "$project" destroy --yes --remove

    done
popd

# Delete build/test artifacts.
git clean -fdX themes/default/static/examples
