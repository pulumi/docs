package myproject;

import com.pulumi.Pulumi;
import com.pulumi.core.Output;
import com.pulumi.aws.s3.Bucket;
import com.pulumi.awsapigateway.RestAPI;
import com.pulumi.awsapigateway.RestAPIArgs;
import static com.pulumi.codegen.internal.Serialization.*;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {

            var api = new RestAPI("api", RestAPIArgs.builder()
                .swaggerString(serializeJson(jsonObject(
                    jsonProperty("swagger", "2.0"),
                    jsonProperty("info", jsonObject(
                        jsonProperty("title", "example"),
                        jsonProperty("version", "1.0")
                    )),
                    jsonProperty("paths", jsonObject(
                        jsonProperty("/", jsonObject(
                            jsonProperty("get", jsonObject(
                                jsonProperty("x-amazon-apigateway-integration", jsonObject(
                                    jsonProperty("httpMethod", "GET"),
                                    jsonProperty("passthroughBehavior", "when_no_match"),
                                    jsonProperty("type", "http_proxy"),
                                    jsonProperty("uri", "https://httpbin.org/uuid")
                                ))
                            ))
                        ))
                    )),
                    jsonProperty("x-amazon-apigateway-binary-media-types", jsonArray(
                        "*/*"
                    ))
                )))
                .build());

            ctx.export("url", api.url());
        });
    }
}
