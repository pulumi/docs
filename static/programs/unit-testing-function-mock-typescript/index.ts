import * as aws from "@pulumi/aws";

// Look up the most recent Amazon Linux 2023 AMI.
const ami = aws.ec2.getAmiOutput({
    owners: ["amazon"],
    mostRecent: true,
    filters: [{ name: "name", values: ["al2023-ami-2023.*-x86_64"] }],
});

export const server = new aws.ec2.Instance("web-server", {
    ami: ami.id,
    instanceType: "t3.micro",
    tags: { Name: "web-server" },
});
