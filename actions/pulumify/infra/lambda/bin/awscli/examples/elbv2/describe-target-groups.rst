**To describe a target group**

This example describes the specified target group.

Command::

  aws elbv2 describe-target-groups --target-group-arns arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067

Output::

  {
    "TargetGroups": [
        {
            "TargetGroupName": "my-targets"
            "Protocol": "HTTP",
            "Port": 80,
            "VpcId": "vpc-3ac0fb5f",
            "TargetType": "instance",
            "HealthyThresholdCount": 5,
            "Matcher": {
                "HttpCode": "200"
            },
            "UnhealthyThresholdCount": 2,
            "HealthCheckPath": "/",
            "HealthCheckProtocol": "HTTP",
            "HealthCheckPort": "traffic-port",
            "HealthCheckIntervalSeconds": 30,
            "HealthCheckTimeoutSeconds": 5,
            "TargetGroupArn": "arn:aws:elasticloadbalancing:us-west-2:123456789012:targetgroup/my-targets/73e2d6bc24d8a067",
            "LoadBalancerArns": [
                "arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188"
            ]
        }
    ]
  }

**To describe all target groups for a load balancer**

This example describes all target groups for the specified load balancer.

Command::

  aws elbv2 describe-target-groups --load-balancer-arn arn:aws:elasticloadbalancing:us-west-2:123456789012:loadbalancer/app/my-load-balancer/50dc6c495c0c9188

**To describe all target groups**

This example describes all of your target groups.

Command::

  aws elbv2 describe-target-groups 
