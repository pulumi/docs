---
title: "Configure AWS credentials"
---

To target AWS in a Pulumi program, you will need to configure your system
so that Pulumi can communicate with AWS.  Pulumi does not store this information anywhere, and these credentials
must include sufficient IAM rights to deploy and manage resources in your AWS account.

The easiest way to configure your AWS credentials is to simply set the `AWS_ACCESS_KEY_ID` and
`AWS_SECRET_ACCESS_KEY` environment variables to the values given to you in the IAM console.  For example,
on macOS or Linux:

```bash
$ export AWS_ACCESS_KEY_ID=AK**************WORA
$ export AWS_SECRET_ACCESS_KEY=7n******************************6eLEKd8G
```

Of course the `**` strings should be replaced with your own credentials.

Alternatively, you can install the [AWS CLI](http://docs.aws.amazon.com/cli/latest/userguide/installing.html) and use
it to configure your IAM credentials locally on your machine.  These will be stored and cached in your home directory:

```bash
$ aws configure
AWS Access Key ID [AK**************WORA]:
AWS Secret Access Key [7n******************************6eLEKd8G]:
Default region name [us-west-2]:
Default output format [None]:
```

In general, you can use any of the other configuration options documented on the [AWS SDK website](
http://docs.aws.amazon.com/sdk-for-go/v1/developer-guide/configuring-sdk.html).
