---
title: "Pulumi ESC Public Preview for 1Password Support"
date: 2024-03-27T12:00:00-06:00
meta_desc: Pulumi ESC adds integration support for 1Password (public preview) to empower developers to work more efficiently and securely using their preferred tooling. 
meta_image: meta.png
authors:
    - tejitha-raju
    - diana-esteves
tags:
    - esc
    - secrets
    - 1password

---

Today, we are thrilled to add integration support for 1Password in preview within Pulumi Environments, Secrets, and Configuration ([ESC](/product/esc)). Since its launch, numerous organizations have leveraged Pulumi ESC to manage secrets and simplify configuration management using hierarchical environments. Leveraging Pulumi ESC’s comprehensive set of providers, users have obtained dynamic cloud provider credentials and retrieved secrets from other secrets management platforms, including HashiCorp Vault.

The addition of 1Password, known for its developer-centric approach to secrets management, to our roster of integrations has been a top request among our community. As users of 1Password ourselves, this collaboration represents more than just a feature release; it embodies our commitment to enriching the developer experience and fostering secure, efficient development workflows.

<!--more-->

Pulumi ESC's addition of the 1Password provider empowers development teams to seamlessly incorporate secrets and configurations stored within 1Password into their workflows. By using the retrieved values as [environment variables](/docs/esc/environments/#projecting-environment-variables) or within [Pulumi Config](/docs/esc/environments/#using-environments-with-pulumi-iac) at runtime, teams can bypass the manual and error-prone process of copying and pasting secrets, significantly enhancing security and efficiency.

{{% notes type="info" %}}
Join our upcoming workshop, ["Managing team secrets with 1Password & Pulumi ESC"](https://www.pulumi.com/resources/managing-team-secrets-1password-pulumi-esc/), to explore Pulumi ESC and the 1Password integration in detail.
{{% /notes %}}

## How does it work?

1. Create a 1Password service account with access to necessary vaults
2. Enter the service token into the 1Password provider configuration within your Pulumi ESC Environment (See syntax below)
3. Define a path-name, and enter the vault name, item name and field name that you want to import into the path name you defined

1Password provider syntax:

```yaml
values:
  1password:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken:
            fn::secret: <input your service token here>
        get:
          <path-name>:
            ref: op://<vault-name>/<item-name>/[section-name/]field-name
```

## Demo

Now that we know how to use the Pulumi ESC 1Password provider, let's use it to pull AWS CLI credentials stored in 1Password and use them within Pulumi ESC.

* Create AWS CLI credentials through AWS IAM and store it in 1Password Vault. In the demo, we've stored the AWS credentials in `Engineering` vault with `aws-cli-creds` item name with two fields `access-key` and `secret-access-key`
* Create a new Pulumi ESC Environment with the following definition. Ensure to replace the `serviceAccountToken` with your 1Password token

```yaml
values:
  1password:
    secrets:
      fn::open::1password-secrets:
        login:
          serviceAccountToken:
            fn::secret: ops_eyJzaWduSW5B..[Redacted]
        get:
          aws-access-key:
            ref: op://Engineering/aws-cli-creds/access-key
          aws-secret-access-key:
            ref: op://Engineering/aws-cli-creds/secret-access-key
  environmentVariables:
    AWS_ACCESS_KEY_ID: ${1password.secrets.aws-access-key}
    AWS_SECRET_ACCESS_KEY: ${1password.secrets.aws-secret-access-key}
 ```

* Open the environment to ensure we are able to successfully pull the credentials from 1Password
* Use the Pulumi ESC run command to run any AWS CLI commands
  
`esc run` passes the configuration stored under the `environmentVariables` section into a temporary environment's env variables. The secure credentials are never stored locally on your machine.

## Placeholder to add a video

## Unlocking New Possibilities

With 1Password now integrated into Pulumi ESC, we unlock a range of opportunities for developers to enhance workflow efficiency and security:

1. **Broad Cloud Provider Support**: What we demonstrated with AWS applies equally to other cloud providers.
2. **Database Secrets Management**: Securely manage and inject database credentials for PostgreSQL, MySQL, etc., into your infrastructure as code (IaC) projects.
3. **CI/CD Integration**: Utilize Pulumi ESC and 1Password within CI/CD pipelines, such as GitHub Actions, to ensure secure and efficient workflows.

These examples merely scratch the surface of what's possible. The combination of 1Password and Pulumi ESC opens up a wealth of scenarios to streamline operations and secure your infrastructure.

## Conclusion

Pulumi ESC's 1Password integration reiterates our commitment to providing choice and flexibility for developers. The 1Password provider brings the power of 1Password within ESC in a highly secure manner. We are excited to continue to work with our partners at 1Password and evolve our integration.

Your journey towards streamlined, secure cloud infrastructure management begins here. We can't wait to see what you build with Pulumi ESC.

* Visit the [1Password CI/CD Integrations page](https://developer.1password.com/docs/ci-cd/) for links to the Pulumi ESC [1Password provider docs](/docs/esc/providers/1password-secrets/)
* Visit our [Pulumi ESC docs](/docs/esc/) to learn more about Pulumi ESC and its supported [providers](docs/esc/providers/)

As always, we deeply value your insights. Your [feedback](https://github.com/pulumi/esc/issues/new/choose) is instrumental in helping us refine and enhance our solutions to better align with your needs.
