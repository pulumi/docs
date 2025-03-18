---
title: "How to configure multiple apps with one load balancer in Kubernetes"
allow_long_title: true
meta_desc: "Use this Pulumi guide to configure multiple apps via a single Kubernetes load balancer. Enhance service management and traffic distribution."
type: ai-answers
date: 2023-07-24
---

Welcome, fellow developers! Today, we are going to explore an interesting use case of Kubernetes and Pulumi. We'll walk through the process of configuring multiple apps with one load balancer in Kubernetes. This approach is achieved by utilizing the powerful Ingress resource in Kubernetes, which acts as a load balancer and directs traffic to different services based on certain rules.

### Understanding the Problem

Imagine you have multiple applications running in your Kubernetes cluster and you want to expose them to the outside world using a single load balancer. Each application should be accessible via a unique path. For example, all traffic with the path "/app1" should be directed to App1, and traffic with the path "/app2" should be directed to App2.

### The Power of Ingress

In Kubernetes, Ingresses allow you to define rules for routing HTTP and HTTPS traffic to backend services. Think of an Ingress as a traffic cop, making decisions about where each request should go based on its path.

To achieve our goal of configuring multiple apps with one load balancer, we will create an Ingress resource and define rules for each application. These rules will map specific paths to different backend services, effectively treating the Ingress as a load balancer.

### Writing the Pulumi Program

Before we dive into writing the Pulumi program, let's lay out the structure. We will create an Ingress resource with two rules, each directing traffic to a different service. The services, in turn, will be responsible for serving our applications.

Here is an example of a Pulumi program written in TypeScript that achieves this:

```typescript
import * as k8s from "@pulumi/kubernetes";

// Create the Ingress
const ingress = new k8s.networking.v1.Ingress("app-ingress", {
    metadata: { annotations: { "kubernetes.io/ingress.class": "nginx" } },
    spec: {
        rules: [
            {
                host: "your.host.com",
                http: {
                    paths: [
                        {
                            path: "/app1",
                            pathType: "Prefix",
                            backend: {
                                service: {
                                    name: "app1-service",
                                    port: {
                                        number: 80,
                                    }
                                }
                            }
                        },
                        {
                            path: "/app2",
                            pathType: "Prefix",
                            backend: {
                                service: {
                                    name: "app2-service",
                                    port: {
                                        number: 80,
                                    }
                                }
                            }
                        },
                    ]
                }
            }
        ]
    }
});
```

In this program, we create an instance of the `k8s.networking.v1.Ingress` resource called `app-ingress`. We define the necessary metadata, such as the `kubernetes.io/ingress.class` annotation, which specifies the Ingress controller to use (in this case, "nginx").

Next, we define the rules within the `spec` property. Each rule consists of a `host` (e.g., "your.host.com") and an `http` object that contains an array of `paths`. Each path represents a specific URL path that should be directed to a backend service.

For example, the path "/app1" is directed to the `app1-service`, and the path "/app2" is directed to the `app2-service`. Notice that we specify the `pathType` as "Prefix," which means that any URL path starting with "/app1" or "/app2" will be directed to the respective service.

### Running the Program

Once you have written the Pulumi program, it's time to deploy it and see the magic happen! First, make sure you have set up your Kubernetes cluster and have the necessary permissions to deploy resources. Then, follow these steps:

1. Initialize the Pulumi project:
   ```shell
   pulumi new kubernetes-typescript
   ```

2. Install the required dependencies (ensure you are in the project root directory):
   ```shell
   npm install @pulumi/kubernetes --save
   ```

3. Deploy the program:
   ```shell
   pulumi up
   ```

Pulumi will work its magic and deploy the Ingress resource along with any other resources defined in your program.

### Verify and Test

Once the deployment is complete, you can verify that the Ingress resource has been created by running the following command:

```shell
kubectl get ingress
```

You should see your Ingress listed, along with its rules and annotations.

To test if the load balancing is working as expected, you can send HTTP requests to your applications using the defined paths. For example, if you have a cluster with the hostname "your.host.com," you can send a request to "http://your.host.com/app1" and "http://your.host.com/app2" to access App1 and App2, respectively.

### Conclusion

Congratulations! You have successfully configured multiple apps with one load balancer in Kubernetes using Pulumi. By leveraging the power of Ingresses and defining rules for each application, you can easily expose multiple services through a single entry point.

Remember, this is just one use case of Ingress resources. Feel free to explore more advanced features such as SSL termination, TLS certificate management, and more.

If you'd like to dive deeper into the details, check out the [official documentation](https://www.pulumi.com/docs/reference/pkg/kubernetes/networking/v1/ingress/) for the `k8s.networking.v1.Ingress` resource in the Pulumi Registry.

Happy coding, and may your apps be always reachable and well-balanced!
