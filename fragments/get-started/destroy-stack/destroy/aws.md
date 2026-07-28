```
Destroying (dev):

     Type                                    Name                 Status
 -   pulumi:pulumi:Stack                     quickstart-dev       deleted (0.31s)
 -   ├─ aws:s3:BucketObject                  index.html           deleted (1s)
 -   ├─ aws:s3:BucketPublicAccessBlock       public-access-block  deleted (0.67s)
 -   ├─ aws:s3:BucketWebsiteConfiguration    website              deleted (0.88s)
 -   ├─ aws:s3:BucketOwnershipControls       ownership-controls   deleted (1s)
 -   └─ aws:s3:Bucket                      my-bucket            deleted (0.58s)

Outputs:
  - bucketEndpoint: "http://my-bucket-dfd6bd0.s3-website-us-east-1.amazonaws.com"
  - bucketName    : "my-bucket-dfd6bd0"

Resources:
    - 5 deleted

Duration: 4s
```
