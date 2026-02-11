---
title_tag: "Creating Templates | Guides"
meta_desc: Learn how to create Pulumi templates that can be used with pulumi new to bootstrap new projects.
title: Creating Templates
h1: Creating Pulumi templates
meta_image: /images/docs/meta-images/docs-meta.png
menu:
    iac:
        name: Creating Templates
        parent: iac-guides-building-extending
        weight: 15
aliases:
  - /docs/iac/guides/building-extending/templates/
---

Pulumi templates are pre-configured project scaffolds that you can use with `pulumi new` to quickly bootstrap new projects. You can create custom templates to share infrastructure patterns, enforce organizational standards, or simplify project setup for your team.

## What is a template?

A template is a directory containing:

- A `Pulumi.yaml` file with a `template` section that defines configurable parameters
- Source code files for your Pulumi program
- Any additional configuration files needed for the project

When someone runs `pulumi new` with your template, Pulumi copies these files to their local directory and prompts them to fill in the configuration values you've defined.

## Template structure

A basic template has the following structure:

```
my-template/
├── Pulumi.yaml
├── index.ts          # or main.py, main.go, etc.
├── package.json      # language-specific dependency files
└── README.md         # optional but recommended
```

### The Pulumi.yaml file

The `Pulumi.yaml` file must include a `template` section to be recognized as a valid template. Here's an example:

```yaml
name: ${PROJECT}
runtime: nodejs
description: ${DESCRIPTION}
template:
  displayName: My Custom Template
  description: A template for deploying widgets to AWS
  config:
    aws:region:
      description: The AWS region to deploy into
      default: us-west-2
    instanceType:
      description: The EC2 instance type
      default: t3.micro
    apiKey:
      description: Your API key for the widget service
      secret: true
  metadata:
    cloud: aws
    category: compute
```

The `template` section supports these fields:

| Field | Description |
|-------|-------------|
| `displayName` | A user-friendly name shown in template listings |
| `description` | A description of what the template creates |
| `config` | Configuration values to prompt for when creating a project |
| `metadata` | Custom key-value pairs for categorization |

Each config value can specify:

| Field | Description |
|-------|-------------|
| `description` | Explains what this value is for |
| `default` | A default value (user can accept or override) |
| `secret` | Set to `true` to encrypt this value |

### Variable substitution

Templates support these placeholder variables in any file:

| Variable | Replaced with |
|----------|--------------|
| `${PROJECT}` | The project name entered by the user |
| `${DESCRIPTION}` | The project description entered by the user |

Use `${PROJECT}` in your `Pulumi.yaml` name field and in code comments or documentation to personalize the generated project.

## Using templates from Git repositories

You can use templates from any Git repository by providing the URL to `pulumi new`:

### Public repositories

```bash
# GitHub
pulumi new https://github.com/myorg/my-template

# GitLab
pulumi new https://gitlab.com/myorg/my-template

# Bitbucket
pulumi new https://bitbucket.org/myorg/my-template

# Any Git host
pulumi new https://git.example.com/myorg/my-template.git
```

### Subdirectories

If your template is in a subdirectory of the repository:

```bash
pulumi new https://github.com/myorg/templates/tree/main/aws-typescript
```

### Branches and tags

To use a specific branch or tag:

```bash
# Branch
pulumi new https://github.com/myorg/my-template/tree/develop

# Tag
pulumi new https://github.com/myorg/my-template/tree/v1.0.0
```

### GitLab subprojects

For GitLab repositories with subprojects, append `.git` to disambiguate:

```bash
pulumi new https://gitlab.com/mygroup/mysubgroup/my-template.git
```

## Private repository authentication

To use templates from private repositories, you have several authentication options:

### SSH authentication

Ensure your SSH agent has the correct identity loaded:

```bash
# Add your SSH key to the agent
ssh-add ~/.ssh/id_rsa

# Use SSH URL format
pulumi new git@github.com:myorg/private-template.git
```

For SSH URLs with a non-standard user:

```bash
pulumi new myuser@git.example.com:myorg/my-template.git
```

If your key requires a passphrase:

```bash
PULUMI_GITSSH_PASSPHRASE=yourpassphrase pulumi new ssh://git@github.com/myorg/private-template.git
```

### HTTPS with credentials

You can embed credentials in the URL (use with caution):

```bash
pulumi new https://username:token@github.com/myorg/private-template.git
```

For GitHub, use a [personal access token](https://docs.github.com/en/authentication/keeping-your-account-and-data-secure/creating-a-personal-access-token) instead of your password.

{{% notes type="warning" %}}
Avoid embedding credentials in scripts or version control. Use environment variables or credential helpers instead.
{{% /notes %}}

### Git credential helpers

If you have Git credential helpers configured (such as the GitHub CLI or Git Credential Manager), Pulumi will use them automatically when you use HTTPS URLs:

```bash
# If gh auth login has been run, this will work automatically
pulumi new https://github.com/myorg/private-template.git
```

## Testing templates locally

You can test a template by providing a local file path:

```bash
pulumi new ~/templates/my-aws-template
```

{{% notes type="warning" %}}
**Avoid testing from within the template directory.** Running `pulumi new /path/to/template` while your current directory is inside `/path/to/template` can cause issues because Pulumi copies the template files to the current directory. This can result in recursive copying or file conflicts.

Always change to a different directory before testing:

```bash
cd /tmp
mkdir test-project
cd test-project
pulumi new ~/templates/my-aws-template
```

{{% /notes %}}

## Sharing templates

You can share templates in several ways:

### Git repositories

The simplest approach is hosting your template in a Git repository. Users can then run:

```bash
pulumi new https://github.com/myorg/my-template
```

### Organization templates

For Pulumi Enterprise and Business Critical customers, you can publish templates to your organization's [Private Registry](/docs/idp/concepts/organization-templates/). This provides:

- Version management with semantic versioning
- Integration with the Pulumi Cloud console
- Access control through your organization settings

See [Organization Templates](/docs/idp/concepts/organization-templates/) for details.

### Multiple templates in one repository

You can organize multiple templates in a single repository:

```
templates/
├── aws-typescript/
│   ├── Pulumi.yaml
│   └── index.ts
├── aws-python/
│   ├── Pulumi.yaml
│   └── __main__.py
└── azure-go/
    ├── Pulumi.yaml
    └── main.go
```

Users can then reference specific templates:

```bash
pulumi new https://github.com/myorg/templates/tree/main/aws-typescript
```

## Best practices

1. **Include a README.md** - Document what resources the template creates and any prerequisites.

1. **Use sensible defaults** - Provide default values for configuration where possible, but make them easy to override.

1. **Keep secrets secret** - Mark sensitive configuration values with `secret: true`.

1. **Test your template** - Create a project from your template and verify it works as expected.

1. **Version your templates** - Use Git tags or branches to maintain stable versions.

1. **Document configuration** - Write clear descriptions for each config value so users understand what they're providing.

## See also

- [Project file reference](/docs/iac/concepts/projects/project-file/) - Full reference for `Pulumi.yaml` including all template options
- [`pulumi new` command](/docs/iac/cli/commands/pulumi_new/) - CLI reference with all available flags
- [Organization templates](/docs/idp/concepts/organization-templates/) - Enterprise template management features
