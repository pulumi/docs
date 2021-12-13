#!/bin/bash

set -o errexit -o pipefail

module=""
topic=""
content_root="themes/default/content/"

prompt_for_module_name() {
    read -p "Module name (e.g., pulumi-101-aws): " module

    if [[ ! -z "$module" && -d "${content_root}learn/${module}" ]]; then
        return
    fi

    echo "Couldn't find a module with that name. Make sure you're using the path as listed under content/learn."
    echo
    prompt_for_module_name
}

prompt_for_topic_name() {
    read -p "Topic name (e.g., basics): " topic

    if [ ! -z "$topic" ]; then
        hugo new --kind learn/topic "${content_root}learn/${module}/${topic}"
        return
    fi

    echo "Please give the topic a name."
    echo
    prompt_for_topic_name
}

echo "So, you want to make a new Learn Pulumi topic? Great! 🙌"
echo
echo "Step 1:"
echo "What is the path name of the module you want to write for?"
echo
prompt_for_module_name

echo
echo "Step 2:"
echo "Now give your new topic a URL-friendly name. For example, to
create a new topic under ${module} that'll live at
https://pulumi.com/learn/${module}/basics, type 'basics'."
echo
prompt_for_topic_name
