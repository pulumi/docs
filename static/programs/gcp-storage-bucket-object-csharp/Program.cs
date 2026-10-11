using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Gcp = Pulumi.Gcp;

return await Deployment.RunAsync(() =>
{
    var bucket = new Gcp.Storage.Bucket("bucket", new()
    {
        Location = "US",
        ForceDestroy = true,
    });

    var role = new Gcp.Projects.IAMCustomRole("role", new()
    {
        RoleId = "bucketViewerRole",
        Title = "Bucket Viewer Role",
        Permissions = new[]
        {
            "storage.objects.get",
            "storage.objects.list",
        },
        Stage = "GA",
    });

    var bucketViewerRoleAssignment = new Gcp.Storage.BucketIAMMember("bucketViewerRoleAssignment", new()
    {
        Bucket = bucket.Name,
        Role = role.Name,
        Member = "allAuthenticatedUsers",
    });

    var bucketName = bucket.Name;
    var roleName = role.RoleId;

    var bucketObject = new Gcp.Storage.BucketObject("bucketObject", new()
    {
        Bucket = bucketName,
        Content = roleName.Apply(roleName => $"My bucket role name is: {roleName}"),
        ContentType = "text/plain",
    });

    return new Dictionary<string, object?>
    {
        ["roleName"] = role.RoleId,
        ["bucketName"] = bucket.Name,
    };
});
