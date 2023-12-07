package myproject;

import java.util.List;

import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupEgressArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.aws.ec2.outputs.GetAmiResult;
import com.pulumi.awsx.ec2.Vpc;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var vpc = new Vpc("vpc");

            var securityGroup = new SecurityGroup("group", SecurityGroupArgs.builder()
                .vpcId(vpc.vpcId())
                .build()
            );

            var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
                .filters(List.of(GetAmiFilterArgs.builder()
                    .name("name")
                    .values(List.of("amzn2-ami-hvm-*"))
                    .build()))
                .owners(List.of("amazon"))
                .mostRecent(true)
                .build());

            var server = new Instance("web-server-www", InstanceArgs.builder()
                .ami(ami.applyValue(GetAmiResult::id))
                .instanceType("t2.micro")
                .vpcSecurityGroupIds(Output.all(securityGroup.id()))
                .subnetId(vpc.publicSubnetIds().applyValue(x -> x.get(0)))
                .build()
            );

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
