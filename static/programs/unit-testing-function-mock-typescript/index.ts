import * as aws from "@pulumi/aws";

// Look up the most recent Amazon Linux 2 AMI.
const ami = aws.ec2.getAmiOutput({
    owners: ["amazon"],
    mostRecent: true,
    filters: [{ name: "name", values: ["amzn2-ami-hvm-*-x86_64-gp2"] }],
});

export const server = new aws.ec2.Instance("web-server", {
    ami: ami.id,
    instanceType: "t3.micro",
    tags: { Name: "web-server" },
});
