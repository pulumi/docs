package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.enums.NatGatewayStrategy;
import com.pulumi.awsx.ec2.inputs.NatGatewayConfigurationArgs;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var vpc = new Vpc("vpc", VpcArgs.builder()
                .natGateways(
                    NatGatewayConfigurationArgs.builder()
                        .strategy(NatGatewayStrategy.Single)
                        .build()
                )
                .build());

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
