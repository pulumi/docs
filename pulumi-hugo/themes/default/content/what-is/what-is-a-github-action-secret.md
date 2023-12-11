---
title: What is a GitHub Action Secret?
meta_desc: |
    Learn more about GitHub Action Secrets and how to use them.

type: what-is
page_title: "What is a GitHub Action Secret?"
---

[GitHub Actions](https://github.com/features/actions) is an automation feature provided by [GitHub](https://github.com/) that allows you to define workflows to automate various aspects of your software development process directly within your GitHub repository. A prevalent example is automatically running a linter test every time a commit is made against an opened pull request.

## What is a GitHub Action Secret?

In GitHub Actions, secrets are encrypted environment variables you can store and use in your workflows. Secrets store sensitive information, such as API keys, access tokens, or passwords, without exposing them to your files.

### Key features

Using GitHub Action Secrets provides several key features that enhance the security and flexibility of your workflows:

- **Automatic encryption** - Secrets are always encrypted.
- **Limited access** - A workflow will access a referenced secret during execution only. The GitHub UI does not expose secrets, nor are they available to users viewing the repository.
- **Log redaction** - GitHub Actions automatically redacts secrets from most logs and prevents them from being exposed in the workflow run logs.
- **Dynamic configurations** - By referencing secrets in workflow files, you can easily update sensitive information without modifying the code. This flexibility is beneficial when collaborating with others or managing multiple environments (e.g., development, staging, production).

## Using GitHub Action Secrets

In this example, we list the steps required to configure a GitHub token for use in one of the most popular GitHub actions, [super linter](https://github.com/marketplace/actions/super-linter). We can obtain extra details about a given commit's code quality when provided with a GitHub token. This token is sensitive; thus, it will be stored and referenced as a secret within a GitHub [Environment](https://docs.github.com/en/actions/deployment/targeting-different-environments/using-environments-for-deployment).

### Prerequisites

An existing GitHub personal access token is required to proceed. Navigate to your [GitHub settings](https://github.com/settings/personal-access-tokens/new) to create one.

### Steps

To use secrets in GitHub Actions, you'd need to follow these steps:

1. **Create a new environment**

    - Go to your GitHub repository.
    - Click on the "Settings" tab.
    - In the left sidebar, click on "Environments".
    - Click on the "New environment" button.
    - Provide a name for the environment, e.g., `demo``.
    - Click on the "Configure environment" button.

2. **Create an environment secret**

    - In the environment configuration page from Step 1,
    - Scroll to the "Environment secrets" section.
    - Click on the "Add secret" button.
    - Provide a name for the secret and its corresponding value.
        e.g., Name: `DEMO_GITHUB_TOKEN`
            Value: `github_pat_123123123`
    - Click "Add secret" to save it.

3. **Use the secret in the workflow**

    - You can see a reference to the secret using the `secrets.` context in the workflow YAML file (e.g., ``.github/workflows/super-linter.yml`)
    - Ensure the name of the secret matches: `GITHUB_TOKEN: ${{ secrets.DEMO_GITHUB_TOKEN }}`

For more information, visit the GitHub guide [Using Secrets in GitHub Actions](https://docs.github.com/en/actions/security-guides/using-secrets-in-github-actions)

## Best practices

- **Restrict access to secrets** - Follow the [principle of least privilege](https://en.wikipedia.org/wiki/Principle_of_least_privilege) and avoid granting unnecessary permissions to actions or workflows. Only provide the minimum required access to complete the necessary tasks.
- **Use environment-specific secrets:** - Consider creating different sets of secrets for different environments (e.g., development, staging, production). This practice helps minimize the impact of a potential compromise and allows for more granular control over which secrets are accessible in different contexts.
- **Audit workflow runs:** - Regularly review the logs and outputs of your workflow runs to ensure that secrets are not inadvertently exposed. GitHub Actions automatically redacts secrets in most logs, but it's a good practice to review logs for any potential issues.

## Challenges and considerations

Using GitHub Action Secrets provides a secure way to manage sensitive information. Still, there are challenges and considerations to remember:

- **Nongrandular access scope** - Secrets are repository-wide, and there's no inherent support for limiting secrets to specific workflows or jobs. Exercise caution with repository-wide secrets and explore external solutions for more granular access control.
- **Unavailability of secrets in Pull Requests** - Secrets are unavailable in workflows triggered by pull requests from forks by default. For workflows involving pull requests, especially from forks, consider alternative solutions or design workflows that don't rely on sensitive information.
- **Limited default visibility and auditing:** - Limited visibility into when and by whom secrets are accessed during workflow runs. Consider implementing additional logging or external monitoring tools to enhance the visibility and audibility of secret usage in workflows.

Refer to the official [secrets documentation](https://docs.github.com/en/actions/security-guides/encrypted-secrets) for more details on GitHub Actions Secrets.

## Conclusion

Github Action secrets are encrypted and only exposed to workflow runs. They are not visible in the GitHub UI, and users or other GitHub actions cannot directly access their values. User precaution is still required to avoid unintentionally exposing secrets in logs. GitHub automatically redacts secrets in most places, but avoid using secrets in unsecured ways in your workflow scripts.

Now that you know about GitHub Action secrets, take your cloud infrastructure management to the next level with Pulumi:

- **Integrate your [continuous delivery with Pulumi](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/github-actions/)**: Ship software faster and more safely by combining Pulumi with the other components of your automated infrastructure.
- **Install the [Pulumi GitHub App](https://www.pulumi.com/docs/using-pulumi/continuous-delivery/github-app/)**:  Once installed, the Pulumi GitHub app will submit rich, inline comments on any pull request or commit that introduces a change to your Pulumi-managed infrastructure.
- **Manage sensitive data and secrets with Pulumi**: Dive into Pulumi's [Secrets Management guide](/blog/managing-secrets-with-pulumi/) for in-depth information on encrypting specific values for added security and ensuring that these values never appear in plain text in your state file​.
- **Use the [GitHub provider for Pulumi](https://www.pulumi.com/registry/packages/github/#github)**: Provision any of the cloud resources available in GitHub.

Our [community on Slack](https://slack.pulumi.com/) is always open for discussions, questions, and sharing experiences. Join us there and become part of our growing community of cloud professionals!
