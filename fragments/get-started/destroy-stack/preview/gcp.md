```
Previewing destroy (dev):

     Type                             Name               Plan
 -   pulumi:pulumi:Stack              quickstart-dev     delete
 -   ├─ gcp:storage:BucketIAMBinding  my-bucket-binding  delete
 -   ├─ gcp:storage:BucketObject      index.html         delete
 -   └─ gcp:storage:Bucket            my-bucket          delete

Outputs:
  - url       : "http://storage.googleapis.com/my-bucket-daa12be/index.html"

Resources:
    - 4 to delete

Do you want to perform this destroy?
> yes
  no
  details
```
