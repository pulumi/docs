---
title: "How to deploy React app to AWS"
allow_long_title: true
meta_desc: "Use Pulumi to quickly deploy React apps to AWS with our step-by-step guide. Ideal for developers conducting regular AWS deployments."
type: ai-answers
date: 2023-07-24
---

If you have developed a React app and want to deploy it to the cloud, AWS Amplify is a great option. And with Pulumi, you can easily automate the deployment process using a simple TypeScript program.

In this article, we'll walk through how to deploy a React app to AWS using Pulumi and AWS Amplify. We'll start by explaining what AWS Amplify is and why it's a good option for hosting React apps. Then, we'll dive into the Pulumi TypeScript program that automates the deployment process.

### What is AWS Amplify?

AWS Amplify is a fully managed service provided by Amazon Web Services (AWS) that makes it easy to develop, build, and deploy web and mobile applications. It provides a simple and intuitive interface for managing the entire application development lifecycle.

One of the key features of AWS Amplify is its ability to deploy static websites and single-page applications (SPAs) built with popular front-end frameworks like React, Angular, and Vue.js. By connecting Amplify to your code repository, it can automatically build and deploy your app whenever changes are pushed to the repository.

### The Pulumi Program

To deploy a React app to AWS using Pulumi, we'll write a simple TypeScript program. This program will use the [@pulumi/aws](https://www.pulumi.com/registry/packages/aws/) package to provision an AWS Amplify App resource.

Here's the Pulumi TypeScript program:

```typescript
import * as aws from "@pulumi/aws";

// After running "git push", AWS Amplify Console will start building and deploying app
let app = new aws.amplify.App("myapp", {
    repository: "https://github.com/myusername/myreactapp",  // Specify your git repository here

    // Specify build settings with the amplify.yml file
    buildSpec: `version: 0.1
        frontend:
        phases:
            preBuild:
            commands:
                - yarn install
            build:
            commands:
                - yarn run build
        artifacts:
            # IMPORTANT - Please verify your build output directory
            baseDirectory: /public
            files:
            - '**/*'
        cache:
            paths:
            - node_modules/**/*`
});

// Output the DNS of the app
export const url = app.defaultDomain;
```

In this program, we import the necessary AWS resources from the `@pulumi/aws` package. Then, we create a new instance of the `aws.amplify.App` class. This will provision an AWS Amplify App resource.

To configure this resource, we provide a few parameters:

- `repository`: The URL of your Git repository containing the React app code. Make sure to replace `"https://github.com/myusername/myreactapp"` with the URL of your own repository.

- `buildSpec`: This specifies the build settings for the app. In the example above, we use a YAML file called `amplify.yml` to define these settings. The `buildSpec` property is a multiline string that contains the content of the `amplify.yml` file. This file specifies the necessary build commands to install dependencies and build the React app.

After creating the `aws.amplify.App` instance, we export the `defaultDomain` property of the app. This property represents the DNS of the app, which will be outputted by the Pulumi program.

### How the Deployment Works

When you run this Pulumi program, it will provision an AWS Amplify App resource. This resource will connect to the React app in your specified Git repository and start building and deploying your app on each push to the repository.

To trigger the build and deployment process, you simply need to run `git push` on your local development machine. AWS Amplify Console will detect the push and start building and deploying your app automatically.

The build process is defined in the `amplify.yml` file. In the example code above, we use YAML syntax to define a multi-phase build process. The `preBuild` phase installs the project dependencies using `yarn install`. Then, the `build` phase builds the React app using `yarn run build`.

The `amplify.yml` file also specifies the output artifacts for the build process. In the example code above, we specify that the build output directory is `/public` and all files in this directory should be included in the build artifacts.

Once the build and deployment process is complete, your React app will be accessible at the output URL, which is available in the Pulumi console or via the command line.

### Conclusion

In this article, we've shown you how to deploy a React app to AWS using Pulumi and AWS Amplify. We've explained what AWS Amplify is and why it's a good option for hosting React apps. We've also walked through a simple Pulumi TypeScript program that automates the deployment process.

By using Pulumi, you can easily manage and automate the deployment of your React app to AWS. You can customize the build process and other settings using the `amplify.yml` file. And with AWS Amplify, you get a fully managed and scalable hosting solution for your React app.

So go ahead and give it a try! Deploy your React app to AWS with Pulumi and AWS Amplify, and experience the power of Infrastructure as Code.

Happy coding!
