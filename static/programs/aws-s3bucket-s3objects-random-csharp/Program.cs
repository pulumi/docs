using Pulumi;
using Pulumi.Aws.S3;
using Pulumi.Random;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var petName = new RandomPet("my-pet-name");

    var bucket = new Bucket("b");

    var index = new BucketObject("index.html", new BucketObjectArgs
    {
        Bucket = bucket.BucketName,
        Content = "Thanks for using Pulumi!"
    }, new CustomResourceOptions { Parent = bucket })

    var randomSite = new BucketObject("random.html", new BucketObjectArgs
    {
        Bucket = bucket.BucketName,
        Content = petName.Id
    }, new CustomResourceOptions { Parent = bucket });

    // Export the name of the bucket
    return new Dictionary<string, object?>
    {
        ["PetName"] = petName.Id
    };
});
