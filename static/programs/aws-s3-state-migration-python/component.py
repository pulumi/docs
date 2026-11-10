import pulumi
import pulumi_aws as aws

from migration import COMPONENT_TYPE, migrate_bucket_state


class VersionedBucket(pulumi.ComponentResource):
    def __init__(
        self, name: str, bucket_name: str, opts: pulumi.ResourceOptions | None = None
    ):
        opts = pulumi.ResourceOptions.merge(
            opts, pulumi.ResourceOptions(state_migrations=[migrate_bucket_state])
        )
        super().__init__(COMPONENT_TYPE, name, {}, opts)

        bucket = aws.s3.Bucket(
            name,
            bucket=bucket_name,
            force_destroy=True,
            tags={"example": "s3-bucket-state-migration", "managed-by": "pulumi"},
            versioning={"enabled": True},
            opts=pulumi.ResourceOptions(parent=self),
        )
        self.bucket_name = bucket.bucket
        self.bucket_id = bucket.id
        self.bucket_urn = bucket.urn
        self.register_outputs({"bucketName": self.bucket_name})
