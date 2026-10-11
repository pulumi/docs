using System.Collections.Generic;
using Pulumi;
using AwsApiGateway = Pulumi.AwsApiGateway;

return await Deployment.RunAsync(() =>
{
    var api = new AwsApiGateway.RestAPI("api", new()
    {
        Routes =
        {
            new AwsApiGateway.Inputs.RouteArgs
            {
                Path = "/",
                Target = new AwsApiGateway.Inputs.TargetArgs()
                {
                    Type = AwsApiGateway.IntegrationType.Http_proxy,
                    Uri = "https://www.example.com/",
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
    };
});
