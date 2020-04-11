---
title: "Unit Testing Infrastructure"
date: 2020-03-24
meta_desc: "Unit testing for infrastructure is now available using Node.js, Python, .NET, and Go"
meta_image: tdd.png
authors:
    - sophia-parafina
tags:
    - testing
    - test driven development
---

We’re pleased to announce that unit testing with Node.js, Python, .NET, and Go is supported in recent releases. You can test resources before deploying your infrastructure using familiar tools and test frameworks. Check your resource configuration and responses without the wait of deploying them and speed up infrastructure development and production deployments.

<!--more-->

Pulumi brings testing to Infrastructure as Code. Testing your infrastructure code will provide early bug notification, cleaner and more extensible code, and simplify refactoring. We implemented testing with these goals in mind.

- Run code without the engine
- Write tests using existing test tools and frameworks
- Mock any dependencies

Here are examples in Python and Go to get you started.

## Python

First we’ll set up an AWS EC2 instance as a web server to test.

```python
import pulumi
from pulumi_aws import ec2

group = ec2.SecurityGroup('web-secgrp', ingress=[
    { "protocol": "tcp", "from_port": 22, "to_port": 22, "cidr_blocks": ["0.0.0.0/0"] },
    { "protocol": "tcp", "from_port": 80, "to_port": 80, "cidr_blocks": ["0.0.0.0/0"] },
])

user_data = '#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &'

server = ec2.Instance('web-server-www;',
    instance_type="t2.micro",
    security_groups=[ group.name ], # reference the group object above
    user_data=user_data,            # start a simple web server
    ami="ami-c55673a0")             # AMI for us-east-2 (Ohio)

pulumi.export('group', group)
pulumi.export('server', server)
pulumi.export('publicIp', server.public_ip)
pulumi.export('publicHostName', server.public_dns)
```

Using Python’s unittest framework we can test if the test service conforms to a configuration that restricts an exposed port 22 and use of user_data and enforces the use of tags and membership in a security group.

```python
import unittest
import pulumi

# Create the mock.
class MyMocks(pulumi.runtime.Mocks):
    def call(self, token, args, provider):
        return {}

    def new_resource(self, type_, name, inputs, provider, id_):
        if type_ == 'aws:ec2/securityGroup:SecurityGroup':
            state = {
                'arn': 'arn:aws:ec2:us-west-2:123456789012:security-group/sg-12345678',
                'name': inputs['name'] if 'name' in inputs else name + '-sg',
            }
            return ['sg-12345678', dict(inputs, **state)]
        elif type_ == 'aws:ec2/instance:Instance':
            state = {
                'arn': 'arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0',
                'instanceState': 'running',
                'primaryNetworkInterfaceId': 'eni-12345678',
                'privateDns': 'ip-10-0-1-17.ec2.internal',
                'publicDns': 'ec2-203-0-113-12.compute-1.amazonaws.com',
                'publicIp': '203.0.113.12',
            }
            return ['i-1234567890abcdef0', dict(inputs, **state)]
        else:
            return ['', {}]

pulumi.runtime.set_mocks(MyMocks())

# Import the EC2 web server.
import infra

class InfraTests(unittest.TestCase):

    # Test if the service has tags and a name tag.
    @pulumi.runtime.test
    def test_server_tags(self):
        def check_tags(args):
            urn, tags = args
            self.assertIsNotNone(tags, f'server {urn} must have tags')
            self.assertIn('Name', tags, 'server {urn} must have a name tag')

        return pulumi.Output.all(infra.server.urn, infra.server.tags).apply(check_tags)

    # Test if the instance is configured with user_data.
    @pulumi.runtime.test
    def test_server_userdata(self):
        def check_user_data(args):
            urn, user_data = args
            self.assertFalse(user_data, f'illegal use of user_data on server {urn}')

        return pulumi.Output.all(infra.server.urn, infra.server.user_data).apply(check_user_data)

    # Test if service is a member of a security group.
    @pulumi.runtime.test
    def test_server_security_groups(self):
        def check_security_groups(args):
            urn, security_groups = args
            self.assertIsNotNone(security_groups, f'server {urn} does not specify security_groups')
            self.assertGreater(len(security_groups), 0, f'server {urn} does not specify security_groups')

        return pulumi.Output.all(infra.server.urn, infra.server.security_groups).apply(check_security_groups)

    # Test if port 22 for ssh is exposed.
    @pulumi.runtime.test
    def test_security_group_rules(self):
        def check_security_group_rules(args):
            urn, ingress = args
            ssh_open = any([rule['from_port'] == 22 and any([block == "0.0.0.0/0" for block in rule['cidr_blocks']]) for rule in ingress])
            self.assertFalse(ssh_open, f'security group {urn} exposes port 22 to the Internet (CIDR 0.0.0.0/0)')

        # Return the results of the unit tests.
        return pulumi.Output.all(infra.group.urn, infra.group.ingress).apply(check_security_group_rules)
```

## Go

This is the same example, but written in Go using the stretchr framework for unit tests.

```go
package main

import (
    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
)

type infrastructure struct {
    group  *ec2.SecurityGroup
    server *ec2.Instance
}

func createInfrastructure(ctx *pulumi.Context) (*infrastructure, error) {
    group, err := ec2.NewSecurityGroup(ctx, "web-secgrp", &ec2.SecurityGroupArgs{
        Ingress: ec2.SecurityGroupIngressArray{
            ec2.SecurityGroupIngressArgs{
                Protocol:   pulumi.String("tcp"),
                FromPort:   pulumi.Int(22),
                ToPort:     pulumi.Int(22),
                CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
            },
            ec2.SecurityGroupIngressArgs{
                Protocol:   pulumi.String("tcp"),
                FromPort:   pulumi.Int(80),
                ToPort:     pulumi.Int(80),
                CidrBlocks: pulumi.StringArray{pulumi.String("0.0.0.0/0")},
            },
        },
    })
    if err != nil {
        return nil, err
    }

    const userData = `#!/bin/bash echo "Hello, World!" > index.html nohup python -m SimpleHTTPServer 80 &`

    server, err := ec2.NewInstance(ctx, "web-server-www", &ec2.InstanceArgs{
        InstanceType:   pulumi.String("t2-micro"),
        SecurityGroups: pulumi.StringArray{group.ID()},
        Ami:            pulumi.String("ami-c55673a0"),
        UserData:       pulumi.String(userData),
    })
    if err != nil {
        return nil, err
    }

    return &infrastructure{
        group:  group,
        server: server,
    }, nil
}

func main() {
    pulumi.Run(func(ctx *pulumi.Context) error {
        infra, err := createInfrastructure(ctx)
        if err != nil {
            return err
        }

        ctx.Export("group", infra.group.ID())
        ctx.Export("server", infra.server.ID())
        ctx.Export("publicIp", infra.server.PublicIp)
        ctx.Export("publicHostName", infra.server.PublicDns)
        return nil
    })
}
```

We implement the same tests used in the Python example.

```go
package main

import (
    "fmt"
    "sync"
    "testing"

    "github.com/pulumi/pulumi-aws/sdk/go/aws/ec2"
    "github.com/pulumi/pulumi/pkg/resource"
    "github.com/pulumi/pulumi/sdk/go/pulumi"
    "github.com/stretchr/testify/assert"
)

type mocks int

// Create the mock.
func (mocks) NewResource(typeToken, name string, inputs resource.PropertyMap, provider, id string) (string, resource.PropertyMap, error) {
    switch typeToken {
    case "aws:ec2/securityGroup:SecurityGroup":
        if _, ok := inputs["name"]; !ok {
            inputs["name"] = resource.NewStringProperty(name + "-sg")
        }
        inputs["arn"] = resource.NewStringProperty("arn:aws:ec2:us-west-2:123456789012:security-group/sg-12345678")
        return "sg-12345678", inputs, nil
    case "aws:ec2/instance:Instance":
        inputs["arn"] = resource.NewStringProperty("arn:aws:ec2:us-west-2:123456789012:instance/i-1234567890abcdef0")
        inputs["instanceState"] = resource.NewStringProperty("running")
        inputs["primaryNetworkInterfaceId"] = resource.NewStringProperty("eni-12345678")
        inputs["privateDns"] = resource.NewStringProperty("ip-10-0-1-17.ec2.internal")
        inputs["publicDns"] = resource.NewStringProperty("ec2-203-0-113-12.compute-1.amazonaws.com")
        inputs["publicIp"] = resource.NewStringProperty("203.0.113.12")
        return "i-1234567890abcdef0", inputs, nil
    default:
        return "", inputs, fmt.Errorf("unexpected resource type %v", typeToken)
    }
}

func (mocks) Call(token string, args resource.PropertyMap, provider string) (resource.PropertyMap, error) {
    return args, fmt.Errorf("unexpected function call %v", token)
}

// Applying unit tests.
func TestInfrastructure(t *testing.T) {
    err := pulumi.RunErr(func(ctx *pulumi.Context) error {
        infra, err := createInfrastructure(ctx)
        assert.NoError(t, err)

        var wg sync.WaitGroup
        wg.Add(4)

             // Test if the service has tags and a name tag.
        pulumi.All(infra.server.URN(), infra.server.Tags).ApplyT(func(all []interface{}) error {
            urn := all[0].(pulumi.URN)
            tags := all[1].(map[string]interface{})

            assert.Containsf(t, tags, "name", "missing a name tag on server %v", urn)
            wg.Done()
            return nil
        })

             // Test if the instance is configured with user_data.
        pulumi.All(infra.server.URN(), infra.server.UserData).ApplyT(func(all []interface{}) error {
            urn := all[0].(pulumi.URN)
            userData := all[1].(*string)

            assert.Nilf(t, userData, "illegal use of userData on server %v", urn)
            wg.Done()
            return nil
        })

             // Test if service is a member of a security group.
        pulumi.All(infra.server.URN(), infra.server.SecurityGroups).ApplyT(func(all []interface{}) error {
            urn := all[0].(pulumi.URN)
            securityGroups := all[1].([]string)

            assert.Greaterf(t, len(securityGroups), 0, "illegal security group spec on server %v", urn)
            wg.Done()
            return nil
        })

             // Test if port 22 for ssh is exposed.
        pulumi.All(infra.group.URN(), infra.group.Ingress).ApplyT(func(all []interface{}) error {
            urn := all[0].(pulumi.URN)
            ingress := all[1].([]ec2.SecurityGroupIngress)

            for _, i := range ingress {
                openToInternet := false
                for _, b := range i.CidrBlocks {
                    if b == "0.0.0.0/0" {
                        openToInternet = true
                        break
                    }
                }

                assert.Falsef(t, i.FromPort == 22 && openToInternet, "illegal SSH port 22 open to the Internet (CIDR 0.0.0.0/0) on group %v", urn)
            }

            wg.Done()
            return nil
        })

        wg.Wait()
        return nil
    }, pulumi.WithMocks("project", "stack", mocks(0)))
    assert.NoError(t, err)
}
```

## Try it out today

We’ve released these features early so that you can try them out before the 2.0 release. To get you started, we've added [full working examples](https://github.com/pulumi/examples#testing) on Github. With the 2.0 release we’ll have more documentation, examples, and blog posts. In the meantime, we would appreciate feedback on our [Community Slack channel](https://pulumi-community.slack.com/).
