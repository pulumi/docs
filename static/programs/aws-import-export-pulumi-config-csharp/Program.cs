using Pulumi;
using System.Threading.Tasks;
using System.Collections.Generic;

class Program
{
    static async Task<int> Main(string[] args)
    {
        return await Deployment.RunAsync(() =>
        {
            // Import the configuration values
            var config = new Config();

            // Retrieve the value of "myEnvironment" and "myPassword"
            var environment = config.Get("myEnvironment");
            var password = config.GetSecret("myPassword");

            // Return a dictionary of outputs
            return new Dictionary<string, object?>
            {
                ["Environment"] = environment,
                ["Password"] = password
            };
        });
    }
}
