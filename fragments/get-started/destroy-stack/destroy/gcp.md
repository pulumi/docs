```
Destroying (dev):

     Type                             Name               Status
 -   pulumi:pulumi:Stack              quickstart-dev     deleted (0.31s)
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  deleted (6s)
 -   ├─ gcp:storage:BucketObject      index.html         deleted (0.78s)
 -   └─ gcp:storage:Bucket            my-bucket          deleted (1s)

Outputs:
  - url       : "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    - 4 deleted

Duration: 9s
```
