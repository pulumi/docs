using System.Collections.Generic;
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var jsonIAMPolicy = Output.Create(
        @"
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
    "
    );

    // Parse the Output<string> into a C# Dictionary.
    var policyWithNoStatements = Output
        .JsonDeserialize<Dictionary<string, object?>>(jsonIAMPolicy)
        .Apply(policy =>
        {
            // Empty the policy's Statements list.
            policy["Statement"] = Output.Create(new List<Dictionary<string, object?>> { });
            return policy;
        });

    // Export the modified policy.
    return new Dictionary<string, object?> { ["policy"] = policyWithNoStatements, };
});
