using System.Collections.Generic;
using System.Text.Json;
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
                Method = AwsApiGateway.Method.GET,
                Data = JsonSerializer.Deserialize<object>(JsonSerializer.Serialize(new Dictionary<string, object>() {
                    ["x-amazon-apigateway-integration"] = new {
                        httpMethod = "GET",
                        passthroughBehavior = "when_no_match",
                        type = "http_proxy",
                        uri = "https://httpbin.org/uuid",
                    },
                })),
            },
        },
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
    };
});
