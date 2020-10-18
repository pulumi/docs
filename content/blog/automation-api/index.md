---
title: "The Pulumi Automation API - The Next Quantum Leap in IaC"
date: 2020-10-10
meta_desc: "Introducing the Pulumi Automation API - Scaling Cloud Projects with Software, Not Humans"
meta_image: automation_api.png
authors:
    - evan-boyle
tags:
    - automation api
---

Today’s Infrastructure as Code platforms have enabled organizations to build rich, reliable, and complex cloud-based applications and architectures. But as teams move to modern cloud technologies and reorganize their engineering organizations to get the full power and agility of the cloud, they continue looking for ways to drive increased software-driven automation.  While modern Infrastructure as Code tools bring key software engineering benefits to cloud engineering, they remain focused on human-driven workflows. For example, a person running `pulumi up` at their terminal or wiring the Pulumi CLI into their CI/CD system. To scale up how we deploy and manage cloud infrastructure and ultimately unlock the cloud's value and agility, we believe it will be critical to building software systems around our Infrastructure as Code platforms - systems that scale with software, not just humans.

Pulumi's approach of using general purpose languages enables a new way of doing Infrastructure as Code -- something we call Infrastructure as Software -- bringing all of the great lessons learned over decades of building software to your infrastructure (languages, IDEs, testing, debugging, componentization, packaging, versioning, and more).

Today we’re excited to announce the Pulumi Automation API, a powerful programmatic layer on top of Pulumi’s declarative Infrastructure as Software. The Automation API exposes Pulumi programs and stacks as strongly-typed and composable building blocks. No CLI, no human-in-the-loop, just code. Pulumi can be fully embedded inside your software projects - to power a wide range of custom cloud infrastructure automation projects within your cloud engineering team.

Pulumi customers are already applying the Automation API to an incredible breadth of different scenarios. We continue to be amazed by the creativity that it unlocks as a new fundamental building block for cloud engineering.

A few examples of the kinds of scenarios we’ve seen users apply the Pulumi Automation API to so far:

- **Platform APIs** - Embedding Pulumi opens up a world of possibility for building internal  and public cloud platforms that serve your infrastructure abstractions, enabling new approaches to SaaS, including IaaS and PaaS products and platforms. Expose declarative infrastructure defined with your best practices behind a REST, gRPC, or Custom Resource API that can be easily consumed by developers and operators alike.
- **Complex Workflow Orchestration** - Distributed systems and microservices incur a significant coordination burden, and dependencies across API boundaries are difficult to track and maintain. Automation API is the layer that orchestrates multi-stack deployments, codifying dependencies, and enabling safe incremental deployment. Networking, database systems, application code, schema migrations, and more can be coordinated in a single strongly typed, familiar programming environment.
- **Cloud Development Frameworks** - Automation API provides building blocks in your favorite language. With them, you can author higher-lever frameworks and components that blur the lines between infrastructure and application. We expect to see more frameworks that focus on application code that ambiently creates the infrastructure to power itself.
- **Supercharged Ops Tooling** - Create hardened and tested tooling to automate anything entering your ticketing system. From allocating timebound developer VMs to upgrading TLS certificates and scaling servers, Automation API enables you to build custom CLIs and tools that leverage the full power of Infrastructure as Software underneath custom user interfaces.

The Automation API is a new subpackage in each of Pulumi’s language-specific SDKs that provides APIs to create and manage Stacks and perform lifecycle operations like update, refresh, preview, and destroy. It is a strongly typed and safe way to use Pulumi in embedded contexts such as web servers without having to shell out to a CLI. You can define a Pulumi program as a function inside of your codebase rather than in a separate project and use methods to get and set config programmatically. The Automation API uses a gRPC interface to execute programs and control and communicate with the core Pulumi engine. It still requires a Pulumi CLI installation, as this is how we bundle and distribute the core engine. Today it’s available in preview for [TypeScript/JavaScript](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/x/auto) and [Go](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/x/auto), with support for [Python](https://github.com/pulumi/pulumi/compare/auto/python) and [C#](https://github.com/pulumi/pulumi/compare/auto/dotnet) under active development.

## Platform APIs

For SaaS scenarios like deploying infrastructure in response to user action, shelling out and relying on scripts in online services brings operational challenges with observability and reliability. Automation API is just another package and can be instrumented, profiled, and monitored with your existing APM tools like Honeycomb, Prometheus, and Datadog.

Automation API runs inside of your favorite frameworks and interacts with your other packages exactly as you’d expect. We can define custom declarative infrastructure and expose it to end users behind a familiar REST interface:

{{< chooser language "typescript,go" >}}

{{% choosable language typescript %}}

```typescript
// an HTTP handler to create instances of our declarative infra
// each request creates an S3-backed static website
//  with content from the POST body
const createHandler: express.RequestHandler = async (req, res) => {
    const stackName = req.body.id;
    const content = req.body.content as string;
    try {
        // create a new stack
        const stack = await LocalWorkspace.createStack({
            stackName,
            projectName,
            // generate our pulumi program on the fly from the POST body
            program: createPulumiProgram(content),
        });
        await stack.setConfig("aws:region", { value: "us-west-2" });
        // deploy the stack, tailing the logs to console
        const upRes = await stack.up({ onOutput: console.info });
        res.json({ id: stackName, url: upRes.outputs.websiteUrl.value });
    } catch (e) {
        // built in support for structured error handling
        if (e instanceof StackAlreadyExistsError) {
            res.status(409).send(`stack "${stackName}" already exists`);
        } else {
            res.status(500).send(e);
        }
    }
};
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// an HTTP handler to create instances of our declarative infra
// each request creates an S3-backed static website
//  with dynamic content from the POST body
func createHandler(w http.ResponseWriter, req *http.Request) {
    w.Header().Set("Content-Type", "application/json")
    var createReq CreateSiteReq
    _ := json.NewDecoder(req.Body).Decode(&createReq)

    stackName := createReq.ID
    // dynamically define our Pulumi Program
    program := createPulumiProgram(createReq.Content)

    s, err := auto.NewStackInlineSource(ctx, stackName, project, program)
    if err != nil {
        // built in support for structured error handling
        // if stack already exists, 409
        if auto.IsCreateStack409Error(err) {
            w.WriteHeader(409)
            fmt.Fprintf(w, fmt.Sprintf("stack %q already exists", stackName))
            return
        }

        w.WriteHeader(500)
        fmt.Fprintf(w, err.Error())
        return
    }
    s.SetConfig(ctx, "aws:region", auto.ConfigValue{Value: "us-west-2"})

    // deploy the stack
    upRes, err := s.Up(ctx, optup.ProgressStreams(os.Stdout))

    response := &SiteResponse{
        ID:  stackName,
        URL: upRes.Outputs["websiteUrl"].Value.(string),
    }
    json.NewEncoder(w).Encode(&response)
}
```

{{% /choosable %}}

{{< /chooser >}}

The handlers work with with your favorite HTTP frameworks like `mux` and `express`:

{{< chooser language "typescript,go" >}}

{{% choosable language typescript %}}

```typescript
// install necessary plugins once upon boot
ensurePlugins();

// configure express
const app = express();
app.use(express.json());

// setup our RESTful routes for our Site resource
app.post("/sites", createHandler);
app.get("/sites", listHandler);
app.get("/sites/:id", getHandler);
app.put("/sites/:id", updateHandler);
app.delete("/sites/:id", deleteHandler);

// start our http server
app.listen(1337, () => console.info("server running on :1337"));
```

{{% /choosable %}}

{{% choosable language go %}}

```go
func main() {
    ensurePlugins()

    router := mux.NewRouter()

    // setup our RESTful routes for our Site resource
    router.HandleFunc("/sites", createHandler).Methods("POST")
    router.HandleFunc("/sites", listHandler).Methods("GET")
    router.HandleFunc("/sites/{id}", getHandler).Methods("GET")
    router.HandleFunc("/sites/{id}", updateHandler).Methods("PUT")
    router.HandleFunc("/sites/{id}", deleteHandler).Methods("DELETE")

    // define and start our http server
    s := &http.Server{
        Addr:    ":1337",
        Handler: router,
    }
    fmt.Println("starting server on :1337")
    log.Fatal(s.ListenAndServe())
}
```

{{% /choosable %}}

{{< /chooser >}}

TODO gif

Check out the full `Pulumi over HTTP` example in [TypeScript](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/pulumiOverHttp-ts) and [Go](https://github.com/pulumi/automation-api-examples/tree/main/go/pulumi_over_http).

Here at Pulumi, we used Automation API as the foundation of our [Kubernetes Operator](https://github.com/pulumi/pulumi-kubernetes-operator/pull/86) that exposes Pulumi stacks as Custom Resources. See how your own platform's operators can [take advantage of the Automation API](https://github.com/pulumi/pulumi-kubernetes-operator/blob/master/pkg/controller/stack/stack_controller.go).

We’re seeing customers reach for Automation API to build internal cloud platforms to empower their application teams, as well as independent software vendors using it to build and sell public cloud offerings like SaaS database products.

## Complex Workflow Orchestration

There’s no longer a choice between small, decoupled units of infrastructure and a maintainable orchestration process. The Automation API executes just like any other code in your application, meaning that a single process can deploy infrastructure and manage related activities such as database migrations and blue/green deployments.

Like any other Pulumi program, we define our cloud resources. In this case an AWS RDS database:

{{< chooser language "typescript,go" >}}

{{% choosable language typescript %}}

```typescript
const clusterInstance = new aws.rds.ClusterInstance("dbInstance", {
    clusterIdentifier: cluster.clusterIdentifier,
    instanceClass: "db.t3.small",
    engine: "aurora-mysql",
    engineVersion: "5.7.mysql_aurora.2.03.2",
    publiclyAccessible: true,
    dbSubnetGroupName: subnetGroup.name,
});

return {
    host: cluster.endpoint,
    dbName,
    dbUser,
    dbPass
};
```

{{% /choosable %}}

{{% choosable language go %}}

```go
_, err = rds.NewClusterInstance(ctx, "dbInstance", &rds.ClusterInstanceArgs{
    ClusterIdentifier:  cluster.ClusterIdentifier,
    InstanceClass:      pulumi.String("db.t3.small"),
    Engine:             pulumi.String("aurora-mysql"),
    EngineVersion:      pulumi.String("5.7.mysql_aurora.2.03.2"),
    PubliclyAccessible: pulumi.Bool(true),
    DbSubnetGroupName:  subnetGroup.Name,
})
if err != nil {
    return err
}

ctx.Export("host", cluster.Endpoint)
ctx.Export("dbName", dbName)
ctx.Export("dbUser", dbUser)
ctx.Export("dbPass", dbPass)
}
```

{{% /choosable %}}

{{< /chooser >}}

But with Automation API we can configure perform database migrations and preload rows in the same program:

{{< chooser language "typescript,go" >}}

{{% choosable language typescript %}}

```typescript
// create (or select if one already exists) a stack that uses our inline program
const stack = await LocalWorkspace.createOrSelectStack({
    stackName: "dev",
    projectName: "databaseMigration",
    // our pulumi program as an "inline" function
    program: pulumiProgram
});

// run the update to deploy our database
const upRes = await stack.up({ onOutput: console.info });
console.log(`db host url: ${upRes.outputs.host.value}`);
console.info("configuring db...");

// establish mysql client
const connection = mysql.createConnection({
    host: upRes.outputs.host.value,
    user: upRes.outputs.dbUser.value,
    password: upRes.outputs.dbPass.value,
    database: upRes.outputs.dbName.value
});

connection.connect();
console.log("creating table...")

// create our table
connection.query(`
CREATE TABLE IF NOT EXISTS hello_pulumi(
    id int(9) NOT NULL,
    color varchar(14) NOT NULL,
    PRIMARY KEY(id)
);
`, function (error, results, fields) {
    if (error) throw error;
    console.log("table created!")
    console.log('Result: ', JSON.stringify(results));
});
```

{{% /choosable %}}

{{% choosable language go %}}

```go
// create our stack with an "inline" Pulumi program (deployFunc)
stack := auto.UpsertStackInlineSource(ctx, stackName, projectName, deployFunc)
// run the update to deploy our database
res, err := stack.Up(ctx, stdoutStreamer)

fmt.Println("Update succeeded!")

// get the connection info
host := res.Outputs["host"].Value
dbName := res.Outputs["dbName"].Value
dbUser := res.Outputs["dbUser"].Value
dbPass := res.Outputs["dbPass"].Value

// establish db connection
db := sql.Open("mysql", fmt.Sprintf("%s:%s@tcp(%s:3306)/%s", dbUser, dbPass, host, dbName))
defer db.Close()

// run our database "migration"
fmt.Println("creating table...")
db.Query(`
CREATE TABLE IF NOT EXISTS hello_pulumi(
    id int(9) NOT NULL,
    color varchar(14) NOT NULL,
    PRIMARY KEY(id)
);
`)
```

{{% /choosable %}}

{{< /chooser >}}

TODO gif

See the full database deployment and migration Automation API program in [TypeScript](https://github.com/pulumi/automation-api-examples/tree/main/nodejs/databaseMigration-ts) and [Go](https://github.com/pulumi/automation-api-examples/tree/main/go/database_migration).

## Cloud Framework Development

The Automation API removes any distinction between infrastructure and application code. Its unique form factor lends all of the predictability and reliability of immutable infrastructure and the desired state configuration you expect from Pulumi while naturally enabling automation and composition in a way that CLIs and DSLs were never designed to handle.

We prototyped a Heroku-like developer experience called `halloumi` that demonstrates this. All you worry about is writing HTTP handlers. Halloumi worries about the rest, including orchestrating cross-service dependencies, networking, and deploying docker images to ECS Fargate or serialized JavaScript to AWS Lambda.

{{< chooser language "typescript,go" >}}

{{% choosable language typescript %}}

```typescript
// this application will deploy multiple services publicly available in the cloud
const application = new App();

const svc1 = new WebService("hello", (expressApp: express.Express) => {
    // a simple static handler
    expressApp.get('/', (req, res) => res.send("omg i'm alive\n"));
});
application.addService(svc1);


const svc2 = new WebService("world", (expressApp: express.Express) => {
    expressApp.get('/', async (req, res) => {
        // track dependencies across services and make them available at runtime
        const svc1Url = svc1.discover();
        // this handler calls svc1 and passes the result through
        const result = await (await fetch(svc1Url)).text()

        res.send(`this is the world. With a window from hello:\n${result} \n`);
    });
});
application.addService(svc2);

application.run().catch(err => { console.error(err) });
```

{{% /choosable %}}

{{% choosable language go %}}

```go
app := app.NewApp("petStore")

// a cloud web service that returns a number [0-100)
randomNumberService := web.NewWebService("randomNumber", func() http.Handler {
    // a normal HTTP handler, halloumi takes care of running this in the cloud
    r := mux.NewRouter()
    handler := func(w http.ResponseWriter, r *http.Request) {
        rand.Seed(time.Now().UnixNano())
        fmt.Fprintf(w, "%d", rand.Intn(100))
    }
    r.HandleFunc("/", handler)
    return r
})
app.Register(randomNumberService)

// a cloud web service that returns N of a random animal.
// this service takes a dependency on the URLs of the previously defined services
nAnimalsService := web.NewWebService("nAnimals", func() http.Handler {
    r := mux.NewRouter()
    // we'll read these variables in via requests to other services
    var num string
    var animal string
    handler := func(w http.ResponseWriter, r *http.Request) {
        // Notice how we have the URL of randomNumberService
        // available to consume here!
        numResp := http.Get(randomNumberService.URL())
        num = readResponse(numResp)

        // Notice how we have the URL of randomAnimalService
        // available to consume here!
        animalResp, err := http.Get(randomAnimalService.URL())
        animal = readResponse(animalResp)

        fmt.Fprintf(w, "Wow, you got %s %ss!", num, animal)
    }
    r.HandleFunc("/", handler)
    return r
})
```

{{% /choosable %}}

{{< /chooser >}}

TODO gif

Check out the full `halloumi` source in [TypeScript](https://github.com/pulumi/halloumi/tree/main/nodejs) and [Go](https://github.com/pulumi/halloumi/tree/main/go).

Like any other framework, you can even set a breakpoint to debug orchestration logic or the pulumi program itself including `Apply` callbacks.

TODO gif

## Supercharged Ops Tooling

Cloud infrastructure is beyond the days of driving deployments and infrastructure by hand, even though many of our tools are CLIs for manual workflows. Cloud engineering demands automated tools to keep up with growth, not just in terms of pace but also in complexity.

Have a look at our temporary development VM provisioner for Azure `vmgr`. A simple Cobra CLI command creates a new stack with a VM ready to go:

```go
func NewAddCmd() *cobra.Command {
    return &cobra.Command{
        Use:   "add",
        Short: "add deploys an additional additional vm stack",
        Run: func(cmd *cobra.Command, args []string) {
                stackName := fmt.Sprintf("vmgr%d", rangeIn(10000000, 99999999))
                // create a new stack for our VM with an Inline program.
                // the program is nil for now, but we'll set it later after retrieving some dependent outputs.
                s, err := auto.NewStackInlineSource(ctx, stackName, projectName, nil /* Program */)
                fmt.Println("ensuring network is configured...")
                // lookout network and resource group info
                subnetID, rgName, err := EnsureNetwork(ctx, projectName)
                // set our program for the deployment with the resulting network info
                stack.SetProgram(GetDeployVMFunc(subnetID, rgName))
                fmt.Println("deploying vm...")
                // deploy our VM stack
                stdoutStreamer := optup.ProgressStreams(os.Stdout)

                res, err := s.Up(ctx, stdoutStreamer)
                if err != nil {
                    fmt.Printf("Failed to deploy vm stack: %v\n", err)
                    os.Exit(1)
                }
                fmt.Printf("deployed server running at public IP %s\n", res.Outputs["ip"].Value)
            },
        }
}
```

TODO gif

Our `vmgr cron` environment cleanup job takes advantage of Pulumi’s declarative model. It queries the Pulumi Service for stacks older than five days and removes them along with any child resources:

```go
// query all stacks in the project
stacks := w.ListStacks(ctx)
expiration := time.Now().Add(-1 * FIVE_DAYS)
var stacksToDestroy []string
for _, stackSummary := range stacks {
    lastUpdateTime := time.Parse(time.RFC3339, stackSummary.LastUpdate)
    // mark all stacks past expriation date for deletion
    if lastUpdateTime.Before(expiration) {
        stacksToDestroy = append(stacksToDestroy, stackSummary.Name)
        fmt.Printf("Found expired stack %s last deployed at %s\n", stackSummary.Name, stackSummary.LastUpdate)
    }
}

fmt.Printf("Found %d stacks to clean up\n", len(stacksToDestroy))

success := 0
for _, sName := range stacksToDestroy {
    stack := auto.SelectStack(ctx, sName, w)

    fmt.Printf("destroying stack %s\n", sName)

    // tail logs to stdout
    stdoutStreamer := optdestroy.ProgressStreams(os.Stdout)
    // destroy the expired stack
    stack.Destroy(ctx, stdoutStreamer)
    success++
    fmt.Printf("removing stack %s and all associated config and history\n", sName)
    w.RemoveStack(ctx, sName)
    fmt.Printf("stack %s successfully reaped \n", sName)
}

fmt.Printf("destroyed %d stack(s)\n", success)
```

Our VM provisioner uses Automation API, but it’s backed by Pulumi’s desired state model. This means that there’s no chance of resources leaking or getting lost. Check out the full [`vmgr` example here](https://github.com/pulumi/automation-api-examples/tree/main/go/vm_manager_azure). For a cloud native example, take a look at our `eksctl` inspired [`aksctl` for Azure AKS](https://github.com/jaxxstorm/aksctl).

## Give it a Try Today!

The Automation API is your tool to tame Cloud Engineering complexity and give your team the leverage to automate your cloud infrastructure. It is fully open source and available today for TypeScript/JavaScript and Go. Want to learn more? Come hang out with us in the [#automation-api community slack channel](https://pulumi-community.slack.com/archives/C019YSXN04B). Download the latest Pulumi release and check out these resources to get started:

- [Go documentation](https://pkg.go.dev/github.com/pulumi/pulumi/sdk/v2/go/x/auto)
- [JavaScript/TypeScript documentation](https://www.pulumi.com/docs/reference/pkg/nodejs/pulumi/pulumi/x/automation/)
- [The Automation API examples repo](https://github.com/pulumi/automation-api-examples/tree/main/go/database_migration)
- The list of [known issues](https://github.com/pulumi/pulumi/issues?q=is%3Aissue+is%3Aopen+label%3Aarea%2Fautomation-api). Please [file more](https://github.com/pulumi/pulumi/issues/new?assignees=&labels=needs-triage&template=bug_report.md&title=) as you find them!
- [The Pulumi Kubernetes Operator](https://github.com/pulumi/pulumi-kubernetes-operator)
- [aksctl](https://github.com/jaxxstorm/aksctl)
- [Halloumi](https://github.com/pulumi/halloumi)

Last, we'd like to give a special thank you to the members of the community who have consulted with us, chimed in on the [original github issue](https://github.com/pulumi/pulumi/issues/3901), and have been there for the journey in [community slack](https://pulumi-community.slack.com/archives/C019YSXN04B).

🏭 🏭 🏭 Happy automating! 🏭 🏭 🏭
