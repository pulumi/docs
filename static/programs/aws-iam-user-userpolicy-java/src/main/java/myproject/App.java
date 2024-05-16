package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.iam.User;
import com.pulumi.aws.iam.UserArgs;
import com.pulumi.aws.iam.UserPolicy;
import com.pulumi.aws.iam.UserPolicyArgs;
import com.pulumi.aws.iam.AccessKey;
import com.pulumi.aws.iam.AccessKeyArgs;
import static com.pulumi.codegen.internal.Serialization.*;
import java.util.Map;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            var user = new User("webmaster", UserArgs.builder()
                .path("/system/")
                .tags(Map.of("Name", "webmaster"))
                .build());

            new AccessKey("webmasterKey", AccessKeyArgs.builder()
                .user(user.name())
                .build());

            new UserPolicy("webmasterPolicy", UserPolicyArgs.builder()
                .user(user.id())
                .policy(serializeJson(
                    jsonObject(
                        jsonProperty("Version", "2012-10-17"),
                        jsonProperty("Statement", jsonArray(jsonObject(
                            jsonProperty("Action", jsonArray("ec2:Describe*")),
                            jsonProperty("Effect", "Allow"),
                            jsonProperty("Resource", "*")
                        )))
                    )))
                .build());
        });
    }
}
