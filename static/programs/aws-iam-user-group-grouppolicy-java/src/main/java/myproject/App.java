package myproject;

import com.pulumi.Pulumi;
import com.pulumi.aws.iam.User;
import com.pulumi.aws.iam.UserArgs;
import com.pulumi.aws.iam.Group;
import com.pulumi.aws.iam.GroupArgs;
import com.pulumi.aws.iam.GroupPolicy;
import com.pulumi.aws.iam.GroupPolicyArgs;
import com.pulumi.aws.iam.GroupMembership;
import com.pulumi.aws.iam.GroupMembershipArgs;
import static com.pulumi.codegen.internal.Serialization.*;
import com.pulumi.core.Output;
import java.util.List;

public class App {
    public static void main(String[] args) {
        Pulumi.run(ctx -> {
            
            var jane = new User("jane", UserArgs.builder().build());
            var mary = new User("mary", UserArgs.builder().build());

            // Create a single output from the two other outputs.
            var userIds = Output.all(jane.id(), mary.id()).applyValue(ids -> List.of(ids.get(0), ids.get(1)));
            
            // Define a group and assign a policy for it.
            var devs = new Group("devs", GroupArgs.builder()
                .path("/users/")
                .build());
            
            new GroupPolicy("my_developer_policy", GroupPolicyArgs.builder()
                .group(devs.name())
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
    
            new GroupMembership("dev-team", GroupMembershipArgs.builder()
                .group(devs.id())
                .users(userIds)
                .build());
        });
    }
}