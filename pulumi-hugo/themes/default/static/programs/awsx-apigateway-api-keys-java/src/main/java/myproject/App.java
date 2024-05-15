package myproject;

import java.util.List;

import com.pulumi.Pulumi;
import com.pulumi.aws.apigateway.ApiKey;
import com.pulumi.aws.apigateway.UsagePlan;
import com.pulumi.aws.apigateway.UsagePlanArgs;
import com.pulumi.aws.apigateway.UsagePlanKey;
import com.pulumi.aws.apigateway.UsagePlanKeyArgs;
import com.pulumi.aws.apigateway.inputs.UsagePlanApiStageArgs;
import com.pulumi.awsapigateway.enums.APIKeySource;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var api = new RestAPI("api", RestAPIArgs.builder()
                .apiKeySource(APIKeySource.HEADER)
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .localPath("data")
                        .index(("index.json"))
                        .contentType("application/json")
                        .apiKeyRequired(true)
                        .build(),
                })
                .build());

            var key = new ApiKey("key");

            var plan = new UsagePlan("plan", UsagePlanArgs.builder()
                .apiStages(List.of(UsagePlanApiStageArgs.builder()
                    .apiId(api.api().apply(a -> a.id()))
                    .stage(api.stage().apply(s -> s.stageName()))
                    .build()))
                .build());

            var planKey = new UsagePlanKey("plan-key", UsagePlanKeyArgs.builder()
                .keyId(key.id())
                .keyType("API_KEY")
                .usagePlanId(plan.id())
                .build());

            ctx.export("url", api.url());
            ctx.export("apiKey", key.value());
        });
    }
}
