using Pulumi;
using Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{
    var role = new Role("my-role", new RoleArgs
    {
        AssumeRolePolicy = JsonSerializer.Serialize(new Dictionary<string, object?>
        {
            ["Version"] = "2012-10-17",
            ["Statement"] = new[]
            {
                new Dictionary<string, object?>
                {
                    ["Action"] = "sts:AssumeRole",
                    ["Effect"] = "Allow",
                    ["Sid"] = "",
                    ["Principal"] = new Dictionary<string, object?>
                    {
                        ["Service"] = "ec2.amazonaws.com",
                    },
                },
            },
        }),
    });
    
    var profile = new InstanceProfile("instance-profile", new()
    { 
        Role = role.Name 
        
    });
});
