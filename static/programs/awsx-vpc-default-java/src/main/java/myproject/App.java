package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.DefaultVpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Fetch the default VPC for the current AWS region.
            var vpc = new DefaultVpc("default-vpc");


            // Export a few properties to make them easy to use.
            ctx.export("vpcId", vpc.vpcId());
            ctx.export("privateSubnetIds", vpc.privateSubnetIds());
            ctx.export("publicSubnetIds", vpc.publicSubnetIds());
        });
    }
}
