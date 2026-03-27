{{- $latestVersionFile := "/static/esc/latest-version" -}}
{{- $latestVersion := readFile $latestVersionFile -}}
{{- if gt (len (findRE "\\s" $latestVersion)) 0 -}}
    {{- errorf "%q must not contain whitespace or newlines" $latestVersionFile -}}
{{- end -}}
{{- $latestVersion -}}
