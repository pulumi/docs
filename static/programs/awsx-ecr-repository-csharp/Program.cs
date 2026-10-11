using Pulumi;
using Pulumi.Aws.S3;
using Awsx = Pulumi.Awsx;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository");

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
    };
});
