using Pulumi;
using Pulumi.Gcp.ServiceAccount;

return await Deployment.RunAsync(() =>
{
    var gcpConfig = new Config("gcp");
    var projectId = gcpConfig.Require("project");
    var serviceAcctEmailSuffix = $"@{projectId}.iam.gserviceaccount.com";
    var serviceAcctDisplayName = "pulumi-tutorial-service-account"; // REPLACE
    var serviceAcctEmailPrefix = "pulumi-tutorial-service-accoun"; // REPLACE

    var importedTutorialServiceAccount = new Account("imported-tutorial-service-account", new AccountArgs
    {
        AccountId = serviceAcctEmailPrefix,
        DisplayName = serviceAcctDisplayName,
        Project = projectId
    }, new CustomResourceOptions
    {
        ImportId = $"{serviceAcctEmailPrefix}{serviceAcctEmailSuffix}"
    });
});
