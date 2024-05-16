package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.ec2.Vpc;
import com.pulumi.aws.ec2.VpcArgs;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.InternetGateway;
import com.pulumi.aws.ec2.InternetGatewayArgs;
import com.pulumi.aws.ec2.Subnet;
import com.pulumi.aws.ec2.SubnetArgs;
import com.pulumi.aws.ec2.RouteTable;
import com.pulumi.aws.ec2.RouteTableArgs;
import com.pulumi.aws.ec2.inputs.RouteTableRouteArgs;
import com.pulumi.aws.ec2.RouteTableAssociation;
import com.pulumi.aws.ec2.RouteTableAssociationArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.vpc.SecurityGroupIngressRule;
import com.pulumi.aws.vpc.SecurityGroupIngressRuleArgs;
import com.pulumi.aws.vpc.SecurityGroupEgressRule;
import com.pulumi.aws.vpc.SecurityGroupEgressRuleArgs;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            // Create a VPC.
            var vpc = new Vpc("vpc", VpcArgs.builder()
                .cidrBlock("10.0.0.0/16")
                .build());

            // Create an internet gateway.
            var gateway = new InternetGateway("gateway", InternetGatewayArgs.builder()
                .vpcId(vpc.id())
                .build());

            // Create a subnet that automatically assigns new instances a public IP address.
            var subnet = new Subnet("subnet", SubnetArgs.builder()
                .vpcId(vpc.id())
                .cidrBlock("10.0.1.0/24")
                .mapPublicIpOnLaunch(true)
                .build());

            // Create a route table.
            var routes = new RouteTable("routes", RouteTableArgs.builder()
                .vpcId(vpc.id())
                .routes(RouteTableRouteArgs.builder()
                    .cidrBlock("0.0.0.0/0")
                    .gatewayId(gateway.id())
                    .build())
                .build());

            // Associate the route table with the public subnet.
            var routeTableAssociation = new RouteTableAssociation("route-table-association", RouteTableAssociationArgs.builder()
                .subnetId(subnet.id())
                .routeTableId(routes.id())
                .build());

            // Create a security group allowing inbound access over port 80 and outbound access to anywhere.
            var securityGroup = new SecurityGroup("security-group", SecurityGroupArgs.builder()        
                .name("allow_public")
                .vpcId(vpc.id())
                .build());
    
            var allowPort80Ipv4 = new SecurityGroupIngressRule("allowPort80Ingress", SecurityGroupIngressRuleArgs.builder()        
                .securityGroupId(securityGroup.id())
                .cidrIpv4("0.0.0.0/0")
                .fromPort(80)
                .ipProtocol("tcp")
                .toPort(80)
                .build());

            var allowAllTrafficIpv4 = new SecurityGroupEgressRule("allowAllTrafficEgress", SecurityGroupEgressRuleArgs.builder()        
                .securityGroupId(securityGroup.id())
                .cidrIpv4("0.0.0.0/0")
                .ipProtocol("-1")
                .build());

            // Find the latest Amazon Linux 2 AMI.
            var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
                .owners("amazon")
                .mostRecent(true)
                .filters(GetAmiFilterArgs.builder()
                    .name("description")
                    .values("Amazon Linux 2 *")
                    .build())
                .build()).applyValue(getAmiResult -> getAmiResult.id());

            // Create and launch an Amazon Linux EC2 instance into the public subnet.
            var instance = new Instance("instance", InstanceArgs.builder()
                .ami(ami)
                .instanceType("t3.nano")
                .subnetId(subnet.id())
                .vpcSecurityGroupIds(Output.all(securityGroup.id()))
                .userData(
                        "#!/bin/bash\n" +
                        "sudo yum update -y\n" +
                        "sudo yum upgrade -y\n" +
                        "sudo amazon-linux-extras install nginx1 -y\n" +
                        "sudo systemctl enable nginx\n" +
                        "sudo systemctl start nginx;\n"
                )
                .build());

            // Export the instance's publicly accessible URL.
            ctx.export("instanceURL", Output.format("http://%s", instance.publicIp()));
        });
    }
}
