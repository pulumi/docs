import pulumi_aws as aws

# Look up the most recent Amazon Linux 2023 AMI.
ami = aws.ec2.get_ami_output(
    owners=["amazon"],
    most_recent=True,
    filters=[{"name": "name", "values": ["al2023-ami-2023.*-x86_64"]}],
)

server = aws.ec2.Instance(
    "web-server",
    ami=ami.id,
    instance_type="t3.micro",
    tags={"Name": "web-server"},
)
