using System.Collections.Generic;
using System.Linq;
using Pulumi;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() => 
{
    var imported_iam_role = new Aws.Iam.Role("imported-role", new()
    {
        AssumeRolePolicy = "{\"Statement\":[{\"Action\":\"sts:AssumeRole\",\"Effect\":\"Allow\",\"Principal\":{\"Service\":\"lambda.amazonaws.com\"}}],\"Version\":\"2012-10-17\"}",
        Description = "Allows Lambda functions to call AWS services on your behalf.",
        ManagedPolicyArns = new[]
        {
            "arn:aws:iam::aws:policy/service-role/AWSLambdaDynamoDBExecutionRole",
        },
        Name = "pulumi-tutorial-iam-role",
    }, new CustomResourceOptions
    {
        ImportId = "pulumi-tutorial-iam-role"
    });

});