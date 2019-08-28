---
title: "AWS Step Functions (Python)"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-py-stepfunctions" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/aws-py-stepfunctions" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


A basic example that demonstrates using AWS Step Functions with a Lambda function, written in Python.

```
# Install dependencies
$ pip install -r ./requirements.txt

# Create and configure a new stack
$ pulumi stack init stepfunctions-dev
$ pulumi config set aws:region us-east-2

# Preview and run the deployment
$ pulumi up

# Start execution using the AWS CLI (or from the console at https://console.aws.amazon.com/states)
$ aws stepfunctions start-execution --state-machine-arn $(pulumi stack output state_machine_arn)

# Remove the app and its stack
$ pulumi destroy && pulumi stack rm -y
```

