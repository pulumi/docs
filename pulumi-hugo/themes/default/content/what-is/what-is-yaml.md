---
title: What is YAML?
meta_desc: |
     YAML is a data serialization language that has steadily increased in popularity. Discover how to use YAML with Pulumi today.

type: what-is
page_title: "What is YAML?"

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

YAML is a data serialization language most commonly used for configuration files. Its easy readability and rich feature set have made it an increasingly popular choice over the years, for everything from configuration files to object serialization. Originally named "Yet Another Markup Language," the creators changed the name to "YAML Ain't a Markup Language" in order to better reflect its strength as a data-oriented language rather than simply markup.

## How To Get Started With YAML

Many of YAML's strongest features were inspired by other programming languages. Like Python, YAML uses whitespace indentation for defining the structure of your file. Strings, integers, floats, lists, and dictionaries are all natively supported, and it does also allow you to define custom data types. Dig far enough into the history of YAML, and you'll find pieces of the PERL, C, and HTML specs.

While YAML is frequently compared to JSON, it's important to note that the two are very closely related. YAML is actually a superset of JSON, and so it is capable of parsing JSON directly.

The following is an example of YAML:

```yaml
---
# An easy-to-read set of data on the Pulumi mascot, in YAML
name: Pulumipus
breed: platypus
color: purple
mascot: True
age: 5
hobbies:
  - Kayaking
  - Bouldering
  - Reading
  - Coding
languages:
  python: Expert
    version: 3.7
  typescript: Expert
  go: Expert
  csharp: Expert
  java: Expert
  yaml: Expert
```

The beginning of a YAML file is usually three dashes (`---`) on the first line. From there, your file is built out of key-value pairs.

```yaml
name: Pulumipus
breed: platypus
color: purple
```

The first three key-value pairs are strings indicating that this creature is a purple platypus named Pulumipus, but YAML also supports integers, floats, and booleans to give their age and current status as a mascot:

```yaml
mascot: True
age: 5
```

We also have access to lists (or arrays), indicated by preceding an indented item with a dash:

```yaml
hobbies:
  - Kayaking
  - Bouldering
  - Reading
  - Coding
```

You can even nest these key-value pairs for more granular information:

```yaml
languages:
  python: Expert
    version: 3.7
  typescript: Expert
  go: Expert
  csharp: Expert
  java: Expert
  yaml: Expert
```

## The Benefits of YAML With Pulumi

If a high degree of readability is your concern and you do not need the expressivity of a full-fledged programming language like Python or Typescript, YAML is a great option for defining and deploying your infrastructure with Pulumi. Take the following example, which creates an AWS S3 bucket and deploys a simple "hello world" website before returning the URL of your bucket:

```yaml
---
name: simple-yaml
runtime: yaml
resources:
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        Fn::StringAsset: <h1>Hello, world!</h1>
      acl: public-read
      contentType: text/html
outputs:
  bucketEndpoint: http://${my-bucket.websiteEndpoint}
```

There are a few Pulumi-specific things happening in this YAML. Let's take a closer look.

```yaml
name: simple-yaml
runtime: yaml
```

To begin with, we're naming our program `simple-yaml`, and defining the runtime for Pulumi as `yaml`.

```yaml
resources:
  my-bucket:
    type: aws:s3:Bucket
    properties:
      website:
        indexDocument: index.html
  index.html:
    type: aws:s3:BucketObject
    properties:
      bucket: ${my-bucket}
      source:
        Fn::StringAsset: <h1>Hello, world!</h1>
      acl: public-read
      contentType: text/html
```

Next, we're defining the resources Pulumi should create for you. In this case, with the name `my-bucket`, an AWS S3 bucket that we want to act like a website. Its should expect to serve an index document called `index.html`, to be publicly readable and contain a simple "Hello, world!" message.

```yaml
outputs:
  bucketEndpoint: http://${my-bucket.websiteEndpoint}
```

Finally, we have an output. This is a value handed to you by Pulumi, after the completion of any work required on behalf of relevant resources. If you're familiar with Javascript, you can think of it sort of like a promise. In this case, we're asking for the URL our document will be visible at.

Defining infrastructure doesn't get much simpler than that! [Try it yourself](/docs/languages-sdks/yaml/) and get started with any major cloud provider in a snap.

## Pulumi Corporation

Pulumi lets infrastructure, developer, and security teams deliver infrastructure as code faster, using programming ([Python](/docs/languages-sdks/python/), [Node.js (JavaScript, TypeScript)](/docs/languages-sdks/javascript/), [Go](/docs/languages-sdks/go/), [.NET (C#, F#, VB)](/docs/languages-sdks/dotnet/), and [Java](/docs/languages-sdks/java/) and markup ([YAML, JSON, and CUE](/docs/languages-sdks/yaml/) languages they already know. It provides a single pipeline for delivering and securing infrastructure and applications on any cloud. [Get started for free today!](/docs/get-started/)
