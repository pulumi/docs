---
title: "Deploying the Infrastructure of OAuth Server for CMS App"
date: "2020-09-02"
draft: false
meta_desc: "Implementing OAuth server for Netlify CMS app, deployING it using ECS Fargate Service, and configurING domain and certificate for it."
meta_image: cms-oauth.png
authors: ["zephyr-zhou"]
tags: ["aws","netlify-cms","github-oauth","ecs-fargate", "github-actions"]
---

In our [previous post]({{< relref "/blog/deploying-netlify-cms-on-aws" >}}), we deployed our CMS app on AWS instead of Netlify. Because we deploy on AWS, we couldn't use [Netlify's Identity Service](https://docs.netlify.com/visitor-access/identity/#enable-identity-in-the-ui) which manages Github access to Netlify CMS. As a result, we need to implement an [External OAuth Client Server](https://www.netlifycms.org/docs/external-oauth-clients/#header).

We used the Netlify CMS Go example to deploy on ECS Fargate and configured the domain and certificate. We'll show how we accomplished the deployment.

<!--more-->

Backend is a package that supports communications between Netlify CMS and repositories like Github, Gitlab, and Bitbucket. In the Pulumi [example code](https://github.com/pulumi/examples/tree/master/aws-ts-netlify-cms-and-oauth/cms-oauth), we use [Netlify CMS's backend](https://www.netlifycms.org/docs/github-backend/) to build the CMS.

The OAuth Server's code `cms-oauth/main.go` also enables authorization for Gitlab and Bitbucket by changing the callback URL to `https://{{YOUR_OAUTH_SERVER_URL}}/callback/{{YOUR_BACKEND_NAME}}`. To learn more about configuring the OAuth server, refer to the "Environment Variable and Pulumi Stack Configuration" section.

## Make Changes to Example Code

Netlify CMS's webiste provides [External OAuth Clients examples](https://www.netlifycms.org/docs/external-oauth-clients/#header) for various languages and platforms. We will use the [Go example]((https://github.com/igk1972/netlify-cms-oauth-provider-go)) for demonstration. Later, we will refer this Go example as *Netlify CMS's example*.

The *Netlify CMS's example code* uses `./dotenv/dotenv.go` to retrieve the environment variables from a file. The main.go file uses [goth](https://github.com/markbates/goth) to build the OAuth Provider. The `./randstr/randstr.go` file generates the random string for the `SESSION_SECRET` environment variable used by main.go. However, we can use Pulumi to implement both functions.

The random string can be generated with Pulumi this way:

```typescript
// Create a random string and also mark its `result` property as a secret,
// so it is not stored in plaintext in the stack's state.
const sessionSecretRandomString = new random.RandomPassword("random", {
    length: 32,
}, { additionalSecretOutputs: ["result"] });
```

Environment variables can be passed when we create a Fargate Service.

```typescript
// Create a Fargate service task that can scale out.
const appService = new awsx.ecs.FargateService("app-svc", {
    cluster,
    taskDefinitionArgs: {
        container: {
            image: img,
            memory: 128 /*MB*/,
            portMappings: [ tg ],
            environment: [
                {
                    name: "HOST",
                    // The target domain which would concatenate with callbacks in main.go
                    value: pulumi.interpolate `https://${cmsStackConfig.targetDomain}`
                },
                {
                    name: "SESSION_SECRET",
                    value: sessionSecretRandomString.result
                },
                {
                    name: "GITHUB_KEY",
                    value: cmsStackConfig.githubKey
                },
                {
                    name: "GITHUB_SECRET",
                    value: cmsStackConfig.githubSecret
                },
                {
                    name: "TARGET_PORT",
                    value: pulumi.interpolate `${inputTargetGroupPort}`
                },
                {
                    name: "GITHUB_SCOPE",
                    value: inputGithubScope
                },
            ]
        },
    },
    desiredCount: 1,
});
```

We can safely remove the `randstr` and `dotenv` folders in the OAuth client.

### Setting Github Scope

When building an OAuth application for Github, it's important to note that that the default  [github scope](https://developer.github.com/apps/building-oauth-apps/understanding-scopes-for-oauth-apps/) of *Netlify CMS's example code* is read-only. When we call the `github.New` function, read and write access must be set to edit a target repository.

We can set the GitHub scope as an environmental variable, e.g., `GITHUB_SCOPE` set to `public_repo`, which grants read and write access to public repository. We can even add several scope values by adding `,` between scope values. The `GITHUB_SCOPE` value is read and parsed when the Fargate Service is created, which sets the scope for the `Github.New` function.

```go
githubScope := os.Getenv("GITHUB_SCOPE")
    if githubScope == "" {
        goth.UseProviders(
            github.New(
                os.Getenv("GITHUB_KEY"), os.Getenv("GITHUB_SECRET"),
                // concatenate with the host name
                fmt.Sprintf("%s/callback/github", host),
                "public_repo",
            ),
            bitbucket.New(
                os.Getenv("BITBUCKET_KEY"), os.Getenv("BITBUCKET_SECRET"),
                fmt.Sprintf("%s/callback//bitbucket", host),
            ),
            gitlabProvider,
        )
    } else {
        scopeArray := strings.Split(githubScope, ",")
        goth.UseProviders(
            github.New(
                os.Getenv("GITHUB_KEY"), os.Getenv("GITHUB_SECRET"),
                // concatenate with the host name
                fmt.Sprintf("%s/callback/github", host),
                scopeArray...,
            ),
            bitbucket.New(
                os.Getenv("BITBUCKET_KEY"), os.Getenv("BITBUCKET_SECRET"),
                fmt.Sprintf("%s/callback//bitbucket", host),
            ),
            gitlabProvider,
        )
    }
```

## Creating the Application Image

Replace the working directory in the Dockerfile with the path to your cloned repository.

```dockerfile
WORKDIR /go/src/github.com/pulumi/aws-ts-netlify-cms-and-oauth/cms-oauth
```

Setting the working directory will copy your content to the Docker Image which we will deploy to AWS Fargate.

Now that CMS Server is deployed, we can start to implement the infrastructure.

## Infrastructure

### Deploying use ECS Fargate

To deploy the OAuth server to AWS Fargate, we'll use the [Hello Fargate Example](https://github.com/pulumi/examples/tree/master/aws-ts-hello-fargate) from the [Pulumi's example repository](https://github.com/pulumi/examples) as a template.

The example creates an ECS cluster, an Application Load Balancer (alb) with a listener, and a Fargate Service. We'll change the script to deploy our Docker image.

First, we specify the port number of the alb to 443, the standard port for HTTPS, instead of port 80 because the URL in main.go starts with `https://`. HTTPS is also more secure when handling the CMS access token.

```typescript
// Define an ec2 application load balancer alb to distribute incomming application traffic across multiple targets, such as EC2 instances, in multiple Availability Zones.
const alb = new awsx.elasticloadbalancingv2.ApplicationLoadBalancer(
    "net-lb", { external: true, securityGroups: cluster.securityGroups });

// alb need a listener to listen to 443 the standard port for the HTTPS traffic, certificate is using the certificate we created above
const web = alb.createListener("web", {
    port: 443,
    external: true,
    protocol: "HTTPS",
    certificateArn: certificate.arn
});
```

We also created a single target group for load balancers to distribute the traffic. This lets the user address a different port for the target group without having to use port 443.

``` typescript
let inputTargetGroupPort: pulumi.Input<number> = cmsStackConfig.targetGroupPort!;

if (inputTargetGroupPort === undefined) {
    inputTargetGroupPort = 80;
}

// when Listener Rule is satisfied then traffic is route to this target group.
const tg = alb.createTargetGroup("oauth-tg", {
    port: inputTargetGroupPort,
    loadBalancer: alb
});
```

The target group port can be optionally configured to use a different target group port.

We can set the ports with `pulumi config set cms-OAuth:targetGroupPort`. The default port is 80, which is the http port for local development.

The load balancer implements a listener and a rule to forward all requests to the target group we created.

```typescript
// when the request are forwarded then every requests are send to the target group we created
new awsx.lb.ListenerRule("oauth-listener-rule", web, {
    actions: [{
        type: "forward",
        targetGroupArn: tg.targetGroup.arn,
    }],
    conditions: [{
        field: "path-pattern",
        values: "/*", //wildcard says every request would be send
    }],
});
```

#### Environment Variables and Pulumi Stack Configuration

When starting the Fargate service, we pass environment variables to main.go.

```typescript
// Create a Fargate service task that can scale out.
const appService = new awsx.ecs.FargateService("app-svc", {
    cluster,
    taskDefinitionArgs: {
        container: {
            image: img,
            memory: 128 /*MB*/,
            portMappings: [ tg ],
            environment: [
                {
                    name: "HOST",
                    // The target domain which would concatenate with callbacks in main.go
                    value: pulumi.interpolate `https://${cmsStackConfig.targetDomain}`
                },
                {
                    name: "SESSION_SECRET",
                    value: sessionSecretRandomString.result
                },
                {
                    name: "GITHUB_KEY",
                    value: cmsStackConfig.githubKey
                },
                {
                    name: "GITHUB_SECRET",
                    value: cmsStackConfig.githubSecret
                },
                {
                    name: "TARGET_PORT",
                    value: pulumi.interpolate `${inputTargetGroupPort}`
                },
                {
                    name: "GITHUB_SCOPE",
                    value: inputGithubScope
                },
            ]
        },
    },
    desiredCount: 1,
});
```

For `HOST`, we set the URL for the OAuth Server by running `pulumi config set pulumi-website-cms:targetDomain https://some-cms-oauth-domain.pulumi-demos.com` and replace the URL.

`SESSION_SECRET` is another environment variable passed to main.go that we generated by using Pulumi's `random.RandomPassword`.

To get `GITHUB_SECRET` and `GITHUB_TOKEN` credentials, we need to register the Github OAuth application. Netlify provides [instructions](https://docs.netlify.com/visitor-access/oauth-provider-tokens/#setup-and-settings) for obtaining these credentials.

The Home Page URL is the targetDomain from our [previous post]({{< relref "/blog/deploying-netlify-cms-on-aws" >}}).

The Authorization callback URL is `https://{{the domain of your OAuth App}}/callback/github`.

```go
    github.New(
        os.Getenv("GITHUB_KEY"), os.Getenv("GITHUB_SECRET"),
        // concatenate with the host name
        fmt.Sprintf("%s/callback/github", host),
        "public_repo",
    )
```

If you use different repositories, like Bitbucket and Gitlab, you can specify callback URL to `https://{{the domain of your OAuth App}}/callback/{{ backend name }}` and replace `{{backend name}}` with `bitbucket` or `github` depending upon the repository.

We can set the github key and secret in the stack configuration.

```bash
$ pulumi config set netlify-cms-oauth-provider-infrastructure:githubKey {{YOUR_GITHUB_KEY}}
$ pulumi config set --secret netlify-cms-oauth-provider-infrastructure:githubSecret
$ {{YOUR_GITHUB_SECRET}}
```

The `--secret` flag encrypts your GitHub secret.

In addition, don't append the secret to the command, e.g., `$ pulumi config set --secret netlify-cms-oauth-provider-infrastructure:githubKey {{YOUR_GITHUB_SECRET}}`.

Your secret would be stored in the command history. Instead, specify the key without a value and enter the secret at the prompt which hides the value.

We pass `TARGET_PORT` to `targetGroupPort` which is the port used to serve the application. We should also check if this variable is set in main.go in case we need to test locally without Pulumi.

```go
targetGroupPort := os.Getenv("TARGET_PORT")
    if targetGroupPort == "" {
        targetGroupPort = "80"
    }
    listenPort := ":" + targetGroupPort
    fmt.Print("Started running on", listenPort, "\n")
    // listen on port 80 where we created the target group
    fmt.Println(http.ListenAndServe(listenPort, nil))
```

As mentioned previously, `GITHUB_SCOPE` sets the type of access the CMS has for the target repository. It is also an optional stack configuration where the default in [our Pulumi example](https://github.com/pulumi/examples/tree/master/aws-ts-netlify-cms-and-oauth/cms-oauth) is set as `public_repo`.

### Create a Certificate for the OAuth Server

The process is similar to how we created a certificate for CMS in our [previous post]({{< relref "/blog/deploying-netlify-cms-on-aws" >}}).

We can extract what we need just for creating the certificate and delete irrelevant parts including uploading content to the S3 bucket and configure CloudFront. Then the rest only involves creating an east region provider, a certificate, and certificate validation.

When we create the Alias Record, we configure it with application load balancer settings.

```typescript
// Creates a new Route53 DNS record pointing the domain to the CloudFront distribution.
function createAliasRecord(
    targetDomain: string, lb: awsx.elasticloadbalancingv2.ApplicationLoadBalancer): aws.route53.Record {
    const domainParts = getDomainAndSubdomain(targetDomain);
    const hostedZoneId = aws.route53.getZone({ name: domainParts.parentDomain }, { async: true }).then(zone => zone.zoneId);
    return new aws.route53.Record(
        targetDomain,
        {
            name: domainParts.subdomain,
            zoneId: hostedZoneId,
            type: "A",
            aliases: [
                {
                    name: lb.loadBalancer.dnsName,
                    zoneId: lb.loadBalancer.zoneId,
                    evaluateTargetHealth: true,
                },
            ],
        });
}
// Create the aliasRecord with targetdomain and application load balancer
const aRecord = createAliasRecord(cmsStackConfig.targetDomain, alb);
```

We run `pulumi up` to deploy.

### Github Workflow (Optional)

We can automate our build with the Github workflow in the folder `cms-oauth/.github/workflows/build-and-deploy.yml`. The workflow uses the repository secret we set in Github.

![Github Secret](./github_secret.jpg)

## Last Step

Finally, we need to update the CMS configuration file.

To combine our deployment of CMS and CMS OAuth Server, we specify the site_domain and URL in `./public/config.yml` of the CMS folder.

```yaml
backend:
  name: github
  # Replace this with the Github repo you want to make change
  repo: github-username/target-github-repo
  # This site_domain and base_url are sudo domains
  # Replace site_domain with targetDomain pulumi stack configuration inside cms/infrastructure folder
  # Replace base_url with targetDomain pulumi stack configuration inside cms-oauth/infrastructure folder
  site_domain: https://some-cms-domain.com
  base_url: https://some-oauth-domain.com
```

The site_domain is the URL of the CMS and the base_url is the URL of the OAuth Server . They should be the same as the `targetDomain` variable we set in the stack configuration of both CMS and OAuth Server.

## In the End

Congratulations on building both CMS web application, the OAuth client-server, and also deploying the infrastructure! Now if everything works perfectly, you should see the **Login with Github** button and clicking it would redirect to the GitHub login page.

![OAuth Client Server](./oauth-client-server.jpg)

People with correct access can now use the CMS.

![CMS](./cms.jpg)

All codes of CMS and OAuth Client Server are available in [Pulumi's example repositories](https://github.com/pulumi/examples)'s [aws-ts-netlify-cms-and-oauth](https://github.com/pulumi/examples/tree/master/aws-ts-netlify-cms-and-oauth/cms-oauth).

---

Special Thanks to:

- Tony Alves @talves for providing [template](https://github.com/ADARTA/netlify-cms-react-example) to separate CMS as a stand-alone React App
- Igor Kuznetsov @igk1972 for providing [go code example](https://github.com/igk1972/netlify-cms-oauth-provider-go) for providing the OAuth Client-Server source code
- Paul Stack @stack72 for developing [Pulumi example of deploying Dockerized App using ECS Fargate](https://github.com/pulumi/examples/tree/master/aws-ts-hello-fargate) and [Pulumi example of deploying the static website on AWS](https://github.com/pulumi/examples/tree/master/aws-ts-static-website)
- Everyone at Pulumi who helped me out with this
