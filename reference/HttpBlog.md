Nodejs, Http-Servers and Pulumi

Almost 10 years ago, Nodejs was introduced, helping to usher in an era of server-side JavaScript development. Right from the beginning, Nodejs made it simple and easy to stand up an http server and to start listening and responding to requests in an environment that felt natural to people already comfortable working with JavaScript.  From the very earliest commits this was a core focus, and very early on Nodejs exposed the initial JavaScript API for creating an [Http Server](https://github.com/nodejs/node/commit/a80591aff6704bd71ac5b136e23ddd7b52cf0299#diff-31b367d1856df8608494b65123d57acd).  That API evolved over time to become the well known [HTTP module](https://nodejs.org/api/http.html) that is the backbone of so many projects.

The core approach taken by Nodejs was that it would provide the facility to easily stand up a reliable and performant Http Server (using the aptly named [http.createServer](https://nodejs.org/api/http.html#http_http_createserver_options_requestlistener) API), but it left the processing and control of those actual Http conversations up to a simple callback function that a user of the API would provide.  This callback function itself was very simple, with the entire API having the form:

```ts
function createServer(requestListener?: (request: IncomingMessage, response: ServerResponse) => void): Server
```

With this a developer could now easily plug in a function that would be called with the information about an incoming `request` in the callback's first parameter, and which could supply the appropriate `response` through the callback's second parameter.  This approach allowed Nodejs to focus on being simple and easy to get the server stood up, while being relatively unopinionated and giving the developer a lot of flexibility in terms of how they woudl actually process requests and responses.

Thanks to this split, the Nodejs ecosystem then came forward to provide more structured design patterns to handle those requests and responses to make things more manageable for developers.  These communities provided 'middleware' APIs that could bridge between this extremely basic entry-point into one more structured and opinionated, but potentially simpler to understand and work with.  Middleware libraries like [Expressjs](http://expressjs.com/) allowed one to write simple route-handlers like:

```ts
const app = express();

// GET method route
app.get('/', function (req, res) {
  res.send('GET request to the homepage')
})

// POST method route
app.post('/', function (req, res) {
  res.send('POST request to the homepage')
})

http.createServer(app).listen();
```

while also themselves having extensible middleware points to plug in other libraries as well (like [Body Parser](https://github.com/expressjs/body-parser), [Passport](http://www.passportjs.org/), and many others).  This large effort across the entire ecosystem has made the task of serving websites using JavaScript dramatically simple, and has helped propel a huge amount of popularity in this space.

Interestingly enough though, the Cloud space has gone a slightly different route here (no pun intended).  While cloud providers like AWS and Azure provide ways to both create Http servers and to use Nodejs, the offer a very different shape altogther for processing http messages.  For example, in AWS, one needs to first setup an [API gateway](https://aws.amazon.com/api-gateway/).  That gateway will then have to 'methods' defined on it which point at 'Lambda Proxies' to finally process the request.  The connected [AWS Lambda](https://aws.amazon.com/lambda/) then will manage the request and response in a decidely AWS-specific manner.  For example, instead of working with [IncomingMessage](https://nodejs.org/api/http.html#http_class_http_incomingmessage) and [ServerResponse](https://nodejs.org/api/http.html#http_class_http_serverresponse) like one normally would with Nodejs, AWS specific messages [like so](https://docs.aws.amazon.com/lambda/latest/dg/eventsources.html#eventsources-api-gateway-request) are the name of the game.  Responding to messages with your own data uses a very different form as well.  Code has to be written like so:

```ts
exports.handler = function(event, context, callback) {
    // process AWS 'event' using information from AWS 'context'
    // ...
    // build response
    var response = {
        statusCode: responseCode,
        headers: {
            "x-custom-header" : "my custom header value"
        },
        body: JSON.stringify(responseBody)
    };

    callback(null, response);
}
```

Azure follows its own [distinct style](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook) as well for processing http messages.  These approaches end up working, but often feel decidedly un-Nodejs-like.  They're full of cloud-provider specific values and behaviors, and they end up making it more difficult to work with the existing ecosystem of middleware components out there.

We thought this was a place we could definitely help Pulumi applications with a simpler approach for these cloud ecosystems.  To further this goal, we've created a new API called [cloud.HttpServer](https://github.com/pulumi/pulumi-cloud/blob/master/api/httpServer.ts).  `HttpServer` is a Pulumi [Resource](https://pulumi.io/reference/programming-model.html#resources), but is designed to work well with the existing large middleware ecosystem out there.  The core API shape that accomplishes this is:

```ts
// Factory function for creating a requestListener function.  The returned function is the same
// callback function that would be passed to http.createServer.  See:
// https://nodejs.org/api/http.html#http_http_createserver_options_requestlistener for more details.
export type RequestListenerFactory = () => (req: http.IncomingMessage, res: http.ServerResponse) => void;

export interface HttpServerConstructor {
    /**
     * @param createRequestListener Function that, when called, will produce the [[requestListener]]
     * function that will be called for each http request to the server.  The function will be
     * called once when the module is loaded.  As such, it is a suitable place for expensive
     * computation (like setting up a set of routes).  The function returned can then utilize the
     * results of that computation.
     */
    new (name: string, createRequestListener: RequestListenerFactory, opts?: pulumi.ResourceOptions): HttpServer;
}
```

The idea here is that a Pulumi app can now simply take the previous Expressjs example and rewrite it as:

```ts
// The `() => { ... }` callback will actually become the code inside an AWS Lambda!**
const server = new cloud.HttpServer("myserver", () => {
    const app = express();

    // GET method route
    app.get('/', function (req, res) {
        res.send('GET request to the homepage')
    })

    // POST method route
    app.post('/', function (req, res) {
        res.send('POST request to the homepage')
    })

    return app;
});
```

The majority of this code is identical to the original Nodejs form.  The only small difference is the creation of the cloud.HttpServer resource (which is needed for Pulumi to track work and dependencies) and the returning of the 'app' variable instead of directly calling `http.createServer`.

Pulumi will take that code and convert the JavaScript callback** into all the AWS API-Gateway and Lambda machinery necessary to make this work.  The API Gateway will be properly setup to communicate with the Lambda function, and the Lambda function will properly handle AWS's specific input/output forms and will map them along so they can properly work with Nodejs' http library expectations.

Effectively, the above callback will get translated into the following code that is uploaded to AWS Lambda.

```ts
// index.js
module.exports = WrapAwsEventAndContextAndCallBackAndForwardTo((() => {
    const app = express();

    // GET method route
    app.get('/', function (req, res) {
        res.send('GET request to the homepage')
    })

    // POST method route
    app.post('/', function (req, res) {
        res.send('POST request to the homepage')
    })

    return app;
})())
```

In other words, that factory function will get called, returning the expected [requestListener](https://nodejs.org/api/http.html#http_http_createserver_options_requestlistener) function.  Pulumi will then inject the call to the helper that will wrap that function with the right translation code to map from the AWS specific inputs to the expected Nodejs form, and from the Nodejs outputs to the AWS expected forms.

Right now, this functionality has been enabled for AWS and Azure in our `@pulumi/cloud-aws` and `@pulumi/cloud-azure` packages.  This means that the above code will run properly on either platform without consumers having to write platform specific code or figure out how they would need to translate between the two.  And, because of the translation from AWS/Azure specific APIs to the common Nodejs API, you can now use virtually any middleware components effectively on either platform.  Currently, this does only work if you are writing a Pulumi application.  However, we are [tracking](https://github.com/pulumi/pulumi-cloud/issues/585) the work to extract the specialized code we've written into its own library.  Once that work is done, you'll then be able to easily do something like create an Azure [FunctionApp](https://docs.microsoft.com/en-us/azure/azure-functions/functions-overview) manually, setup the appropriate [bindings](https://docs.microsoft.com/en-us/azure/azure-functions/functions-bindings-http-webhook), and then upload your code which will setup the appropriate Azure endpoint, but then call into this library to translate to the Nodejs http form that will allow you to then code things up as simply as if this was just an Expressjs app!

** One thing glossed over was how Pulumi knows how to convert a JavaScript callback into an AWS Lambda or an Azure FunctionApp.  Stay tuned though!  It's an incredibly cool part of Pulumi, and we can't wait to dive deeper into that functionality and how it can make it simple and clear to create an entire Cloud App in one single package, even including all the code in-line that will end up executing in the cloud at runtime!  That magic, along with powerful components like the new HttpServer API can hopefully help make cloud applications dramatically simpler to write and maintain for you.  Happy coding!
