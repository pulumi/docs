import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as fs from "fs";

const role = new aws.iam.Role("deepSeekRole", {
    name: "deepseek-role",
    assumeRolePolicy: JSON.stringify({
        Version: "2012-10-17",
        Statement: [
            {
                Action: "sts:AssumeRole",
                Effect: "Allow",
                Principal: {
                    Service: "ec2.amazonaws.com",
                },
            },
        ],
    }),
});

new aws.iam.RolePolicyAttachment("deepSeekS3Policy", {
    policyArn: "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
    role: role.name,
});

const instanceProfile = new aws.iam.InstanceProfile("deepSeekProfile", {
    name: "deepseek-profile",
    role: role.name,
});

const vpc = new aws.ec2.Vpc("deepSeekVpc", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
});

const subnet = new aws.ec2.Subnet("deepSeekSubnet", {
    vpcId: vpc.id,
    cidrBlock: "10.0.48.0/20",
    availabilityZone: pulumi.interpolate`${aws.getAvailabilityZones().then(it => it.names[0])}`,
    mapPublicIpOnLaunch: true,
});

const internetGateway = new aws.ec2.InternetGateway("deepSeekInternetGateway", {
    vpcId: vpc.id,
});

const routeTable = new aws.ec2.RouteTable("deepSeekRouteTable", {
    vpcId: vpc.id,
    routes: [
        {
            cidrBlock: "0.0.0.0/0",
            gatewayId: internetGateway.id,
        },
    ],
});

const routeTableAssociation = new aws.ec2.RouteTableAssociation("deepSeekRouteTableAssociation", {
    subnetId: subnet.id,
    routeTableId: routeTable.id,
});

const securityGroup = new aws.ec2.SecurityGroup("deepSeekSecurityGroup", {
    vpcId: vpc.id,
    egress: [
        {
            fromPort: 0,
            toPort: 0,
            protocol: "-1",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    ingress: [
        {
            fromPort: 22,
            toPort: 22,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
        {
            fromPort: 3000,
            toPort: 3000,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
        {
            fromPort: 11434,
            toPort: 11434,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
});

const keyPair = new aws.ec2.KeyPair("deepSeekKey", {
    publicKey: pulumi.output(fs.readFileSync("deepseek.rsa", "utf-8")),
});

const deepSeekAmi = aws.ec2
    .getAmi({
        filters: [
            {
                name: "name",
                values: ["amzn2-ami-hvm-2.0.*-x86_64-gp2"],
            },
            {
                name: "architecture",
                values: ["x86_64"],
            },
        ],
        owners: ["137112412989"], // Amazon
        mostRecent: true,
    })
    .then(ami => ami.id);

const deepSeekInstance = new aws.ec2.Instance("deepSeekInstance", {
    ami: deepSeekAmi,
    instanceType: "g4dn.xlarge",
    keyName: keyPair.keyName,
    rootBlockDevice: {
        volumeSize: 100,
        volumeType: "gp3",
    },
    subnetId: subnet.id,
    vpcSecurityGroupIds: [securityGroup.id],
    iamInstanceProfile: instanceProfile.name,
    userData: fs.readFileSync("cloud-init.yaml", "utf-8"),
    tags: {
        Name: "deepSeek-server",
    },
});

export const amiId = deepSeekAmi;
export const instanceId = deepSeekInstance.id;
export const instancePublicDns = deepSeekInstance.publicIp;
