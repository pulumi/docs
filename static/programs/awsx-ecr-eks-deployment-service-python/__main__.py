import pulumi
import pulumi_awsx as awsx
import pulumi_eks as eks
import pulumi_kubernetes as kubernetes

app_name = "my-app"

repository = awsx.ecr.Repository(
    "repository",
    awsx.ecr.RepositoryArgs(force_delete=True),
)

image = awsx.ecr.Image(
    "image",
    awsx.ecr.ImageArgs(
        repository_url=repository.url, context="./app", platform="linux/amd64"
    ),
)

cluster = eks.Cluster("cluster")

cluster_provider = kubernetes.Provider(
    "clusterProvider", kubeconfig=cluster.kubeconfig, enable_server_side_apply=True
)

deployment = kubernetes.apps.v1.Deployment(
    "deployment",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": app_name,
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=2,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "appClass": app_name,
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "appClass": app_name,
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[
                    kubernetes.core.v1.ContainerArgs(
                        name=app_name,
                        image=image.image_uri,
                        ports=[
                            kubernetes.core.v1.ContainerPortArgs(
                                name="http",
                                container_port=80,
                            )
                        ],
                    ),
                ],
            ),
        ),
    ),
    opts=pulumi.ResourceOptions(provider=cluster_provider),
)

service = kubernetes.core.v1.Service(
    "service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": app_name,
        },
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        type="LoadBalancer",
        selector={
            "appClass": app_name,
        },
        ports=[
            kubernetes.core.v1.ServicePortArgs(
                port=80,
                target_port="http",
            )
        ],
    ),
    opts=pulumi.ResourceOptions(provider=cluster_provider),
)

pulumi.export("url", service.status.load_balancer.ingress[0].hostname)
