#!/bin/bash

set -o errexit -o pipefail

source ./scripts/common.sh

cloud=""
example_name=""
example_description=""
examples_dir="themes/default/static/programs"

prompt_for_cloud() {
    read -p "Cloud (e.g., aws): " cloud

    if [[ ! -z "$cloud" ]]; then
        return
    fi

    echo "Enter a cloud name that exists in pulumi/templates, like 'aws-native' or 'scaleway'."
    echo
    prompt_for_cloud
}

prompt_for_example_name() {
    read -p "Example name (e.g., awsx-api-gateway-rest-api): " example_name

    if [ ! -z "$example_name" ]; then
        return
    fi

    echo "Please give the example a name."
    prompt_for_example_name
}

prompt_for_example_description() {
    read -p "Example description (e.g., 'An example that deploys an API Gateway REST API on AWS.'): " example_description

    if [ ! -z "$example_description" ]; then
        return
    fi

    echo "Please give the example a description."
    prompt_for_example_description
}

generate_example() {
    languages=(javascript typescript python go csharp java yaml)
    echo

    for language in "${languages[@]}"; do
        example_dir="${examples_dir}/${example_name}-${language}"

        rm -rf "${example_dir}"
        mkdir -p "${example_dir}"

        pushd "$example_dir" > /dev/null
            echo "Creating ${example_dir} ..."
            pulumi new "${cloud}-${language}" --description="${example_description}" --yes --force --generate-only > /dev/null
            pulumi install > /dev/null
        popd > /dev/null
    done

    unsuffix_gomods
}

echo
echo "So, you want to make a new example program? Awesome! 🙌"
echo
echo "Step 1: Choose a cloud. Your example will be built from an existing Pulumi template,
so choose a cloud/provider that we have an existing <cloud>-<language> template for, like
'aws', 'azure', 'gcp', or 'digitalocean'."
echo
prompt_for_cloud

echo
echo "Step 2: Give the example a descriptive, Pulumi project-friendly name. This name will
be used for the project prefix. Try to choose a name that succinctly describes the content
of the example, rather than the specific page you're building it for, as this'll make the
example more easily findable and reusable."
echo
prompt_for_example_name

echo
echo "Step 3: Give the example a project description. This will be used for the description
field in Pulumi.yaml."
echo
prompt_for_example_description

generate_example
echo
echo "✨ Done! Your new projects are now available at ${examples_dir}/${example_name}. To
include them in any Markdown file (blog post, doc, whatever), use the '{{< example-program >}}'
shortcode thusly:

{{< example-program path=\"${example_name}\">}}

Enjoy!"
echo
