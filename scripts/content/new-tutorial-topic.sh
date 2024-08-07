#!/bin/bash

set -o errexit -o pipefail

module=""
topic=""
content_dir="content"

prompt_for_module_name() {
    read -p "Module name (e.g., pulumi-101-aws): " module

    if [[ ! -z "$module" && -d "${content_dir}/tutorials/${module}" ]]; then
        return
    fi

    if [[ -z "$module" ]]; then
        return
    fi

    echo "Couldn't find a module with that name. Make sure you're using the path as listed under content/tutorials."
    echo
    prompt_for_module_name
}

prompt_for_topic_name() {
    read -p "Topic name (e.g., basics): " topic

    if [ ! -z "$topic" ]; then
        if [[ ! -z "$module" ]]; then
            hugo new --kind tutorials/topic --contentDir "${content_dir}" "tutorials/${module}/${topic}"
            return
        else
            hugo new --kind tutorials/topic --contentDir "${content_dir}" "tutorials/${topic}"
            return
        fi
    fi

    echo "Please give the topic a name."
    echo
    prompt_for_topic_name
}

echo "So, you want to make a new tutorial topic? Great! 🙌"
echo
echo "Step 1:"
echo "What is the path name of the module you want to write for?"
echo "This is optional; if you want to create a single-page tutorial,"
echo "you can leave this blank."
echo
prompt_for_module_name

echo
echo "Step 2:"
echo "Now give your new topic a URL-friendly name. For example, to
create a new topic under ${module} that'll live at
https://pulumi.com/learn/${module}/basics, type 'basics'."
echo
prompt_for_topic_name
