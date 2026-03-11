using System.Collections.Generic;
using System.Threading.Tasks;

using Pulumi;

return await Deployment.RunAsync(() =>
{
    var pageHTML = "<h1>I love Pulumi!</h1>";

    var page = new StaticPage("my-static-page", new StaticPageArgs {
        IndexContent = pageHTML,
    });

    return new Dictionary<string, object?> {
        ["websiteURL"] = Output.Format($"http://{page.Endpoint}"),
    };
});
