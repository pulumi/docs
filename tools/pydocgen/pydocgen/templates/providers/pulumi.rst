Pulumi Python SDK
=================

The Pulumi Python SDK (`pulumi`) is the core package used when writing Pulumi programs in Python. It contains everything
that you'll need in order to interact with Pulumi resource providers and express infrastructure using Python code.
Pulumi resource providers all depend on this library and express their resources in terms of the types defined in this
module.

.. epigraph::

  **Note**: The Pulumi Python SDK requires Python version 3.6 or greater. Please see the
  `Python getting started </docs/reference/python/#getting-started>`_ documentation for details on how to get started with
  Python.

The Pulumi Python Resource Model
--------------------------------

Like most languages usable with Pulumi, Pulumi represents cloud resources as classes and Python programs can instantiate
those classes. All classes that can be instantiated to produce actual resources derive from the `pulumi.Resource` class.

A class that derives from `pulumi.Resource` will, when instantiated, communicate with the Pulumi Engine and record that
a piece of infrastructure that the instantiated class represents should be provisioned. All resources whose provisioning
is implemented in a resource provider derive from the `pulumi.CustomResource` class.

It is also possible to write your own resources, written in Python, that are themselves composed of custom resources.
Resources written in Python are called "component resources" and they are written by deriving from the
`pulumi.ComponentResource` class.

Finally, Pulumi allows for resource providers to directly project themselves into Python, so that provider instances
can be instantiated and used to create other resources. These "provider resources" derive from the
`pulumi.ProviderResource` class.

.. autoclass:: pulumi.Resource
    :members:

.. autoclass:: pulumi.CustomResource
    :members:

.. autoclass:: pulumi.ComponentResource
    :members:

.. autoclass:: pulumi.ProviderResource
    :members:

.. autoclass:: pulumi.ResourceOptions
    :members:

.. autoclass:: pulumi.InvokeOptions
    :members:

.. autoexception:: pulumi.RunError
    :members:

Configuration and Metadata
--------------------------

Pulumi programs can receive configuration that is specified by the command-line using `pulumi config`. This
configuration information can be retrieved at runtime using the `pulumi.Config` class:

.. code:: python

    import pulumi
    # After running `pulumi config set myconfig 42`

    conf = pulumi.Config()
    print(conf.get_int("myconfig")) # prints 42

Pulumi programs also have the ability to query the current project and stack, as well as whether or not the current run
of the program is a preview or not.

.. autoclass:: pulumi.Config
    :members:

.. autoexception:: pulumi.ConfigMissingError
    :members:

.. autoexception:: pulumi.ConfigTypeError
    :members:

.. autofunction:: pulumi.get_project

.. autofunction:: pulumi.get_stack

.. autofunction:: pulumi.runtime.is_dry_run

Outputs and Inputs
------------------

Like other languages in the Pulumi ecosystem, all Resources in Python have two kinds of properties: *inputs* and
*outputs*. Inputs are specified as arguments to resource constructors, to be used as inputs to the resource itself.
Outputs are *returned* as properties on the instantiated resource object. Outputs are similar to futures in that they
are resolved asynchronously, but they also contain information about the dependency graph of resources within your
program.

Pulumi does not offer direct access to the values contained within Outputs. Instead, you must use the `apply` function
on the Output class in order to observe the value of an output. See
`the documentation </docs/intro/concepts/programming-model/#outputs>`_ for more details on this part of the Pulumi programming model.

.. autoclass:: pulumi.Output
    :members:

    .. automethod:: __getitem__

    .. automethod:: __getattr__

Logging
-------

The Pulumi SDK contains a few helper functions for logging to the console. Messages logged using these functions are
sent directly to the Pulumi Engine and rendered with the rest of the CLI output.

.. autofunction:: pulumi.debug

.. autofunction:: pulumi.info

.. autofunction:: pulumi.warn

.. autofunction:: pulumi.error

Stack Exports
-------------

Python programs can export values. Exported values are attached to the program's Stack resource and accessed using the
`pulumi stack output` CLI command:

.. code:: python

    import pulumi

    pulumi.export("the-answer", 42)

    # pulumi stack export:
    # Current stack outputs (1):
    # OUTPUT      VALUE
    # the-answer  42

.. autofunction:: pulumi.export

Automation API
--------------

.. automodule:: pulumi.x.automation

.. autofunction:: pulumi.x.automation.create_stack

.. autofunction:: pulumi.x.automation.select_stack

.. autofunction:: pulumi.x.automation.create_or_select_stack

.. autoclass:: pulumi.x.automation.LocalWorkspace
    :members:

.. autoclass:: pulumi.x.automation.Stack
    :members:

.. autoclass:: pulumi.x.automation.LocalWorkspaceOptions

.. autoclass:: pulumi.x.automation.ProjectSettings

.. autoclass:: pulumi.x.automation.StackSettings

.. autoclass:: pulumi.x.automation.ConfigValue
