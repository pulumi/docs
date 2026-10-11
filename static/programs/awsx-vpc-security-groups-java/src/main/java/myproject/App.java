package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupEgressArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var vpc = new Vpc("vpc");

            var securityGroup = new SecurityGroup("group", SecurityGroupArgs.builder()
                .vpcId(vpc.vpcId())
                .ingress(SecurityGroupIngressArgs.builder()
                    .fromPort(22)
                    .toPort(22)
                    .protocol("tcp")
                    .cidrBlocks("203.0.113.25/32")
                    .build())
                .ingress(SecurityGroupIngressArgs.builder()
                    .fromPort(443)
                    .toPort(443)
                    .protocol("tcp")
                    .cidrBlocks("0.0.0.0/0")
                    .build())
                .egress(SecurityGroupEgressArgs.builder()
                    .fromPort(0)
                    .toPort(0)
                    .protocol("-1")
                    .cidrBlocks("0.0.0.0/0")
                    .build())
                .build()
            );

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
