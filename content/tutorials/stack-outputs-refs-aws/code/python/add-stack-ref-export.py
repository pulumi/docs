import pulumi

stack_ref = pulumi.StackReference("my-org/my-first-program/dev")

# Add an export to output the value of the Lambda function name using the stack reference above
pulumi.export("firstProgramLambdaName", stack_ref.get_output("lambdaName"))