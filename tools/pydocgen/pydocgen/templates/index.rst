.. toctree::
    {% for provider in input.providers %}
    providers/{{provider.package_name}}
    {% endfor %}
