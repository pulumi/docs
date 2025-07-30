import pulumi
import pulumi_awsx as awsx
import os

root = pulumi.get_root_directory()
cwd = os.getcwd()
app_path = os.path.join(root, "app")
relative_path = os.path.relpath(app_path, cwd)

repository = awsx.ecr.Repository("repository", force_delete=True)

image = awsx.ecr.Image(
    "image",
    repository_url=repository.url,
    context=relative_path,
    platform="linux/amd64",
)

pulumi.export("url", repository.url)
