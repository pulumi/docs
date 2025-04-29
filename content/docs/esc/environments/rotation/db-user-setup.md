---
title: Database User Setup
title_tag: Database User Setup
meta_desc: Explanation on how to prepare the database for credentials rotation
h1: Database User Setup
menu:
  esc:
    identifier: db-user-setup
    parent: esc-rotating-secrets
    weight: 1
---

In order to create an [ESC rotator for database credentials](/docs/esc/integrations/rotated-secrets), you need to prepare 2 users to rotate and a managing user. To start, connect to your existing database or provision a new one. The following sections will explain why we need these users and provide sample SQL commands to easily create them in your database.

## Rotated users

First, you need to provision 2 users whose passwords will be rotated. You need two to always have one as the active user while the other is being rotated and vice versa, ensuring 100% uptime. If you already have 2 existing users with correct privileges, you can use those. Otherwise, use commands below to setup simple users. Make sure to replace `yourDatabase` with your database name and adjust privileges as needed. You can also adjust the initial password to anything you'd like.

## Managing user

Second, you need to setup a managing user, who will have the permissions to actually rotate passwords for the 2 rotated users we discussed above. Pulumi ESC will have access to this user, so we will scope down this user's privileges to a minimum. Same as above, replace `yourDatabase` with your database name and `manager_password` with anything you'd like, just make sure to memorize or note it down somewhere.

## MySQL

Commands to create rotated users:

```
CREATE USER IF NOT EXISTS 'user1'@'%' IDENTIFIED BY 'initial_password';
GRANT SELECT, INSERT, UPDATE
    ON yourDatabase.*
    TO 'user1'@'%';
CREATE USER IF NOT EXISTS 'user2'@'%' IDENTIFIED BY 'initial_password';
GRANT SELECT, INSERT, UPDATE
    ON yourDatabase.*
    TO 'user2'@'%';
```

Commands to create the managing user:

```
CREATE USER IF NOT EXISTS 'managing_user'@'%' IDENTIFIED BY 'manager_password';
GRANT ALTER ON yourDatabase.* TO 'managing_user'@'%';
GRANT CREATE USER ON *.* TO 'managing_user'@'%';
```

## PostgreSQL

Commands to create rotated users:

```
CREATE USER user1 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user1;
CREATE USER user2 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user2;
```

Commands to create the managing user:

```
CREATE USER managing_user WITH PASSWORD 'manager_password';
ALTER USER managing_user WITH CREATEROLE;
GRANT user1 TO managing_user WITH ADMIN OPTION;
GRANT user2 TO managing_user WITH ADMIN OPTION;
```

## Next steps

That is all, your database users are ready for rotation. Check out the [Rotation Connectors](/docs/esc/environments/rotation#rotation-connectors) section for next steps.
