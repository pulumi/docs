---
user-invocable: false
---

# Directory Category Hints

Match keywords from the user's description to suggest appropriate documentation locations.

## Keyword-to-Directory Mapping

- **Concepts** (`*/concepts/`): "what is", "understanding", "overview"
- **Guides** (`*/guides/`): "how to", "guide", "tutorial"
- **Clouds** (`iac/clouds/[provider]/`): AWS, Azure, GCP, Kubernetes
- **Languages** (`iac/languages-sdks/[lang]/`): TypeScript, Python, Go, .NET, Java, YAML
- **CLI** (`iac/cli/`): "command", "cli"
- **Automation API** (`iac/automation-api/`): "automation", "programmatic"
- **Administration** (`administration/`): "organizations", "teams", "SAML", "SSO"
- **ESC** (`esc/`): "secrets", "environment"
- **Deployments** (`deployments/`): "deploy", "drift"

## Usage

Extract 2-3 key terms from the user's description and match against these patterns to suggest the most appropriate location.
