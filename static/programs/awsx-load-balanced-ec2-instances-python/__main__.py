import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

# Get the default VPC for the current region.
vpc = awsx.ec2.DefaultVpc("default-vpc")

# Create a security group to allow traffic to and from the virtual machine.
security_group = aws.ec2.SecurityGroup(
    "web-sg",
    vpc_id=vpc.vpc_id,
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol="tcp",
            from_port=80,
            to_port=80,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            protocol="-1",
            from_port=0,
            to_port=0,
            cidr_blocks=["0.0.0.0/0"],
        ),
    ],
)

# Create an ALB in the default VPC listening on port 80.
alb = awsx.lb.ApplicationLoadBalancer(
    "web-traffic",
    listener=awsx.lb.ListenerArgs(
        port=80,
    ),
    security_groups=[security_group.id],
)

# Get the latest Amazon Linux 2 AMI.
ami = aws.ec2.get_ami_output(
    most_recent=True,
    owners=["amazon"],
    filters=[aws.ec2.GetAmiFilterArgs(name="name", values=["amzn2-ami-hvm-*"])],
)

def create_instance(subnet_id, i):
    vm = aws.ec2.Instance(
        f"web-{str(i)}",
        aws.ec2.InstanceArgs(
            ami=ami.id,
            instance_type="t2.micro",
            subnet_id=subnet_id,
            vpc_security_group_ids=alb.load_balancer.security_groups,
            user_data=f"""#!/bin/bash
            echo 'Hello World, from Server {str(i + 1)}!' > index.html
            nohup python -m SimpleHTTPServer 80 &
            """,
        ),
    )
    attachment = awsx.lb.TargetGroupAttachment(
        f"attachment-{str(i)}",
        awsx.lb.TargetGroupAttachmentArgs(
            target_group=alb.default_target_group,
            instance=vm,
        ),
    )

def create_and_attach_instances(subnet_ids):
    for index, subnet_id in enumerate(subnet_ids):
        create_instance(subnet_id, index)

# In each VPC subnet, create an EC2 instance and attach it to the ALB.
vpc.public_subnet_ids.apply(create_and_attach_instances)

# Export the resulting URL so that it's easy to access.
pulumi.export("endpoint", alb.load_balancer.dns_name)
