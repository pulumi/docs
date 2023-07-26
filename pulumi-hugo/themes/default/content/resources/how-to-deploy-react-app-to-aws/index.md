---
title: "How to deploy React app to AWS"
allow_long_title: true
meta_desc: "Use Pulumi to quickly deploy React apps to AWS with our step-by-step guide. Ideal for developers conducting regular AWS deployments."
type: ai-answers
date: 2023-07-24
---

To deploy a react app to AWS, one option is to use the AWS Amplify App resource. This service takes your React application and deploys it to a AWS-managed hosting resource.

Below is a simple Pulumi TypeScript program to accomplish this types from the [@pulumi/aws](https://www.pulumi.com/registry/packages/aws/) package.

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

Ensure that you replace "https://github.com/myusername/myreactapp" with the URL of your own repository.

When this Pulumi program runs, it will provision an [AWS Ampl App](https://www.pulumi.com/registry/packages/aws/api-docs/amplify/app/). The Amplify App will connect to the React app in your specified GitHub and start building and deploying your React app on each push to the repository.

The buildSpec attribute is where you provide build configurations. In the above code, it is set to build the project using yarn which is a common package manager for Node.js. You can adjust this if you're using npm or a different build system.

Remember that this Pulumi program doesn't handle the creation of AWS resources needed to serve the app such as an S3 bucket or CloudFront distribution. Those are automatically by AWS Amplify.

Once your Pulumi program has successfully run, your React app will be accessible at the output URL, available in the Pulumi console or via the command line.

Use the URL from this program's output to interact with your deployed app. When you push changes to your Git repository, AWS will use the instructions in "amplify.yml" to rebuild and redeploy your app. So remember to push this Pulumi program and the amplify.yml file to your repository.

Note: This requires setting up the appropriate IAM permissions for the Amplify service to access your repository. For GitHub, that specifically involves creating a personal access token and providing it to AWS.