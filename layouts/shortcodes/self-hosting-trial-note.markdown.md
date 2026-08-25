{{- /* Says only what the page's `pulumi_cloud_feature: self-hosting` callout
       can't: how to try it. The edition sentence this note used to open with is
       generated from data/pulumi_pricing.yaml now, in the callout directly
       above — see AGENTS.md, "Don't say it twice". Kept in step with the HTML
       sibling, layouts/shortcodes/self-hosting-trial-note.html. */ -}}
{{- $product := default "self-hosted Pulumi Cloud" (.Get "product") -}}
{{- $text := printf "If you would like to evaluate the %s, [request a Proof of Concept (PoC)](/product/self-hosted/#self-hosted-trial) or [contact us](/contact/)." $product -}}
{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Note:** {{ $text }}{{ with $inner }} {{ . }}{{ end }}
