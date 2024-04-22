import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository", awsx.ecr.RepositoryArgs(
    force_delete=True,
))

image = awsx.ecr.Image("image", awsx.ecr.ImageArgs(
    repository_url=repository.url,
    context="./app",
    platform="linux/amd64",
))

pulumi.export("url", repository.url)
