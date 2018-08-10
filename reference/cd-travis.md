---
title: Travis CI
---

This page details how to use [Travis CI](https://travis-ci.com/) to manage deploying separate
staging and production stacks based on commits to specific Git branches. This is sometimes
referred to as Push-to-Deploy.

Pulumi doesn't require any particular arrangement of stacks or git workflow to work in a
continuous integration / continuous deployment system. So the steps described here can be
altered to fit into any existing type of deployment setup.

## Stack and Branch Mappings

The scripts below act on two hypothetical stacks: `acme/website-staging` and
`acme/website-production`. The source code for both stacks are in the same repository. And we will
update the `website-staging` stack whenever code is pushed into the `master` branch, and update the
`website-production` stack whenever code is pushed into the `production` branch.

We will also run previews of infrastructure changes for pull requests into `master` and
`production` branches, to identify an potentially impactful changes before they get merged.

## Configuring Travis

To support this deployment strategy, you need to enable Travis to create both `push` and
`pull_request` jobs. In the Travis UI, this is done by checking the "Build pushed branches" and
"Build pushed pull requests" options.

`push` jobs are created when a Git push is made to a branch. We configure the build script for
`push` jobs to run `pulumi update`, i.e. carry out the push-to-deploy operation.

`pull_request` jobs are created when a push is made to a _pull request topic branch_. (That same
push will also trigger a separate `push` job.) We configure the `pull_request` job to run
`pulumi preview` to see any infrastructure changes that would happen as _a result of_ the pull
request being merged.

### Environment Variables

To use Pulumi within Travis CI, there are a few environment variables you'll need to set for each
build.

The first is `PULUMI_ACCESS_TOKEN`, which is required to authenticate with pulumi.com in order to
perform the preview or update. You can create a new Pulumi access token specifically for your
CI/CD job on your [Pulumi Account page](https://app.pulumi.com/account/tokens).

Next, you will also need to set environment variables specific to your cloud resource provider.
For example, if your stack is managing resources on AWS, `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY`.

## Scripts

With Travis configured, we then just need to add three files to the repository:
`.travis.yml`, `scripts/travis_push.sh`, and `scripts/travis_pull_request.sh`. (Though of course
you are free to rename and/or move these files to whatever makes sense in your repo.)

The following is a minimal `.travis.yml`, which describes the steps Travis CI will perform as part
of building the repository. Before the build begins, Travis will download the Pulumi CLI and then
run `pulumi login`. (Which will use `PULUMI_ACCESS_TOKEN` mentioned earlier.)

Then Travis runs whatever build script matches the job type, since we want to have different
behavior for `push` jobs vs. `pull_request`.

```yaml
language: generic
before_install:
  - curl -L https://get.pulumi.com/ | bash -s -- --version 0.14.3
  - export PATH=$PATH:$HOME/.pulumi/bin
  - pulumi login
script:
  - ./scripts/travis_${TRAVIS_EVENT_TYPE}.sh
```

`scripts/travis_push.sh` is the script that is executed on `push` jobs. And for the push-to-deploy stategy,
is when we will run `pulumi update`. For `push` jobs, the `TRAVIS_BRANCH` environment variable is the
pushed branch. So we use that to determine which stack to update, e.g. pushes to `master` update the
staging stack and `production` update the production stack.

```bash
echo "Travis push job"

# Download dependencies and build
npm install
npm run build

# Update the stack
case ${TRAVIS_BRANCH} in
    master)
        pulumi stack select acme/website-staging
        pulumi update --yes
        ;;
    production)
        pulumi stack select acme/website-production
        pulumi update --yes
        ;;
    *)
        echo "Push to non-master branch. No stacks to update."
        ;;
esac
```

`scripts/travis_pull_request.sh` is triggered on pushes to a pull request branch. For these jobs
the meaning of `TRAVIS_BRANCH` is the branch being _targeted_ by the pull request.

So if the pull request is going to be merged into the `master` branch, then we would want to
preview the changes that would be made to the staging stack. For pull requests targeting the
`production` branch, we want to preview the production stack.

```bash
echo "Travis pull_request job"

# Download dependencies and build
npm install
npm run build

# Preview changes that would be made if the PR were merged.
case ${TRAVIS_BRANCH} in
    master)
        pulumi stack select acme/website-staging
        pulumi preview
        ;;
    production)
        pulumi stack select acme/website-production
        pulumi preview
        ;;
    *)
        echo "Pull Request to be merged into unknown branch. No stacks to preview."
        ;;
esac
```

## Concurrency

When using Travis to continuously deploy your Pulumi stacks, you may run into a problem. What
happens if there are multiple commits merged into the `master` branch in rapid succession?

Travis will trigger multiple `push` jobs, which will then both try to run `pulumi update` on the
same stack at the same time.

Pulumi prevents any stack updates while one is already in progress. (To avoid conflicting resource
updates and/or corrupting resource state.) So the stack and its resources won't be harmed by the
concurrent update, but it will likely fail your Travis build.

There are a few ways to address this, such as preventing Travis from starting concurrent builds.
However, the recommended way to deal with this is to use the [travisqueue](https://github.com/pulumi/travisqueue)
tool.

`travisqueue` is a tool that you can add to your `.travis.yml` file to limit build concurrency on
a per-branch basis. This allows you to limit the number of concurrent builds for any branches that
are configured to perform a Pulumi update, for example.

See the [README.md](https://github.com/pulumi/travisqueue/blob/master/README.md) file for more
information on how it works, and will effectively queue / restart builds for a repo that were
cancelled.
