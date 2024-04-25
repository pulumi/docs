using Pulumi;
using Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{
    var user = new User("webmaster", new UserArgs
    {
        Path = "/system/",
        Tags = new InputMap<string>
        {
            { "Name", "webmaster" }
        },
    });
    
    var userAccessKey = new AccessKey("webmasterKey", new AccessKeyArgs
    {
        User = user.Name,
    });
    
    var userPolicy = new UserPolicy("webmasterPolicy", new UserPolicyArgs
    {
        User = user.Id,
        Policy = JsonSerializer.Serialize(new Dictionary<string, object>
        {
            ["Version"] = "2012-10-17",
            ["Statement"] = new[]
            {
                new Dictionary<string, object?>
                {
                    ["Action"] = new[]
                    {
                        "ec2:Describe*",
                    },
                    ["Effect"] = "Allow",
                    ["Resource"] = "*",
                },
            },
        }),
    });
});
