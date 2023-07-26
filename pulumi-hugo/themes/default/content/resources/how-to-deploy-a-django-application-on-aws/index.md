---
title: "How to host a Django application on AWS"
allow_long_title: true
meta_desc: "Deploy Django on AWS with our pulumi example. Ideal for developers and DevOps, improve scalability and performance of Python web apps."
type: ai-answers
date: 2023-07-24
---

Sure! To host a Django application on AWS, you can use a combination of AWS services, specifically AWS Elastic Beanstalk, S3, and RDS.

The aws.elasticbeanstalk.Application and aws.elasticbeanstalk.Environment resources handle the deployment and hosting of your Django application.

For static files, we will use aws.s3.Bucket and for the database, we will use aws.rds.Instance.

Let's get started!

Here's a simple Pulumi program in Python that will create an Elastic Beanstalk application:

```python

import pulumi
from pulumi_aws import elasticbeanstalk, s3, rds

# Create an Elastic Beanstalk Application
application = elasticbeanstalk.Application('django_application',
    description="A Django application")

# Create a S3 bucket for the static files
static_bucket = s3.Bucket('my-static-bucket')

# Create a database instance
db_instance = rds.Instance('my-database-instance',
    engine='postgres', # use postgres engine 
    instance_class='db.t2.micro', # define the instance class
    allocated_storage=20, # define the allocated storage in gigabytes
    engine_version='11', # define the engine version
    name='mydatabase', # instance name
    username='admin', username
    password='adminpassword', # password. Make sure to use a strong password in production.
    skip_final_snapshot=True) # set to False in production

# Create an Elastic Beanstalk Environment
environment = elasticbeanstalk.Environment('django_env',
    application=application.name,
    solution_stack_name="64bit Amazon Linux 2018.03 v2.15.0 running Python 3.6")

# Export the DNS name of the
pulumi.export("bucket_name",static_bucket.bucket)
# Export the RDS instance endpoint
pulumi.export("db_endpoint",db_instance.endpoint)
# the EB environment URL
pulumi.export("django_env_url", environment.application)
```

Please replace the username, password, etc. in the script to suit your environment.

Remember to update the Django settings.py to connect to the RDS instance and the S3 bucket for static files.

The above script will create an Elastic Beanstalk application environment, a S3 bucket for static files, and a RDS Postgres database instance. The DNS names and endpoints are then exported for you to use in your Django configuration.

For more information, check the following Pulumi Registry documentation:

* [aws.elasticbeanstalk.Application](https://www.pulumi.com/registry/packages/aws/api-docs/elasticbeanstalk/application/)
* [aws.elasticbeanstalk.Environment](https://www.pulumi.com/registry/packages/aws/api-docs/elasticbeanstalk/environment/)
* [aws.s3.Bucket](https://www.pulumi.com/registry/packages/aws/api-docs/s3/bucket/)
* [aws.rds.Instance](https://www.pulumi.com/registry/packages/aws/api-docs/rds/instance/)