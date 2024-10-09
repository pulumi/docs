---
title: "Why Storing Secrets in Environment Variables is a Bad Idea"
date: "2024-10-08"
meta_desc: "Don't trade convenience for security. Learn why storing secrets in environment variables is a bad idea and how Pulumi ESC SDK can help."
meta_image: meta.png
authors:
- engin-diri

tags:
- security
- secrets
- env
- esc
- sdk
---

I have to make a confession. I've been storing secrets in environment variables for ages. It is such a convenient way to store and access secrets that I never thought about any security risks.

Here is an example of how I usually connect to a database in my `Go` application:

<!--more-->

```go
package main

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq" // Import PostgreSQL driver
)

func main() {
	// Retrieve the database connection string from environment variable
	dbConnStr := os.Getenv("DB_CONN_STRING")

	if dbConnStr == "" {
		log.Fatal("DB_CONN_STRING environment variable not set")
	}

	// Connect to the database using the connection string
	db, err := sql.Open("postgres", dbConnStr)
	if err != nil {
		log.Fatalf("Failed to connect to the database: %v", err)
	}
	defer db.Close()

	// Verify connection is established
	err = db.Ping()
	if err != nil {
		log.Fatalf("Failed to ping the database: %v", err)
	}

	fmt.Println("Successfully connected to the database!")
}
```

And my example is not an isolated case. The use of environment variables is a common practice in the world of DevOps as it provides easy access to configuration values.

Almost all modern applications built to run in containerized environments follow this convenient way to pass configuration values as environment variables. Famous is [the twelve-factor app](https://12factor.net/) methodology and its 12 principles.

### The Twelve-Factor App Methodology and environment variables

And one of the principles of the twelve-factor app is to store configuration in environment variables:

> Apps sometimes store config as constants in the code. This is a violation of twelve-factor, which requires strict
> separation of config from code. Config varies substantially across deploys, code does not.
> ...
> The twelve-factor app stores config in environment variables (often shortened to env vars or env).

You will hardly find a modern application that does not follow this principle. But, when we backtrack to my code from above, it becomes a problem when the database connection string, which is a secret, is stored in an environment variable.

The convenience of storing secrets in environment variables becomes an easy way for attackers to gain access to other parts of the system once they have access to the environment.

Additionally, environment variables are stored as plain text. Which means that anyone with access to the runtime environment, through such simple things as overly verbose logs or sophisticated attacks through remote code execution vulnerabilities, can exploit this.

There is even a common weakness enumeration entry [CWE-526](https://cwe.mitre.org/data/definitions/526.html?ref=blog.arcjet.com). And the hidden danger of environment variables is that it allows users to unintentionally cross security boundaries. The probability of this leakage increases with every child process that is spawned from the parent process.

To summarize the problems with storing secrets in environment variables:

### Risk #1: Lateral Movement

When an attacker gains access to the environment, they can easily access the secrets stored in the environment variables. Once they have access to those credentials or API keys, they can use them to start hopping around in your infrastructure.

### Risk #2: Exposure to Logs

Another risk is that secrets stored in environment variables can be exposed in logs or as process dumps. Think about how often we use during debugging `fmt.Println(os.Environ())` to print all the environment variables. If you accidentally commit this code to your repository, you are exposing your secrets to some third-party logging service. Redacting sensitive data from logs is now an extra task that you have to take care of.

### Risk #3: Managing Secrets in Environment Variables

When you have a lot of secrets, managing them in environment variables becomes a nightmare:

- Where is each secret? Was the new database password for the staging environment or the production environment? You have to keep track of all the secrets and where they are used, and the more environments you have, the greater the risk that it gets easily out of sync.
- Rotating secrets is a pain. You have to update the environment variables in all the places where they are used because you detected a security breach or a leak. Have fun with downtimes or rollout issues due to system restarts.
- No Audit Trail. You have no way to track who accessed the secrets and when. What if a secret was leaked? You have no way to track it back to which system an attacker accessed. Additionally, you have no way to track who changed the secret as you have no history of changes.

## How to Store Secrets Securely: Runtime secret injection with Pulumi ESC SDK

The best way to store secrets is to use a [secret management system](/what-is/what-is-secrets-management/). Using a secret management system that offers an SDK that you can integrate into your application code. Pulumi ESC is provider-agnostic so you only need to define one secret manager and in the backend Pulumi ESC [dynamically import secrets](/docs/esc/integrations/dynamic-secrets/) and configuration from the other provider (AWS, Azure, GCP, Vault, etc.).

This is how it works with [Pulumi ESC SDK](/docs/esc/development/languages-sdks/):

- Permissions are managed by [Pulumi ESC](/product/secrets-management/), so you can control who has access to the secrets and audit who accessed them.
- With the help of the Pulumi ESC SDK, you can fetch the secrets at startup time or when they are needed.
- Pulumi ESC SDK provides convenient objects representing the secrets, so you can access them by their name inside your application code. Additionally, you get type safety out of the box.

Here is an example of how we can implement the database connection string retrieval with [Pulumi ESC Go SDK](/docs/esc/development/languages-sdks/go/):

```go
package main

import (
	"database/sql"
	"fmt"
	"log"
	"os"

	_ "github.com/lib/pq"
	esc "github.com/pulumi/esc-sdk/sdk/go"
)

func main() {
	accessToken := os.Getenv("PULUMI_ACCESS_TOKEN")
	projectName := os.Getenv("ESC_PROJECT")
	orgName := os.Getenv("PULUMI_ORG")
	envName := os.Getenv("ESC_ENVIRONMENT")
	configuration := esc.NewConfiguration()
	escClient := esc.NewClient(configuration)
	authCtx := esc.NewAuthContext(accessToken)

	_, values, err := escClient.OpenAndReadEnvironment(authCtx, orgName, projectName, envName)
	if err != nil {
		log.Fatalf("Failed to open and read environment: %v", err)
	}
	dbConnStr := values["postgres"].(map[string]interface{})["connStr"].(string)

	if dbConnStr == "" {
		log.Fatal("DB_CONN_STRING environment variable not set")
	}

	db, err := sql.Open("postgres", dbConnStr)
	if err != nil {
		log.Fatalf("Failed to connect to the database: %v", err)
	}
	defer db.Close()

	err = db.Ping()
	if err != nil {
		log.Fatalf("Failed to ping the database: %v", err)
	}

	fmt.Println("Successfully connected to the database!")

}
```

With the Pulumi ESC SDK, we can fetch the secrets at runtime when they are needed. This way, we avoid storing secrets in environment variables and reduce any of the risks I mentioned above.

## Conclusion

Storing secrets in environment variables is a bad idea. It may be convenient, but it is definitely not secure. Don't
make it easy for attackers to compromise your system:

- Use a secret management system, like [Pulumi ESC](/product/secrets-management/). It provides a secure and compliant way to store and access secrets,
  which you will never get with environment variables.
- Fetch secrets only at runtime when they are needed.
- Don't expose secrets in logs or process dumps.

Start using Pulumi ESC and ESO today by creating an account on the Pulumi Cloud Console and begin managing your secrets in a secure and efficient way.

<a class="btn btn-secondary" href="https://app.pulumi.com/signup" target="_blank">Create an Account</a>
