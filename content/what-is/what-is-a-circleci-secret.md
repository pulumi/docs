---
title: What is a CircleCI Secret?
meta_desc: |
    Learn more about CircleCI secrets and how to use them.

meta_image: /images/what-is/what-is-a-circleci-secret-meta.png
type: what-is
page_title: "What is a CircleCI Secret?"
authors: ["diana-esteves"]
---

[CircleCI](https://circleci.com/) is an agile, continuous integration/continuous deployment ([CI/CD](/what-is/what-is-ci-cd/)) platform. It aims to automate software development processes for faster, more reliable releases. CircleCI secrets empower developers to safeguard critical data while streamlining workflows.

## What is a CircleCI secret?

CircleCI secrets are sensitive information that must be protected to guarantee the safe and reliable building and deployment of applications within your CI/CD pipeline. They can include API tokens, SSH keys, and environment variables containing credentials. These are to be hidden from the public and protected with access control to maintain security and integrity. In CircleCI, secrets are used within the configuration of continuous integration and delivery pipelines to allow automated processes to interact securely with other services, repositories, and infrastructure. Managing these secrets is crucial to prevent unauthorized access and potential security breaches.

### Key features

- **Pipeline integration:** CircleCI secrets integrate into workflows, eliminating the need for complex setup. This built-in solution ensures automatic retrieval and management of credentials throughout the build, test, and deployment phases.
- **Environment variable flexibility:** CircleCI secrets can be easily referenced as environment variables across workflows. This flexibility allows a single codebase to cater to various development environments, including Dev, QA, pre-prod, etc.
- **Centralized version control:** CircleCI centralizes configuration files with secret references in the `.circleci` home directory. This approach removes the necessity of embedding sensitive data directly into your application.
- **Native CircleCI tools for secrets management:** The [CircleCI CLI](https://github.com/CircleCI-Public/circleci-cli) and [CircleCI-Env-Inspector](https://github.com/CircleCI-Public/CircleCI-Env-Inspector) provide support for secrets management. The Inspector tool includes the ability to effortlessly create, rotate, audit, and generate reports, all without the hassle of installing additional complex systems.

## Getting started with CircleCI secrets

### Define a CircleCI secret

CircleCI stores secrets as project environment variables or in [contexts](https://circleci.com/docs/contexts/). You add them in the CircleCI web app under Project Settings > Environment Variables, or programmatically through the [API v2](https://circleci.com/docs/api/v2/). For example, to add a project environment variable with the API:

```bash
curl -X POST "https://circleci.com/api/v2/project/{project-slug}/envvar" \
  -H "Circle-Token: $CIRCLECI_TOKEN" \
  -H "Content-Type: application/json" \
  -d '{"name": "API_KEY", "value": "your-secret-value"}'
```

Once set, the variable is available to your jobs as `$API_KEY`.

### Reference secrets in CircleCI jobs

A CircleCI job is a collection of steps. You can leverage CircleCI secrets within your jobs to allow the pipeline to access confidential data without exposing it directly in the code. Here's a `.circleci/config.yml` file definition using a secret named `API_KEY` inside of a job:

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: circleci/python:3.8
    steps:
      - checkout
      # Your build steps here...
  test:
    docker:
      - image: circleci/node:18
    steps:
      - checkout
      # Your test steps here...
  deploy:
    docker:
      - image: circleci/python:3.8
    steps:
      - checkout
      # Deploy step that uses the secret
      - run:
          name: Deploy to Production
          command: |
            echo "Deploying to production..."
            # Use the API_KEY secret in your deployment script or command
            ./deploy_script.sh $API_KEY

workflows:
  build_and_deploy:
    jobs:
      - build
      - test
      - deploy:
          # Pass the context that holds API_KEY to the deploy job
          context:
            - production-secrets
          requires:
            - build
            - test
```

In this example:

1. Three jobs are defined: `build`, `test`, and `deploy`.
2. The `deploy` job includes a deploy step that uses the `$API_KEY` secret. The secret is accessed securely without exposing its actual value in the configuration file.
3. The `build_and_deploy` workflow is defined to execute the `build`, `test`, and `deploy` jobs in sequence.
4. The `deploy` job is given the `production-secrets` context, which makes `API_KEY` available as an environment variable for that specific job in the workflow.

This example illustrates how CircleCI secrets can be leveraged within jobs to securely access confidential data during different stages of your CI/CD pipeline. The secret is referenced in the job configuration without exposing its value in the code, enhancing security and maintaining best practices for handling sensitive information.

### Configure CircleCI workflows with secrets

A workflow is a set of rules defining a collection of jobs and their run order. You can integrate CircleCI secrets into workflows by referencing them in the configuration files. Doing so ensures your sensitive data remains secure while being accessible during the execution of CI/CD pipelines. For example, assume you have a secret named `API_KEY` defined for your CircleCI project. In your `.circleci/config.yml` file, you can reference this secret within your workflow steps:

```yaml
version: 2.1

jobs:
  build:
    docker:
      - image: circleci/python:3.8
    steps:
      - checkout
      # Your build steps here...
  deploy:
    docker:
      - image: circleci/python:3.8
    steps:
      - checkout
      - run:
          name: Deploy to Production
          command: |
            echo "Deploying to production..."
            # Use the API_KEY secret in your deployment script or command
            ./deploy_script.sh $API_KEY

workflows:
  build_and_deploy:
    jobs:
      - build
      - deploy:
          # The context exposes API_KEY to the deploy job
          context:
            - production-secrets
          requires:
            - build
```

In this example:

- The `build` and `deploy` jobs are each defined with their necessary steps.
- The `build_and_deploy` workflow runs `build`, then runs `deploy` once `build` succeeds.
- The `deploy` job is given the `production-secrets` context, which exposes the secrets in that context as environment variables.
- Inside the `deploy` job, you reference the `API_KEY` secret using the `$API_KEY` syntax, which securely passes the value to your deployment script or command.

Adjust the job names, workflow structure, and secret references according to your project requirements. This example demonstrates the basic concept of integrating a CircleCI secret into your workflow by referencing it in the configuration file.

### Best practices

Here are five best practices for managing CircleCI secrets:

- **Adopt context-based management:** Organize your secrets using [contexts](https://circleci.com/docs/contexts/) in CircleCI. Group related secrets together in a context, making managing access controls and permissions easier. Contexts ensure that only authorized personnel can access specific secrets based on their roles or responsibilities.
- **Use fine-grained access controls:** Set up fine-grained access controls and permissions for each context to restrict who can manage and utilize the secrets within that context. By carefully assigning permissions, you reduce the risk of unauthorized access to sensitive information, enhancing the overall security of your CI/CD process.
- **Avoid hardcoding secrets in configuration files:** Refrain from hardcoding secret values directly in your configuration files. Instead, reference secrets using the `$SECRET_NAME` syntax. This approach keeps sensitive information separate from the codebase, minimizing the risk of accidental exposure and making it easier to update or rotate secrets without modifying the code.
- **Rotate secrets:** Implement a regular rotation schedule for your secrets, especially for long-lived API keys or credentials. CircleCI provides an easy way to update secrets without modifying the configuration files. Note that OIDC can eliminate the need to store long-lived secrets in CircleCI. Learn [how to use OIDC with Pulumi ESC](/docs/esc/environments/configuring-oidc/#configuring-openid-with-your-cloud-provider) to connect to AWS, GCP, ECR, and more.
- **Perform auditing and monitoring:** Implement auditing and monitoring mechanisms to track changes and usage of secrets within your CI/CD pipeline. CircleCI provides tools and logs that enable you to monitor when and how secrets are accessed.

Check out [more security recommendations](https://circleci.com/docs/security-recommendations/) provided by CircleCI.

### Challenges and considerations

Using CircleCI secrets comes with particular challenges and considerations that organizations should know to ensure a secure and efficient CI/CD pipeline.

- **Management of secrets overhead:** As the number of secrets and contexts grows, managing them can become challenging. Teams must actively track and monitor the usage of secrets, identifying where and by whom they are employed.
- **Access control complexity:** Setting up fine-grained access controls is crucial but can become complex as teams and projects scale. Defining and maintaining access permissions for different roles and responsibilities can be challenging. Clearly define roles to determine who needs access to specific secrets. Use role-based access control (RBAC) principles to simplify and organize permissions.
- **Integration with external secret management systems:** Organizations may already have established processes for secret management using external tools, and integrating these with CircleCI secrets can be complex. Evaluate whether integrating with an external secrets management system is necessary for your organization. If required, explore solutions that integrate with CircleCI and provide a unified approach to secrets management. Ensure that the chosen solution aligns with your security and compliance requirements.

Addressing these challenges and considerations requires a thoughtful approach to [secrets management](/what-is/what-is-secrets-management/), clear communication within the development team, and a commitment to maintaining security best practices throughout the CI/CD pipeline. Regular reviews and updates to your secret management strategy will help ensure a secure and efficient development process.

## Conclusion

CircleCI secrets solve storage and access, but they leave you holding long-lived credentials that someone has to track, rotate, and audit as your contexts multiply. The more durable move is to remove the secret from the loop entirely: use OIDC so CircleCI exchanges a short-lived, job-scoped token at runtime instead of reading a stored key. Treat stored secrets as the exception you actively work to eliminate, not the default you accumulate.

To go further, learn how to [use OIDC with Pulumi ESC](/docs/esc/environments/configuring-oidc/#configuring-openid-with-your-cloud-provider) to connect CircleCI to your cloud provider without storing long-lived secrets.

The [Pulumi community on Slack](https://slack.pulumi.com/) is open for questions and discussion.
