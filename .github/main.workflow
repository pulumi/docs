workflow "Pulimify" {
    on = "pull_request"
    resolves = [ "Publish Live Preview" ]
}

action "Publish Live Preview" {
    uses = "./.github/action"
    env = {
        "PULUMIFY_BUILD" = "make ensure && hugo --buildFuture -e $GITHUB_SHA",
        "PULUMIFY_ROOT" = "public"
    }
    secrets = [
        "GITHUB_TOKEN",
        "PULUMI_ACCESS_TOKEN",
        "AWS_ACCESS_KEY_ID",
        "AWS_SECRET_ACCESS_KEY"
    ]
}
