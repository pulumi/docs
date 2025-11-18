---
title_tag: Running Commands with ESC
title: Running Commands with esc run
h1: Running Commands with esc run
meta_desc: Learn how to use esc run to inject secrets and configuration from Pulumi ESC into any command or script.
menu:
  esc:
    parent: esc-guides
    identifier: esc-guides-running-commands
    weight: 3
---

This guide shows you how to use `esc run` to inject secrets and configuration from ESC environments into any command or script as environment variables.

## Prerequisites

- [ESC CLI](/docs/install/esc/) installed
- [Pulumi account](https://app.pulumi.com/signup) created
- An ESC environment with values (see [Managing secrets](/docs/esc/guides/managing-secrets/))

## Basic usage

The `esc run` command opens an ESC environment, exports values as environment variables, and runs a command with those variables:

```bash
esc run <org>/<project>/<env-name> -- <command>
```

For example, if your environment contains:

```yaml
values:
  environmentVariables:
    DATABASE_URL: postgres://localhost/mydb
    API_KEY:
      fn::secret: my-api-key-123
```

Run a script with these variables:

```bash
esc run my-org/my-project/dev -- node app.js
```

The `app.js` script will have access to `DATABASE_URL` and `API_KEY` as environment variables.

## Using the environmentVariables block

ESC exports values to environment variables using the `environmentVariables` block:

```yaml
values:
  database:
    host: db.example.com
    password:
      fn::secret: db-password-123

  environmentVariables:
    DB_HOST: ${database.host}
    DB_PASSWORD: ${database.password}
```

The `environmentVariables` block:

- Maps ESC values to environment variable names
- Uses interpolation (`${...}`) to reference other values
- Automatically includes secrets (they're revealed when the environment is opened)

## Common patterns

### Running cloud CLI commands

Inject cloud credentials into CLI commands:

```yaml
values:
  aws:
    login:
      fn::open::aws-login:
        oidc:
          roleArn: arn:aws:iam::123456789012:role/my-role
          sessionName: esc-session

  environmentVariables:
    AWS_ACCESS_KEY_ID: ${aws.login.accessKeyId}
    AWS_SECRET_ACCESS_KEY: ${aws.login.secretAccessKey}
    AWS_SESSION_TOKEN: ${aws.login.sessionToken}
```

Run AWS CLI commands:

```bash
esc run my-org/my-project/aws-prod -- aws s3 ls
esc run my-org/my-project/aws-prod -- aws ec2 describe-instances
```

The same pattern works for other cloud CLIs:

```bash
esc run my-org/my-project/azure-prod -- az vm list
esc run my-org/my-project/gcp-prod -- gcloud compute instances list
```

### Running tests with secrets

Configure test environments with secrets:

```yaml
values:
  environmentVariables:
    TEST_DATABASE_URL: postgres://localhost/test_db
    TEST_API_KEY:
      fn::secret: test-api-key
    TEST_WEBHOOK_SECRET:
      fn::secret: test-webhook-secret
```

Run tests:

```bash
esc run my-org/my-project/test -- npm test
esc run my-org/my-project/test -- pytest
esc run my-org/my-project/test -- go test ./...
```

### Running deployment scripts

Inject credentials for deployment scripts:

```yaml
values:
  environmentVariables:
    DEPLOY_TOKEN:
      fn::secret: github-deploy-token
    DOCKER_REGISTRY: myregistry.azurecr.io
    DOCKER_USERNAME: myuser
    DOCKER_PASSWORD:
      fn::secret: registry-password
```

Run deployment:

```bash
esc run my-org/my-project/prod -- ./deploy.sh
```

### Running interactive shells

Start a shell session with environment variables loaded:

```bash
esc run my-org/my-project/dev -- bash
```

All environment variables from the ESC environment are available in the shell. This is useful for:

- Debugging issues locally with production-like configuration
- Running multiple commands without repeating `esc run`
- Interactive exploration of cloud resources

Exit the shell to clear the environment variables.

## Combining with other tools

### Docker

Run containers with secrets:

```bash
esc run my-org/my-project/dev -- docker run --env DATABASE_URL myapp
```

Or use with Docker Compose:

```bash
esc run my-org/my-project/dev -- docker-compose up
```

### Make

Run Makefile targets with secrets:

```bash
esc run my-org/my-project/dev -- make deploy
```

### CI/CD

Use in CI/CD pipelines to inject secrets without storing them in CI configuration:

```bash
# GitHub Actions
- run: esc run my-org/my-project/prod -- ./deploy.sh

# GitLab CI
script:
  - esc run my-org/my-project/prod -- ./deploy.sh
```

## Security considerations

### Secrets are revealed during execution

When you run `esc run`, secrets are revealed and passed as environment variables to the command. The command and any child processes can access these secrets.

### Secrets are temporary

Environment variables only exist for the duration of the command. Once the command exits, the secrets are no longer available.

### Use appropriate environments

Use separate environments for different security contexts:

- Dev environment for local development
- CI environment for continuous integration
- Prod environment for production deployments

Configure RBAC to control who can run commands with production secrets.

## Next steps

- [Managing secrets](/docs/esc/guides/managing-secrets/) - Store and organize secrets
- [Integrate with Pulumi IaC](/docs/esc/guides/integrate-with-pulumi-iac/) - Use ESC in infrastructure code
- [Dynamic login credentials](/docs/esc/integrations/dynamic-login-credentials/) - Generate dynamic cloud credentials with OIDC
- [CLI reference](/docs/esc/cli/commands/esc_run/) - Complete `esc run` documentation
