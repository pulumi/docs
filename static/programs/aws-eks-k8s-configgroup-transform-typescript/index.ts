import * as pulumi from "@pulumi/pulumi";
import * as eks from "@pulumi/eks";
import * as k8s from "@pulumi/kubernetes";

// Create an EKS cluster.
const cluster = new eks.Cluster("my-cluster");
const eksProvider = cluster.provider;
const namespaceName = "guestbook";

const guestbook = new k8s.yaml.v2.ConfigGroup("guestbook", { files: "yaml/*.yaml" }, {
    provider: eksProvider,
    transforms: [
        async args => {
            const props = args.props as any;
            // Make every service private to the cluster.
            if (args.type === "kubernetes:core/v1:Service" && props?.spec?.type === "LoadBalancer") {
                props.spec.type = "ClusterIP";
            }
            // Put every resource in the created namespace.
            props.metadata = { ...props.metadata, namespace: namespaceName };
            return { props, opts: args.opts };
        },
    ],
});
