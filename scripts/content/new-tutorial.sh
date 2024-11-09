#!/bin/bash

set -o errexit -o pipefail
slug=""

content_dir="content"

prompt_for_tutorial_name() {
    read -p "Tutorial name (e.g., pulumi-101): " slug

    if [ ! -z "$slug" ]; then
        hugo new --kind tutorials/single --contentDir "${content_dir}" "tutorials/${slug}"
        return
    fi

    echo "Please give the tutorial a name."
    prompt_for_tutorial_name
}

echo "So, you want to make a new tutorial? Awesome! 🙌"
echo
echo "Give the module a URL- and SEO-friendly name. For example, to create a new
tutorial that'll live at https://pulumi.com/tutorials/pulumi-101, type 'pulumi-101'."
echo
prompt_for_tutorial_name
