#!/bin/bash
set -exuo pipefail

# This is the Pulumify GitHub Action container's entrypoint. It does the following:
#
#     * Anytime a pull request for a branch is updated (opened/edited/synchronized/etc),
#       the script checks for a Pulumi stack with the branch's name (with appropriate character
#       substitution to avoid illegal Pulumi stack names).
#
#         - The first time this branch is detected, a new stack is created.
#
#         - After that, and on all subsequent updates, that stack is updated. The Pulumi program
#           uses AWS S3 to host a static website, serving the specified content. This program uses
#           a configurable location in the Git repo (specified by PULUMIFY_ROOT).
#
#         - Each time an update is made, a comment is left behind on the pull request, with a URL.
#
#     * Upon closure of the pull request (e.g., due to merging), the branch is deleted.
#
# This allows easy review of static website changes in line with GitHub pull request workflows.

# See if we have the requisite credentials. If not, we might be in a fork. Exit cleanly.
if [ -z "${AWS_ACCESS_KEY_ID:-}" ] || [ -z "${AWS_SECRET_ACCESS_KEY:-}" ] || [ -z "${PULUMI_ACCESS_TOKEN:-}" ]; then
    echo "# Missing secret tokens -- possibly due to a forked PR -- skipping"
    exit
fi

# Set up some variables so that the Pulumi CLI knows it's running in the context of GitHub.
if [ ! -z "$GITHUB_WORKFLOW" ]; then
    export PULUMI_CI_SYSTEM="GitHub"
    export PULUMI_CI_BUILD_ID=
    export PULUMI_CI_BUILD_TYPE=
    export PULUMI_CI_BUILD_URL=
    export PULUMI_CI_PULL_REQUEST_SHA="$GITHUB_SHA"
fi

# Detect what action is being taken. If it's a PR that's been edited, we will preview the changes;
# if it's a "close" or branch deletion, we will delete the stack; otherwise, we exit cleanly because
# there's nothing to do.
case "$GITHUB_EVENT_NAME" in
    "pull_request")
        # Extract PR attributes.
        GH_PR_ACTION=$(cat "$GITHUB_EVENT_PATH" | jq -r ".action")
        GH_PR_NUMBER=$(cat "$GITHUB_EVENT_PATH" | jq -r ".number")
        GH_BRANCH=$(cat "$GITHUB_EVENT_PATH" | jq -r ".pull_request.head.ref")
        echo "# PR #$GH_PR_NUMBER, action '$GH_PR_ACTION', branch $GH_BRANCH"
        # Switch on the action type to determine how to proceed.
        case "$GH_PR_ACTION" in
            "opened" | "reopened" | "synchronize")
                PULUMI_UPDATE=true
                ;;
            "closed")
                PULUMI_UPDATE=false
                ;;
            *)
                echo "# Nothing to do for '$GH_PR_ACTION' action"
                exit
                ;;
        esac
        ;;
    "delete")
        # Extract deletion attributes.
        GH_BRANCH=$(cat "$GITHUB_EVENT_PATH" | jq -r ".ref")
        echo "# Branch deletion for $GH_BRANCH"
        # For branch deletions, always delete the branch.
        PULUMI_UPDATE=false
        ;;
esac

# Extract the branch name and clean it to produce a stack name.
PULUMI_STACK_NAME=$(echo "pulumify_${GITHUB_REPOSITORY}_${GH_BRANCH}" | sed "s/[^[:alnum:].-]/-/g")

if [ ! -z "${PULUMIFY_ORGANIZATION:-}" ]; then
    # If an organization stack is requested, put the stack under the organization.
    PULUMI_STACK_NAME=$PULUMIFY_ORGANIZATION/$PULUMI_STACK_NAME
fi
echo "# PR stack name: $PULUMI_STACK_NAME"

# Now attempt to change to the desired stack. Ignore errors, we'll check the result later.
pulumi stack select $PULUMI_STACK_NAME >/dev/null 2>&1 && \
    PULUMI_STACK_EXISTS=$? || PULUMI_STACK_EXISTS=$?

# Ensure we refresh the configuration if the stack actually exists.
if [ $PULUMI_STACK_EXISTS -eq 0 ]; then
    pulumi config refresh -f
fi

# Now actually perform the desired action (either update or removal).
if [ "$PULUMI_UPDATE" = true ]; then
    echo "# Updating ..."

    # If the stack doesn't exist yet, create it.
    if [ $PULUMI_STACK_EXISTS -ne 0 ]; then
        pulumi stack init $PULUMI_STACK_NAME
        pulumi config set root $GITHUB_WORKSPACE/${PULUMIFY_ROOT:-public}
        pulumi config set aws:region ${AWS_REGION:-us-east-1}
    fi

    # Now simply run an update to provision and/or update the static website.
    pulumi up --skip-preview

    # Next, post a comment to the PR that directs the user to the resulting bucket URL.
    # TODO(joe): recognize failures?
    PR_COMMENT_API_LINK=$(cat "$GITHUB_EVENT_PATH" | jq -r ".pull_request._links.comments.href")
    curl -X POST -H "Authorization: token $GITHUB_TOKEN" \
        -d "{ \"body\": \"Your [site preview]($(pulumi stack | grep -oE "https://.*")) for commit **${GITHUB_SHA:0:7}** is now available! :tropical_drink:\n\n<$(pulumi stack output url)>\n\n_Deploy previews powered by [Pulumify](https://github.com/pulumi/actions-pulumify)_\" }" \
        $PR_COMMENT_API_LINK
else
    echo "# Destroying ..."

    # If the stack doesn't even exist, there's nothing to do. Otherwise, we must destroy and then
    # remove the resulting stack altogether.
    if [ $PULUMI_STACK_EXISTS -eq 0 ]; then
        pulumi destroy --skip-preview
        pulumi stack rm --yes
    else
        echo "# Already destroyed -- nothing more to do"
    fi
fi
