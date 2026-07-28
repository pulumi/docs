{{- /*
    Renders a shell command as the standard OS chooser pair: a bash block for
    linux/macos (with a "$" prompt) and a PowerShell block for windows (with a
    ">" prompt).

    Usage: {{< os-command "pulumi destroy" >}}
           {{< os-command "curl -fsSL https://get.pulumi.com | sh" "choco install pulumi" >}}

    The optional second argument overrides the Windows form of the command when
    it differs from the POSIX one.
*/ -}}
{{- $cmd := .Get 0 -}}
{{- if not $cmd -}}
    {{- errorf "os-command: a command argument is required (in %s)" .Page.File.Path -}}
{{- end -}}
{{- $winCmd := $cmd -}}
{{- with .Get 1 -}}{{- $winCmd = . -}}{{- end -}}
{{- $md := printf "{{%% choosable os \"linux,macos\" %%}}\n\n```bash\n$ %s\n```\n\n{{%% /choosable %%}}\n\n{{%% choosable os \"windows\" %%}}\n\n```powershell\n> %s\n```\n\n{{%% /choosable %%}}\n" $cmd $winCmd -}}
{{ .Page.RenderString (dict "display" "block") $md }}
