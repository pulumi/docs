using System.Collections.Generic;
using Pulumi;
using Pulumi.Aws.S3;

return await Deployment.RunAsync(() => 
{
    var bucket = new Bucket("bucket");

    var file = new BucketObject("bucket-object", new BucketObjectArgs
    {
        Bucket = bucket.Id,
        Key = "some-file.txt",
        Content = "some-content",
    });

    var s3Url = Output.Format($"s3://{bucket.Id}/{file.Key}");

    return new Dictionary<string, object?>
    {
        ["s3Url"] = s3Url,
    };
});
