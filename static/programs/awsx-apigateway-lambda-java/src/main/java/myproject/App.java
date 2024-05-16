package myproject;

import java.util.List;

import com.pulumi.Pulumi;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.iam.enums.ManagedPolicy;
import com.pulumi.awsapigateway.enums.Method;
import com.pulumi.aws.lambda.Function;
import com.pulumi.aws.lambda.FunctionArgs;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            // An execution role to use for the Lambda function.
            var role = new Role("role", RoleArgs.builder()
                .assumeRolePolicy(serializeJson(
                    jsonObject(
                        jsonProperty("Version", "2012-10-17"),
                        jsonProperty("Statement", jsonArray(jsonObject(
                            jsonProperty("Action", "sts:AssumeRole"),
                            jsonProperty("Effect", "Allow"),
                            jsonProperty("Sid", ""),
                            jsonProperty("Principal", jsonObject(
                                jsonProperty("Service", "lambda.amazonaws.com")
                            ))
                        )))
                    )))
                .managedPolicyArns(List.of(ManagedPolicy.AWSLambdaBasicExecutionRole.getValue()))
                .build());

            // An execution role to use for the Lambda function.
            var handler = new Function("handler", FunctionArgs.builder()
                .runtime("python3.9")
                .handler("handler.handler")
                .role(role.arn())
                .code(new com.pulumi.asset.FileArchive("./function"))
                .build());

            // An execution role to use for the Lambda function.
            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .eventHandler(handler)
                        .build(),
                })
                .build());

            // An execution role to use for the Lambda function.
            ctx.export("url", api.url());
        });
    }
}
