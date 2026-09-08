package myproject;

import java.util.Map;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.outputs.GetAmiResult;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        // Look up the most recent Amazon Linux 2 AMI.
        var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
            .owners("amazon")
            .mostRecent(true)
            .filters(GetAmiFilterArgs.builder()
                .name("name")
                .values("amzn2-ami-hvm-*-x86_64-gp2")
                .build())
            .build());

        var server = new Instance("web-server", InstanceArgs.builder()
            .ami(ami.applyValue(GetAmiResult::id))
            .instanceType("t3.micro")
            .tags(Map.of("Name", "web-server"))
            .build());
    }
}
