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
        slug=$(echo "$(_jq '.cloud')-$(decodeResource '.name')-$(_jq '.framework')" | awk '{print tolower($0)}' | sed 's/ /-/g')
        layout=$(_jq '.framework' | awk '{print tolower($0)}' | sed 's/ /-/g')
        title="$(_jq '.framework') Compliance for $(_jq '.cloud') $(decodeResource '.name')"
    # Create a new markdown file for each entry
    cat > "content/compliance/${slug}.md" <<EOF
---
# This file is auto-generated. Any alterations made within are subject
# to being overwritten.
title: $title
date: $(date +"%Y-%m-%dT%}H:%M:%S")
cloud: $(_jq '.cloud')
layout: "$layout"
slug: $slug
framework: $(_jq '.framework')
resource: $(decodeResource '.name')
full: $(decodeResource '.full')
meta_desc: Pulumi can assist your organization with becoming $(_jq '.framework') compliant. Get in touch with our Solutions Architects to learn more.
---

EOF
    done
    cat > "content/compliance/$(echo "$(_jq '.cloud')-$(_jq '.framework')" | awk '{print tolower($0)}').md" <<EOF
---
# This file is auto-generated. Any alterations made within are subject
# to being overwritten.
title: "$(_jq '.framework') Compliance for $(_jq '.cloud')"
date: $(date +"%Y-%m-%dT%}H:%M:%S")
cloud: $(_jq '.cloud')
layout: "$layout"
slug: $(echo "$(_jq '.cloud')-$(_jq '.framework')" | awk '{print tolower($0)}')
framework: $(_jq '.framework')
resource: "$(_jq '.cloud')"
full: "$(_jq '.cloud') cloud infrastructure"
meta_desc: Pulumi can assist your organization with becoming $(_jq '.framework') compliant. Get in touch with our Solutions Architects to learn more.
---

EOF
done
