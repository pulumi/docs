{{- $currentPage := .Page -}}
{{- $unsortedPages := slice $currentPage -}}
{{- if $currentPage.Parent -}}
    {{- if $currentPage.Parent.File -}}
        {{- if eq $currentPage.File.Dir $currentPage.Parent.File.Dir -}}
            {{- $unsortedPages = $unsortedPages | append $currentPage.Parent -}}
        {{- end -}}
    {{- end -}}
{{- end -}}
{{- range $index, $page := .Page.CurrentSection.Pages -}}
    {{- if and (gt $page.Weight 0) (ne $page.RelPermalink $currentPage.RelPermalink) -}}
        {{- $unsortedPages = $unsortedPages | append $page -}}
    {{- end -}}
{{- end -}}
{{- $pages := sort $unsortedPages "Weight" -}}
{{- $first := 0 -}}
{{- $last := sub (len $pages) 1 -}}
{{- $step := -1 -}}
{{- range $index, $element := $pages -}}
    {{- if eq $element.RelPermalink $currentPage.RelPermalink -}}
        {{- $step = $index -}}
    {{- end -}}
{{- end -}}

---
{{ if ne $step $first }}
{{- $prev := index $pages (sub $step 1) -}}
[← Previous step]({{ $prev.RelPermalink }})
{{ end }}
{{- if ne $step $last -}}
{{- $next := index $pages (add $step 1) -}}
{{- $linkTitle := printf "Next: %s" $next.LinkTitle -}}
{{- if isset $next.Params "stepper_link" -}}
    {{- $linkTitle = $next.Params.stepper_link -}}
{{- end -}}
[{{ $linkTitle }} →]({{ $next.RelPermalink }})
{{ end }}
