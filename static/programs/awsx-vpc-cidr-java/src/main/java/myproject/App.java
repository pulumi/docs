package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Allocate a new VPC with a custom CIDR block.
            var vpc = new Vpc("vpc", VpcArgs.builder()
                .cidrBlock("172.16.8.0/24")
                .build());

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
