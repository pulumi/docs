import pulumi
from pulumi_gcp import storage, projects

role = projects.IAMCustomRole(
    "bucketViewerRole",
    role_id="bucketViewerRole",
    title="Bucket Viewer Role",
    permissions=[
        "storage.objects.get",
        "storage.objects.list"
    ],
    stage="GA"
)

bucket = storage.Bucket(
    "my-bucket",
    location="US",
    force_destroy=True
)

bucket_iam_member = storage.BucketIAMMember(
    "bucketViewerRoleAssignment",
    bucket=bucket.name,
    role=role.name,
    member="allAuthenticatedUsers"
)

bucket_name = bucket.name
role_name = role.role_id

file_content = f"My bucket role name is: {role_name}"

bucket_object = storage.BucketObject(
    "my-object",
    bucket=bucket_name,
    source=pulumi.StringAsset(file_content),
    content_type="text/plain"
)

pulumi.export("roleName", role.role_id)
pulumi.export("bucketName", bucket.name)
