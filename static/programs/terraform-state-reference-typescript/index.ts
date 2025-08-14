import * as pulumi from "@pulumi/pulumi";
import * as terraform from "@pulumi/terraform";
import * as eks from "@pulumi/eks";

const tfState = terraform.state.getLocalReferenceOutput({
  path: "../terraform/terraform.tfstate",
});

const vpcId = tfState.outputs["vpc_id"] as pulumi.Output<string>;
const publicSubnetIds = tfState.outputs["public_subnet_ids"] as pulumi.Output<string[]>;
const privateSubnetIds = tfState.outputs["private_subnet_ids"] as pulumi.Output<string[]>;

const cluster = new eks.Cluster("my-cluster", {
  vpcId: vpcId,
  publicSubnetIds: publicSubnetIds,
  privateSubnetIds: privateSubnetIds,
});
