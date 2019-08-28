---
title: "AWS Step Functions"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-ts-stepfunctions" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/aws-ts-stepfunctions" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


A basic example that demonstrates using AWS Step Functions with a Lambda function.

```
# Create and configure a new stack
$ pulumi stack init stepfunctions-dev
$ pulumi config set aws:region us-east-2

# Install dependencies
$ npm install

# Preview and run the deployment
$ pulumi up

# Start execution using the AWS CLI (or from the console at https://console.aws.amazon.com/states)
$ aws stepfunctions start-execution --state-machine-arn $(pulumi stack output stateMachineArn)

# Remove the app
$ pulumi destroy
```
