package main

import (
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/iam"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/lambda"
	"github.com/pulumi/pulumi-aws/sdk/v6/go/aws/sfn"
	"github.com/pulumi/pulumi/sdk/v3/go/pulumi"
)

func main() {
	pulumi.Run(func(ctx *pulumi.Context) error {

		lambdaRole, err := iam.NewRole(ctx, "lambda-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.JSONMarshal(map[string]interface{}{
				"Version": pulumi.ToOutput("2012-10-17"),
				"Statement": pulumi.ToOutput([]interface{}{
					pulumi.ToMapOutput(map[string]pulumi.Output{
						"Action": pulumi.ToOutput("sts:AssumeRole"),
						"Effect": pulumi.ToOutput("Allow"),
						"Principal": pulumi.ToMapOutput(map[string]pulumi.Output{
							"Service": pulumi.ToOutput("lambda.amazonaws.com"),
						}),
					}),
				}),
			}),
			ManagedPolicyArns: pulumi.StringArray{
				pulumi.String("arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"),
			},
		})
		if err != nil {
			return err
		}

		sfnRole, err := iam.NewRole(ctx, "sfn-role", &iam.RoleArgs{
			AssumeRolePolicy: pulumi.JSONMarshal(map[string]interface{}{
				"Version": pulumi.ToOutput("2012-10-17"),
				"Statement": pulumi.ToOutput([]interface{}{
					pulumi.ToMapOutput(map[string]pulumi.Output{
						"Action": pulumi.ToOutput("sts:AssumeRole"),
						"Effect": pulumi.ToOutput("Allow"),
						"Principal": pulumi.ToMapOutput(map[string]pulumi.Output{
							"Service": pulumi.ToOutput("states.amazonaws.com"),
						}),
					}),
				}),
			}),
			ManagedPolicyArns: pulumi.StringArray{
				pulumi.String("arn:aws:iam::aws:policy/AWSLambda_FullAccess"),
			},
		})
		if err != nil {
			return err
		}

		helloFunction, err := lambda.NewFunction(ctx, "hello-function", &lambda.FunctionArgs{
			Runtime: lambda.RuntimePython3d9,
			Handler: pulumi.String("handler.handler"),
			Role:    lambdaRole.Arn,
			Code:    pulumi.NewFileArchive("./function"),
		})
		if err != nil {
			return err
		}

		_, err = sfn.NewStateMachine(ctx, "stateMachine", &sfn.StateMachineArgs{
			RoleArn: sfnRole.Arn,
			Type:    pulumi.String("EXPRESS"),
			Definition: pulumi.JSONMarshal(map[string]interface{}{
				"Comment": pulumi.ToOutput("A Hello World example of the Amazon States Language using two AWS Lambda Functions"),
				"StartAt": pulumi.ToOutput("Hello"),
				"States": pulumi.ToMapOutput(map[string]pulumi.Output{
					"Hello": pulumi.ToMapOutput(map[string]pulumi.Output{
						"Type":     pulumi.ToOutput("Task"),
						"Resource": helloFunction.Arn,
						"End":      pulumi.ToOutput(true),
					}),
				}),
			}),
		})
		if err != nil {
			return err
		}

		return nil
	})
}
