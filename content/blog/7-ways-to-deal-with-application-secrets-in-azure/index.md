---
title: "7 Ways to Deal with Application Secrets in Azure"
authors: ["mikhail-shilkov"]
tags: ["Azure", "Security"]
date: "2019-07-26"
meta_desc: In this post, we will look at 7 ways to deal with application secrects in Azure.
meta_image: "feature.jpg"
---

# Duplicate Heading

Every non-trivial application relies on configuration values that may depend on the current execution environment. Some of these values contain sensitive information that shouldn't be shared publicly. In general, the fewer parties that have access to those secret values, the safer the application will be&mdash;in fact, in an ideal world, no one would be granted direct access to those secrets.
<!--more-->

Examples of secret configuration values include:

- A connection string to a message bus or a database
- A SAS Token to an Azure Storage account
- An access key for a third-party service

There's no one universal way to manage secrets, as a lot depends on the context in which they are used. In this article, I go through seven ways to use secret values in a .NET Core application running in Azure. I start with naively hard-coded strings and build up from there to more secure options.

While the concepts are universally applicable, my code samples focus on a .NET application running in **Azure App Service** and configured with Pulumi.

## 1. Hard-coded Secrets

Whenever you want to try a new API requiring a secret access token, it's natural to copy-paste that secret into your code and run it&mdash;simply to make sure that the setup works.

For example, you are testing integration with a payment service:

``` cs
var apiKey = "payment-service-key";
var paymentService = new PaymentService(apiKey);
```

or you want to start sending messages to an **Azure Storage Queue**:

``` cs
var connectionString = "DefaultEndpointsProtocol=https;AccountName=account-name;AccountKey=account-key";
var storageAccount = CloudStorageAccount.Parse(connectionString);
var queueClient = storageAccount.CreateCloudQueueClient();
```

Both snippets are fine for a Hello-World application with a lifespan of two hours. However, I would strongly discourage doing so in any code that can potentially be checked into a source control system, even for a 10-minute experiment. Don't copy-paste secrets into files which are part of a git repository. One accidental `git commit & git push`&mdash;and the secrets are compromised.

Avoid the "Secrets as Code" practice: there are bots scanning your GitHub repository for those.

## 2. Configuration Files

Traditionally, putting secrets in a configuration file is considered more secure. For classic .NET applications, this would be an `app.config` or a `web.config` file. The idea is that the values on a developer machine are different from the values in the production environment. Non-sensitive development settings are kept on disk and maybe in source control, while the real secrets are only injected by a deployment script or a CI/CD system, so they are not exposed publicly.

In the .NET Core world, a configuration is usually stored in an `appsettings.json` file:

``` json
{
   "MyConfig": {
       "PaymentApiKey": "payment-service-key",
       "StorageConnectionString": "DefaultEndpointsProtocol=https;AccountName=account-name;AccountKey=account-key"
  }
}
```

which is then mapped to a plain C# object in code:

``` cs
public class MyConfig
{
   public string PaymentApiKey { get; set; }
   public string StorageConnectionString { get; set; }
}
```

With some configuration not shown here, the properties are filled at startup time and can be used in the code as a plain object:

``` cs
var apiKey = config.PaymentApiKey;
var paymentService = new PaymentService(apiKey);
// ...

var connectionString = config.StorageConnectionString;
var storageAccount = CloudStorageAccount.Parse(connectionString);
var queueClient = storageAccount.CreateCloudQueueClient();
```

In my experience, such setup still poses substantial risks. `appsettings.production.json` may still be accidentally checked into the source control. Developers tend to use real cloud resources for their local and test environments, which do contain sensitive information that can be exploited when leaked.

On top of that, it doesn't feel right to mix configuration&mdash;how many threads to run, or how big the message batches should be&mdash;with secret connection strings and API keys in the same file. These are separate kinds of configuration, and they warrant different workflows.

## 3. Environment Variables and Application Settings

One alternative approach is to read the secret values from environment variables. .NET Core configuration system can parse environment variables instead of, or in addition to the settings files. Likewise, one could read such values with a one-liner in C#:

``` cs
var apiKey = Environment.GetEnvironmentVariable("PAYMENT_API_KEY");
// ...

var connectionString = Environment.GetEnvironmentVariable("STORAGE_CONNECTION_STRING");
// ...
```

Your CI/CD system should inject those values as part of the deployment pipeline.

The App Service gives you the ability to set environment variables via **Application Settings**. Here is a snippet of a Pulumi program that passes both secret values to `appSettings`:

``` ts
const cfg = new pulumi.Config();
const paymentApiKey = cfg.requireSecret("paymentApiKey");

const storageAccount = new azure.storage.Account("storage", {
   resourceGroupName: resourceGroup.name,
   accountReplicationType: "LRS",
   accountTier: "Standard",
});

const app = new azure.appservice.AppService("app", {
   resourceGroupName: resourceGroup.name,
   appServicePlanId: appServicePlan.id,
   appSettings: {
       "PAYMENT_API_KEY": paymentApiKey,
       "STORAGE_CONNECTION_STRING": storageAccount.primaryConnectionString,
   },
});
```

The Storage connection string is produced by the Pulumi program directly, so it doesn't have to be placed anywhere outside the program itself.

The payment service key is provided by a third party, so its encrypted value is stored in Pulumi configuration. Read [Managing Secrets with Pulumi](https://www.pulumi.com/blog/managing-secrets-with-pulumi/) to learn about security options available for secrets in Pulumi config.

## 4. Azure Key Vault

In the previous example, both secrets end up in Application Settings. Every person with sufficient permissions may go to the App Service and see them in clear text. While this can be restricted, it's a good idea to grant full read access to the application developers and operators of the App Service to give them the full picture when troubleshooting issues.

In some cases, compliance to a certain standard may *require* the use of a certified key management service offering enhanced security for sensitive secrets.

Azure has a dedicated service for storing secrets, **Azure Key Vault**. You can create and populate a Key Vault with all the secrets from the same Pulumi program:

``` ts
const vault = new azure.keyvault.KeyVault("vault", {
   resourceGroupName: resourceGroup.name,
   sku: {
       name: "standard",
   },
   tenantId: tenantId,
   accessPolicies: [{
       tenantId,
       // The current principal has to be granted permissions to Key Vault so that it can actually add and then remove
       // secrets to/from the Key Vault. Otherwise, 'pulumi up' and 'pulumi destroy' operations will fail.
       objectId: currentPrincipal,
       secretPermissions: ["delete", "get", "list", "set"],
   }],
});

const secret = new azure.keyvault.Secret("paymentApiKey", {
   keyVaultId: vault.id,
   value: paymentApiKey,
});
```

Additionally, one or many **Service Principals** (SP) should be configured to access the Key Vault. One SP which has been granted secret management access deploys the infrastructure by running the Pulumi program. That's why the snippet above assigns an access policy to `currentPrincipal`.

Another SP is used by the application itself to read the secret values. The Client ID and Client Secret parameters are placed in the application configuration. Finally, .NET Core configuration gets hooked to the Key Vault at startup:

``` cs
builder.AddAzureKeyVault(
   $"https://{config["azureKeyVault:vault"]}.vault.azure.net/",
   config["azureKeyVault:clientId"],
   config["azureKeyVault:clientSecret"]
);
```

This solution is not entirely satisfying though, since we've traded storing the secrets for storing SP credentials. Is that a big enough win?  Luckily, it's easy to get rid of those credentials with Managed identities.

## 5. Accessing Key Vault with Managed Identities

With **Managed identities**, Azure takes care of creating a Service Principal, passing the credentials, rotating secrets, and so on. Enabling a managed identity on App Service is just an extra option:

``` ts
const app = new azure.appservice.AppService("app", {
   resourceGroupName: resourceGroup.name,
   appServicePlanId: appServicePlan.id,
   // A system-assigned managed identity
   identity: {
       type: "SystemAssigned",
   },
});
```

On top of that, the managed principal must be granted access to the Key Vault:

``` ts
const principalId = app.identity.apply(id => id.principalId);

// Grant App Service access to KV secrets
new azure.keyvault.AccessPolicy("app-policy", {
   keyVaultId: vault.id,
   tenantId: tenantId,
   objectId: principalId,
   secretPermissions: ["get"],
});
```

Now, the configuration block in the .NET Core app doesn't need to retrieve any secrets. `AzureServiceTokenProvider` helps with the authentication process:

``` cs
var azureServiceTokenProvider = new AzureServiceTokenProvider();
var keyVaultClient = new KeyVaultClient(
   new KeyVaultClient.AuthenticationCallback(
       azureServiceTokenProvider.KeyVaultTokenCallback));
builder.AddAzureKeyVault(
   keyVaultEndpoint, keyVaultClient, new DefaultKeyVaultSecretManager());
```

That's quite a bit of a boilerplate, but there is a way to get rid of it.

## 6. Accessing Key Vault from Application Settings

App Service has a neat feature of integrating its Application Settings with Key Vault. It allows us to combine #3 and #5's approaches and get the best of both:

``` ts
// Produce a URI of the KV secret defined above
const secretUri = pulumi.interpolate`${secret.vaultUri}secrets/${secret.name}/${secret.version}`;

const app = new azure.appservice.AppService("app", {
   resourceGroupName: resourceGroup.name,
   appServicePlanId: appServicePlan.id,
   // A system-assigned managed identity
   identity: {
       type: "SystemAssigned",
   },
   appSettings: {
       // The setting points directly to the KV setting
       "PAYMENT_API_KEY": pulumi.interpolate`@Microsoft.KeyVault(SecretUri=${secretUri})`,
   }
});
```

With that, the API key is loaded into the App Service environment variable without its value being publicly exposed anywhere!

## 7. Role-based Access Control

What is the most secure way to deal with secrets? *Have no secrets*. The Storage Account connection string is a great example when it's possible to avoid storing and reading the sensitive value altogether.

**Role-based access control** (RBAC) of **Azure Active Directory** (AAD) is a great tool to manage permissions in a declarative way. Let's assume our application only needs to send messages to one Storage Queue. Instead of storing a full connection string with an access token, the connection string should point to the account, and the identity behind the App Service should be granted write permissions to the required Storage Queue:

``` ts
const permission = new azure.role.Assignment("send", {
   principalId,
   scope: pulumi.interpolate`${storageAccount.id}/queueServices/default/queues/${queue.name}`,
   roleDefinitionName: "Storage Queue Data Message Sender",
});
```

We can put the queue URL into Application Settings because there's nothing secret in it:

``` ts
const queueUri = pulumi.interpolate`${storageAccount.primaryQueueEndpoint}${queue.name}`;

const app = new azure.appservice.AppService("app", {
   resourceGroupName: resourceGroup.name,
   appServicePlanId: appServicePlan.id,
   identity: {
       type: "SystemAssigned"
   },
   appSettings: {
       "STORAGE_QUEUE_URL": queueUri,
   },
```

It takes a bit of C# boilerplate to send a message with role-based authorization:

``` cs
var provider = new AzureServiceTokenProvider();
string accessToken = await provider.GetAccessTokenAsync("https://storage.azure.com/");
var tokenCredential = new TokenCredential(accessToken);
var storageCredentials = new StorageCredentials(tokenCredential);
var url = Environment.GetEnvironmentVariable("StorageBlobUrl");
var queue = new CloudQueue(new Uri(url), storageCredentials);
queue.AddMessage(new CloudQueueMessage("Hello"));
```

Let's hope another quality-of-life improvement is on the way.

## Role of Infrastructure as Code

While security practices may vary depending on application requirements, Pulumi plays an essential role in the appropriate setup of service configuration and environment:

- It links an output of one resource to another one's input, avoiding the need to store the values.
- It provides a built-in mechanism to manage external secrets.
- It is a great way to take advantage of Azure features like Managed identities and RBAC in a cohesive way.

Infrastructure as Code helps make your applications secure and reliable. Refer to [this full example](https://github.com/pulumi/examples/tree/master/azure-ts-msi-keyvault-rbac) of using Key Vault, Managed identities, RBAC with App Service and Pulumi.
