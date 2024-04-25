using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using AwsApiGateway = Pulumi.AwsApiGateway;

return await Deployment.RunAsync(() =>
{
    var userPool = new Aws.Cognito.UserPool("user-pool");

    var api = new AwsApiGateway.RestAPI(
        "api",
        new()
        {
            Routes =
            {
                new AwsApiGateway.Inputs.RouteArgs
                {
                    Path = "/",
                    Method = AwsApiGateway.Method.GET,
                    LocalPath = "www",
                    Authorizers =
                    {
                        new AwsApiGateway.Inputs.AuthorizerArgs
                        {
                            ParameterName = "Authorization",
                            IdentitySource = { "method.request.header.Authorization" },
                            ProviderARNs = { userPool.Arn },
                        },
                    },
                },
            },
        }
    );

    return new Dictionary<string, object?> { ["url"] = api.Url };
});
