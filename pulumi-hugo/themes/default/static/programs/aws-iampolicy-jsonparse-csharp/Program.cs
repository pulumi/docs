using Pulumi;
using Pulumi.Aws.S3;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var jsonIAMPolicy = Output.Create(@"
            {
                ""Version"": ""2012-10-17"",
                ""Statement"": [
                    {
                        ""Sid"": ""VisualEditor0"",
                        ""Effect"": ""Allow"",
                        ""Action"": [
                            ""s3:ListAllMyBuckets"",
                            ""s3:GetBucketLocation""
                        ],
                        ""Resource"": ""*""
                    },
                    {
                        ""Sid"": ""VisualEditor1"",
                        ""Effect"": ""Allow"",
                        ""Action"": [
                            ""s3:*""
                        ],
                        ""Resource"": ""arn:aws:s3:::my-bucket""
                    }
                ]
            }
        ");
    
    var policyWithNoStatements = Pulumi.Output.JsonDeserialize<IAMPolicy>(jsonIAMPolicy).Apply(policy =>
    {
        // delete the policy statements.
        policy.Statement = Pulumi.Output.Create(new List<StatementEntry> { });
        return policy;
    })

    // Export the name of the bucket
    return new Dictionary<string, object?>
    {
        ["policy"] = policyWithNoStatements
    };
});
