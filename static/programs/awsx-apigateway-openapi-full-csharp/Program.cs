using System;
using System.Collections.Generic;
using System.Text.Json;
using Pulumi;
using AwsApiGateway = Pulumi.AwsApiGateway;

return await Deployment.RunAsync(() =>
{
    var api = new AwsApiGateway.RestAPI("api", new()
    {
        SwaggerString = JsonSerializer.Serialize(new Dictionary<string, object>() {
            ["swagger"] = "2.0",
            ["info"] = new {
                title = "example",
                version = "1.0",
            },
            ["paths"] = new Dictionary<string, object>() {
                ["/"] = new {
                    get = new Dictionary<string, object>() {
                        ["x-amazon-apigateway-integration"] = new {
                            httpMethod = "GET",
                            passthroughBehavior = "when_no_match",
                            type = "http_proxy",
                            uri = "https://httpbin.org/uuid",
                        },
                    },
                },
            },
            ["x-amazon-apigateway-binary-media-types"] = new[] {
                "*/*"
            },
        }),
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
    };
});
