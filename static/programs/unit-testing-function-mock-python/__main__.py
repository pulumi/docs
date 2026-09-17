import pulumi_aws as aws

# Look up the most recent Amazon Linux 2 AMI.
ami = aws.ec2.get_ami_output(
    owners=["amazon"],
    most_recent=True,
    filters=[{"name": "name", "values": ["amzn2-ami-hvm-*-x86_64-gp2"]}],
)

server = aws.ec2.Instance(
    "web-server",
    ami=ami.id,
    instance_type="t3.micro",
    tags={"Name": "web-server"},
)
