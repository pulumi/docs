import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

lb = awsx.lb.ApplicationLoadBalancer("lb")
cluster = aws.ecs.Cluster("cluster")

service = awsx.ecs.FargateService("service",
    cluster=cluster.arn,
    assign_public_ip=True,
    desired_count=2,
    task_definition_args=awsx.ecs.FargateServiceTaskDefinitionArgs(
        container=awsx.ecs.TaskDefinitionContainerDefinitionArgs(
            name="my-service",
            image="nginx:latest",
            cpu=128,
            memory=512,
            essential=True,
            port_mappings=[awsx.ecs.TaskDefinitionPortMappingArgs(
                container_port=80,
                target_group=lb.default_target_group,
            )],
        ),
    ))

pulumi.export("url", pulumi.Output.concat("http://", lb.load_balancer.dns_name))
