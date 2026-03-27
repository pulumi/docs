using Pulumi;
using Kubernetes = Pulumi.Kubernetes;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var helm = new Kubernetes.Helm.V3.Release("helm", new()
    {
        Chart = "https://charts.bitnami.com/bitnami/wordpress-15.2.17.tgz",
    });

});
