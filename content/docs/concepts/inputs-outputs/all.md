---
title_tag: "Accessing Multple Outputs with All | Inputs and Outputs"
meta_desc: "Learn how to access multiple output values using the All method in Pulumi."
title: Accessing multiple outputs with All
h1: Accessing multiple outputs with All
meta_image: /images/docs/meta-images/docs-meta.png
menu:
  concepts:
    weight: 3
    parent: inputs-outputs
---

If you need to access and use multiple outputs together, the `all` function acts like an [`apply`](/docs/concepts/inputs-outputs/apply/) across many resources, allowing you to retrieve and use multiple outputs at the same time. The `all` function waits for all output values to become available and then provides them as _plain values_ to the {{< pulumi-apply >}} function.

This can be used to compute an entirely new output value, such as creating a new string by adding or concatenating outputs from two different resources together, or by creating a new data structure that uses their values. Just like with `apply`, the result of `all` is itself an Output<T>.

## Creating a new string

Outputs that return to the engine as strings cannot be used directly in operations such as string concatenation until the output value has returned to Pulumi. In these scenarios, you'll need to wait for the value to return using [`apply`](/docs/concepts/inputs-outputs/apply/).

To demonstrate, let’s say you have created a server resource and a database resource, and their output values are as follows:

```python
# Example outputs for the server resource
{
    "name": "myDbServer",
    "ipAddress": "10.0.0.0/24"
}

# Example outputs for the database resource
{
    "name": "myExampleDatabase",
    "engine": "sql-db"
}
```

From the outputs of these resources, you want to create a database connection string that uses the following format:

```bash
Server=tcp:<YourServerName>.database.windows.net,initial catalog=<YourDatabaseName>;
```

In the following example, you provide the name of the server and the name of the database as arguments to `all()`. Those arguments are made available to the {{< pulumi-apply >}} function and subsequently used to create the database connection string:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
var pulumi = require("@pulumi/pulumi");
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db};`);
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...
let connectionString = pulumi.all([sqlServer.name, database.name])
    .apply(([server, db]) => `Server=tcp:${server}.database.windows.net;initial catalog=${db};`);
```

{{% /choosable %}}

{{% choosable language python %}}

In python, you can pass in unnamed arguments to `Output.all` to create an Output list, for example:

```python
from pulumi import Output
# ...
connection_string = Output.all(sql_server.name, database.name) \
    .apply(lambda args: f"Server=tcp:{args[0]}.database.windows.net;initial catalog={args[1]};")
```

Or, you can pass in named (keyword) arguments to `Output.all` to create an Output dictionary, for example:

```python
from pulumi import Output
# ...
connection_string = Output.all(server=sql_server.name, db=database.name) \
    .apply(lambda args: f"Server=tcp:{args['server']}.database.windows.net;initial catalog={args['db']};")
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// ...
connectionString := pulumi.All(sqlServer.Name, database.Name).ApplyT(
    func (args []interface{}) pulumi.StringOutput  {
        server := args[0]
        db := args[1]
        return pulumi.Sprintf("Server=tcp:%s.database.windows.net;initial catalog=%s;", server, db)
    },
)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
//...

// When all the input values have the same type, Output.All can be used and produces an ImmutableArray.
var connectionString = Output.All(sqlServer.name, database.name)
    .Apply(t => $"Server=tcp:{t[0]}.database.windows.net;initial catalog={t[1]};");

// For more flexibility, 'Output.Tuple' is used so that each unwrapped value will preserve their distinct type.
var connectionString2 = Output.Tuple(sqlServer.name, database.name)
    .Apply(t => $"Server=tcp:{t.Item1}.database.windows.net;initial catalog={t.Item2};");

// Or using a more natural Tuple syntax and a statement lambda expression.
var connectionString3 = Output.Tuple(sqlServer.name, database.name).Apply(t =>
{
    var (serverName, databaseName) = t;
    return $"Server=tcp:{serverName}.database.windows.net;initial catalog={databaseName};";
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// ...

// When all the input values have the same type, Output.all can be used
var connectionString = Output.all(sqlServer.name(), database.name())
        .applyValue(t -> String.format("Server=tcp:%s.database.windows.net;initial catalog=%s;", t.get(0), t.get(1));

// For more flexibility, 'Output.tuple' is used so that each unwrapped value will preserve their distinct type.
var connectionString2 = Output.tuple(sqlServer.name, database.name)
        .applyValue(t -> String.format("Server=tcp:%s.database.windows.net;initial catalog=%s;", t.t1, t.t2));
```

{{% /choosable %}}

{{% choosable language yaml %}}

YAML does not have the `Apply` or `All` functions. Instead, you can access property values directly.

```yaml
variables:
  connectionString: Server=tcp:${sqlServer.name}.database.windows.net;initial catalog=${database.name};
```

{{% /choosable %}}

{{< /chooser >}}

The `all` function works by returning an output that represents the combination of multiple outputs. Based on the example output values provided above, the final value of the generated connection string will resemble the following:

```bash
Server=tcp:myDbServer.database.windows.net;initial catalog=myExampleDatabase;
```

### Using string interpolation

There is an easier way to generate a concatenated string value using multiple outputs, and that is by using interpolation. Pulumi exposes interpolation helpers that enables you to create strings that contain outputs. These interpolation methods wrap [all](/docs/concepts/inputs-outputs/all/) and [apply](/docs/concepts/inputs-outputs/apply/) with an interface that resembles your language's native string formatting functions. The example below demonstrates how to create a URL from the hostname and port output values of a web server.

{{< example-program path="aws-s3bucket-bucketobject-interpolate" >}}

You can use string interpolation to do things like export a [stack output](/docs/using-pulumi/stack-outputs-and-references/) or provide a dynamically computed string as a new resource argument.

## Creating a new data structure

In addition to strings, the `all` function can also be used to create new data structures such as:

- Lists | Arrays | Slices
- Dicts | Objects | Maps

Using the same example server and database resources and their corresponding output values, you can see this demonstrated in the example below:

{{< chooser language "javascript,typescript,python,go,csharp,java,yaml" >}}

{{% choosable language javascript %}}

```javascript
const pulumi = require("@pulumi/pulumi");
// ...

// An example of creating a new Output of type Object
const connectionDetails = pulumi.all([sqlServer.ipAddress, database.port])
    .apply(([serverIp, databasePort]) => ({
        server_ip: serverIp,
        database_port: databasePort,
    })
);

// An example of creating a new Output of type Array
const connectionDetails = pulumi.all([server.ipAddress, database.port])
    .apply(([ip, port]) => [ip, port]);
```

{{% /choosable %}}

{{% choosable language typescript %}}

```typescript
import * as pulumi from "@pulumi/pulumi";
// ...

// An example of creating a new Output of type Dictionary
let connectionDetails = pulumi.all([server.ipAddress, database.port])
    .apply(([ip, port]) => {
        return {
            serverIp: ip,
            databasePort: port,
        };
    }
);

// An example of creating a new Output of type Array
let connectionDetails = pulumi.all([server.ipAddress, database.port])
    .apply(([ip, port]) => {
        return [ip, port];
    }
);
```

{{% /choosable %}}

{{% choosable language python %}}

```python
from pulumi import Output
# ...

# An example of creating an Output of type Dict
connection_details = Output.all(sql_server.ipAddress, database.port) \
    .apply(lambda args: {
        "server_ip": args[0],
        "database_port": args[1]
    })

# An example of creating an Output of type List
connection_details = Output.all(sql_server.ipAddress, database.port) \
    .apply(lambda args: [args[0], args[1]])
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// ...

// An example of creating an Output of type Map
connectionDetails := pulumi.All(sqlServer.IpAddress, database.Port).ApplyT(
    func(args []interface{}) map[string]interface{} {
    	ipAddress := args[0].(string)
		port := args[1].(string)
    	return map[string]interface{}{
    		"server_ip":     ipAddress),
    		"database_port": port,
    	}
    }
)

// An example of creating an Output of type Array
connectionDetails := pulumi.All(sqlServer.IpAddress, database.Port).ApplyT(
    func(args []interface{}) []interface{} {
		return args
	}).(pulumi.ArrayOutput)
```

{{% /choosable %}}

{{% choosable language csharp %}}

```csharp
//...

// An example of creating an Output of type Dictionary
var connectionDetails = Output.All(sqlServer.IpAddress, database.Port).Apply(values =>
{
    var ipAddress = values[0];
    var port = values[1];
    return new Dictionary<string, object>
    {
        {"serverIp", ipAddress},
        {"port", port}
    };
});

// An example of creating an Output of type List
var connectionDetails = Output.All(sqlServer.IpAddress, database.Port).Apply(values =>
{
    var ipAddress = values[0];
    var port = values[1];
    return new List<object> { ipAddress, port };
});
```

{{% /choosable %}}

{{% choosable language java %}}

```java
// ...

// An example of creating an Output of type Map
var connectionDetails = Output.tuple(sqlServer.ipAddress(), database.port())
    .applyValue(t -> Map.of("ServerIp", t.t1, "DatabasePort", t.t2));

// An example of creating an Output of type List
var connectionDetails2 = Output.tuple(sqlServer.ipAddress(), database.port())
    .applyValue(t -> List.of(t.t1, t.t2));
```

{{% /choosable %}}

{{% choosable language yaml %}}

YAML does not have the `Apply` or `All` functions. Instead, you can access property values directly.

```yaml
This example is not applicable in Pulumi YAML.
```

{{% /choosable %}}

{{< /chooser >}}

## Creating a JSON object

You can also [create JSON objects](/docs/concepts/inputs-outputs/apply/#outputs-and-json) using multiple output values in Pulumi. Doing so requires the use of `apply` or one of Pulumi's [JSON-specific helpers](/docs/concepts/inputs-outputs/apply/#converting-outputs-to-json).

{{< example-program path="aws-s3websitebucket-oai-bucketpolicy" >}}
