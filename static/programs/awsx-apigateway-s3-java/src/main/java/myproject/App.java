package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .localPath("www")
                        .build(),
                })
                .build());

            ctx.export("url", api.url());
        });
    }
}
