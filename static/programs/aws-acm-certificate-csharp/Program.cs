using Pulumi;
using Pulumi.Aws.Acm;
using System.Collections.Generic;

return await Deployment.RunAsync(() =>
{
    var cert = new Certificate("cert", new CertificateArgs
    {
        DomainName = "example",
        ValidationMethod = "DNS",
    });
});
