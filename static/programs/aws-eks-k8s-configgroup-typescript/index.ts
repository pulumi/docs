import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");

// Create resources from standard Kubernetes guestbook YAML example.
const guestbook = new k8s.yaml.v2.ConfigGroup("guestbook", { files: "yaml/*.yaml" }, { provider: cluster.provider });

// Export the (cluster-private) IP address of the Guestbook frontend.
export const frontendIp = guestbook.getResource("v1/Service", "frontend", "").spec.clusterIP;
