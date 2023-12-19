package myproject;

import java.util.List;

import com.pulumi.Pulumi;
import com.pulumi.aws.cognito.UserPool;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.AuthorizerArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var userPool = new UserPool("user-pool");

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .localPath("www")
                        .authorizers(new AuthorizerArgs[]{
                            AuthorizerArgs.builder()
                                .parameterName("Authorization")
                                .identitySource(List.of("method.request.header.Authorization"))
                                .providerARNs(List.of(userPool.arn()))
                                .build(),
                        })
                        .build(),
                })
                .build());

            ctx.export("url", api.url());
        });
    }
}
