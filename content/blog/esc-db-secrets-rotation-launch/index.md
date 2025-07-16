---
title: "Introducing Automated Database Credential Rotation for PostgreSQL and MySQL in Pulumi ESC"
date: 2025-04-30 
allow_long_title: true
meta_desc: "Pulumi ESC now automates the rotation of database credentials for PostgreSQL and MySQL (publicly accessible or in AWS private VPCs), enhancing security and reducing operational burden."
meta_image: meta.png
authors:
- sean-yeh
- iaroslav-titov
- arun-loganathan
tags:
- esc
- secrets
- features
- rotation
- database
- security
---

Securing access to critical data stores is paramount in today's cloud-native world. Yet, managing database credentials often involves static, long-lived passwords – a significant security blind spot. These static secrets, frequently embedded in application configurations or accessible to multiple team members, represent a prime target for attackers. Manually rotating these credentials is a cumbersome, error-prone task that’s often neglected, leaving databases vulnerable for extended periods. Building on our commitment to robust secrets management, we are excited to launch **Automated Database Credential Rotation** for **PostgreSQL and MySQL** in [Pulumi ESC!](/product/esc)

<!--more-->

## The Persistent Challenge of Static Database Secrets

Relying on static database credentials introduces substantial risks, which automated rotation helps mitigate:

*   **Security Vulnerabilities & Exposure:** Static credentials, if compromised through leaks, phishing, or unauthorized access, provide long-term access to attackers. Automated rotation significantly shrinks this window of opportunity.
*   **Operational & Compliance Burdens:** Manually rotating database credentials is complex, error-prone, and requires careful coordination to avoid downtime. These manual rotations are hard to audit and demonstrate compliance with regulations like SOC 2, GDPR, or HIPAA (which often mandate rotation).
*   **Network Complexity & The DIY Burden:** Databases in private networks (like AWS VPCs) require secure access for rotation. We provide an open-source **Lambda connector** for AWS VPCs. While homegrown solutions can bridge the network gap, building and maintaining the *actual rotation logic* (state, error handling, two-secret strategy) is complex. Crucially, DIY approaches typically lack integrated revision history, centralized auditing, and unified management provided by platforms like Pulumi ESC, increasing operational overhead.
*   **Tooling, Ecosystem, and Cloud-Native Connectivity:** Despite cloud IAM authentication options, many standard tools (GUIs, BI, ETL), legacy apps, and even certain cloud-native configurations (multi-cloud, specific Kubernetes setups) still rely on username/password. Direct IAM integration isn't always feasible or practical, making automated rotation of traditional credentials essential for broad compatibility and security.

Pulumi ESC addresses these challenges by automating the secrets rotation process, including connectivity options for databases in private AWS networks using our Lambda connector, and allows you to consume them in your applications through ESC's various developer-friendly methods including [ESC SDK](/docs/esc/development/languages-sdks/), [ESC CLI](/docs/esc/cli/), [Kubernetes External Secrets Operator](/docs/esc/integrations/kubernetes/external-secrets-operator/), [CSI Driver](/docs/esc/integrations/kubernetes/secret-store-csi-driver/), etc.

## Introducing ESC Rotated Secrets for Databases

Pulumi ESC’s [Rotated Secrets](/docs/esc/integrations/rotated-secrets/) capability now extends to your critical databases, bringing automation and enhanced security to credential lifecycle management. We are adding support for the following databases and connectivity options:

| Database                                                         | Publicly Accessible | AWS VPCs               | Azure VNETs                                                                  | GCloud VPCs                                                                  |
| :--------------------------------------------------------------- | :------------------: | :---------------------: | :---------------------------------------------------------------------------: | :---------------------------------------------------------------------------: |
| [**PostgreSQL**](/docs/esc/integrations/rotated-secrets/postgres/) | ✅                  | ✅ <small>(via Lambda)</small> | Planned <small>([upvote issue](https://github.com/pulumi/esc/issues/521))</small> | Planned <small>([upvote issue](https://github.com/pulumi/esc/issues/522))</small> |
| [**MySQL**](/docs/esc/integrations/rotated-secrets/mysql/)       | ✅                  | ✅ <small>(via Lambda)</small> | Planned <small>([upvote issue](https://github.com/pulumi/esc/issues/521))</small> | Planned <small>([upvote issue](https://github.com/pulumi/esc/issues/522))</small> |


Key benefits include:

*   **Automated Rotation Schedules:** Effortlessly define rotation frequencies (daily, weekly, monthly) that align with your security policies, eliminating manual toil and ensuring consistency.
*   **On-Demand Rotation:** Instantly rotate credentials in response to security events, personnel changes, or policy updates with a single click or command.
*   **Seamless ESC Environment Integration:** Manage rotated database credentials alongside all your other application configurations within ESC Environments, leveraging composition and environment inheritance.
*   **Two-Secret Strategy:** ESC maintains both the current and previous valid credentials simultaneously. This prevents application downtime during rotation, as instances can gracefully transition to the new credential.
*   **Auditing and Tracking:** Maintain a complete audit trail of credential rotations, including who initiated the rotation and when, simplifying compliance and governance.
*   **Admin and Creator Control:** Securely configure rotation using privileged database "managing user" credentials stored within ESC, keeping them separate from the rotated credentials consumed by applications.
*   **Configure Webhooks for Automation:** Trigger notifications, CI/CD pipelines (e.g., Pulumi Deployments to update application stacks), or custom workflows upon successful rotation, keeping dependent systems synchronized.

{{% notes type="info" %}}
The following setup guide provides a detailed walkthrough for rotating [**PostgreSQL**](/docs/esc/integrations/rotated-secrets/postgres/) credentials for an **AWS RDS instance hosted within a private VPC**, which requires the AWS Lambda-based connector. For publicly accessible databases (PostgreSQL or MySQL), you can use the simpler **Direct Connect** method documented on the respective integration pages. Please refer to the [**MySQL**](/docs/esc/integrations/rotated-secrets/mysql/) documentation page for specific instructions on MySQL rotation (both Direct Connect and Lambda Connector).
{{% /notes %}}

## How to Set Up and Use Rotation for AWS RDS PostgreSQL running in VPC

Setting up rotation for AWS RDS or Aurora PostgreSQL databases running inside an AWS VPC involves [creating the required users](/docs/esc/environments/rotation/db-user-setup/) within your database, deploying the AWS Lambda connector infrastructure via a Pulumi template, configuring ESC environments, and scheduling the rotation.

**Understanding the AWS Lambda Connector:** The open-source [ESC Lambda connector](https://github.com/pulumi/templates/tree/master/esc-connector-lambda-typescript) acts as a secure proxy for database credential rotation within your VPC. It enables Pulumi ESC to safely rotate database credentials without needing direct network access from ESC to your database and without exposing your database to external networks. This connector is currently required to rotate credentials for PostgreSQL or MySQL databases hosted within an AWS VPC. Note: The AWS Lambda Connector is only available to Enterprise and Business Critical customers.

**Step 1: Prepare Your PostgreSQL Database Users**

You'll need two *types* of users configured, resulting in *three* specific database user accounts:

1.  **Managing User:** A privileged user that ESC will use (via the Lambda connector) to perform the password rotations. This user needs permissions to change the passwords of the application users.
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

**Step 2: Bootstrap Rotation Infrastructure (Lambda Connector) and Create ESC Environments**

To rotate credentials for PostgreSQL databases within AWS VPCs securely, you need to configure an [AWS Lambda function (the connector)](/docs/esc/environments/rotation/aws-lambda/) within your VPC and create the corresponding ESC environments.

If your PostgreSQL instance is running on AWS RDS, we recommend using our [Pulumi Template](https://github.com/pulumi/templates/tree/master/esc-connector-lambda-typescript) to simplify the process of creating the Lambda function, associated AWS IAM Roles, Security Groups, and the basic ESC environment structure. You can start it from the [Pulumi console](https://app.pulumi.com/new?template=https://github.com/pulumi/templates/esc-connector-lambda-typescript) or by running the following command in your terminal:

*   Run `pulumi new esc-connector-lambda-typescript` in your terminal.
*   This command initializes a new Pulumi project designed to provision the necessary AWS Lambda connector resources and create the ESC environments.
*   Follow the prompts. You will first provide a **Pulumi project name** (e.g., `my-db-rotation-infra`). Then, you will be prompted for configuration values like:
    *   Your target AWS Region (`aws:region`)
    *   The RDS Database Identifier (`rdsDbIdentifier`)
    *   The specific **name for the ESC rotation environment** (e.g., `postgresrotation/Rotator`). This environment will contain the two application users' credentials and configuration for rotation.
    *   The specific **name for the ESC managing credentials environment** (e.g., `postgresrotation/ManagingCreds`).
*   Run `pulumi up` to deploy the AWS resources and create the ESC environments using the names you provided.

**Step 3: Configure ESC Environments and Test**

The Pulumi template creates two ESC environments with most of the configuration pre-filled. You need to update them with your specific PostgreSQL user credentials and database name.

*   **Managing Credentials Environment (e.g., `postgresrotation/ManagingCreds`):** Navigate to this environment in the Pulumi Cloud console. Update the managing user's username and password. The `awsLogin` section, which provides credentials for the Lambda connector to assume, should be pre-filled by the template.
  ```yaml
  # postgresrotation/ManagingCreds
  values:
    managingUser:
      username: managing_user # Replace with your managing user's name
      password:
        # Securely replace the placeholder with your managing user's password using fn::secret
        fn::secret:
          ciphertext: ZXNjeA... # Replace with your encrypted password
    awsLogin:
      fn::open::aws-login:
        oidc:
          duration: 1h
          roleArn: arn:aws:iam::616138583583:role/PulumiEscSecretRotatorLambda-InvocationRole-7e4646f # Example Role ARN populated by template
          sessionName: pulumi-esc-secret-rotator-${esc.context.environment} # Example Session Name populated by template
  ```
*   **Rotation Environment (e.g., `<project-name>/Rotator`):** Navigate to this environment. Most fields related to the Lambda connector (Lambda ARN, host, port, references) are pre-filled by the template outputs. You *must* update the database name and the application usernames mapping. Note the `connector.awsLambda` block indicating the use of the Lambda connector.
  ```yaml
  # postgresrotation/Rotator
  values:
    dbRotator:
      fn::rotate::postgres:
        inputs:
          database:
            # Configure the AWS Lambda connector for private VPC access
            connector:
              awsLambda:
                login: ${environments.postgresrotation.ManagingCreds.awsLogin}
                lambdaArn: arn:aws:lambda:us-west-2:616138583583:function:PulumiEscSecretRotatorLambda-Function-d9932fe # Example Lambda ARN populated by template
            # Database connection details (used by the Lambda connector)
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
      *   Alternatively, use the ESC CLI: `esc env rotate <your-org>/<project-name>/Rotator>` (e.g., `esc env rotate myorg/postgresrotation/Rotator`). Remember to replace `<your-org>` and `<project-name>`.
      *   Perform a rotation. If you *didn't* provide the `state` block, this first rotation generates a new password for the user designated as `current` (e.g., `user1` associated with `username1`) and updates it in the database via the Lambda connector. The `dbRotator` value in ESC will now show this user/password under `current`, and the `state` block will be populated.
      *   Perform a *second* rotation. Observe how the previous `current` user (`user1`/`username1`) and its password become the `previous` entry in the ESC value. The system now rotates the password for the *other* user (`user2`/`username2`), makes it the new `current`, and updates the database accordingly. Subsequent rotations cycle between `user1` and `user2`.
      *   Check the Environment Revision History in the Pulumi Cloud console to track the changes to the `current` and `previous` state fields after each rotation.

**Step 4: Schedule Automated Rotations**

*   Once you are satisfied that manual rotations via the Lambda connector are working correctly, navigate to the "Secret Rotation" tab for your Rotator environment (e.g., `postgresrotation/Rotator`) in the Pulumi Cloud console.
*   Define your desired automated rotation schedule (e.g., every 30 days). ESC will automatically trigger rotations according to this schedule, ensuring your credentials stay fresh without manual intervention.

## What’s Next?

This launch significantly enhances database security posture through automation for PostgreSQL and MySQL, but we're just getting started. We plan to expand our rotated secrets capabilities:

*   **More Databases:** Support for [MongoDB](https://github.com/pulumi/esc/issues/525), [Microsoft SQL Server](https://github.com/pulumi/esc/issues/526), [Oracle](https://github.com/pulumi/esc/issues/527), and others.
*   **Databases in Private Networks on Other Clouds:** Rotation solutions for databases hosted in private networks within [Azure](https://github.com/pulumi/esc/issues/521), [Google Cloud](https://github.com/pulumi/esc/issues/522), and more.

Have a specific database or integration in mind? Upvote existing issues or open a new request in our [GitHub repository](https://github.com/pulumi/esc/issues)!

## Conclusion

Pulumi ESC's Automated Database Credential Rotation drastically simplifies a critical security task. By automating the rotation of **PostgreSQL** and **MySQL** credentials, ESC reduces operational overhead, minimizes the risk associated with static secrets, and helps you meet compliance requirements more easily. Whether your databases are publicly accessible (using Direct Connect) or in private AWS networks (using the Lambda connector), ESC provides a unified way to manage their lifecycle securely.

We encourage you to explore the [Pulumi ESC documentation](/docs/esc/) and try out rotated database secrets for [PostgreSQL](/docs/esc/integrations/rotated-secrets/postgres/) and [MySQL](/docs/esc/integrations/rotated-secrets/mysql/). Your feedback is invaluable – please share your experiences and suggestions on our [GitHub repository](https://github.com/pulumi/esc). Secure your databases with automated rotation and build with confidence!
