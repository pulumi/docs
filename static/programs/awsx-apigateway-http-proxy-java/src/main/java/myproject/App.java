package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsapigateway.enums.IntegrationType;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;
import com.pulumi.awsapigateway.inputs.TargetArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .target(TargetArgs.builder()
                            .type(IntegrationType.Http_proxy)
                            .uri("https://www.example.com/")
                            .build()
                        )
                        .build(),
                })
                .build());

            ctx.export("url", api.url());
        });
    }
}
