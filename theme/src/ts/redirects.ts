const path = document.location.pathname;

if (path === "/docs/intro/concepts/programming-model/" || path === "/docs/reference/programming-model/") {

    // The following list maps the headings that previously appeared on these pages to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    let redirects = {
        "#additionalsecretoutputs": "/docs/iac/concepts/resources/options/additionalsecretoutputs/",
        "#aliases": "/docs/iac/concepts/resources/options/aliases/",
        "#all": "/docs/iac/concepts/inputs-outputs/all/",
        "#apply": "/docs/iac/concepts/inputs-outputs/apply/",
        "#assets-and-archives": "/docs/iac/concepts/assets-archives/",
        "#autonaming": "/docs/iac/concepts/resources/names/#autonaming",
        "#components": "/docs/iac/concepts/components/",
        "#config": "/docs/iac/concepts/config/",
        "#custom-resources": "/docs/iac/concepts/resources/",
        "#declaring-infrastructure": "/docs/iac/concepts/",
        "#deletebeforereplace": "/docs/iac/concepts/resources/options/deletebeforereplace/",
        "#dependson": "/docs/iac/concepts/resources/options/dependson/",
        "#dynamicproviders": "/docs/iac/concepts/providers/dynamic-providers/",
        "#explicit-provider-configuration": "/docs/iac/concepts/providers/#explicit-provider-configuration",
        "#import": "/docs/iac/concepts/resources/options/import/",
        "#introduction": "/docs/iac/concepts/",
        "#lifting": "/docs/iac/concepts/inputs-outputs/apply/#using-lifting-to-simplify-nested-access",
        "#names": "/docs/iac/concepts/resources/names/",
        "#outputs": "/docs/iac/concepts/inputs-outputs/",
        "#outputs-and-strings": "/docs/iac/concepts/inputs-outputs/all/",
        "#program-structure": "/docs/iac/concepts/",
        "#programs": "/docs/iac/concepts/",
        "#providers": "/docs/iac/concepts/providers/",
        "#reading-configuration-values": "/docs/iac/concepts/config/#code",
        "#resource-get": "/docs/iac/concepts/functions/get-functions/",
        "#resource-providers": "/docs/iac/concepts/providers/",
        "#resourceoptions": "/docs/iac/concepts/resources/options/",
        "#resources": "/docs/iac/concepts/resources/",
        "#runtime": "/docs/iac/concepts/",
        "#runtime-functions": "/docs/iac/concepts/",
        "#secrets": "/docs/iac/concepts/secrets/",
        "#stack-outputs": "/docs/iac/concepts/stacks/#outputs",
        "#stack-references": "/docs/iac/concepts/stacks/#stackreferences",
        "#transformations": "/docs/iac/concepts/resources/options/transformations/",
    };

    var redirect = redirects[location.hash];
    if (redirect) {
        location.href = redirect;
    }
}
