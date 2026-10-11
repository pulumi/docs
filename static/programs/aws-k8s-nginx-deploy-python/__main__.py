import pulumi
import pulumi_kubernetes as kubernetes

# Create an NGINX Deployment and load balanced Service.
my_deployment = kubernetes.apps.v1.Deployment("my-deployment",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.apps.v1.DeploymentSpecArgs(
        replicas=2,
        selector=kubernetes.meta.v1.LabelSelectorArgs(
            match_labels={
                "appClass": "my-deployment",
            },
        ),
        template=kubernetes.core.v1.PodTemplateSpecArgs(
            metadata=kubernetes.meta.v1.ObjectMetaArgs(
                labels={
                    "appClass": "my-deployment",
                },
            ),
            spec=kubernetes.core.v1.PodSpecArgs(
                containers=[kubernetes.core.v1.ContainerArgs(
                    name="my-deployment",
                    image="nginx",
                    ports=[kubernetes.core.v1.ContainerPortArgs(
                        name="http",
                        container_port=80,
                    )],
                )],
            ),
        ),
    ))
my_service = kubernetes.core.v1.Service("my-service",
    metadata=kubernetes.meta.v1.ObjectMetaArgs(
        labels={
            "appClass": "my-deployment",
        },
    ),
    spec=kubernetes.core.v1.ServiceSpecArgs(
        type="LoadBalancer",
        ports=[kubernetes.core.v1.ServicePortArgs(
            port=80,
            target_port="http",
        )],
        selector={
            "appClass": "my-deployment",
        },
    ))

# Export the URL for the load balanced service.
pulumi.export("url", my_service.status.load_balancer.ingress[0].hostname)
