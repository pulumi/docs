package myproject;

import com.pulumi.Context;
import com.pulumi.Pulumi;
import com.pulumi.aws.ec2.Instance;
import com.pulumi.aws.ec2.InstanceArgs;
import com.pulumi.aws.ec2.SecurityGroup;
import com.pulumi.aws.ec2.SecurityGroupArgs;
import com.pulumi.aws.ec2.inputs.SecurityGroupIngressArgs;

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

        var server = new Instance("web-server-www", InstanceArgs.builder()
            .instanceType("t2.micro")
            .securityGroups(group.name())  // reference the group object above
            .ami("ami-c55673a0")           // AMI for us-east-2 (Ohio)
            .userData(userData)            // start a simple web server
            .build());
    }
}
