using System.Collections.Generic;
using Pulumi;
using Pulumi.AwsApiGateway.Inputs;
using AwsApiGateway = Pulumi.AwsApiGateway;

return await Deployment.RunAsync(() =>
{
    var api = new AwsApiGateway.RestAPI("api", new()
    {
        RequestValidator = AwsApiGateway.RequestValidator.PARAMS_ONLY,

        Routes = {
            new RouteArgs()
            {
                Path = "/search",
                Method = AwsApiGateway.Method.GET,
                Target = new TargetArgs()
                {
                    Type = AwsApiGateway.IntegrationType.Http_proxy,
                    Uri = "https://www.example.com/",
                },
                RequestValidator = AwsApiGateway.RequestValidator.ALL,
                RequiredParameters = {
                    new RequiredParameterArgs() {
                        Name = "q",
                        In = "query",
                    },
                },
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
    };
});
