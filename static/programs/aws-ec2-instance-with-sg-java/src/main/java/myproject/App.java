package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;

import java.util.List;


public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {

        var group = new SecurityGroup("web-sg",
            SecurityGroupArgs.builder()
            .description("Enable HTTP access")
            .ingress(SecurityGroupIngressArgs.builder()
                .protocol("tcp")
                .fromPort(80)
                .toPort(80)
                .cidrBlocks("0.0.0.0/0")
                .build())
            .build());

        var server = new Instance("web-server",
            InstanceArgs.builder()
                .ami("ami-0319ef1a70c93d5c8")
                .instanceType("t2.micro")
                .vpcSecurityGroupIds(group.id().applyValue(List::of))
                .build());

        ctx.export("publicIp", server.publicIp());
        ctx.export("publicDns", server.publicDns());
    }
}
