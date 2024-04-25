package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.iam.Role;
import com.pulumi.aws.iam.RoleArgs;
import com.pulumi.aws.iam.RolePolicyAttachment;
import com.pulumi.aws.iam.RolePolicyAttachmentArgs;
import static com.pulumi.codegen.internal.Serialization.*;
import com.pulumi.aws.iam.enums.ManagedPolicy;
import com.pulumi.core.Output;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var role = new Role("my-role", RoleArgs.builder()        
            .assumeRolePolicy(serializeJson(
                jsonObject(
                    jsonProperty("Version", "2012-10-17"),
                    jsonProperty("Statement", jsonArray(jsonObject(
                        jsonProperty("Action", "sts:AssumeRole"),
                        jsonProperty("Effect", "Allow"),
                        jsonProperty("Sid", ""),
                        jsonProperty("Principal", jsonObject(
                            jsonProperty("Service", "ec2.amazonaws.com")
                        ))
                    )))
                )))
            .build());

        new RolePolicyAttachment("my-rpa", RolePolicyAttachmentArgs.builder()        
            .role(role.name())
            .policyArn(Output.format(ManagedPolicy.ReadOnlyAccess.getValue()))
            .build());
    }
}