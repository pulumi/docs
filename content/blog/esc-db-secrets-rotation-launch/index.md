---
title: "Introducing Automated Database Credential Rotation in Pulumi ESC"
date: 2025-04-29T10:00:00-07:00 
allow_long_title: true
meta_desc: "Pulumi ESC now automates the rotation of database credentials for PostgreSQL, MySQL (on AWS), and Snowflake, enhancing security and reducing operational burden."
meta_image: meta.png
authors:
  - sean-yeh
  - arun-loganathan
tags:
  - esc
  - secrets
  - rotation
  - database
  - security

---

Securing access to critical data stores is paramount in today's cloud-native world. Yet, managing database credentials often involves static, long-lived passwords – a significant security blind spot. These static secrets, frequently embedded in application configurations or accessible to multiple team members, represent a prime target for attackers. Manually rotating these credentials is a cumbersome, error-prone task that’s often neglected, leaving databases vulnerable for extended periods. Building on our commitment to robust secrets management, we are excited to launch **Automated Database Credential Rotation** in [Pulumi ESC!](/product/esc)

<!--more-->

## The Persistent Challenge of Static Database Secrets

Relying on static database credentials introduces substantial risks, which automated rotation helps mitigate:

*   **Security Vulnerabilities & Exposure:** Static credentials, if compromised through leaks, phishing, or unauthorized access, provide long-term access to attackers. Automated rotation significantly shrinks this window of opportunity.
*   **Operational & Compliance Burdens:** Manually rotating database credentials is complex, error-prone, and requires careful coordination to avoid downtime. It also makes demonstrating compliance with regulations like SOC 2, GDPR, or HIPAA (which often mandate rotation) difficult and hard to audit consistently.
*   **Network Complexity:** Many databases reside within private networks (like AWS VPCs) for security. Rotating credentials for these databases typically requires bridging this network gap securely, often involving proxies, bastion hosts, or specific agents, adding significant setup and maintenance overhead for manual or homegrown solutions.

Pulumi ESC addresses these challenges by automating the rotation process, even for databases in private networks.

## Introducing ESC Rotated Secrets for Databases

Pulumi ESC’s Rotated Secrets capability now extends to your critical databases within your private VPCs, bringing automation and enhanced security to credential lifecycle management. We're launching support for:

*   **PostgreSQL** (Hosted on AWS, including RDS and Aurora instances)
*   **MySQL** (Hosted on AWS, including RDS and Aurora instances)
*   **Snowflake**

Here’s how ESC Rotated Secrets for Databases tackles the challenges:

*   **Automated Rotation Schedules:** Effortlessly define rotation frequencies (daily, weekly, monthly) that align with your security policies, eliminating manual toil and ensuring consistency.
*   **On-Demand Rotation:** Instantly rotate credentials in response to security events, personnel changes, or policy updates with a single click or command.
*   **Seamless ESC Environment Integration:** Manage rotated database credentials alongside all your other application configurations within ESC Environments, leveraging composition and environment inheritance.
*   **Two-Secret Strategy:** ESC maintains both the current and previous valid credentials simultaneously. This prevents application downtime during rotation, as instances can gracefully transition to the new credential.
*   **Auditing and Tracking:** Maintain a complete audit trail of credential rotations, including who initiated the rotation and when, simplifying compliance and governance.
*   **Admin and Creator Control:** Securely configure rotation using privileged database "managing user" credentials stored within ESC, keeping them separate from the rotated credentials consumed by applications.
*   **Configure Webhooks for Automation:** Trigger notifications, CI/CD pipelines (e.g., Pulumi Deployments to update application stacks), or custom workflows upon successful rotation, keeping dependent systems synchronized.

## How to set up and use PostGres and MySQL Rotations

**1. Bootstrap Rotation Infrastructure (for AWS PostgreSQL / MySQL):**

Rotating credentials for databases within AWS VPCs requires a secure mechanism. Pulumi ESC uses a dedicated AWS Lambda function deployed within your VPC for this. Use our [Pulumi New Project Wizard Template](https://app.pulumi.com/new?template=https://github.com/pulumi/esc-rotator-lambdas/blob/main/deploy/README.md#gh-dark-mode-only), or follow the steps in your terminal: 

*   Run `pulumi new esc-rotator-lambda` in your terminal.
*   This command initializes a new Pulumi project designed to provision the necessary AWS resources: the Lambda function, an execution IAM Role for the Lambda, an invocation IAM Role for ESC, and the required Security Group rules to allow the Lambda to communicate with your RDS instance.
*   Follow the prompts, providing configuration values like:
    *   Your target AWS Region (`aws:region`)
    *   The RDS Database Identifier (`esc-rotator-lambda:rdsDbIdentifier`)
    *   The name for the new ESC environment that will contain your rotation configuration (e.g., (`orders/prod-db-secrets-rotation`)
    *   *(Optional)* The name for a *separate* ESC environment to hold the privileged managing database credentials (e.g., `orders/prod-db-managingUser-creds`). 
*   Run `pulumi up` to deploy the resources
  
This template *also* creates ESC environment definition with most of the configuration population based on the resources created by the Pulumi Program. Note down the rotated secret environment Name and the managing creds Environment name. 

**2. Prepare Your Database:**

*   Ensure you have a designated "managing user" account in your database with privileges to modify passwords for other users (e.g., the `admin` user, or a custom user with specific grants, especially recommended for MySQL as shown in our docs).
*   Create the user account(s) (e.g., `user1`, `user2`) within your database whose passwords you want ESC to rotate automatically.

**3. Configure Your ESC Environment(s):**

*   **Managing Credentials Environment:** Navigate to this environment using the Pulumi Cloud console in step 1 and update the managing user's username and password.
    ```yaml
    # orders/prod-db-managingUser-creds
    values:
      dbAdmin:
        username: db_admin_user
        password:
          fn::secret: <your-secure-admin-password>
    ```
*   **Rotation Environment:** Navigate to the rotated secret environment.
    *   If you used the Pulumi Template to create this environment, you will notice that most of the required fields are filled out including: `connector.awsLambda`, `database`, `host`, `port`, `managingUser` credentials reference
    *   Replace the the user1 and user2 placeholder with actual database usernames.
    *   *(Optional)* If migrating existing credentials, populate the `state` block with the `current` and `previous` username/password pairs. Otherwise, ESC generates the first password on the initial rotation.

    *Example for AWS MySQL (using Lambda Connector & separate managing creds env):*
    ```yaml
    # orders/prod-db-secrets-rotation
    values:
      db-creds:
        fn::rotate::mysql:
          inputs:
            database:
              # Connector configured with outputs from the Pulumi template
              connector:
                awsLambda:
                  roleArn: <paste-role-arn-from-pulumi-output>
                  lambdaArn: <paste-lambda-arn-from-pulumi-output>
              # Database connection details
              database: my_database_name
              host: <my-database-endpoint.rds.amazonaws.com>
              port: 3306
              # Reference the imported managing user credentials
              managingUser:
                username: ${dbAdmin.username}
                password: ${dbAdmin.password}
            # List of users whose passwords will be rotated
            rotateUsers:
              appUser1: user1 # Logical name 'appUser1' maps to DB user 'user1'
              appUser2: user2 # Logical name 'appUser2' maps to DB user 'user2'
          # state section is optional - provide if migrating existing keys
          # state:
          #   current:
          #     username: user1
          #     password:
          #       fn::secret: existing_current_password
          #   previous:
          #     username: user2 # Note: The user being rotated changes here
          #     password:
          #       fn::secret: existing_previous_password
    ```

**4. Test with Manual Rotation:**

*   Use the triple-dot menu -> "Rotate Secrets" or go to the "Secret Rotation" tab.
*   Alternatively, use the ESC CLI: `esc env rotate <your/rotation/environment/name>`
*   Perform a rotation. If you didn't provide `state`, this will generate the first password for the `current` user (e.g., `user1`). The database password for `user1` will be updated.

**5. Monitor Rotations:**

*   Perform another rotation. Observe how the previous `current` user/password (`user1`) becomes the `previous` entry in the ESC value, and the system rotates the *next* user specified in `rotateUsers` (`user2`), making it the new `current`. The database password for `user2` is updated. Subsequent rotations cycle through the users listed in `rotateUsers`.
*   Check the Environment Revision History in the Pulumi Cloud console to track the changes to the `current` and `previous` state fields after each rotation.

**6. Schedule Automated Rotations:**

*   Once satisfied with the setup, navigate to the "Secret Rotation" tab for your environment in the Pulumi Cloud console.
*   Define your desired automated rotation schedule (e.g., every 30 days). ESC will automatically trigger rotations according to this schedule.

## What’s Next?

This launch significantly enhances database security posture through automation, but we're just getting started. We are actively working on expanding our rotated secrets capabilities:

*   **More Databases:** Support for MongoDB, Microsoft SQL Server, Oracle, and others.
*   **Broader Network Scenarios:** Rotation solutions for databases running in Azure and GCP private networks
  
Have a specific database or integration in mind? Upvote existing issues or open a new request in our [GitHub repository](https://github.com/pulumi/esc/issues)!

## Conclusion

Pulumi ESC's Automated Database Credential Rotation drastically simplifies a critical security task. By automating the rotation of PostgreSQL, MySQL (on AWS), and Snowflake credentials, ESC reduces operational overhead, minimizes the risk associated with static secrets, and helps you meet compliance requirements more easily.

We encourage you to explore the [Pulumi ESC documentation](placeholder-link-to-esc-docs) and try out rotated database secrets today. Your feedback is invaluable – please share your experiences and suggestions on our [GitHub repository](https://github.com/pulumi/esc). Secure your databases with automated rotation and build with confidence!
