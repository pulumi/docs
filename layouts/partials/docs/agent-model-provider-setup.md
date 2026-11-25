{{- if eq (.Get 0) "open" -}}
Organizations on the legacy Business Critical edition also have access to this feature. To connect the provider, you need permission to manage your organization's integrations, such as the Admin role.

1. In Pulumi Cloud, open your organization's **Agent Settings**.
1. Select **Model provider**, then **Add model provider**.
1. Enter a unique **Name** using lowercase letters, numbers, and hyphens. Choose a name you can recognize when configuring an agent. The name is permanent, and Pulumi reserves `pulumi`.
1. Under **Provider**, select **{{ .Get 1 }}**.
{{- else -}}
Select **Save**. Pulumi sends a test request to each configured model and shows any errors. If a request fails, correct the settings and save again.

To use the connection for one agent, [open the agent's configuration](/docs/ai/agents/configure/#choose-a-model), select the provider by name under **Model**, and save the agent. Start a new task to use that selection.

To use the connection for new tasks that follow the organization default, check whether it is already the default. If needed, select **Set as default** in **Agent Settings**. See [how Pulumi chooses the default provider](/docs/ai/agents/model-providers/#the-default-provider).
{{- end -}}
