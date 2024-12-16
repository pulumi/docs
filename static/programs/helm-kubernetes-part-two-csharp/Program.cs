using Pulumi;
using Pulumi.Experimental.Provider;
using Pulumi.Kubernetes.Helm.V4;
using Pulumi.Kubernetes.Types.Inputs;
using Pulumi.Kubernetes.Types.Inputs.Helm.V4;
using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using System.Collections.Immutable;

await Deployment.RunAsync<MyStack>();


class MyStack : Stack
{
    public MyStack() 
    {
        var certman = new Chart("cert-manager", new ChartArgs
        {
            Namespace = "cert-manager",
            Chart = "oci://registry-1.docker.io/bitnamicharts/cert-manager",
            Version = "1.3.1",
        }, 
        new ComponentResourceOptions
        {
            ResourceTransforms =
            {
               async (args, _) => 
                {
                    Console.WriteLine("Transforming resource");
                    if (args.Type != "kubernetes:helm.sh/v4:Chart")
                    {
                    var myTags = ImmutableDictionary.Create<string, object>().Add("cost-center", "12345");

                    InputMap<object> tags =
                    args.Args.TryGetValue("metadata", out var tagsValue) && tagsValue is not null ?
                        tagsValue is Output<ImmutableDictionary<string, object>> tagsOutput ? tagsOutput :
                        tagsValue is ImmutableDictionary<string, object> tagsDictionary ? tagsDictionary :
                        throw new InvalidOperationException($"Unexpected tags type: {tagsValue.GetType()}") :
                    ImmutableDictionary<string, object>.Empty;

                    tags = tags.Apply(t => t.SetItems(myTags));
                    return new( args.Args.SetItem("metadata", tags), args.Options);
                    }
                    return null;
                },
            },
        });
    }
}
