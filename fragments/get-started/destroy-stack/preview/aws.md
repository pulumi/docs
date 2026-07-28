```
Previewing destroy (dev):

     Type                                    Name                 Status
 -   pulumi:pulumi:Stack                     quickstart-dev       delete
 -   ├─ aws:s3:BucketObject                  index.html           delete
 -   ├─ aws:s3:BucketOwnershipControls       ownership-controls   delete
 -   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  delete
 -   ├─ aws:s3:BucketWebsiteConfiguration    website              delete
 -   └─ aws:s3:Bucket                      my-bucket            delete

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 to delete

Do you want to perform this destroy?
> yes
  no
  details
```
