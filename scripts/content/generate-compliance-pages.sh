#!/bin/bash

# Load JSON data
pages=$(cat data/compliance/pages.json)

for row in $(echo "${pages}" | jq -r '.[] | @base64'); do
    for res in $(echo "${row}" | base64 --decode | jq -r '.resources[] | @base64'); do
        _jq() {
            echo ${row} | base64 --decode | jq -r ${1}
        }
        decodeResource() {
            echo ${res} | base64 --decode | jq -r ${1}
        }
        slug=$(echo "$(_jq '.cloud')-$(decodeResource '.name')-$(_jq '.framework')" | awk '{print tolower($0)}')
        layout=$(_jq '.framework' | awk '{print tolower($0)}')
        title="$(_jq '.cloud') $(decodeResource '.name') $(_jq '.framework') Compliance"
    # Create a new markdown file for each entry
    cat > "content/compliance/${slug}.md" <<EOT
---
title: $title
date: $(date +"%Y-%m-%dT%}H:%M:%S")
cloud: $(_jq '.cloud')
layout: "$layout"
slug: $slug
framework: $(_jq '.framework')
resource: $(decodeResource '.name')
full: $(decodeResource '.full')
meta_desc: add meta desc here add meta desc here add meta desc here add meta desc here add meta desc here
---

EOT
    done
done
