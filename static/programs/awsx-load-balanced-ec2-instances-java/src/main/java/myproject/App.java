package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupEgressArgs;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.outputs.GetAmiResult;
import com.pulumi.awsx.ec2.DefaultVpc;
import com.pulumi.awsx.lb.ApplicationLoadBalancer;
import com.pulumi.awsx.lb.ApplicationLoadBalancerArgs;
import com.pulumi.awsx.lb.TargetGroupAttachment;
import com.pulumi.awsx.lb.TargetGroupAttachmentArgs;
import com.pulumi.awsx.lb.inputs.ListenerArgs;
import com.pulumi.resources.CustomResourceOptions;
import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Get the default VPC for the current region.
            var vpc = new DefaultVpc("default-vpc");

            // Create a security group to allow traffic to and from the virtual machine.
            var securityGroup = new SecurityGroup("web-sg", SecurityGroupArgs.builder()
                .vpcId(vpc.vpcId())
                .ingress(SecurityGroupIngressArgs.builder()
                    .protocol("tcp")
                    .fromPort(80)
                    .toPort(80)
                    .cidrBlocks(List.of("0.0.0.0/0"))
                    .build())
                .egress(SecurityGroupEgressArgs.builder()
                    .protocol("-1")
                    .fromPort(0)
                    .toPort(0)
                    .cidrBlocks(List.of("0.0.0.0/0"))
                    .build())
                .build());

            // Create an ALB in the default VPC listening on port 80.
            var alb = new ApplicationLoadBalancer("web-traffic", ApplicationLoadBalancerArgs.builder()
                .listener(ListenerArgs.builder()
                    .port(80)
                    .build())
                .securityGroups(securityGroup.id().applyValue(id -> List.of(id)))
                .build());

            // Get the latest Amazon Linux 2 AMI.
            var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
                .filters(List.of(GetAmiFilterArgs.builder()
                    .name("name")
                    .values(List.of("amzn2-ami-hvm-*"))
                    .build()))
                .owners(List.of("amazon"))
                .mostRecent(true)
                .build());

            // In each VPC subnet, create an EC2 instance and attach it to the ALB.
            vpc.publicSubnetIds().applyValue(subnetIds -> {
                for(int i = 0; i < subnetIds.size(); i++){
                    var subnetId = subnetIds.get(i);

                    var vm = new Instance(String.format("web-%s", i), InstanceArgs.builder()
                        .ami(ami.applyValue(GetAmiResult::id))
                        .instanceType("t2.micro")
                        .subnetId(subnetId)
                        .vpcSecurityGroupIds(alb.loadBalancer().apply(lb -> lb.securityGroups()))
                        .userData("#!/bin/bash\n"
                            + String.format("echo \"Hello World, from Server %s!\" > index.html\n", i + 1)
                            + "nohup python -m SimpleHTTPServer 80 &")
                        .build(),
                        CustomResourceOptions.builder()
                            .dependsOn(List.of(securityGroup))
                            .build());

                    new TargetGroupAttachment(String.format("attachment-%s", i), TargetGroupAttachmentArgs.builder()
                        .targetGroup(alb.defaultTargetGroup())
                        .instance(vm)
                        .build());
                }

                return subnetIds;
            });

            // Export the resulting URL so that it's easy to access.
            ctx.export("endpoint", alb.loadBalancer().apply(loadBalancer -> loadBalancer.dnsName()));
        });
    }
}
