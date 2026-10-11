package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Allocate a new VPC with the default settings.
            var vpc = new Vpc("vpc");

            // Export a few properties to make them easy to use.
            ctx.export("vpcId", vpc.vpcId());
            ctx.export("privateSubnetIds", vpc.privateSubnetIds());
            ctx.export("publicSubnetIds", vpc.publicSubnetIds());
        });
    }
}
