using System.Collections.Generic;
using Pulumi;
using ApiGateway = Pulumi.AwsApiGateway;
using Aws = Pulumi.Aws;

return await Deployment.RunAsync(() =>
{
    var hostedZoneName = "example.com";
    var domainName = $"myapp.{hostedZoneName}";

    var zone = Aws.Route53.GetZone.Invoke(new()
    {
        Name = hostedZoneName,
    });

    var usEast1 = new Aws.Provider("us-east-1", new()
    {
        Region = "us-east-1",
    });

    var certificate = new Aws.Acm.Certificate("certificate", new() {
        DomainName = domainName,
        ValidationMethod = "DNS",
    }, new CustomResourceOptions { Provider = usEast1 });

    var validationOption = certificate.DomainValidationOptions.GetAt(0);
    var validationRecord = new Aws.Route53.Record("certificate-validation", new()
    {
        Name = validationOption.Apply(option => option.ResourceRecordName!),
        Type = validationOption.Apply(option => option.ResourceRecordType!),
        Records = { validationOption.Apply(option => option.ResourceRecordValue!), },
        ZoneId = zone.Apply(zone => zone.ZoneId),
        Ttl = 60,
    });

    var validation = new Aws.Acm.CertificateValidation("certificate-validation", new()
    {
        CertificateArn = certificate.Arn,
        ValidationRecordFqdns = { validationRecord.Fqdn },
    },  new CustomResourceOptions { Provider = usEast1 });

    var api = new ApiGateway.RestAPI("api", new()
    {
        Routes =
        {
            new ApiGateway.Inputs.RouteArgs {
                Path = "/",
                LocalPath = "www",
            },
        },
    });

    var gatewayDomainName = new Aws.ApiGateway.DomainName("gateway-domain-name", new()
    {
        CertificateArn = certificate.Arn,
        Domain = domainName,
    }, new CustomResourceOptions { DependsOn = validation });

    var gatewayDNSRecord = new Aws.Route53.Record("gateway-dns-record", new()
    {
        ZoneId = zone.Apply(zone => zone.ZoneId),
        Type = "A",
        Name = domainName,
        Aliases =
        {
            new Aws.Route53.Inputs.RecordAliasArgs
            {
                Name = gatewayDomainName.CloudfrontDomainName,
                ZoneId = gatewayDomainName.CloudfrontZoneId,
                EvaluateTargetHealth = true,
            },
        },
    });

    var basePathMapping = new Aws.ApiGateway.BasePathMapping("gateway-path-mapping", new()
    {
        RestApi = api.Api.Apply(api => api.Id),
        StageName = api.Stage.Apply(stage => stage.StageName),
        DomainName = gatewayDomainName.Domain,
    });

    return new Dictionary<string, object?>
    {
        ["url"] = Output.Format($"https://{basePathMapping.DomainName}/"),
    };
});
