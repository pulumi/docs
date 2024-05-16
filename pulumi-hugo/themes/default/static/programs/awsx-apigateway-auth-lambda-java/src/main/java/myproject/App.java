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
import com.pulumi.awsapigateway.inputs.AuthorizerArgs;
import com.pulumi.awsapigateway.inputs.RouteArgs;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

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

            var authorizer = new Function("authorizer", FunctionArgs.builder()
                .runtime("python3.9")
                .handler("handler.handler")
                .role(role.arn())
                .code(new com.pulumi.asset.FileArchive("./authorizer"))
                .build());

            var api = new RestAPI("api", RestAPIArgs.builder()
                .routes(new RouteArgs[]{
                    RouteArgs.builder()
                        .path("/")
                        .method(Method.GET)
                        .localPath("www")
                        .authorizers(new AuthorizerArgs[]{
                            AuthorizerArgs.builder()
                                .authType("custom")
                                .type("request")
                                .parameterName("Authorization")
                                .identitySource(List.of("method.request.header.Authorization"))
                                .handler(authorizer)
                                .build(),
                        })
                        .build(),
                })
                .build());

            ctx.export("url", api.url());
        });
    }
}
