---
title: "AWS Step Functions"
---

<p class="mb-4 flex">
    <a class="flex flex-wrap items-center rounded text-xs text-white bg-blue-600 border-2 border-blue-600 px-2 mr-2 whitespace-no-wrap hover:text-white" style="height: 32px" href="https://github.com/pulumi/examples/tree/master/aws-ts-stepfunctions" target="_blank">
        <span><i class="fab fa-github pr-2"></i> View Code</span>
    </a>

    <a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-ts-stepfunctions" target="_blank">
        <img src="https://get.pulumi.com/new/button.svg" alt="Deploy">
    </a>
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
