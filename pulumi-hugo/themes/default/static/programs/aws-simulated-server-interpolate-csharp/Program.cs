using System.Collections.Generic;
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var webServer = Output.Create(new
    {
        HostName = "www.mywebserver.com",
        Port = "8080",
    });

    // Format takes a FormattableString and expands outputs correctly:
    var url = Output.Format($"http://{webServer.HostName}:{webServer.Port}/");

    return new Dictionary<string, object?>
    {
        ["serverUrl"] = url,
    };
});