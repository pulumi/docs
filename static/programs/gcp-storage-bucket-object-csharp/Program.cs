using Pulumi;
using Pulumi.Gcp.Storage;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    // Create a GCP resource (Storage Bucket)
    var bucket = new Bucket("my-bucket", new BucketArgs
    {
        Location = "US"
    });

    // Export the DNS name of the bucket
    return new Dictionary<string, object?>
    {
        ["bucketName"] = bucket.Url
    };
});
