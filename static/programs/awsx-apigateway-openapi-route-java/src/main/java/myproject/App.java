package myproject;

import com.pulumi.Pulumi;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .data(jsonObject(
                            jsonProperty("x-amazon-apigateway-integration", jsonObject(
                                jsonProperty("httpMethod", "GET"),
                                jsonProperty("passthroughBehavior", "when_no_match"),
                                jsonProperty("type", "http_proxy"),
                                jsonProperty("uri", "https://httpbin.org/uuid")
                            ))
                        ))
                        .build(),
                })
                .build());

            ctx.export("url", api.url());
        });
    }
}
