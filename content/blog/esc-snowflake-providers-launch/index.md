---
title: "Announcing Snowflake Dynamic and Rotated Credentials with Pulumi ESC"
date: 2025-05-01
allow_long_title: true
meta_desc: "Secure your Snowflake access with Pulumi ESC's new dynamic OIDC login for temporary credentials and automated RSA keypair rotation for user secrets."
meta_image: meta.png
authors:
- claire-gaestel
- arun-loganathan
tags:
- esc
- secrets
- features
- snowflake
- rotation
- dynamic-login
- oidc
- security
- configuration-management
---

Snowflake is the data cloud powerhouse for countless businesses, critical for everything from customer dashboards to billing pipelines. The stakes are immense: this data must be strictly secured and always available. Yet, relying on static credentials or manual key rotation forces a dangerous trade-off between security risks from stale secrets and operational disruption from clumsy updates. [Pulumi ESC](/product/esc) eliminates this dilemma with two purpose-built Snowflake integrations:

1.  **[`snowflake-login`](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/):** Provides dynamic, short-lived OIDC tokens for temporary authentication *to* Snowflake.
2.  **[`snowflake-user`](/docs/esc/integrations/rotated-secrets/snowflake-user/):** Automates the rotation of RSA keypair secrets *for* Snowflake users, essential for secure key-pair authentication.

<!--more-->

Pulumi ESC allows you to securely manage and consume these Snowflake credentials in your applications, development workflows through [ESC SDK](/docs/esc/development/languages-sdks/), [CLI](/docs/esc/cli/), [Kubernetes integrations](/docs/esc/integrations/kubernetes/), and more!

## snowflake-login: Dynamic OIDC Authentication for Temporary Access

Use the `snowflake-login` provider when you need temporary, just-in-time credentials to interact with Snowflake, such as from local development environments, CI/CD pipelines, or scripts. It leverages OIDC to mint short-lived access tokens, eliminating the need to store static tokens.

This approach significantly reduces the attack surface by removing long-lived credentials required for *authentication*.

**Setup:**

1.  **Configure OIDC in Snowflake:** Create a Security Integration in Snowflake to trust the Pulumi OIDC provider (`https://api.pulumi.com/oidc`), map the appropriate user claims and create a Snowflake user. Check out the [docs](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/#configuring-oidc-for-snowflake)] for more details
2.  **Configure ESC Environment:** Define the `snowflake-login` provider in your ESC environment, specifying the Snowflake account and the user configured for OIDC.
    
```yaml
# my-org/logins/snowflake
values:
  snowflake:
    login:
      fn::open::snowflake-login:
        oidc:
          account: myorganization-account 
          user: ESC_LOGIN_USER          
          role: ESC_ROLE  # Optional
```
When this environment is opened, ESC securely handles the OIDC flow and makes the temporary token available under `snowflake.login.token`.

## snowflake-user: Automated Rotation for RSA Key Secrets

For applications or services using Snowflake's key-pair authentication, maintaining the security of those RSA keys is crucial. The `snowflake-user` rotator automates the lifecycle management of these keys as **rotated secrets** within ESC. This rotater uses the same two-secret rotation strategy we use in rest of ESC's [rotated secrets](/docs/esc/integrations/rotated-secrets/) providers. This eliminates manual rotation toil and ensures keys are regularly refreshed according to policy, enhancing the security of the *user secret* itself. Check out the rotated secrets [blog post](/blog/esc-rotated-secrets-launch/#introducing-esc-rotated-secrets) to learn more about its benefits. 

**Setup:**

*  **Prepare Snowflake:**
    *   Create the [target user](/docs/esc/integrations/rotated-secrets/snowflake-user/#step-1-create-the-target-user) (e.g., `MY_APP_SNOWFLAKE_USER`) whose keys need rotation.
    *   Set up a dedicated [rotation role](/docs/esc/integrations/rotated-secrets/snowflake-user/#step-2-create-a-rotator-role) with `OWNERSHIP` permission over the users you wish to rotate, so it can modify their keys.
    *   Create a [service user](/docs/esc/integrations/rotated-secrets/snowflake-user/#step-3-create-a-rotation-service-user) using the rotation role, and [setup OIDC](/docs/esc/integrations/rotated-secrets/snowflake-user/#step-4-set-up-oidc-for-the-rotation-service-user) to allow ESC to assume the role for rotation. 
*   **Rotation Environment:** Define the rotation, importing the managing credentials and specifying the target user.

```yaml
# Environment: my-org/rotators/snowflake-app-key
values:
  rotatedKey: 
    fn::rotate::snowflake-user:
      inputs:
        login: ${environments.logins.snowflake.snowflake.login} #reference credentials created using `snowflake-login`
        targetUser: ESC_ROTATION_DEMO_USER # User whose keys rotate
```

After setup, use the triple-dot menu -> “Rotate Secrets” in the Pulumi Cloud UI and ensure rotation happens. Once you rotate a couple of time and ensured everything works well, navigate to the “Secret Rotation” tab for your Rotation environment in the Pulumi Cloud console and define the rotation schedule. 

## When to Use Dynamic Login vs. Rotated Secrets

|**Feature**                | **`snowflake-login` (Dynamic OIDC Login)**                                        | **`snowflake-user` (Rotated Secrets)**                                                                 |
| :--------------------- | :---------------------------------------------------------------------------- | :--------------------------------------------------------------------------------------------------------- |
| **Credential Type**    | Short-lived OIDC access token                                                 | Long-lived RSA Private Key secret (managed by ESC) + Public Keys (in Snowflake)                             |
| **Primary Use Case**   | Temporary authentication *to* Snowflake (CLI, scripts, dev, CI/CD).             | Key-pair authentication *for* long-lived applications/services connecting to Snowflake.                               |
| **Ideal Scenario**     | Short-lived tasks; frequent, temporary access needs.                          | Applications needing persistent connections; keys required at deploy time; apps sensitive to auth blips. |
| **Lifecycle**          | Generated on-demand, expires quickly (minutes/hours).                         | Rotated automatically on a schedule (e.g., days/months).                                                   |
| **Connection Impact** | Requires re-authentication or new token fetch when token expires.             | Rotation is typically seamless; two-key strategy avoids connection drops if apps update keys promptly.      |
| **Benefit Focus**      | Eliminates static *authentication* tokens/credentials.                        | Automates lifecycle management of user *key-pair secrets*, ensures key freshness.                            |

## Conclusion

Pulumi ESC's new Snowflake integrations provide robust solutions for modern credential management challenges. Use `snowflake-login` for secure, temporary OIDC-based access and `snowflake-user` to automate the rotation of critical RSA key secrets. By adopting these capabilities, you can significantly enhance your Snowflake security posture, reduce operational overhead, and simplify compliance.

Explore the detailed documentation for [`snowflake-login`](/docs/esc/integrations/dynamic-login-credentials/snowflake-login/) and [`snowflake-user`](/docs/esc/integrations/rotated-secrets/snowflake-user/), and see how Pulumi ESC can centralize and secure your configuration and secrets across all your environments. Join the conversation in the [Pulumi Community Slack](https://slack.pulumi.com/) or our [GitHub repository](https://github.com/pulumi/esc).