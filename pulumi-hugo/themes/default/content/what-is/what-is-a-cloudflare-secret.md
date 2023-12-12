---
title: What is a Cloudflare Secret?
meta_desc: |
    Learn more about Cloudflare secrets and how to use them.

type: what-is
page_title: "What is a Cloudflare Secret?"
---

[Cloudflare](https://www.cloudflare.com/) operates one of the world's largest networks, providing network and cloud services to improve website and application security and performance. A critical security aspect of building applications and solutions integrating with Cloudflare involves the management of sensitive data, commonly known as [secrets](/what-is/what-is-secrets-management/)." Cloudflare has a secure mechanism for handling secrets, offering tools for storing, accessing, and managing confidential information in the cloud.

## What is a Cloudflare secret?

Cloudflare secrets are sensitive information stored as encrypted environment variables for [Cloudflare Workers](https://developers.cloudflare.com/workers/) - serverless applications. Secrets include but are not limited to database credentials, API keys, and other confidential data. There is no need to hard-code sensitive information in plain text.

### Key features

- **Secure and encrypted storage**: Secrets in Cloudflare are encrypted during transit and at rest, ensuring high security.
- **Native application integration:** Cloudflare secrets integrate directly with Cloudflare Workers, eliminating the need for complex setup. This built-in solution provides automatic retrieval and management of credentials.
- **Environment variable flexibility:** Cloudflare secrets are easily referenced as environment variables across Workers.

## Creating Cloudflare secrets via the CLI

You can create secrets via [Wrangler](https://developers.cloudflare.com/workers/wrangler/), the Cloudflare Workers CLI.

### Prerequisites

- Install [Wrangler](https://developers.cloudflare.com/workers/wrangler/install-and-update/)
- Sign up for a free [Cloudflare account](https://dash.cloudflare.com/sign-up)
- Create a new project and navigate to it's directory:

    ```bash
    $ npx wrangler init secrets-demo
    # Select "Hello World" Worker
    # Confirm "Yes" to using Typescript
    # Confirm "Yes" to using using Git
    # Select "No" to deploy the application

    $ cd secrets-demo
    ```

- Login to your Cloudflare account and authorize Wrangler:

    ```bash
    $ npx wrangler login  
    # Confirm authorization to Wrangler
    ```

### Create a secret

You can create a secret by running the command:

```bash
$ npx wrangler secret put MY_SECRET_NAME_KEY
```

Next, you will be prompted to input the secret’s value, type:

```bash
 ⛅️ wrangler 3.19.0
-------------------
? Enter a secret value: › dragons and unicorns are real
```

Press Enter to save the secret. You'll see output similar to the following:

```bash
✔ Enter a secret value: … *****************************
🌀 Creating the secret for the Worker "secrets-demo"
✨ Success! Uploaded secret MY_SECRET_NAME_KEY
```

Verify the secret was created:

```bash
$ npx wrangler secret list
[
  {
    "name": "MY_SECRET_NAME_KEY",
    "type": "secret_text"
  }
]
```

### Accessing the secret from a Cloudflare Worker

Now that you have created a secret, your application can access it by referencing it in the Worker code.

Edit the `src/index.ts` so the return response reads:

```typescript
export default {
        async fetch(request: Request, env: Env, ctx: ExecutionContext): Promise<Response> {
                return new Response(`Secret: ${env.MY_SECRET_NAME_KEY}`);
        },
};
```

Deploy the changes.

```bash
$ npx wrangler deploy
 ⛅️ wrangler 3.19.0
-------------------
Total Upload: 0.21 KiB / gzip: 0.18 KiB
Uploaded secrets-demo (0.92 sec)
Published secrets-demo (3.61 sec)
  https://secrets-demo.diana-247.workers.dev
Current Deployment ID: e7c2b8e7-e13a-4a11-9667-024eed3cce05
```

Here's an example of using `curl` against a Cloudflare Worker serverless application using the code above to retrieve and return a Cloudflare secret value:

```bash
$ curl https://secrets-demo.diana-247.workers.dev

Secret: dragons and unicorns are real
```

## Best practices

- **Rotate secrets regularly**: Implement a routine for periodically rotating secrets to enhance security.
- **Provide least-privilege access**: Employ policies for granular access control to secrets.
- **Audit and monitor secret access**: Use monitoring tools to track access and modifications to your secrets.

### Challenges and considerations

Using Cloudflare secrets comes with particular challenges and considerations:

- **Management of secrets overhead:**  As the number of secrets and contexts grows, managing them can become challenging. Teams must actively track and monitor the usage of secrets, identifying where and by whom they are employed.
- **Access control complexity:** Setting up fine-grained access controls is crucial but can become complex as teams and projects scale. Defining and maintaining access permissions for different roles and responsibilities can be challenging. Clearly define roles and duties to determine who needs access to specific secrets. Use role-based access control (RBAC) principles to simplify and organize permissions.
- **Integration with external secret management systems:**  Organizations may already have established processes for secrets management using external tools, and integrating these with Cloudflare secrets can be complex. Evaluate whether integrating with an external secrets management system is necessary for your organization. If required, explore solutions that integrate with Cloudflare and provide a unified approach to secrets management. Ensure that the chosen solution aligns with your security and compliance requirements. Two popular secret management systems include [AWS Secrets Manager](./what-is-aws-secrets-manager.md) and [Google Cloud Secret Manager](./what-is-google-cloud-secret-manager).

Addressing these challenges and considerations requires a thoughtful approach to [secrets management](
/what-is/what-is-secrets-management/), clear communication within the development team, and a commitment to maintaining security best practices. A beta product to facilitate secrets management and tackle the above challenges is available for Cloudflare as the [Cloudflare Secrets Store](https://blog.cloudflare.com/secrets-store/).

## Conclusion  

Following security best practices for Cloudflare secrets are crucial in managing sensitive information in your solutions, applications, and cloud environments.

Now that you know Cloudflare secrets, take your cloud infrastructure management to the next level with [Pulumi](link):

- **Streamlined infrastructure management with Infrastructure as Code (IaC)**: Learn about other Cloudflare resources using Pulumi’s IaC capabilities. Pulumi lets you define and provision your cloud infrastructure using familiar programming languages, directly integrating secrets management into your workflows. Discover how to integrate Cloudflare secrets into your broader cloud infrastructure with Pulumi by exploring the [Cloudflare Provider documentation](https://www.pulumi.com/registry/packages/cloudflare/). Below are some examples of how to create a Cloudflare secret in several supported programming languages:

```bash
$ pulumi config set secrets-demo --secret
value:  ****
```

{{< chooser language "typescript,python,go" / >}}
{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as cloudflare from "@pulumi/cloudflare";
import * as fs from "fs";

const config = new pulumi.Config();
const accountId = config.require("accountId");
const secret = config.require("secrets-demo");  // mark as required

const myScript = new cloudflare.WorkerScript("myScript", {
    accountId: accountId,
    name: "script_1",
    content: fs.readFileSync("script.js", "utf8"),
    secretTextBindings: [{
        name: "MY_SECRET_NAME_KEY",   // secret key
        text: secret,                 // secret value
    }],
});
```

{{% /choosable %}}
{{% choosable language python %}}

```python
"""A Python Pulumi program"""

import pulumi
import pulumi_cloudflare as cloudflare

config = pulumi.Config()
account_id = config.require("accountId")
secret = config.require("secrets-demo")

# Sets the script with the name "script_1"
my_script = cloudflare.WorkerScript("myScript",
    account_id=account_id,
    name="script_1",
    content=(lambda path: open(path).read())("script.js"),
    secret_text_bindings=[cloudflare.WorkerScriptSecretTextBindingArgs(
        name="MY_SECRET_NAME_KEY",
        text=secret,
    )],

    )
```

{{% /choosable %}}
{{% choosable language go %}}

```go
package main

import (
	"os"

	"github.com/pulumi/pulumi-cloudflare/sdk/v5/go/cloudflare"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi/config"
)

func readFileOrPanic(path string) pulumi.StringInput {
	data, err := os.ReadFile(path)
	if err != nil {
		panic(err.Error())
	}
	return pulumi.String(string(data))
}

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {
		conf := config.New(ctx, "")

		accountId := conf.Require("accountId")
		secret := conf.Require("secrets-demo")

		_, err := cloudflare.NewWorkerScript(ctx, "myScript", &cloudflare.WorkerScriptArgs{
			AccountId: pulumi.String(accountId),
			Name:      pulumi.String("script_1"),
			Content:   readFileOrPanic("script.js"),
			SecretTextBindings: cloudflare.WorkerScriptSecretTextBindingArray{
				&cloudflare.WorkerScriptSecretTextBindingArgs{
					Name: pulumi.String("MY_SECRET_NAME_KEY"),
					Text: pulumi.String(secret),
				},
			},
		})
		if err != nil {
			return err
		}
		return nil
	})
}
```

{{% /choosable %}}

- **Get started tutorial**: Follow a simple tutorial to [deploy a Hello World web application using Cloudflare Workers and Pulumi](https://developers.cloudflare.com/pulumi/tutorial/hello-world/)
- **Advanced secrets management**: For organizations that use more than one secrets manager or store configuration data in multiple locations, [Pulumi ESC (Environments, Secrets, and Configurations)](/docs/pulumi-cloud/esc/) offers a centralized solution for managing secrets and configurations across various environments. Moreover, Pulumi ESC integrates with OIDC to allow the dynamic generation of credentials, elevating its utility in scenarios where secrets need to be frequently rotated or updated. Dive deeper into how Pulumi ESC can streamline your secrets management workflows by visiting the Pulumi ESC documentation for the [Pulumi ESC documentation for the AWS Secrets provider](/docs/pulumi-cloud/esc/providers/aws-secrets/).

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
