"""A Kubernetes Python Pulumi program"""
import pulumi
import pulumi_kubernetes as k8s

nginx_deployment = k8s.apps.v1.Deployment(
    "nginx-deployment",
    metadata=k8s.meta.v1.ObjectMetaArgs(
        name="nginx-deployment",
    ),
    spec=k8s.apps.v1.DeploymentSpecArgs(
        replicas=1,
        selector=k8s.meta.v1.LabelSelectorArgs(
            match_labels={
                "app": "nginx",
            },
        ),
        template=k8s.core.v1.PodTemplateSpecArgs(
            metadata=k8s.meta.v1.ObjectMetaArgs(
                labels={
                    "app": "nginx",
                },
            ),
            spec=k8s.core.v1.PodSpecArgs(
                containers=[
                    k8s.core.v1.ContainerArgs(
                        name="nginx",
                        image="nginx:latest",
                    ),
                ],
            ),
        ),
    ),
)
