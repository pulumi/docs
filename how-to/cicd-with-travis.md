---
layout: default 
nav_section: "how-to"
type: tutorial
---

<p><a href="/how-to">How-to Guides</a> &gt; <b>Use Travis to continuously deploy</b></p>

# Use Travis to continuously deploy Pulumi programs

This tutorial describes how to configure a Pulumi program to be continuously built and deployed using the Pulumi service and [Travis CI](https://travis-ci.com/).

## Requirements

To begin, you'll need the following:

1. An existing Travis job. If you aren't already a Travis user, check out the 
   [Travis getting started guide](https://docs.travis-ci.com/user/getting-started/).

1. Your _Pulumi Access Token_. It is listed on your [account page](https://beta.pulumi.com/account)
   on the Pulumi Console. See documentation on the [Pulumi access token](./console.html#access-token).

1. A Pulumi program that has already been deployed to a managed stack. For more information, see [Create and work with managed stacks](./cloud-stack.html).

## Creating a Travis script

To perform continuously delivery with Travis, start with the follow bash script. This script updates the Pulumi `testing-stack` stack whenever there is a push to the `master` Git branch. Similarly, a push to the `production` branch performs an update to the `production-stack` stack.

If you're using different stack or branch names, simply change those values in the script. The sections below describe how to further customize the script.

### Sample Travis bash script

```bash
#!/bin/bash
echo "Deploying Pulumi Application via Travis"
echo "TRAVIS_BRANCH    : ${TRAVIS_BRANCH}"
echo "TRAVIS_EVENT_TYPE: ${TRAVIS_EVENT_TYPE}"

if [ "$TRAVIS_EVENT_TYPE" != "push" ]; then
    echo "Non-push event type. Ignoring."
    exit 0
fi

# Set PULUMI_STACK_NAME to be the name of the Pulumi stack you wish to update.
case "$TRAVIS_BRANCH" in
    master
        export PULUMI_STACK_NAME="testing-stack"
        ;;
    production
        export PULUMI_STACK_NAME="production-stack"
        ;;
    *)
        echo "Branch is not associated with a stack. Ignoring."
        exit 0
esac


# TODO: Build any prerequisites for your Pulumi program
#       and CD into the Pulumi program's directory.
# $ make build
# $ cd tool/pulumi

set -e
pulumi login

# Initialize the Pulumi workspace
pulumi init

# Select the Pulumi managed stack
pulumi stack select $PULUMI_STACK_NAME

echo "Running pulumi preview:"
pulumi preview

echo "Running pulumi update:"
pulumi update
```

### Environment variable checks

Travis defines [several environment variables](https://docs.travis-ci.com/user/environment-variables/#Default-Environment-Variables)
when it starts your job. The script first inspects `$TRAVIS_EVENT_TYPE` and ignores everything but
"push" events. It then looks at the specific `$TRAVIS_BRANCH` variable to see if it is one of the
branches we wish to associate with a Pulumi program.

### Pulumi login

The script first logs in to Pulumi via `pulumi login`. For security, the `login` command does not accept the Pulumi access token as a command-line flag. Instead, you must use the environment variable `PULUMI_ACCESS_TOKEN`.

You can add your Pulumi access token to your Travis job's settings. Since this secret should be protected, *never* display its value in the build log.

![adding-travis-setting](/images/tutorial-travis/01-add-travis-envvar.png)

### Pulumi init and stack select

The script also does the following:
- Runs `pulumi init` to initialize the local Pulumi workspace.
- Runs `pulumi stack` to select the desired managed stack.

### Pulumi preview and update

To update your program, all you need to do is run `pulumi update`. However for production
environments, it is recommended you run `pulumi preview` first.

The command `pulumi preview` executes the Pulumi program but doesn't modify any cloud resources. By running
`pulumi preview` before updating, you can safely check for certain classes of runtime error.

That's it! The next time Travis starts a "push" job for the "master" or "production" branch,
your corresponding Pulumi stack will be updated.
