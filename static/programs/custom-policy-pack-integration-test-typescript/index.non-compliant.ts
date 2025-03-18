import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";

// Create an AWS S3 Bucket
const bucket = new aws.s3.BucketV2("my-bucket", {
    bucketPrefix: "something-unexpected-",
    tags: {},
});

// Export the name of the bucket
export const bucketName = bucket.id;

// Create an AWS EC2 Instance

// Find an appropriate AMI
const ubuntu = aws.ec2.getAmi({
    mostRecent: true,
    filters: [
        {
            name: "name",
            values: ["ubuntu/images/hvm-ssd/ubuntu-jammy-22.04-amd64-server-*"],
        },
        {
            name: "virtualization-type",
            values: ["hvm"],
        },
    ],
    owners: ["099720109477"], // Canonical
});

// Define a security group
// Create a new security group that permits SSH access.
const ssh_security_group = new aws.ec2.SecurityGroup("ssh-security-group", {
    description: "Enable SSH access",
    ingress: [{ protocol: "tcp", fromPort: 22, toPort: 22, cidrBlocks: ["0.0.0.0/0"] }],
});

// Define the EC2 instance
const instance = new aws.ec2.Instance("web-server", {
    instanceType: aws.ec2.InstanceType.T3_Micro, // Instance type
    ami: ubuntu.then(ubuntu => ubuntu.id),
    vpcSecurityGroupIds: [ssh_security_group.id],
    tags: {
        Name: "web-server",
    },
});

// Export the instance's public IP address
export const publicIp = instance.publicIp;
