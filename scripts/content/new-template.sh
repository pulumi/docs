#!/bin/bash

set -o errexit -o pipefail

type=""
template=""
content_dir="content"

prompt_for_template_type() {
    read -p "Template type (e.g., static-website): " type

    if [[ ! -z "$type" && -d "${content_dir}/templates/${type}" ]]; then
        return
    fi

    create_template_type
}

create_template_type() {
    echo
    read -e -p "Template type '${type}' doesn't exist in '${content_dir}/templates'. Create it [y/n]? " choice

    if [[ "$choice" == [Yy]* ]]; then
        hugo new --kind templates/type --contentDir "${content_dir}" "templates/${type}"
        return
    fi

    echo "Ok, exiting."
    exit 0
}

prompt_for_template_name() {
    read -p "Template name (e.g., azure): " template

    if [ ! -z "$template" ]; then
        hugo new --kind templates/template --contentDir "${content_dir}" "templates/${type}/${template}"
        return
    fi

    echo "Please give the template a name."
    echo
    prompt_for_template_name
}

echo "So, you want to make a new Pulumi template? Great! 🙌"
echo
echo "Step 1:"
echo "What type of template would you like to create?"
echo
prompt_for_template_type

echo
echo "Step 2:"
echo "Now give your new template a URL-friendly name. For example, to
create a new template under ${type} that'll live at
https://pulumi.com/templates/${type}/azure, type 'azure'."
echo
prompt_for_template_name && echo && echo "Done! You can now run 'make serve' to get started."
