import pulumi
import pulumi_aws as aws

# Create a VPC.
vpc = aws.ec2.Vpc("vpc",
    cidr_block="10.0.0.0/16",
)

# Create an internet gateway.
gateway = aws.ec2.InternetGateway("gateway",
    vpc_id=vpc.id,
)

# Create a subnet that automatically assigns new instances a public IP address.
subnet = aws.ec2.Subnet("subnet",
    vpc_id=vpc.id,
    cidr_block="10.0.1.0/24",
    map_public_ip_on_launch=True,
)

# Create a route table.
routes = aws.ec2.RouteTable("routes",
    vpc_id=vpc.id,
    routes=[
        aws.ec2.RouteTableRouteArgs(
            cidr_block="0.0.0.0/0",
            gateway_id=gateway.id,
        ),
    ],
)

# Associate the route table with the public subnet.
route_table_association = aws.ec2.RouteTableAssociation("route-table-association",
    subnet_id=subnet.id,
    route_table_id=routes.id,
)

# Create a security group allowing inbound access over port 80 and outbound
# access to anywhere.
security_group = aws.ec2.SecurityGroup("security-group",
    vpc_id=vpc.id,
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            cidr_blocks=["0.0.0.0/0"],
            protocol="tcp",
            from_port=80,
            to_port=80,
        ),
    ],
    egress=[
        aws.ec2.SecurityGroupEgressArgs(
            cidr_blocks=["0.0.0.0/0"],
            from_port=0,
            to_port=0,
            protocol="-1",
        ),
    ],
)

# Find the latest Amazon Linux 2 AMI.
ami = pulumi.Output.from_input(aws.ec2.get_ami(
    owners=["amazon"],
    most_recent=True,
    filters=[{"name": "description", "values": ["Amazon Linux 2 *"]}],
)).apply(lambda ami: ami.id)

# Create and launch an Amazon Linux EC2 instance into the public subnet.
instance = aws.ec2.Instance("instance",
    ami=ami,
    instance_type="t3.nano",
    subnet_id=subnet.id,
    vpc_security_group_ids=[security_group.id],
    user_data="""
        #!/bin/bash
        sudo yum update -y
        sudo yum upgrade -y
        sudo amazon-linux-extras install nginx1 -y
        sudo systemctl enable nginx
        sudo systemctl start nginx;
    """,
)

# Export the instance's publicly accessible URL.
pulumi.export("instanceURL", pulumi.Output.concat("http://", instance.public_ip))
