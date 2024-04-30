package myproject;

import java.util.Arrays;
import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.enums.SubnetType;
import com.pulumi.awsx.ec2.inputs.SubnetSpecArgs;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var vpc = new Vpc("vpc", VpcArgs.builder()
                .subnetSpecs(new SubnetSpecArgs[]{
                    SubnetSpecArgs.builder()
                        .type(SubnetType.Public)
                        .cidrMask(22)
                        .build(),
                    SubnetSpecArgs.builder()
                        .type(SubnetType.Private)
                        .cidrMask(20)
                        .build()
                    })
                .build());

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
