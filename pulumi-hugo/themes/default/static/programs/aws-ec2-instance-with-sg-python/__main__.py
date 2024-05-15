import pulumi
import pulumi_aws as aws

group = aws.ec2.SecurityGroup(
    "web-sg",
    description="Enable HTTP access",
    ingress=[
        {
            "protocol": "tcp",
            "from_port": 80,
            "to_port": 80,
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
)

server = aws.ec2.Instance(
    "web-server",
    ami="ami-0319ef1a70c93d5c8",
    instance_type="t2.micro",
    vpc_security_group_ids=[group.id],
)

pulumi.export("public_ip", server.public_ip)
pulumi.export("public_dns", server.public_dns)
