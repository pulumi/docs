{{- $path := .Get "path" -}}
{{- $languages := default "javascript,typescript,python,go,csharp,java,yaml" (.Get "languages") -}}
{{- $programsDir := slice "static" "programs" -}}
{{- $showChooser := gt (len (split $languages ",")) 1 -}}
{{- $chooserLangs := slice -}}
{{- if $showChooser -}}
{{- $eachLang := split $languages "," -}}
{{- range $eachLang -}}
{{- $lang := index (split . ":") 0 -}}
{{- $programDir := path.Join $programsDir (printf "%s-%s" $path $lang) -}}
{{- if fileExists $programDir -}}
{{- $chooserLangs = $chooserLangs | append $lang -}}
{{- end -}}
{{- end -}}

<!-- chooser: language -->
{{- end -}}
{{- range $i, $language := split $languages "," -}}
{{- $range := split $language ":" -}}
{{- $language = index $range 0 -}}
{{- $specifiedFilename := "" -}}
{{- $lineRange := "" -}}
{{- $specifiesFilename := gt (len $range) 2 -}}
{{- if $specifiesFilename -}}
{{- $specifiedFilename = index $range 1 -}}
{{- $lineRange = split (index $range 2) "-" -}}
{{- else -}}
{{- $lineRange = split (index $range 1) "-" -}}
{{- end -}}
{{- $from := default 1 (index $lineRange 0) -}}
{{- $to := default 9999 (index $lineRange 1) -}}
{{- $program := "" -}}
{{- if eq $language "javascript" -}}
{{- $program = "index.js" -}}
{{- else if eq $language "typescript" -}}
{{- $program = "index.ts" -}}
{{- else if eq $language "python" -}}
{{- $program = "__main__.py" -}}
{{- else if eq $language "go" -}}
{{- $program = "main.go" -}}
{{- else if eq $language "csharp" -}}
{{- $program = "Program.cs" -}}
{{- else if eq $language "java" -}}
{{- $program = "src/main/java/myproject/App.java" -}}
{{- else if eq $language "yaml" -}}
{{- $program = "Pulumi.yaml" -}}
{{- end -}}
{{- if ne $specifiedFilename "" -}}
{{- $program = $specifiedFilename -}}
{{- end -}}
{{- if ne $program "" -}}
{{- $programFilePath := path.Join $programsDir (printf "%s-%s" $path $language) $program -}}
{{- if fileExists $programFilePath -}}
{{- $code := readFile $programFilePath -}}
{{- $lines := split $code "\n" -}}
{{- $toEnd := after (sub (int $from) 1) $lines -}}
{{- $lineCount := add (sub (int $to) (int $from)) 1 -}}
{{- $toTo := first $lineCount $toEnd -}}
{{- $code = delimit $toTo "\n" -}}
{{- if $showChooser }}

<!-- option: {{ $language }} -->
{{ end }}
```{{ $language }}
{{ $code }}
```

[View full example on GitHub](https://github.com/pulumi/docs/tree/master/static/programs/{{ $path }}-{{ $language }})
{{ if $showChooser }}
<!-- /option -->
{{- end -}}
{{- end -}}
{{- end -}}
{{- end -}}
{{- if $showChooser }}

<!-- /chooser -->
{{- end }}
