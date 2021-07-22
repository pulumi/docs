---
title: "Automate Your Infrastructure with Automation API and Python"
date: 2021-02-09
meta_desc: "Combine the power of Automation API with the flexibility of Python"
meta_image: automation_api.png
authors:
- sophia-parafina
tags:
- Automation API
- Python
---

General-purpose languages enable [Infrastructure as Software]({{< relref "/what-is/what-is-infrastructure-as-software" >}}) -- bringing tested toolchains and best practices to building infrastructure, e.g., languages, IDEs, testing, debugging, componentization, packaging, and versioning. Available in public preview, Pulumi's Automation API is a robust programmatic layer on top of Pulumi's infrastructure engine. It exposes Pulumi programs and stacks as strongly-typed and composable building blocks. Automation API allows you to embed the Pulumi engine inside your software projects so you can build software automation around entire infrastructure provisioning processes that normally require humans to operate.

Today, we are excited to announce Python support for this powerful feature, opening up a world of possibilities for Python developers.

<!--more-->

## Enabling Cloud Engineering

The Automation API is a subpackage in Pulumi’s language-specific SDKs that provides a programmable interface for creating and managing [Stacks]({{< relref "/docs/intro/concepts/stack" >}}) and performing infrastructure updates, refresh, previews, and destroy. You can define a Pulumi program as a function within your codebase and use methods to get and set configuration parameters programmatically. The Automation API uses a gRPC interface to execute programs that control and communicate with the core Pulumi engine.

To use Automation API, install the Pulumi CLI, which bundles and distributes the core engine. Today it’s available for [Python](https://github.com/pulumi/pulumi/tree/master/sdk/python/lib/pulumi/automation), [TypeScript/JavaScript](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/automation) and [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v3/go/auto), with support for [C#](https://github.com/pulumi/pulumi/compare/auto/dotnet) under active development.

## Automation Use Cases

Let's look at two use cases where Pulumi customers are applying the Automation API:

### Platform APIs

Deploying infrastructure with shell scripts for online services creates operational challenges with observability and reliability, especially for SaaS scenarios. Automation API is just another package and can be instrumented, profiled, and monitored with your existing APM tools like Honeycomb, Prometheus, and Datadog.

Automation API runs inside your favorite frameworks and interacts with your other packages precisely as you’d expect. We can define custom declarative infrastructure and expose it to end-users behind a familiar REST interface, as in this example, that creates an S3 website with a POST request.

```python
# an HTTP handler to create instances of our declarative infra
# each request creates an S3-backed static website with dynamic content from the POST body
@app.route("/sites", methods=["POST"])
def create_handler():
    """creates new sites"""
    stack_name = request.json.get('id')
    content = request.json.get('content')
    try:
        def pulumi_program():
            return create_pulumi_program(content)
        # create a new stack, generating our pulumi program on the fly from the POST body
        stack = auto.create_stack(stack_name=stack_name,
                                  project_name=project_name,
                                  program=pulumi_program)
        stack.set_config("aws:region", auto.ConfigValue("us-west-2"))
        # deploy the stack, tailing the logs to stdout
        up_res = stack.up(on_output=print)
        return jsonify(id=stack_name, url=up_res.outputs['website_url'].value)
    except auto.StackAlreadyExistsError:
        return make_response(f"stack '{stack_name}' already exists", 409)
    except Exception as exn:
        return make_response(str(exn), 500)
```

The handlers work with your favorite HTTP frameworks, including `flask`:

```python
import Flask

# install necessary plugins once upon boot
ensure_plugins()

# initialize our Flask app
app = Flask(__name__)

# set up our routes
@app.route("/sites", methods=["POST"])
def create_handler():
    ...

@app.route("/sites", methods=["GET"])
def list_handler():
    ...

@app.route("/sites/<string:id>", methods=["GET"])
def get_handler(id: str):
    ...

@app.route("/sites/<string:id>", methods=["UPDATE"])
def update_handler(id: str):
    ...

@app.route("/sites/<string:id>", methods=["DELETE"])
def delete_handler(id: str):
    ...
```

Check out the full `Pulumi over HTTP` example in [Python](https://github.com/pulumi/automation-api-examples/tree/main/python/pulumi_over_http).

### Complex Workflow Orchestration

The Automation API executes just like any other code in your application, meaning that a single process can deploy infrastructure and manage related activities such as database migrations and blue/green deployments.

In this example, we define an AWS RDS database:

```python
cluster_instance = aws.rds.ClusterInstance(
    "db_instance",
    cluster_identifier=cluster.cluster_identifier,
    instance_class=aws.rds.InstanceType.T3_SMALL,
    engine=aws.rds.EngineType.AURORA_MYSQL,
    engine_version="5.7.mysql_aurora.2.03.2",
    publicly_accessible=True,
    db_subnet_group_name=subnet_group.name
)

pulumi.export("host", cluster.endpoint)
pulumi.export("db_name", db_name)
pulumi.export("db_user", db_user)
pulumi.export("db_pass", db_pass)
```

With Automation API, we can perform database migrations and preload rows in the same program:

```python
# create (or select if one already exists) a stack that uses our inline program
stack = auto.create_or_select_stack(stack_name=stack_name,
                                    project_name=project_name,
                                    program=pulumi_program)

up_res = stack.up(on_output=print)
print(f"db host url: {up_res.outputs['host'].value}")

print("configuring db...")
with connect(
        host=up_res.outputs['host'].value,
        user=up_res.outputs['db_user'].value,
        password=up_res.outputs['db_pass'].value,
        database=up_res.outputs['db_name'].value) as connection:
    print("db configured!")

    # make sure the table exists
    print("creating table...")
    create_table_query = """CREATE TABLE IF NOT EXISTS hello_pulumi(
        id int(9) NOT NULL PRIMARY KEY,
        color varchar(14) NOT NULL);
        """
    with connection.cursor() as cursor:
        cursor.execute(create_table_query)
        connection.commit()

```

See the full database deployment and migration Automation API program in [Python](https://github.com/pulumi/automation-api-examples/tree/main/python/database_migration).

## Automation API Resources

To get started with Automation API check out these links and watch our video.

- [Python documentation]({{< relref "/docs/reference/pkg/python/pulumi#module-pulumi.x.automation" >}})
- [Automation API examples](https://github.com/pulumi/automation-api-examples#python-examples)

{{< youtube "8XFjqzX9ZK4" >}}

Automation API is still in alpha. We maintain a list of [known issues](https://github.com/pulumi/pulumi/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%2Fautomation-api). Please [file more](https://github.com/pulumi/pulumi/issues/new?assignees=&labels=needs-triage&template=bug_report.md&title=) as you find them!

🏭 🏭 🏭 Happy automating! 🏭 🏭 🏭
