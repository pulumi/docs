.. toctree::
    providers/pulumi
    {% for provider in input.providers %}
    providers/{{provider.package_name}}
    {% endfor %}
