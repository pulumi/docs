using Pulumi;
using Pulumi.Aws.Acm;
using Pulumi.Aws.Route53;

return await Deployment.RunAsync(() =>
{
    var zone = new Zone("zone", new ZoneArgs
    {
        Name = "example.com",
    });

    var cert = new Certificate("cert", new CertificateArgs
    {
        DomainName = "example.com",
        ValidationMethod = "DNS",
    });

    // Using apply to access nested output values
    var certValidationApply = new Record("certValidationApply", new RecordArgs
    {
        Name = cert.DomainValidationOptions.Apply(opts => opts[0].ResourceRecordName!),
        Type = cert.DomainValidationOptions.Apply(opts => opts[0].ResourceRecordType!),
        ZoneId = zone.ZoneId,
        Ttl = 60,
        Records = { cert.DomainValidationOptions.Apply(opts => opts[0].ResourceRecordValue!) },
    });

    // Using lifting to access nested output values
    var certValidationLifting = new Record("certValidationLifting", new RecordArgs
    {
        Name = cert.DomainValidationOptions.GetAt(0).Apply(opt => opt.ResourceRecordName!),
        Type = cert.DomainValidationOptions.GetAt(0).Apply(opt => opt.ResourceRecordType!),
        ZoneId = zone.ZoneId,
        Ttl = 60,
        Records = { cert.DomainValidationOptions.GetAt(0).Apply(opt => opt.ResourceRecordValue!) },
    });
});
