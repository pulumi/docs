export const awsEC2Ubuntu =
`# This Terraform sample provisions an AWS EC2 instance running Ubuntu.
# Choose a language on the right hand side -- or try replacing it with your own!

data "aws_ami" "ubuntu" {
    most_recent = true

    filter {
        name   = "name"
        values = ["ubuntu/images/hvm-ssd/ubuntu-trusty-14.04-amd64-server-*"]
    }

    filter {
        name   = "virtualization-type"
        values = ["hvm"]
    }

    owners = ["099720109477"] # Canonical
}

resource "aws_instance" "web" {
    ami           = "\${data.aws_ami.ubuntu.id}"
    instance_type = "t2.micro"

    tags = {
        Name = "HelloWorld"
    }
}`
