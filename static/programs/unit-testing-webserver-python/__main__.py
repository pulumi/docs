import pulumi
from pulumi_aws import ec2

group = ec2.SecurityGroup('web-secgrp', ingress=[
    { "protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"] },
    { "protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"] },
])

user_data = '#!/bin/bash echo "Hello, World!" > index.html nohup python3 -m http.server 80 &'

# Look up the latest Amazon Linux 2 AMI.
ami = ec2.get_ami_output(
    owners=["amazon"],
    most_recent=True,
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}])

server = ec2.Instance('web-server-www',
    instance_type="t2.micro",
    security_groups=[ group.name ], # reference the group object above
    ami=ami.id,
    user_data=user_data)            # start a simple web server
