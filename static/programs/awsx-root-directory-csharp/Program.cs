using System.Collections.Generic;
using System.IO;
using Pulumi;
using Awsx = Pulumi.Awsx;

return await Deployment.RunAsync(() =>
{
    var root = Pulumi.Deployment.Instance.RootDirectory;
    var cwd = Directory.GetCurrentDirectory();
    var appPath = Path.Combine(root, "app");
    var relativePath = Path.GetRelativePath(cwd, appPath);

    var repository = new Awsx.Ecr.Repository("repository", new()
    {
        ForceDelete = true,
    });

    var image = new Awsx.Ecr.Image("image", new()
    {
        RepositoryUrl = repository.Url,
        Context = relativePath,
        Platform = "linux/amd64",
    });

    return new Dictionary<string, object?>
    {
        ["url"] = repository.Url,
    };
});
