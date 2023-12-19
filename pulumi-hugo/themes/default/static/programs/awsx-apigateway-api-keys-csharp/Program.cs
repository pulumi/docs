using System.Collections.Generic;
using Pulumi;
using Aws = Pulumi.Aws;
using AwsApiGateway = Pulumi.AwsApiGateway;
using Pulumi.AwsApiGateway.Inputs;

return await Deployment.RunAsync(() =>
{
    var api = new AwsApiGateway.RestAPI("api", new()
    {
        ApiKeySource = AwsApiGateway.APIKeySource.HEADER,
        Routes =
        {
            new RouteArgs()
            {
                Path = "/",
                LocalPath = "data",
                Index = "index.json",
                ContentType = "application/json",
                ApiKeyRequired = true,
            },
        },
    });

    var key = new Aws.ApiGateway.ApiKey("key");

    var plan = new Aws.ApiGateway.UsagePlan("plan", new()
    {
        ApiStages = {
            new Aws.ApiGateway.Inputs.UsagePlanApiStageArgs()
            {
                ApiId = api.Api.Apply(api => api.Id),
                Stage = api.Stage.Apply(stage => stage.StageName),
            },
        },
    });

    var planKey = new Aws.ApiGateway.UsagePlanKey("plan-key", new()
    {
        KeyId = key.Id,
        KeyType = "API_KEY",
        UsagePlanId = plan.Id,
    });

    return new Dictionary<string, object?>
    {
        ["url"] = api.Url,
        ["apiKey"] = key.Value,
    };
});
