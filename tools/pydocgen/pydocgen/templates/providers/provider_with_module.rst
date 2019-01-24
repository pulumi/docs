{{ provider.name }}
===================

.. toctree::
    {% for module in submodules %}
    {{provider.package_name}}/{{module}}{% endfor %}
