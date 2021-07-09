#!/bin/bash

set -o errexit -o pipefail

module=""
topic=""

prompt_for_module_name() {
    read -p "Module name (e.g., pulumi-101-aws): " module

    if [ ! -z "$module" ]; then
        hugo new --kind learn/module "learn/${module}"
        return
    fi

    echo "Please give the module a name."
    prompt_for_module_name
}

prompt_for_topic_name() {
    read -p "Topic name (e.g., basics): " topic

    if [ ! -z "$topic" ]; then
        hugo new --kind learn/topic "learn/${module}/${topic}"
        return
    fi

    echo "Please give the topic a name."
    prompt_for_topic_name
}

echo "So, you want to make a new Learn Pulumi module? Awesome! 🙌"
echo
echo "Step 1:"
echo "First, give the module a URL- and SEO-friendly name.
For example, to create a new module that'll live at
https://pulumi.com/learn/pulumi-101, type 'pulumi-101'."
echo
prompt_for_module_name

echo
echo "Step 2:"
echo "Now give your new module at least one new topic, also expressed
as a URL-friendly name. For example, to create a new topic under ${module}
that'll live at https://pulumi.com/learn/${module}/basics, type 'basics'."
echo
prompt_for_topic_name
