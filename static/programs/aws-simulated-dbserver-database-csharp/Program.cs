using System.Collections.Generic;
using Pulumi;

return await Deployment.RunAsync(() =>
{
    var sqlServer = Output.Create(new
    {
        Name = "myDbServer",
        IpAddress = "10.0.0.0/24",
    });

    var database = Output.Create(new
    {
        Name = "myExampleDatabase",
        IpAddress = "sql-db",
    });

    return new Dictionary<string, object?>
    {
        ["sqlServerName"] = sqlServer.Apply(server => server.Name),
        ["databaseName"] = database.Apply(db => db.Name),
    };
});