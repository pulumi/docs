import pulumi
import pulumi_aws as aws

# Create an AWS S3 Bucket
bucket = aws.s3.BucketV2("my-bucket",
    bucket_prefix="something-unexpected-",
    tags={}
)

# Export the name of the bucket
pulumi.export('bucket_name', bucket.id)

# Find an appropriate AMI
ubuntu = aws.ec2.get_ami(
    most_recent=True,
    filters=[
        {
            'name': 'name', 
            'values': ['ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*']
        },
        {
            "name": "virtualization-type",
            "values": ["hvm"],
        }
    ],
    owners=['099720109477'], # Canonical
)

# Define a security group that permits SSH access
ssh_security_group = aws.ec2.SecurityGroup('ssh-security-group',
    description='Enable SSH access',
    ingress=[
        aws.ec2.SecurityGroupIngressArgs(
            protocol='tcp', from_port=22, to_port=22, cidr_blocks=['0.0.0.0/0'],
        )
    ]
)

# Define the EC2 instance
instance = aws.ec2.Instance('web-server',
    instance_type=aws.ec2.InstanceType.T3_MICRO, # Instance type
    ami=ubuntu.id,
    vpc_security_group_ids=[ssh_security_group.id],
    tags={
        "Name": "web-server",
    }
)

# Export the instance's public IP address
pulumi.export('public_ip', instance.public_ip)