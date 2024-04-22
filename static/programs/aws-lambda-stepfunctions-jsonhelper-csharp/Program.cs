using Pulumi;
using Pulumi.Aws.Iam;
using Pulumi.Aws.Lambda;
using Pulumi.AwsNative.StepFunctions;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{

    var lambdaAssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        ["Version"] = "2012-10-17",
        ["Statement"] = new[]
        {
            new {
                Action = "sts:AssumeRole",
                Effect = "Allow",
                Principal = new {
                    Service = "lambda.amazonaws.com"
                }
            }
        }
    });

    var lambdaRole = new Role("lambda-role", new RoleArgs
    {
        AssumeRolePolicy = lambdaAssumeRolePolicy,
        ManagedPolicyArns = { "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole" }
    });

    var sfnAssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
    {
        ["Version"] = "2012-10-17",
        ["Statement"] = new[]
        {
            new {
                Action = "sts:AssumeRole",
                Effect = "Allow",
                Principal = new {
                    Service = "states.amazonaws.com"
                }
            }
        }
    });

    var sfnRole = new Role("sfn-role", new RoleArgs
    {
        AssumeRolePolicy = sfnAssumeRolePolicy,
        ManagedPolicyArns = { "arn:aws:iam::aws:policy/AWSLambda_FullAccess" }
    });

    var helloFunction = new Function("hello-function", new FunctionArgs
    {
        Runtime = "python3.9",
        Handler = "handler.handler",
        Role = lambdaRole.Arn,
        Code = new FileArchive("./function")
    });

    var stateMachine = Pulumi.Output.JsonSerialize(Output.Create(new { // converts JSON into string
            Comment = "A Hello World example of the Amazon States Language using two AWS Lambda Functions",
            StartAt = "Hello",
            States = new Dictionary<string, object?>{
            ["Hello"] = new {
                Type = "Task",
                Resource = helloFunction.Arn, // unwraps Pulumi resource Output
                End = true,
            },
        },
    }));
});
