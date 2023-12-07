package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.ec2.VpcArgs;
import com.pulumi.awsx.ec2.Vpc;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var vpc = new Vpc("vpc", VpcArgs.builder()
                .numberOfAvailabilityZones(4)
                .build());

            ctx.export("vpcId", vpc.vpcId());
        });
    }
}
