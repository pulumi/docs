import pulumi
import pulumi_aws as aws
import pulumi_awsx as awsx

vpc = awsx.ec2.Vpc("vpc")

security_group = aws.ec2.SecurityGroup(
    "group",
    vpc_id=vpc.vpc_id,
)

ami = aws.ec2.get_ami_output(
    most_recent=True,
    owners=["amazon"],
    filters=[aws.ec2.GetAmiFilterArgs(name="name", values=["amzn2-ami-hvm-*"])],
)

instance = aws.ec2.Instance(
    "instance",
    ami=ami.id,
    instance_type="t2.micro",
    vpc_security_group_ids=[security_group.id],
    subnet_id=vpc.public_subnet_ids.apply(lambda ids: ids[0]),
)

pulumi.export("vpcId", vpc.vpc_id)
