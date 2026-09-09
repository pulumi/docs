{{- /* Renders a template-driven page's frontmatter `sections:` array as markdown,
       for the text/markdown output format (Accept: text/markdown negotiation).
       Shared by the homepage (layouts/index.md), template pages
       (layouts/page/template-page.md), and the generic fallbacks
       (layouts/_default/single.md, list.md).

       Rather than dispatching on section type (as template-page-content.html
       does for HTML), this walks the textual fields the section types share —
       headings, descriptions, cards, columns, features, quotes — so new
       section types degrade gracefully. Purely visual sections (logo
       carousels, image grids, code overlays, social embeds) contribute
       nothing. Section descriptions are authored as markdown in frontmatter
       and pass through unmodified. */ -}}
{{- range .Params.sections -}}
{{- if .quote -}}
{{- /* Testimonials: .title is the speaker's role here, not a heading. */}}
> {{ replace (trim .quote " \n") "\n" " " }}
{{- $attribution := slice -}}
{{- with .author }}{{ $attribution = $attribution | append . }}{{ end -}}
{{- with or .role .title }}{{ $attribution = $attribution | append . }}{{ end -}}
{{- with .company }}{{ $attribution = $attribution | append . }}{{ end -}}
{{- with $attribution }}
>
> — {{ delimit . ", " }}
{{- end }}
{{ else -}}
{{- $heading := or .heading .title "" -}}
{{- with .title_line_2 }}{{ $heading = printf "%s %s" $heading . }}{{ end -}}
{{- /* Hero headlines carry <br> to force a line break; markdown wraps on its own. */ -}}
{{- $heading = replaceRE `<br\s*/?>` " " $heading -}}
{{- with replaceRE `\s+` " " $heading }}

## {{ . }}
{{ end -}}
{{- with .subtitle }}
{{ trim . " \n" }}
{{ end -}}
{{- with .description }}
{{ trim . " \n" }}
{{ end -}}
{{- with .text }}
{{ trim . " \n" }}
{{ end -}}
{{- $cards := slice -}}
{{- with .cards }}{{ $cards = $cards | append . }}{{ end -}}
{{- with .large_cards }}{{ $cards = $cards | append . }}{{ end -}}
{{- with .small_cards }}{{ $cards = $cards | append . }}{{ end -}}
{{- with .features }}{{ $cards = $cards | append . }}{{ end -}}
{{- $items := slice -}}
{{- range $cards -}}
{{- $card := . -}}
{{- if $card.number -}}
{{- $items = $items | append (printf "- **%s** %s" $card.number (or $card.label "")) -}}
{{- else if $card.title -}}
{{- $cardTitle := replace $card.title "\n" " " -}}
{{- $title := printf "**%s**" $cardTitle -}}
{{- with $card.cta_link }}{{ $title = printf "**[%s](%s)**" $cardTitle . }}{{ end -}}
{{- $line := printf "- %s" $title -}}
{{- with $card.description }}{{ $line = printf "%s — %s" $line (replace (trim . " \n") "\n" " ") }}{{ end -}}
{{- $items = $items | append $line -}}
{{- end -}}
{{- end -}}
{{- with $items }}
{{ delimit . "\n" }}
{{ end -}}
{{- range .columns }}

### {{ with .label }}{{ . }}: {{ end }}{{ replace (or .title "") "\n" " " }}
{{- with .subheader }}
{{ . }}
{{- end }}
{{- with .description }}
{{ trim . " \n" }}
{{- end }}
{{- end -}}
{{- $videoTitle := or .title "Video" -}}
{{- with .youtube_id }}
[Watch: {{ $videoTitle }}](https://www.youtube.com/watch?v={{ . }})
{{ end -}}
{{- end -}}
{{- end -}}
