using Pulumi;
using Pulumi.Aws.Ec2;
using Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.IO;
using Pulumi.Aws.Ec2.Inputs;
using System.Threading.Tasks;
using System.Text.Json;
class MyStack: Stack
{
    public MyStack()
        {
            // IAM Role for EC2 instances
            var rolePolicy = new Dictionary < string,
                object >
                {
                    {
                        "Version",
                        "2012-10-17"
                    },
                    {
                        "Statement",
                        new []
                        {
                            new Dictionary < string, object >
                            {
                                {
                                    "Action",
                                    "sts:AssumeRole"
                                },
                                {
                                    "Effect",
                                    "Allow"
                                },
                                {
                                    "Principal",
                                    new Dictionary < string,
                                    string >
                                    {
                                        {
                                            "Service",
                                            "ec2.amazonaws.com"
                                        }
                                    }
                                }
                            }
                        }
                    }
                };
            var role = new Role("deepSeekRole", new RoleArgs
            {
                Name = "deepseek-role",
                    AssumeRolePolicy = JsonSerializer.Serialize(rolePolicy)
            });
            // Attach S3 read-only policy to the IAM Role
            var rolePolicyAttachment = new RolePolicyAttachment("deepSeekS3Policy", new RolePolicyAttachmentArgs
            {
                PolicyArn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess",
                    Role = role.Name
            });
            // Instance Profile containing the IAM Role
            var instanceProfile = new InstanceProfile("deepSeekProfile", new InstanceProfileArgs
            {
                Name = "deepseek-profile",
                    Role = role.Name
            });
            // Create a VPC
            var vpc = new Vpc("deepSeekVpc", new VpcArgs
            {
                CidrBlock = "10.0.0.0/16",
                    EnableDnsHostnames = true,
                    EnableDnsSupport = true
            });
            // Create a subnet
            var subnet = new Subnet("deepSeekSubnet", new SubnetArgs
            {
                VpcId = vpc.Id, CidrBlock = "10.0.48.0/20",
                    AvailabilityZone = "eu-central-1a", MapPublicIpOnLaunch = true
            });
            // Create an internet gateway
            var internetGateway = new InternetGateway("deepSeekInternetGateway", new InternetGatewayArgs
            {
                VpcId = vpc.Id
            });
            // Create a route table and route table association
            var routeTable = new RouteTable("deepSeekRouteTable", new RouteTableArgs
            {
                VpcId = vpc.Id,
                    Routes = {
                        new RouteTableRouteArgs
                        {
                            CidrBlock = "0.0.0.0/0",
                                GatewayId = internetGateway.Id
                        }
                    }
            });
            var routeTableAssociation = new RouteTableAssociation("deepSeekRouteTableAssociation", new RouteTableAssociationArgs
            {
                SubnetId = subnet.Id,
                    RouteTableId = routeTable.Id
            });
            // Create a security group
            var securityGroup = new SecurityGroup("deepSeekSecurityGroup", new SecurityGroupArgs
            {
                VpcId = vpc.Id,
                    Egress = {
                        new SecurityGroupEgressArgs
                        {
                            FromPort = 0, ToPort = 0, Protocol = "-1",
                                CidrBlocks = {
                                    "0.0.0.0/0"
                                }
                        }
                    },
                    Ingress = {
                        new SecurityGroupIngressArgs
                        {
                            FromPort = 22, ToPort = 22,
                                Protocol = "tcp",
                                CidrBlocks = {
                                    "0.0.0.0/0"
                                }
                        },
                        new SecurityGroupIngressArgs
                        {
                            FromPort = 3000, ToPort = 3000,
                                Protocol = "tcp",
                                CidrBlocks = {
                                    "0.0.0.0/0"
                                }
                        },
                        new SecurityGroupIngressArgs
                        {
                            FromPort = 11434, ToPort = 11434,
                                Protocol = "tcp",
                                CidrBlocks = {
                                    "0.0.0.0/0"
                                }
                        }
                    }
            });
            // Key pair for SSH access
            var publicKey = File.ReadAllText("deepseek.rsa");
            var keyPair = new KeyPair("deepSeekKey", new KeyPairArgs
            {
                PublicKey = publicKey
            });
            // Get the latest Amazon Linux 2 AMI
            var amazonLinux = GetAmi.Invoke(new()
            {
                MostRecent = true,
                    Filters = new []
                    {
                        new GetAmiFilterInputArgs
                        {
                            Name = "name",
                                Values = new []
                                {
                                    "amzn2-ami-hvm-*-x86_64-gp2",
                                },
                        },
                        new GetAmiFilterInputArgs
                        {
                            Name = "architecture",
                                Values = new []
                                {
                                    "x86_64",
                                },
                        },
                    },
                    Owners = new []
                    {
                        "137112412989",
                    },
            });
            // Create an EC2 instance
            var userData = File.ReadAllText("cloud-init.yaml");
            var instance = new Instance("deepSeekInstance", new InstanceArgs
            {
                Ami = amazonLinux.Apply(GetAmiResult => GetAmiResult.Id),
                    InstanceType = "g4dn.xlarge", KeyName = keyPair.KeyName,
                    RootBlockDevice = new InstanceRootBlockDeviceArgs
                    {
                        VolumeSize = 100,
                            VolumeType = "gp3"
                    },
                    SubnetId = subnet.Id, VpcSecurityGroupIds = {
                        securityGroup.Id
                    },
                    IamInstanceProfile = instanceProfile.Name, UserData = userData,
                    Tags = {
                        {
                            "Name",
                            "deepSeek-server"
                        }
                    }
            });
            this.AmiId = amazonLinux.Apply(GetAmiResult => GetAmiResult.Id);
            this.InstanceId = instance.Id;
            this.InstancePublicDns = instance.PublicIp;
        }
        [Output]
    public Output < string > AmiId
        {
            get;
            set;
        }
        [Output]
    public Output < string > InstanceId
        {
            get;
            set;
        }
        [Output]
    public Output < string > InstancePublicDns
    {
        get;
        set;
    }
}
class Program
{
    static Task < int > Main() => Deployment.RunAsync < MyStack > ();
}
