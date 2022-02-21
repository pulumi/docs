---
title: JavaScript and Infrastructure as Code
meta_desc: |
    Learn why JavaScript and Infrastructure as Code are a perfect match for creating versionable, testable and repeatable infrastructure.

type: what-is
page_title: "JavaScript and Infrastructure as Code"

customer_logos:
  title: Leading engineering organizations are building with Pulumi
  logos:
    - items:
      - snowflake
      - tableau
      - atlassian
      - fauna
      - ware2go
    - items:
      - mindbody
      - sourcegraph
      - fenergo
      - skai
      - lemonade
    - items:
      - clearsale
      - angellist
      - webflow
      - supabase
      - ro
---

[Infrastructure as Code (IaC)]({{< relref "/what-is/what-is-infrastructure-as-code" >}}) means that you use code to define and manage your infrastructure automatically rather than with manual processes. In a broader sense, IaC enables [cloud engineering]({{< relref "/blog/what-exactly-is-cloud-engineering" >}}) and allows you to effectively apply software engineering practices to your infrastructure. With IaC, you can automatically build, deploy and manage your infrastructure much more effectively and reliably than you can manually. IaC makes your whole infrastructure versionable, [testable]({{< relref "/what-is/how-to-step-up-cloud-infrastructure-testing" >}}) and repeatable.

People use many different programming languages to implement IaC (for our purposes, we mean infrastructure in the cloud). One of the most widely used is JavaScript.

## Why is JavaScript So Popular?

On its own, JavaScript is a programming language for writing client-side scripts. Those scripts run in a browser. How then can we use it to build our infrastructure? Enter Node.js. Node.js is a cross-platform, open-source, run-time environment that allows JavaScript to run on the server-side. In other words, Node.js allows Javascript code to run outside the browser.

JavaScript has always been popular. It is relatively easy to learn and has an active, helpful community that has created a large number of libraries, tools and frameworks that make it easy to develop and test JavaScript code. With the advent of Node.js, its popularity dramatically increased because the idea of “JavaScript everywhere” became possible. All forms of web development could use a single programming language. Consequently, different teams had a common language and could communicate and collaborate more effectively. As any DevOps advocate will tell you, good communication is essential for fostering innovation and decreasing time to market.

Node.js has also made it possible for developers to expand their areas of expertise. They can apply their existing JavaScript skills to new areas, such as creating infrastructure in the cloud with JavaScript and infrastructure as code. They don’t have to learn specialized, vendor-specific languages that have many more limitations than a standard programming language. Because virtually all cloud providers support JavaScript, developers can pick the vendor (or even vendors) they prefer rather than being tied to a specific provider.

## JavaScript Infrastructure as Code and Serverless Computing

Many developers now use JavaScript to create IaC, often in [serverless applications]({{< relref "/blog/architecture-as-code-serverless" >}}). Serverless computing (or serverless for short), is an execution model where the cloud provider is responsible for executing a piece of code by dynamically allocating the resources. You are only charged for the resources used to run that code. Typically, some sort of event, such as a http request or a monitoring event, triggers the code. Some of the reasons that Javascript (running in Node.js) is so popular for IaC and serverless apps are:

- Programmers can use the JavaScript skills they already possess so they become productive right away.
- Node.js is a very fast runtime.
- Node.js requires very little memory.
- Node.js doesn’t need to be compiled.
- There is a vast ecosystem of reusable modules that developers can leverage to create microservices.
- The npm package manager makes it easy to make JavaScript modules easy to discover and it manages dependency conflicts.
- JavaScript is the best language for processing the JSON format. A common serverless function (called Lambdas on AWS, Azure Functions on Azure and Google Cloud Functions on GCP) is to perform some sort of translation on a JSON object.

## The Serverless Framework

The Serverless Framework is another reason for JavaScript’s popularity for serverless architectures. It is written in Node.js and it lets you develop and deploy serverless applications to AWS, Azure, GCP and other cloud providers. A Serverless app can be as simple as a couple of lambda functions or an entire back-end composed of hundreds of lambda functions.

## Find the Right Platform: JavaScript and Infrastructure as Code

There are platforms available that can really boost your productivity when it comes to JavaScript and Infrastructure as Code. Here are a few qualities to look for:

- **Support for Standard Languages.** Of course, you need a platform that [fully supports JavaScript and Node.js]({{< relref "/docs/intro/languages/javascript" >}}).
- **Multi-cloud support.** Make sure the platform allows you to build, manage and deploy your infrastructure to [any cloud provider]({{< relref "/registry" >}}).
- **Improves on the Serverless Framework.** While the Serverless Framework definitely helps with serverless computing, it only helps with that part of your application. Find a platform that lets you adopt a more holistic approach and treats the entire program as cloud-native. You should be able to write entire applications within that platform. Some parts of that application may be serverless functions, but you should also be able to include resources such as containers, databases, and cloud services.

## Pulumi Corporation

Pulumi's Cloud Engineering Platform unites infrastructure teams, application developers, and compliance teams around a unified software engineering process for delivering modern cloud applications faster and speeding innovation. Pulumi’s open-source tools help infrastructure teams tame the cloud’s complexity with Modern Infrastructure-as-Code using the world’s most popular programming languages and communities, including [Python]({{< relref "/docs/intro/languages/python" >}}), [Node.js (JavaScript, TypeScript)]({{< relref "/docs/intro/languages/javascript" >}}), [Go]({{< relref "/docs/intro/languages/go" >}}), and [].NET (C#, F#, VB)]({{< relref "/docs/intro/languages/dotnet" >}}). [Get started for free today]({{< relref "/docs/get-started" >}}), or check out one of our on-demand workshops on getting started with [Infrastructure as Code and JavaScript]({{< relref "/resources/getting-from-code-to-cloud-with-vscode-and-pulumi" >}}).
