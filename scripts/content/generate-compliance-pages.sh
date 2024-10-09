#!/bin/bash

# Load JSON data
pages=$(cat data/compliance/pages.json)

for row in $(echo "${pages}" | jq -r '.frameworks[] | @base64'); do
    for svc in $(echo "${pages}" | jq -r '.services[] | @base64'); do
        _jq() {
            echo ${row} | base64 --decode | jq -r ${1}
        }
        decodeService() {
            echo ${svc} | base64 --decode | jq -r ${1}
        }
        # Check if the cloud from the framework matches the cloud from the service
        if [ "$(_jq '.cloud')" = "$(decodeService '.cloud')" ]; then
        slug=$(echo "$(_jq '.framework')-$(_jq '.cloud')-$(decodeService '.name')" | awk '{print tolower($0)}' | sed 's/ /-/g')
        layout=$(_jq '.framework' | awk '{print tolower($0)}' | sed 's/ /-/g')
        title="How to Achieve $(_jq '.framework') Compliance for $(_jq '.cloud' ) $(decodeService '.name' | sed 's/Cloud //')"
        if [ ${#title} -gt 60 ]; then
            title="Achieve $(_jq '.framework') Compliance for $(_jq '.cloud' ) $(decodeService '.name' | sed 's/Cloud //')"
        fi
        metadesc="Pulumi helps achieve $(_jq '.framework') compliance for $(_jq '.cloud') $(decodeService '.name' | sed 's/Cloud //') by enforcing security, cost, and compliance requirements. Speak with an expert to get started."
        if [ ${#metadesc} -gt 160 ]; then
            metadesc="Pulumi helps achieve $(_jq '.framework') compliance for $(_jq '.cloud') $(decodeService '.name' | sed 's/Cloud //') by enforcing security, cost, and compliance requirements."
        fi
    # Create a new markdown file for each entry
    cat > "content/compliance/${slug}.md" <<EOF
---
# This file is auto-generated. Any alterations made within are subject
# to being overwritten.
title: $title
cloud: $(_jq '.cloud')
layout: "$layout"
slug: $slug
framework: $(_jq '.framework')
service: $(decodeService '.name')
full: $(decodeService '.full')
description: "$(_jq '.description')"
whatis: "$(decodeService '.whatis')"
page_type: service
meta_desc: $metadesc
---

EOF
fi
    done
    cat > "content/compliance/$(echo "$(_jq '.cloud')-$(_jq '.framework')" | sed 's/ /-/g' | awk '{print tolower($0)}').md" <<EOF
---
# This file is auto-generated. Any alterations made within are subject
# to being overwritten.
title: "$(_jq '.framework') Compliance for $(_jq '.cloud')"
cloud: $(_jq '.cloud')
layout: "$layout"
slug: $(echo "$(_jq '.framework')-$(_jq '.cloud')" | awk '{print tolower($0)}' | sed 's/ /-/g')
framework: $(_jq '.framework')
service: "$(_jq '.cloud')"
full: "$(_jq '.cloud') cloud infrastructure"
description: "$(_jq '.description')"
page_type: cloud
meta_desc: Pulumi helps achieve $(_jq '.framework') compliance for $(_jq '.cloud') by enforcing security, cost, and compliance requirements. Speak with an expert to get started.
---

EOF
done
