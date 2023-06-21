---
title: "Programming Model"
url: /docs/intro/concepts/programming-model
block_external_search_index: true
---

<script>
    // The following list maps the headings that previously appeared on this page to their new locations.
    // We use this list to determine whether we can redirect visitors from the old content to the new.
    var redirects = {
        "#additionalsecretoutputs": "/docs/concepts/resources/#additionalsecretoutputs",
        "#aliases": "/docs/concepts/resources/#aliases",
        "#all": "/docs/concepts/inputs-outputs/#all",
        "#apply": "/docs/concepts/inputs-outputs/#apply",
        "#assets-and-archives": "/docs/concepts/inputs-outputs/assets-archives/",
        "#autonaming": "/docs/concepts/resources/#autonaming",
        "#components": "/docs/concepts/resources/#components",
        "#config": "/docs/concepts/config",
        "#custom-resources": "/docs/concepts/resources/#custom-resources",
        "#declaring-infrastructure": "/docs/concepts/#overview",
        "#deletebeforereplace": "/docs/concepts/resources/#deletebeforereplace",
        "#dependson": "/docs/concepts/resources/#dependson",
        "#dynamicproviders": "/docs/concepts/resources/#dynamicproviders",
        "#explicit-provider-configuration": "/docs/concepts/resources/#explicit-provider-configuration",
        "#import": "/docs/concepts/resources/#import",
        "#introduction": "/docs/intro/concepts",
        "#lifting": "/docs/concepts/inputs-outputs/#lifting",
        "#names": "/docs/concepts/resources/#names",
        "#outputs": "/docs/concepts/inputs-outputs",
        "#outputs-and-strings": "/docs/concepts/inputs-outputs/#outputs-and-strings",
        "#program-structure": "/docs/concepts/#overview",
        "#programs": "/docs/concepts/#overview",
        "#providers": "/docs/concepts/resources/#providers",
        "#reading-configuration-values": "/docs/concepts/config/#code",
        "#resource-get": "/docs/concepts/resources/#resource-get",
        "#resource-providers": "/docs/concepts/resources/#providers",
        "#resourceoptions": "/docs/concepts/resources/#options",
        "#resources": "/docs/concepts/resources",
        "#runtime": "/docs/concepts/",
        "#runtime-functions": "/docs/concepts/",
        "#secrets": "/docs/concepts/secrets",
        "#stack-outputs": "/docs/concepts/stack/#outputs",
        "#stack-references": "/docs/concepts/stack/#stack-references",
        "#transformations": "/docs/concepts/resources/#transformations",
    };

    var redirect = redirects[location.hash];
    if (redirect) {
        location.href = redirect;
    }
</script>

<!--
    Including a fallback redirect lets search engines know the content has moved, and
    waiting a few seconds before redirecting gives the script a chance to locate
    a matching anchor.
-->
<meta http-equiv="refresh" content="4; url=/docs/concepts">

This content has moved. Redirecting to [Pulumi Concepts](/docs/concepts)....
