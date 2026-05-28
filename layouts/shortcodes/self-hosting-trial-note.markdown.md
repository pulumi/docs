{{- $product := default "self-hosted Pulumi Cloud" (.Get "product") -}}
{{- $text := printf "Self-hosting is only available with **Pulumi Business Critical**. If you would like to evaluate the %s, [request a Proof of Concept (PoC)](/product/self-hosted/#self-hosted-trial) or [contact us](/contact/)." $product -}}
{{- $inner := trim (printf "%s" .Inner) " \t\n\r" -}}

> **Note:** {{ $text }}{{ with $inner }} {{ . }}{{ end }}
