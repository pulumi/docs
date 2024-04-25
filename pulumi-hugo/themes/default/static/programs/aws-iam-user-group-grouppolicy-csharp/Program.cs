using Pulumi;
using Pulumi.Aws.Iam;
using System.Collections.Generic;
using System.Text.Json;

return await Deployment.RunAsync(() =>
{
    // Create our users.
    var jane = new User("jane", new UserArgs());
    var mary = new User("mary", new UserArgs());

    // Define a group and assign a policy for it.
    var devs = new Group("devs", new GroupArgs
    {
        Path = "/users/",
    });

    var myDeveloperPolicy = new GroupPolicy("my_developer_policy", new GroupPolicyArgs
    {
        Group = devs.Id,
        Policy = JsonSerializer.Serialize(new
        {
            Version = "2012-10-17",
            Statement = new[]
            {
                new
                {
                    Action = new[] { "ec2:Describe*" },
                    Effect = "Allow",
                    Resource = "*"
                }
            }
        }),
    });

    // Finally, add the users as members to this group.
    var devTeam = new GroupMembership("dev-team", new GroupMembershipArgs
    {
        Group = devs.Id,
        Users = { jane.Id, mary.Id }
    });
});
