import pulumi
import pulumi_awsx as awsx

repository = awsx.ecr.Repository("repository")
pulumi.export("url", repository.url)
