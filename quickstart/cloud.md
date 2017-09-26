---
layout: default 
nav_section: "quickstart"
---

<p><a href="/quickstart">Quickstart</a> &gt; <b>Programming the Cloud</b></p>

<h1 class="title f1">Programming the Cloud</h1>

The `@pulumi/cloud` package lets you program infrastructure and application logic, side by side in harmony, using
simple, high-level cloud building blocks.  This package has three key defining attributes:

* __Easy Cloud Development__: The `@pulumi/cloud` library makes it simple to build robust and scalable cloud
  applications with just a few lines of code.
* __Cloud Agnostic__: The `@pulumi/cloud` library doesn't tie you to using any one particular cloud (AWS, Azure,
  Google Cloud, Kubernetes, and various on-premises clouds).  Applications built using the high-level `@pulumi/cloud`
  components like [Table](/packages/pulumi-cloud/interfaces/_table_.table.html), [Topic](
  /packages/pulumi-cloud/interfaces/_topic_.topic.html) and [HttpEndpoint](
  /packages/pulumi-cloud/interfaces/_httpendpoint_.httpendpoint.html) can be deployed to a variety of cloud platforms.
* __Serverless__: The `@pulumi/cloud` makes it easy to build applications with minimal fixed infrastructure,
  event-driven application logic, and using resources that are charged only based on actual consumption.

### A Simple Application

As our first example, we'll build a simple URL shortener.

We start with just an `index.ts` file importing `@pulumi/cloud`.  (See the secction on
[Using TypeScript](./reading.html#using-typescript) for additional details on using TypeScript for your Pulumi program).
We can use the `HttpEndpoint` class to create a publicly accessible HTTP endpoint:

```typescript
import * as cloud from "@pulumi/cloud";

let app = new cloud.HttpEndpoint("urlshortener");

app.get("/", (req,res) => {
    res.json({hello: "world"});
});

app.publish().then(url => console.log(`Serving at: ${url}`));
```

Note that the signature of the `get` method is similar to popular JavaScript web routing frameworks, like Express.js,
and uses standard request/response parameters and familiar `res.json` APIs.  Underneath the covers, however, this
program will use a true API Gateway that supports infinite scale out, DDOS protection, SSL, and more.

We run `pulumi config aws:config:region us-west-2` to set the AWS region to deploy this application into.  Then
we run `pulumi update` to deploy this code and activate our HTTPS endpoint:

```bash
$ pulumi update
...
<snip>
...
info: Serving at: https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/
info: 14 changes performed:
    + 14 resources created
Update duration: 38.783839863s
```

After that, we can curl our newly created HTTPS endpoint to see our message:

```bash
$ curl https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/
{"hello":"world"}
```

*Note that in the future we will support branded application URLs rather than the raw AWS URL shown above.*

We can turn this into a robust hosted URL shortener service in just a few steps.  First, we add a `/shorten` route:

```typescript
app.post("/shorten", (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];
    console.log(`POST /shorten ${url} ${name}`);
    res.json({shortenedURLName: name});
});
```

Again, we see we can use Express-like APIs to define a simple service.  But now we also need to persist the mapping
between short `name` and `url`.  So we can create a data store to use for this mapping directly within our application:

```typescript
let urls = new cloud.Table("urls", "name");
```

And then we simply modify our `/shorten` handler to insert into this table:

```typescript
app.post("/shorten", async (req, res) => {
    let url = req.query["url"];
    let name = req.query["name"];
    console.log(`POST /shorten ${url} ${name}`);
    await urls.insert({name, url});
    res.json({shortenedURLName: name});
});
```

Notice that we simply captured a reference to the `urls` object, and called runtime APIs on it.  Pulumi handles
all of the configuration and wiring necessary to make this happen, something that would usually entail messy manually
configured URLs, environment variables, and the like.  Also notice that we can use asynchronous code via `async` and
`await`, so that we wait for the insert to complete before responding to the REST API request.

We can now push this updated code, which will provision the data store, update the hosted REST API, and wire up the
route handlers to the new code.  We can then hit the new API endpoint to shorten a URL:

```bash
$ pulumi update
...
$ curl -X POST "https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/shorten?name=g&url=http://www.google.com"
{"shortenedURL":"g"}
```

Pulumi figures out what has changed, and makes the minimal edits required to make the changes take effect.

And finally, we can implement the `GET `handlers for any registered short name to return a 301 response with
`Location` header to redirect:

```typescript
app.get("/{name}", async (req, res) => {
    let name = req.params["name"];
    let data = await urls.get({name});
    console.log(`GET /${name} => ${data.url}`)
    res.setHeader("Location", data.url);
    res.status(301);
    res.end("");
});
```

And then we deploy and invoke it:

```bash
$ pulumi update
...
$ curl https://hskuj2l449.execute-api.us-west-2.amazonaws.com/stage/g
<!doctype html>...contents of google.com ...
...
```

We have a working URL shortener with persistent storage and robust and scalable compute!

That's a quick tour of the `@pulumi/cloud` framework.  There is a lot you can do with this powerful cloud programming
framework, and we are excited to see what the community builds on top of it.  Many more examples will be coming
soon; however, in the meantime, please check out the [API documentation](/packages/pulumi-cloud/) for more details.

<h2 class="h2" style="font-weight: bold" markdown="1">Next Up: [Further Reading](./reading.html)</h2>

