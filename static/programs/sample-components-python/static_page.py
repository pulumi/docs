import json
from typing import Optional, TypedDict

import pulumi
from pulumi import ResourceOptions
from pulumi_aws import s3


class StaticPageArgs(TypedDict):
    index_content: pulumi.Input[str]
    """The HTML content for index.html."""


class StaticPage(pulumi.ComponentResource):
    endpoint: pulumi.Output[str]
    """The URL of the static website."""

    def __init__(self,
                 name: str,
                 args: StaticPageArgs,
                 opts: Optional[ResourceOptions] = None) -> None:

        super().__init__("sample-components:index:StaticPage", name, {}, opts)

        bucket = s3.Bucket(
            f"{name}-bucket",
            opts=ResourceOptions(parent=self))

        bucket_website = s3.BucketWebsiteConfiguration(
            f"{name}-website",
            bucket=bucket.bucket,
            index_document={"suffix": "index.html"},
            opts=ResourceOptions(parent=self))

        s3.BucketObject(
            f"{name}-index-object",
            bucket=bucket.bucket,
            key="index.html",
            content=args.get("index_content"),
            content_type="text/html",
            opts=ResourceOptions(parent=self))

        bucket_public_access_block = s3.BucketPublicAccessBlock(
            f"{name}-public-access-block",
            bucket=bucket.id,
            block_public_acls=False,
            opts=ResourceOptions(parent=self))

        s3.BucketPolicy(
            f"{name}-bucket-policy",
            bucket=bucket.bucket,
            policy=bucket.bucket.apply(_allow_getobject_policy),
            opts=ResourceOptions(parent=self, depends_on=[bucket_public_access_block]))

        self.endpoint = bucket_website.website_endpoint

        self.register_outputs({
            "endpoint": bucket_website.website_endpoint
        })


def _allow_getobject_policy(bucket_name: str) -> str:
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [
            {
                "Effect": "Allow",
                "Principal": "*",
                "Action": ["s3:GetObject"],
                "Resource": [
                    f"arn:aws:s3:::{bucket_name}/*",
                ],
            },
        ],
    })
