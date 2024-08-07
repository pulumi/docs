#!/bin/bash

set -o errexit -o pipefail
echo "hey girl"
module=""
topic=""

content_dir="content"

prompt_for_module_name() {
    read -p "Module name (e.g., pulumi-101): " module

    if [ ! -z "$module" ]; then
        hugo new --kind tutorials/module --contentDir "${content_dir}" "tutorials/${module}"
        return
    fi

    echo "Please give the module a name."
    prompt_for_module_name
}

prompt_for_topic_name() {
    read -p "Topic name (e.g., basics): " topic

    if [ ! -z "$topic" ]; then
        hugo new --kind tutorials/topic --contentDir "${content_dir}" "tutorials/${module}/${topic}"
        return
    fi

    echo "Please give the topic a name."
    prompt_for_topic_name
}

echo "So, you want to make a new tutorial module? Awesome! 🙌"
echo
echo "Step 1:"
echo "First, give the module a URL- and SEO-friendly name.
For example, to create a new module that'll live at
https://pulumi.com/tutorials/pulumi-101, type 'pulumi-101'."
echo
prompt_for_module_name

echo
echo "Step 2:"
echo "Now give your new module at least one new topic, also expressed
as a URL-friendly name. For example, to create a new topic under ${module}
that'll live at https://pulumi.com/tutorials/${module}/basics, type 'basics'."
echo
prompt_for_topic_name
