---
title: "Introducing Automated Database Credential Rotation for PostgreSQL, MySQL, and Snowflake in Pulumi ESC"
date: 2025-04-30 # Adjust T00:00:00-00:00 as needed for timezone/exact time
allow_long_title: true
meta_desc: "Pulumi ESC now automates the rotation of database credentials for PostgreSQL and MySQL (on AWS), and Snowflake, enhancing security and reducing operational burden."
meta_image: meta.png
authors:
- sean-yeh
- claire-gaestel
- arun-loganathan
tags:
- esc
- secrets
- features
- rotation
- database
- security
---

Securing access to critical data stores is paramount in today's cloud-native world. Yet, managing database credentials often involves static, long-lived passwords – a significant security blind spot. These static secrets, frequently embedded in application configurations or accessible to multiple team members, represent a prime target for attackers. Manually rotating these credentials is a cumbersome, error-prone task that’s often neglected, leaving databases vulnerable for extended periods. Building on our commitment to robust secrets management, we are excited to launch **Automated Database Credential Rotation** for **PostgreSQL, MySQL, and Snowflake** in [Pulumi ESC!](/product/esc)

<!--more-->

## The Persistent Challenge of Static Database Secrets

Relying on static database credentials introduces substantial risks, which automated rotation helps mitigate:

*   **Security Vulnerabilities & Exposure:** Static credentials, if compromised through leaks, phishing, or unauthorized access, provide long-term access to attackers. Automated rotation significantly shrinks this window of opportunity.
*   **Operational & Compliance Burdens:** Manually rotating database credentials is complex, error-prone, and requires careful coordination to avoid downtime. These manual rotations are hard to audit and demonstrate compliance with regulations like SOC 2, GDPR, or HIPAA (which often mandate rotation).
*   **Network Complexity:** Many databases reside within private networks (like AWS VPCs) for security. Rotating credentials for these databases typically requires bridging this network gap securely, often involving mechanisms like proxies, bastion hosts, or specific agents. This adds significant setup and maintenance overhead for manual or homegrown solutions.
*   **Tooling and Ecosystem Compatibility:** Many standard database administration GUIs, Business Intelligence platforms, ETL tools, and custom scripts were built primarily for username/password authentication. While support for cloud provider-specific methods like AWS IAM database authentication is growing, it's not universal. Older versions, generic ODBC/JDBC connectors, or specific tools may lack native support or require complex configuration, making username/password the more straightforward or only viable connection method for these essential parts of the data ecosystem, reinforcing the need for automated password rotation.

Pulumi ESC addresses these challenges by automating the rotation process, including databases in private networks.

## Introducing ESC Rotated Secrets for Databases

Pulumi ESC’s [Rotated Secrets](/docs/esc/integrations/rotated-secrets/) capability now extends to your critical databases, bringing automation and enhanced security to credential lifecycle management. We're launching support for:

*   [**PostgreSQL**](/docs/esc/integrations/rotated-secrets/postgres/) (Including instances hosted on AWS RDS/Aurora or in your Private VPCs)
*   [**MySQL**](/docs/esc/integrations/rotated-secrets/mysql/) (Including instances hosted on AWS RDS/Aurora or in your Private VPCs)
*   [**Snowflake**](/docs/esc/integrations/rotated-secrets/snowflake-user/)

Here’s how ESC Rotated Secrets for Databases tackles the challenges:

*   **Automated Rotation Schedules:** Effortlessly define rotation frequencies (daily, weekly, monthly) that align with your security policies, eliminating manual toil and ensuring consistency.
*   **On-Demand Rotation:** Instantly rotate credentials in response to security events, personnel changes, or policy updates with a single click or command.
*   **Seamless ESC Environment Integration:** Manage rotated database credentials alongside all your other application configurations within ESC Environments, leveraging composition and environment inheritance.
*   **Two-Secret Strategy:** ESC maintains both the current and previous valid credentials simultaneously. This prevents application downtime during rotation, as instances can gracefully transition to the new credential.
*   **Auditing and Tracking:** Maintain a complete audit trail of credential rotations, including who initiated the rotation and when, simplifying compliance and governance.
*   **Admin and Creator Control:** Securely configure rotation using privileged database "managing user" credentials stored within ESC, keeping them separate from the rotated credentials consumed by applications.
*   **Configure Webhooks for Automation:** Trigger notifications, CI/CD pipelines (e.g., Pulumi Deployments to update application stacks), or custom workflows upon successful rotation, keeping dependent systems synchronized.

{{% notes type="info" %}}
The following setup guide provides a detailed walkthrough for [**PostgreSQL**](/docs/esc/integrations/rotated-secrets/postgres/) hosted within an AWS private VPC, which requires a Lambda-based connector. Please refer to the [**MySQL**](/docs/esc/integrations/rotated-secrets/mysql/) or [**Snowflake**](/docs/esc/integrations/rotated-secrets/snowflake-user/) documentation page for instructions on these two databases.
{{% /notes %}}

## How to Set Up and Use PostgreSQL Rotation (AWS VPC Example)

Setting up rotation for PostgreSQL databases running inside an AWS VPC involves [creating the required users](/docs/esc/environments/rotation/db-user-setup/) within your database, deploying the connector Lambda infrastructure via a Pulumi template, configuring ESC environments, and scheduling the rotation.

**Step 1: Prepare Your PostgreSQL Database Users**

You'll need two *types* of users configured, resulting in *three* specific database user accounts:

1.  **Managing User:** A privileged user that ESC will use to perform the password rotations. This user needs permissions to change the passwords of the application users.
2.  **Application User 1 and Application User 2:** The two application users whose passwords ESC will manage. ESC rotates between these two users, ensuring two users are always active as applications gradually phase out the `previous` user credentials.

Connect to the database as a superuser and run the following SQL commands:

  *   Create the application users whose passwords you want ESC to rotate automatically:
      ```sql
      CREATE USER user1 WITH PASSWORD 'initial_password';
      GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user1;
      CREATE USER user2 WITH PASSWORD 'initial_password';
      GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user2;
      ```

  *   Create the designated "managing user" account with privileges to modify passwords for the application users:
      ```sql
      CREATE USER managing_user WITH PASSWORD 'manager_password';
      ALTER USER managing_user WITH CREATEROLE;
      GRANT user1 TO managing_user WITH ADMIN OPTION;
      GRANT user2 TO managing_user WITH ADMIN OPTION;
      ```

**Step 2: Bootstrap Rotation Infrastructure and Create ESC Environments**

To rotate credentials for PostgreSQL databases within AWS VPCs securely, you need to configure an [AWS Lambda function](/docs/esc/environments/rotation/aws-lambda/) within your VPC and create the corresponding ESC environments.

If your PostgreSQL instance is running on AWS RDS, we recommend using our [Pulumi New Project Wizard Template](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/esc-connector-lambda-typescript) to simplify the process of creating the Lambda function, associated AWS IAM Roles, Security Groups, and the basic ESC environment structure. You can start it from the [Pulumi console](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/esc-connector-lambda-typescript) or by running the following command in your terminal:

*   Run `pulumi new esc-connector-lambda-typescript` in your terminal.
*   This command initializes a new Pulumi project designed to provision the necessary AWS resources and create the ESC environments.
*   Follow the prompts. You will first provide a **Pulumi project name** (e.g., `my-db-rotation-infra`). Then, you will be prompted for configuration values like:
    *   Your target AWS Region (`aws:region`)
    *   The RDS Database Identifier (`rdsDbIdentifier`)
    *   The specific **name for the ESC rotation environment** (e.g., `postgresrotation/Rotator`). This environment will contain the two application users' credentials and configuration for rotation.
    *   The specific **name for the ESC managing credentials environment** (e.g., `postgresrotation/ManagingCreds`).
*   Run `pulumi up` to deploy the AWS resources and create the ESC environments with the names you provided.

**Step 3: Configure ESC Environments and Test**

The Pulumi template creates two ESC environments with most of the configuration pre-filled. You need to update them with your specific PostgreSQL user credentials and database name.

*   **Managing Credentials Environment (e.g., `postgresrotation/ManagingCreds`):** Navigate to this environment in the Pulumi Cloud console. Update the managing user's username and password. The `awsLogin` section should be pre-filled by the template.
  ```yaml
  # postgresrotation/ManagingCreds
  values:
    managingUser:
      username: managing_user # Replace with your managing user's name
      password:
        # Securely replace placeholder with your managing user's password using fn::secret
        fn::secret:
          ciphertext: ZXNjeA... # Replace with your encrypted password
    awsLogin:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::616138583583:role/PulumiEscSecretRotatorLambda-InvocationRole-7e4646f # Example Role ARN populated by template
          sessionName: pulumi-esc-secret-rotator-${esc.context.environment} # Example Session Name populated by template
  ```
*   **Rotation Environment (e.g., `<project-name>/Rotator`):** Navigate to this environment. Most fields are pre-filled by the template outputs (Lambda ARN, host, port, references). You *must* update the database name and the application usernames mapping.
  ```yaml
  # postgresrotation/Rotator
  values:
    dbRotator:
      fn::rotate::postgres:
        inputs:
          database:
            connector:
              awsLambda:
                login: ${environments.postgresrotation.ManagingCreds.awsLogin}
                lambdaArn: arn:aws:lambda:us-west-2:616138583583:function:PulumiEscSecretRotatorLambda-Function-d9932fe # Example Lambda ARN populated by template
            # Database connection details
            database: mydb # Replace with your DB name
            host: tf-20250428212643894700000001.cluster-chuqccm8uxqx.us-west-2.rds.amazonaws.com # Example Host populated by template
            port: 5432 # Example Port populated by template
            managingUser: ${environments.postgresrotation.ManagingCreds.managingUser}
          # List of application users whose passwords will be rotated
          rotateUsers:
            username1: user1 # Replace DB username if different from logical name
            username2: user2 # Replace DB username if different from logical name

        # state section is automatically managed by ESC after first rotation
        # Do not provide state unless migrating existing, known credentials.
        # state:
        #  current:
        #    password:
        #      fn::secret:
        #        ciphertext: ZXNjeAAAA...
        #    username: user1
        #  previous:
        #    password:
        #      fn::secret:
        #        ciphertext: ZXNje21AA...
        #    username: user2
  ```
*   **Test with Manual Rotation:**
      *   Use the triple-dot menu -> "Rotate Secrets" in the Pulumi Cloud UI for the Rotator environment.
      *   Alternatively, use the ESC CLI: `esc env rotate <your-project/Rotator>` (e.g., `esc env rotate postgresrotation/Rotator`).
      *   Perform a rotation. If you *didn't* provide the `state` block, this first rotation generates a new password for the user designated as `current` (e.g., `user1` associated with `username1`) and updates it in the database. The `dbRotator` value in ESC will now show this user/password under `current`, and the `state` block will be populated.
      *   Perform a *second* rotation. Observe how the previous `current` user (`user1`/`username1`) and its password become the `previous` entry in the ESC value. The system now rotates the password for the *other* user (`user2`/`username2`), makes it the new `current`, and updates the database accordingly. Subsequent rotations cycle between `user1` and `user2`.
      *   Check the Environment Revision History in the Pulumi Cloud console to track the changes to the `current` and `previous` state fields after each rotation.

**Step 4: Schedule Automated Rotations**

*   Once you are satisfied that manual rotations are working correctly, navigate to the "Secret Rotation" tab for your Rotator environment (e.g., `postgresrotation/Rotator`) in the Pulumi Cloud console.
*   Define your desired automated rotation schedule (e.g., every 30 days). ESC will automatically trigger rotations according to this schedule, ensuring your credentials stay fresh without manual intervention.

## What’s Next?

This launch significantly enhances database security posture through automation, but we're just getting started. We are actively working on expanding our rotated secrets capabilities:

*   **More Databases:** Support for MongoDB, Microsoft SQL Server, Oracle, and others.
*   **Databases in Private Networks on Other Clouds:** Rotation solutions for databases hosted in private networks within Azure and GCP.

Have a specific database or integration in mind? Upvote existing issues or open a new request in our [GitHub repository](https://github.com/pulumi/esc/issues)!

## Conclusion

Pulumi ESC's Automated Database Credential Rotation drastically simplifies a critical security task. By automating the rotation of **PostgreSQL**, **MySQL** (on AWS), and **Snowflake** credentials, ESC reduces operational overhead, minimizes the risk associated with static secrets, and helps you meet compliance requirements more easily. Whether your databases are in private networks or publicly accessible, ESC provides a unified way to manage their lifecycle.

We encourage you to explore the [Pulumi ESC documentation](placeholder-link-to-esc-docs) and try out rotated database secrets for [PostgreSQL](/docs/esc/integrations/rotated-secrets/postgres/), [MySQL](/docs/esc/integrations/rotated-secrets/mysql/), and [Snowflake](/docs/esc/integrations/rotated-secrets/snowflake-user/). Your feedback is invaluable – please share your experiences and suggestions on our [GitHub repository](https://github.com/pulumi/esc). Secure your databases with automated rotation and build with confidence!
