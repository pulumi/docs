using System.Collections.Generic;
using Pulumi;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var repository = new Awsx.Ecr.Repository("repository", new()
    {
        ForceDelete = true,
    });

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Context = "./app",
        Platform = "linux/amd64",
    });

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
    };
});
