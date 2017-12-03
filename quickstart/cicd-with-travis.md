---
layout: default 
nav_section: "quickstart"
type: tutorial
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>CI/CD with Travis</b></p>

# CI/CD of Pulumi Programs using Travis

This tutorial walks through configuring a Pulumi applications to be
continuously deployed using the Pulumi Cloud Mangement Console and [Travis CI](https://travis-ci.com/).

## Requirements

To begin, you'll need the following:

1. An existing Travis job. If you aren't already a Travis user, check out their
   [getting started](https://docs.travis-ci.com/user/getting-started/) guide.
1. You _Pulumi Access Token_. It is listed on your [account page](https://beta.pulumi.com/account)
   on the Pulumi Cloud Management Console.
1. A Pulumi program already deployed to the Pulumi Console. For more information on deploying
   Pulumi programs to the cloud management console, see our [quickstart guide](/quickstart/console.html).

## Script

The following Bash script is all you'll need to do continuous deliver with Travis. After every push
to the `master` branch of your Git repository, the testing instance of your Pulumi program will be
updated. And every push to the `production` branch will update your production instance.


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
# TODO: and CD into the Pulumi program's directory.
# $ make build
# $ cd tool/pulumi

set -e
pulumi login

pulumi init
pulumi stack select $PULUMI_STACK_NAME

echo "Running pulumi preview:"
pulumi preview

echo "Running pulumi update:"
pulumi update
```

## EnvVar Checks

Travis defines [several environment variables](https://docs.travis-ci.com/user/environment-variables/#Default-Environment-Variables)
when it starts your job. The script first inspects `$TRAVIS_EVENT_TYPE` and ignores everything but
"push" events. It then looks at the specific `$TRAVIS_BRANCH` variable to see if it is one of the
branches we wish to associate with a Pulumi program.

## Pulumi login

To access the Pulumi Service, you need to first login. The `login` command does not accept a
command-line flag with the access token, instead it looks in an environment variable named
`PULUMI_ACCESS_TOKEN`.

You can add your Pulumi access token to your Travis job's settings. Given its sensitive nature,
be sure _not_ to display the value in the build log.

![adding-travis-setting](/images/tutorial-travis/01-add-travis-envvar.png)

## Pulumi init and stack select

Once logged into Pulumi, you'll then need to select the program you wish to deploy. This is done
through the two commands: `pulumi init` and `pulumi stack select`.

`pulumi init` initializes the local Pulumi workspace. Most importantly, it sets the current
_organization_ and _repository_. These are values used to identify the Pulumi program to deploy.

`pulumi stack select` selects the Pulumi stack you wish to update. Since the stack name
"chris-test" is probably not globally unique, the organization, repository, and project name
(from `Pulumi.yaml`) are used to uniquely identify the stack.

The script above assumes the name of the stacks to be updated are "testing-stack" and
"production-stack", but you'll likely have used different values.

## Pulumi preview and update

To update your program, all you need to do is run `pulumi update`. However for production
environments, it is recommended you run `pulumi preview` first.

`pulumi preview` executes the Pulumi program but doesn't modify any cloud resources. By running
`pulumi preview` before updating, you can safely check for certain classes of runtime error.

That's it! The next time Travis starts a "push" job for the "master" or "production" branch,
your corresponding Pulumi stack will be updated.
