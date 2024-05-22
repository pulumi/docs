import * as aws from "@pulumi/aws";
import * as pulumi from "@pulumi/pulumi";

const userData = `
    #!/bin/bash
    sudo yum update -y
    sudo yum upgrade -y
    sudo amazon-linux-extras install nginx1 -y
    sudo systemctl enable nginx
    sudo systemctl start nginx`
    
// [Step 2: Create a security group.]
const securityGroup = // TO-DO

// [Step 1: Create an EC2 instance.]
const server = new aws.ec2.Instance("webserver-www2", {
    instanceType: "t2.micro",
    ami: "ami-09538990a0c4fe9be",
    userData: userData,
});

export const publicIp = server.publicIp;