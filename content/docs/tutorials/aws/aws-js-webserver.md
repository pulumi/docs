---
title: "AWS EC2 Web Server"
---

<a href="https://app.pulumi.com/new?template=https://github.com/pulumi/examples/tree/master/aws-js-webserver" target="_blank">
    <img src="https://get.pulumi.com/new/button.svg" alt="Deploy" style="float: right; padding: 8px; margin-top: -65px; margin-right: 8px">
</a>

<p class="mb-4">
    <a class="btn btn-secondary" href="https://github.com/pulumi/examples/tree/master/aws-js-webserver" target="_blank"><i class="fab fa-github pr-2"></i> VIEW CODE</a>
</p>


This example deploys a simple AWS EC2 virtual machine running a Python web server.

## Deploying the App

To deploy your infrastructure, follow the below steps.

### Prerequisites

1. [Install Pulumi](https://www.pulumi.com/docs/reference/install/)
2. [Configure AWS Credentials](https://www.pulumi.com/docs/reference/clouds/aws/setup/)

### Steps

After cloning this repo, from this working directory, run these commands:

1. Create a new stack, which is an isolated deployment target for this example:

    ```bash
    $ pulumi stack init
    ```

2. Set the required configuration variables for this program:

    ```bash
    $ pulumi config set aws:region us-east-1
    ```

3. Stand up the VM, which will also boot up your Python web server on port 80:

    ```bash
    $ pulumi up
    ```

4. After a couple minutes, your VM will be ready, and two stack outputs are printed:

    ```bash
    $ pulumi stack output
    Current stack outputs (2):
    OUTPUT          VALUE
    publicIp        53.40.227.82
    ```

5. Thanks to the security group making port 80 accessible to the 0.0.0.0/0 CIDR block, we can curl it:

    ```bash
    $ curl $(pulumi stack output publicIp)
    Hello, World!
    ```

6. From there, feel free to experiment. Simply making edits and running `pulumi up` will incrementally update your VM.

7. Afterwards, destroy your stack and remove it:

    ```bash
    $ pulumi destroy --yes
    $ pulumi stack rm --yes
    ```

