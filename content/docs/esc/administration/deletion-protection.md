---
title: Deletion protection
title_tag: Deletion protection | Pulumi ESC
h1: Deletion protection
meta_desc: Prevent accidental deletion of critical environments with deletion protection.
menu:
  esc:
    identifier: deletion-protection
    parent: pulumi-esc-admin
    weight: 5
---

Deletion protection prevents accidental deletion of environments containing sensitive configuration. When enabled for an environment, deletion attempts are blocked until protection is explicitly disabled.

## Enabling deletion protection

### In the Pulumi Cloud console

Navigate to your environment's settings page and find the deletion protection tab. Toggle the setting to enable protection.

When protection is enabled, the environment delete button is disabled and displays instructions for removing protection.

### Using the ESC CLI

Enable deletion protection using the `esc env settings set` command:

```bash
esc env settings set myorg/myproject/prod deletion-protected true
```

View the current protection status:

```bash
esc env settings get myorg/myproject/prod deletion-protected
```

View all environment settings:

```bash
esc env settings get myorg/myproject/prod
```

## Deleting protected environments

Attempting to delete a protected environment returns an error:

```bash
$ esc env rm myorg/myproject/prod --yes
error: deletion protection is enabled for this environment
```

To delete a protected environment, first disable protection:

```bash
esc env settings set myorg/myproject/prod deletion-protected false
esc env rm myorg/myproject/prod
```

## Visual indicators

Protected environments display an orange shield icon in the environment list and in stack overview pages where the environment is imported. The shield icon links to the deletion protection settings.

## Permissions

Only environment admins can modify deletion protection settings. This requires the `EnvironmentSettingsUpdate` permission.

## Use cases

Deletion protection helps prevent:

- Accidental deletion of production environments
- Removal of environments shared across multiple stacks
- Loss of critical configuration during team transitions

Enable deletion protection for environments that contain production secrets, are imported by multiple stacks, or represent stable configuration that should persist.
