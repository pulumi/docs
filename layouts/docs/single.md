---
title: {{ .Title }}
{{ with .Description }}description: {{ . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- /* Convert Chroma syntax-highlighted HTML to fenced code blocks */ -}}
{{- $content = replaceRE `<div[^>]*>\s*<pre[^>]*><code class="language-([^"]*)"[^>]*>` "```$1\n" $content -}}
{{- $content = replaceRE `</code></pre>\s*</div>` "\n```" $content -}}
{{- /* Convert bare pre/code blocks (no language class) to fenced code blocks */ -}}
{{- $content = replaceRE `<pre[^>]*><code>` "```\n" $content -}}
{{- $content = replaceRE `</code></pre>` "\n```" $content -}}
{{- /* Strip span tags (Chroma highlighting) */ -}}
{{- $content = replaceRE `</?span[^>]*>` "" $content -}}
{{- /* Strip icon tags and other decorative elements (before heading conversion) */ -}}
{{- $content = replaceRE `<i[^>]*></i>` "" $content -}}
{{- $content = replaceRE `<input[^>]*>` "" $content -}}
{{- $content = replaceRE `<label[^>]*>([^<]*)</label>` "$1" $content -}}
{{- /* Convert HTML links to markdown links */ -}}
{{- $content = replaceRE `<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>` "[$2]($1)" $content -}}
{{- /* Convert common inline HTML to markdown */ -}}
{{- $content = replaceRE `<code>([^<]*)</code>` "`$1`" $content -}}
{{- $content = replaceRE `<strong>([^<]*)</strong>` "**$1**" $content -}}
{{- $content = replaceRE `<em>([^<]*)</em>` "*$1*" $content -}}
{{- /* Convert heading tags to markdown headings */ -}}
{{- $content = replaceRE `<h1[^>]*>([^<]*)</h1>` "\n# $1\n" $content -}}
{{- $content = replaceRE `<h2[^>]*>([^<]*)</h2>` "\n## $1\n" $content -}}
{{- $content = replaceRE `<h3[^>]*>([^<]*)</h3>` "\n### $1\n" $content -}}
{{- $content = replaceRE `<h4[^>]*>([^<]*)</h4>` "\n#### $1\n" $content -}}
{{- $content = replaceRE `<h5[^>]*>([^<]*)</h5>` "\n##### $1\n" $content -}}
{{- $content = replaceRE `<h6[^>]*>([^<]*)</h6>` "\n###### $1\n" $content -}}
{{- /* Strip remaining block-level tags */ -}}
{{- $content = replaceRE `</?div[^>]*>` "" $content -}}
{{- $content = replaceRE `</?p>` "" $content -}}
{{- $content = replaceRE `</?blockquote>` "" $content -}}
{{- $content = replaceRE `</?ol>` "" $content -}}
{{- $content = replaceRE `</?li>` "" $content -}}
{{- $content = replaceRE `</?pre[^>]*>` "" $content -}}
{{- /* Strip HTML comments that aren't chooser delimiters */ -}}
{{- $content = replaceRE `<!--\s*markdownlint[^>]*-->` "" $content -}}
{{- /* Decode HTML entities */ -}}
{{- $content = $content | htmlUnescape -}}

{{ $content }}
