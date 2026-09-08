package myproject;

import java.util.List;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Ec2Functions;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.GetAmiArgs;
import com.pulumi.aws.ec2.inputs.GetAmiFilterArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;
import com.pulumi.aws.ec2.outputs.GetAmiResult;

public class App {
    public static void main(String[] args) {
        Pulumi.run(App::stack);
    }

    public static void stack(Context ctx) {
        var group = new SecurityGroup("web-secgrp", SecurityGroupArgs.builder()
            .ingress(
                SecurityGroupIngressArgs.builder()
                    .protocol("tcp").fromPort(22).toPort(22).cidrBlocks("0.0.0.0/0")
                    .build(),
                SecurityGroupIngressArgs.builder()
                    .protocol("tcp").fromPort(80).toPort(80).cidrBlocks("0.0.0.0/0")
                    .build())
            .build());

        var userData = "#!/bin/bash echo \"Hello, World!\" > index.html nohup python3 -m http.server 80 &";

        // Look up the latest Amazon Linux 2 AMI.
        var ami = Ec2Functions.getAmi(GetAmiArgs.builder()
            .owners("amazon")
            .mostRecent(true)
            .filters(GetAmiFilterArgs.builder()
                .name("name")
                .values("amzn2-ami-hvm-*-x86_64-gp2")
                .build())
            .build());

        var server = new Instance("web-server-www", InstanceArgs.builder()
            .instanceType("t2.micro")
            .securityGroups(group.name().applyValue(List::of))  // reference the group object above
            .ami(ami.applyValue(GetAmiResult::id))
            .userData(userData)            // start a simple web server
            .build());
    }
}
