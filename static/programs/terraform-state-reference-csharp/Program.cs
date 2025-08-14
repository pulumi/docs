using System.Linq;
using System.Collections.Immutable;
using Pulumi;
using Pulumi.Terraform.State;
using Pulumi.Eks;

return await Deployment.RunAsync(() =>
{
    var tfState = GetLocalReference.Invoke(new GetLocalReferenceInvokeArgs
    {
        Path = "../terraform/terraform.tfstate"
    });

    var vpcId = tfState.Apply(state => (string)state.Outputs["vpc_id"]);

    var publicSubnetIds = tfState.Apply(state =>
        ((ImmutableArray<object>)state.Outputs["public_subnet_ids"])
            .Select(id => (string)id)
            .ToArray());

    var privateSubnetIds = tfState.Apply(state =>
        ((ImmutableArray<object>)state.Outputs["private_subnet_ids"])
            .Select(id => (string)id)
            .ToArray());

    var cluster = new Cluster("my-cluster", new ClusterArgs
    {
        VpcId = vpcId,
        PublicSubnetIds = publicSubnetIds,
        PrivateSubnetIds = privateSubnetIds
    });
});