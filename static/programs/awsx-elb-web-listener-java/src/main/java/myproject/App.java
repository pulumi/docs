package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsx.lb.ApplicationLoadBalancer;
import com.pulumi.awsx.lb.ApplicationLoadBalancerArgs;
import com.pulumi.awsx.lb.inputs.ListenerArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Create a load balancer in the default VPC listening on port 80.
            var alb = new ApplicationLoadBalancer("lb", ApplicationLoadBalancerArgs.builder()
                .listener(ListenerArgs.builder()
                    .port(80)
                    .build())
                .build());

            // Export the resulting URL so that it's easy to access.
            ctx.export("endpoint", alb.loadBalancer().apply(loadBalancer -> loadBalancer.dnsName()));
        });
    }
}
