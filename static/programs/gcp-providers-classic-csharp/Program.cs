using System.Collections.Generic;
using Pulumi;
using Gcp = Pulumi.Gcp;

return await Deployment.RunAsync(() =>
{
    // Create a Cloud Storage bucket using the GCP Classic provider.
    var bucket = new Gcp.Storage.Bucket("my-bucket", new()
    {
        Location = "US",
        UniformBucketLevelAccess = true,
        ForceDestroy = true,
    });

    // Create a Cloud Run service.
    var service = new Gcp.CloudRunV2.Service("my-service", new()
    {
        Location = "us-central1",
        DeletionProtection = false,
        Template = new Gcp.CloudRunV2.Inputs.ServiceTemplateArgs
        {
            Containers = new[]
            {
                new Gcp.CloudRunV2.Inputs.ServiceTemplateContainerArgs
                {
                    Image = "us-docker.pkg.dev/cloudrun/container/hello",
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Name,
        ["serviceUrl"] = service.Uri,
    };
});
