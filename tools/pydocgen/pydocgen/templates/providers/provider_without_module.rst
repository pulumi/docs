{{ provider.name }}
====================================
{% if provider.terraform_provider_name is ne "" %}
    This provider is a derived work of the `Terraform Provider 
    <https://github.com/terraform-providers/terraform-provider-{{provider.terraform_provider_name}}>`__ distributed under
    `MPL 2.0 <https://www.mozilla.org/en-US/MPL/2.0/>`__. If you encounter a bug or missing feature, first check the 
    `pulumi/pulumi-{{provider.terraform_provider_name}} repo 
    <https://github.com/pulumi/pulumi-{{provider.terraform_provider_name}}/issues>`__; however, if that doesn't turn up 
    anything, please consult the source `terraform-providers/terraform-provider-{{provider.terraform_provider_name}} repo
    <https://github.com/terraform-providers/terraform-provider-{{provider.terraform_provider_name}}/issues>`__.
{% endif %}

.. automodule:: {{ provider.package_name }}
    :ignore-module-all:
    :members:
    :imported-members:
