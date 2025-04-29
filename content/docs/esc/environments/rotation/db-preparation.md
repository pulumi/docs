---
title: Database Preparation
title_tag: Database Preparation
meta_desc: Explanation on how to prepare the database for credentials rotation
h1: Database Preparation
menu:
  esc:
    identifier: db-preparation
    parent: esc-rotating-secrets
    weight: 1
---

In order to create an [ESC rotator for database credentials](/docs/esc/integrations/rotated-secrets), you need to prepare users in the database. To start, connect to your existing database or provision a new one.

## User setup

First, you need to provision users that will be rotated. If you already have 2 existing users you can use those, otherwise run commands below to setup simple users. Make sure to replace `yourDatabase` with your database name and adjust privileges as needed! You can also adjust the initial password to anything you'd like.

### MySQL

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

### PostgreSQL

```
CREATE USER user1 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user1;
CREATE USER user2 WITH PASSWORD 'initial_password';
GRANT SELECT, INSERT, UPDATE ON yourDatabase TO user2;
```

## Managing user

Next, you need to setup a managing user, who will be in charge of actually rotating passwords for the 2 users we created above. Pulumi ESC will have access to this user, so we will scope down this user's privileges to a minimum. Same as above, replace `yourDatabase` with your database name and `manager_password` with anything you'd like, just make sure to memorize or note it down somewhere.

### MySQL

```
CREATE USER IF NOT EXISTS 'managing_user'@'%' IDENTIFIED BY 'manager_password';
GRANT ALTER ON yourDatabase.* TO 'managing_user'@'%';
GRANT CREATE USER ON *.* TO 'managing_user'@'%';
```

### PostgreSQL

```
CREATE USER managing_user WITH PASSWORD 'manager_password';
ALTER USER managing_user WITH CREATEROLE;
GRANT user1 TO managing_user WITH ADMIN OPTION;
GRANT user2 TO managing_user WITH ADMIN OPTION;
```

That is all, your database users are ready for rotation. Check out the [Rotation Connectors](/docs/esc/environments/rotation#rotation-connectors) section for next steps.
