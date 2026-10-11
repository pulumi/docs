import pulumi
import pulumi_aws as aws
import json
import os

# IAM Role for EC2 instances
role = aws.iam.Role(
    "deepSeekRole",
    name="deepseek-role",
    assume_role_policy=json.dumps(
        {
            "Version": "2012-10-17",
            "Statement": [
                {
                    "Action": "sts:AssumeRole",
                    "Effect": "Allow",
                    "Principal": {
                        "Service": "ec2.amazonaws.com",
                    },
                }
            ],
        }
    ),
)

# Attach S3 read-only policy to the IAM Role
iam_policy_attachment = aws.iam.RolePolicyAttachment(
    "deepSeekS3Policy",
    policy_arn="arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
    role=role.name,
)

# Instance Profile containing the IAM Role
instance_profile = aws.iam.InstanceProfile(
    "deepSeekProfile", name="deepseek-profile", role=role.name
)

# Create a VPC
vpc = aws.ec2.Vpc(
    "deepSeekVpc",
    cidr_block="10.0.0.0/16",
    enable_dns_hostnames=True,
    enable_dns_support=True,
)

# Create a subnet
subnet = aws.ec2.Subnet(
    "deepSeekSubnet",
    vpc_id=vpc.id,
    cidr_block="10.0.48.0/20",
    availability_zone="eu-central-1a",
    map_public_ip_on_launch=True,
)

# Create an internet gateway
internet_gateway = aws.ec2.InternetGateway("deepSeekInternetGateway", vpc_id=vpc.id)

# Create a route table and route table association
route_table = aws.ec2.RouteTable(
    "deepSeekRouteTable",
    vpc_id=vpc.id,
    routes=[
        aws.ec2.RouteTableRouteArgs(
            cidr_block="0.0.0.0/0", gateway_id=internet_gateway.id
        )
    ],
)

route_table_association = aws.ec2.RouteTableAssociation(
    "deepSeekRouteTableAssociation", subnet_id=subnet.id, route_table_id=route_table.id
)

# Create a security group
security_group = aws.ec2.SecurityGroup(
    "deepSeekSecurityGroup",
    vpc_id=vpc.id,
    egress=[
        {
            "from_port": 0,
            "to_port": 0,
            "protocol": "-1",
            "cidr_blocks": ["0.0.0.0/0"],
        }
    ],
    ingress=[
        {
            "from_port": 22,
            "to_port": 22,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "from_port": 3000,
            "to_port": 3000,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
        {
            "from_port": 11434,
            "to_port": 11434,
            "protocol": "tcp",
            "cidr_blocks": ["0.0.0.0/0"],
        },
    ],
)

# Key pair for SSH access
public_key = open("deepseek.rsa", "r").read()
key_pair = aws.ec2.KeyPair("deepSeekKey", public_key=public_key)


# Get the latest Amazon Linux 2 AMI
ami = aws.ec2.get_ami(
    filters=[
        {"name": "name", "values": ["amzn2-ami-hvm-2.0.*-x86_64-gp2"]},
        {"name": "architecture", "values": ["x86_64"]},
    ],
    owners=["137112412989"],  # Amazon
    most_recent=True,
).id

# Create an EC2 instance
user_data = open("cloud-init.yaml", "r").read()
instance = aws.ec2.Instance(
    "deepSeekInstance",
    ami=ami,
    instance_type="g4dn.xlarge",
    key_name=key_pair.key_name,
    root_block_device=aws.ec2.InstanceRootBlockDeviceArgs(
        volume_size=100, volume_type="gp3"
    ),
    subnet_id=subnet.id,
    vpc_security_group_ids=[security_group.id],
    iam_instance_profile=instance_profile.name,
    user_data=user_data,
    tags={"Name": "deepSeek-server"},
)

pulumi.export("amiId", ami)
pulumi.export("instanceId", instance.id)
pulumi.export("instancePublicDns", instance.public_ip)
