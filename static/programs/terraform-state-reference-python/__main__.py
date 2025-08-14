import pulumi
import pulumi_terraform as terraform
import pulumi_eks as eks

tf_state = terraform.state.get_local_reference_output(
    path="../terraform/terraform.tfstate"
)

vpc_id = tf_state.outputs["vpc_id"]
public_subnet_ids = tf_state.outputs["public_subnet_ids"]
private_subnet_ids = tf_state.outputs["private_subnet_ids"]

cluster = eks.Cluster("my-cluster",
    vpc_id=vpc_id,
    public_subnet_ids=public_subnet_ids,
    private_subnet_ids=private_subnet_ids
)
