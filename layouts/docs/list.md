---
title: {{ .Title }}
{{ with .Description }}description: {{ . }}
{{ end }}url: {{ .RelPermalink }}
---
{{- $content := .RenderShortcodes -}}
{{- /* Phase 1: Convert Chroma syntax-highlighted HTML to fenced code blocks */ -}}
{{- $content = replaceRE `<div[^>]*>\s*<pre[^>]*><code class="language-([^"]*)"[^>]*>` "```$1\n" $content -}}
{{- $content = replaceRE `</code></pre>\s*</div>` "\n```" $content -}}
{{- $content = replaceRE `<pre[^>]*><code>` "```\n" $content -}}
{{- $content = replaceRE `</code></pre>` "\n```" $content -}}
{{- /* Phase 2: Strip all block-level and decorative tags */ -}}
{{- $content = replaceRE `</?span[^>]*>` "" $content -}}
{{- $content = replaceRE `<i[^>]*></i>` "" $content -}}
{{- $content = replaceRE `<input[^>]*>` "" $content -}}
{{- $content = replaceRE `</?label[^>]*>` "" $content -}}
{{- $content = replaceRE `</?div[^>]*>` "" $content -}}
{{- $content = replaceRE `</?p>` "" $content -}}
{{- $content = replaceRE `</?blockquote>` "" $content -}}
{{- $content = replaceRE `</?ol>` "" $content -}}
{{- $content = replaceRE `</?ul>` "" $content -}}
{{- $content = replaceRE `</?li>` "" $content -}}
{{- $content = replaceRE `</?pre[^>]*>` "" $content -}}
{{- $content = replaceRE `</?section[^>]*>` "" $content -}}
{{- $content = replaceRE `</?table[^>]*>` "" $content -}}
{{- $content = replaceRE `</?thead>` "" $content -}}
{{- $content = replaceRE `</?tbody>` "" $content -}}
{{- $content = replaceRE `</?tr>` "" $content -}}
{{- $content = replaceRE `</?td[^>]*>` "" $content -}}
{{- $content = replaceRE `</?th[^>]*>` "" $content -}}
{{- $content = replaceRE `</?details>` "" $content -}}
{{- $content = replaceRE `</?summary>` "" $content -}}
{{- $content = replaceRE `<!--\s*markdownlint[^>]*-->` "" $content -}}
{{- /* Phase 3: Normalize whitespace so inline conversions can match cleanly */ -}}
{{- $content = replaceRE `(?m)^[ \t]+` "" $content -}}
{{- $content = replaceRE `\n{3,}` "\n\n" $content -}}
{{- /* Phase 4: Convert inline HTML to markdown */ -}}
{{- $content = replaceRE `<a[^>]*href="([^"]*)"[^>]*>([^<]*)</a>` "[$2]($1)" $content -}}
{{- /* Collapse whitespace inside markdown link brackets (from multi-line <a> tags) */ -}}
{{- $content = replaceRE `\[\s+` "[" $content -}}
{{- $content = replaceRE `\s+\]\(` "](" $content -}}
{{- $content = replaceRE `<code>([^<]*)</code>` "`$1`" $content -}}
{{- $content = replaceRE `<strong>([^<]*)</strong>` "**$1**" $content -}}
{{- $content = replaceRE `<em>([^<]*)</em>` "*$1*" $content -}}
{{- /* Phase 5: Convert heading tags to markdown headings */ -}}
{{- $content = replaceRE `<h1[^>]*>([^<]*)</h1>` "\n# $1\n" $content -}}
{{- $content = replaceRE `<h2[^>]*>([^<]*)</h2>` "\n## $1\n" $content -}}
{{- $content = replaceRE `<h3[^>]*>([^<]*)</h3>` "\n### $1\n" $content -}}
{{- $content = replaceRE `<h4[^>]*>([^<]*)</h4>` "\n#### $1\n" $content -}}
{{- $content = replaceRE `<h5[^>]*>([^<]*)</h5>` "\n##### $1\n" $content -}}
{{- $content = replaceRE `<h6[^>]*>([^<]*)</h6>` "\n###### $1\n" $content -}}
{{- /* Strip any remaining HTML tags not yet handled */ -}}
{{- $content = replaceRE `</?a[^>]*>` "" $content -}}
{{- /* Strip lone +/- lines left from accordion toggle spans */ -}}
{{- $content = replaceRE `(?m)^[+\-]\n` "" $content -}}
{{- /* Phase 6: Decode HTML entities and final cleanup */ -}}
{{- $content = $content | htmlUnescape -}}
{{- $content = replaceRE `\n{3,}` "\n\n" $content -}}

{{ $content }}
