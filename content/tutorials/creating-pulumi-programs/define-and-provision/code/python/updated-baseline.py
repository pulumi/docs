import pulumi
import pulumi_aws as aws

user_data = """
#!/bin/bash
sudo yum update -y
sudo yum upgrade -y
sudo amazon-linux-extras install nginx1 -y
sudo systemctl enable nginx
sudo systemctl start nginx
"""

# [Step 2: Create a security group.]
security_group = # TO-DO

# [Step 1: Create an EC2 instance.]
server = aws.ec2.Instance(
    'webserver-www',
    instance_type="t2.micro",
    ami="ami-09538990a0c4fe9be",
    user_data=user_data,
    vpc_security_group_ids=[security_group.id], # Security group property and reference
)

pulumi.export('publicIp', server.public_ip)