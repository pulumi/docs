import pulumi
import pulumi_gcp as gcp

# Create a Cloud Storage bucket using the GCP Classic provider.
bucket = gcp.storage.Bucket(
    "my-bucket",
    location="US",
    uniform_bucket_level_access=True,
    force_destroy=True,
)

# Create a Cloud Run service.
service = gcp.cloudrunv2.Service(
    "my-service",
    location="us-central1",
    deletion_protection=False,
    template=gcp.cloudrunv2.ServiceTemplateArgs(
        containers=[
            gcp.cloudrunv2.ServiceTemplateContainerArgs(
                image="us-docker.pkg.dev/cloudrun/container/hello",
            ),
        ],
    ),
)

pulumi.export("bucketName", bucket.name)
pulumi.export("serviceUrl", service.uri)
