package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.lb.inputs.ListenerDefaultActionArgs;
import com.pulumi.aws.lb.inputs.ListenerDefaultActionRedirectArgs;
import com.pulumi.awsx.lb.ApplicationLoadBalancer;
import com.pulumi.awsx.lb.ApplicationLoadBalancerArgs;
import com.pulumi.awsx.lb.inputs.ListenerArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // Create a load balancer in the default VPC.
            var alb = new ApplicationLoadBalancer("lb", ApplicationLoadBalancerArgs.builder()
                .listeners(new ListenerArgs[] {

                    // Redirect HTTP traffic on port 8080 to port 8081.
                    ListenerArgs.builder()
                        .port(8080)
                        .protocol("HTTP")
                        .defaultActions(new ListenerDefaultActionArgs[] {
                            ListenerDefaultActionArgs.builder()
                                .type("redirect")
                                .redirect(ListenerDefaultActionRedirectArgs.builder()
                                    .port("8081")
                                    .protocol("HTTP")
                                    .statusCode("HTTP_301")
                                    .build())
                                .build(),
                        })
                        .build(),

                    // Accept HTTP traffic on port 8081.
                    ListenerArgs.builder()
                        .port(8081)
                        .protocol("HTTP")
                        .build(),
                })
                .build());

            // Export the resulting URL so that it's easy to access.
            ctx.export("endpoint", alb.loadBalancer().apply(loadBalancer -> loadBalancer.dnsName()));
        });
    }
}
