using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;

return await Deployment.RunAsync(() =>
{
    var pageHTML = "<h1>I love Pulumi!</h1>";

    var page = new StaticWebsite("my-static-website", new StaticWebsiteArgs {
        IndexContent = pageHTML,
    });

    return new Dictionary<string, object?> {
        ["websiteURL"] = Output.Format($"http://{page.Endpoint}"),
    };
});
