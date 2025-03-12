import * as pulumi from "@pulumi/pulumi";
import * as kubernetes from "@pulumi/kubernetes";

const applyPatchForceAnnotation = async (args: pulumi.ResourceTransformArgs) => {
    switch (args.type) {
        case "kubernetes:helm.sh/v4:Chart":
            break;
        default:
            args.props.metadata.annotations = {
                "cost-center": "12345",
                ...args.props.metadata.annotations,
            };
    }
    return {
        props: args.props,
        opts: args.opts,
    };
};

const ns = new kubernetes.core.v1.Namespace("cert-manager", {
    metadata: {
        name: "cert-manager",
    },
});

const certman = new kubernetes.helm.v4.Chart(
    "cert-manager",
    {
        namespace: "cert-manager",
        chart: "oci://registry-1.docker.io/bitnamicharts/cert-manager",
        version: "1.3.1",
    },
    { transforms: [applyPatchForceAnnotation] },
);

export const namespace = ns.metadata.name;
