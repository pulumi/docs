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
                LocalPath = "www",
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
    };
});
