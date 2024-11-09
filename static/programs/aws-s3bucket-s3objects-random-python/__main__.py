import pulumi
import pulumi_random as random
import pulumi_aws as aws

pet_name = random.RandomPet('my-pet-name')

bucket = aws.s3.Bucket("b")

index = aws.s3.BucketObject("index.html",
    bucket=bucket.bucket,
    content="Thanks for using Pulumi!",
    opts=pulumi.ResourceOptions(parent=bucket)
)

random_site = aws.s3.BucketObject("random.html",
    bucket=bucket.bucket,
    content=pet_name.id,
    opts=pulumi.ResourceOptions(parent=bucket)
)

pulumi.export('PetName', pet_name.id)