"""
(A) Pulumi Python documentation generator, at your service!

This module provides a mechanism for producing HTML documentation for Pulumi packages directly from their source, in a
format that is amenable for inclusion in the Pulumi Docs repo. It accomplishes this using a two-fold transformation:

    1. This script walks all providers that it intends to generate documentation and generates an input to Sphinx, the
       documentation generator. The output of this stage is a directory full of reStructuredText files (.rst) that
       Sphinx will interpret.
    2. The script invokes sphinx directly. Sphinx walks the packages that we intend to document and generates a lot of
       documentation for them. We use the "json" builder for Sphinx, which is a target that splats a large amount of
       HTML into a JSON document for each input RST file that we gave it.
    3. The script processes the JSON output of Sphinx and produces a series of folders and Markdown documents that our
       Hugo front-end is aware of and can render in a reasonable fashion in the context of our docs website.

This is a little crazy. I will understand if you hate me. However, this script is very effective at what it does, mostly
because Sphinx is an incredibly powerful tool that is well-suited for this purpose. The "correct" way to accomplish this
task is likely to create a custom Sphinx theme that outputs HTML directly in the format that our site expects, but this
is "hard" (read: time-consuming for the author).
"""

import glob
import importlib
import keyword
import json
from os import path, mkdir
import shutil
from subprocess import check_call
import sys
import tempfile
from typing import NamedTuple, List, Optional
from jinja2 import Environment, PackageLoader, select_autoescape


class Project(NamedTuple):
    """
    A Project is a collection of metadata about the current project that we'll feed to Sphinx.
    """
    name: str
    copyright: str
    author: str
    version: str
    release: str


class Provider(NamedTuple):
    """
    A provider is a tuple of "name" (a human-readable name) and "package_name" (the actual Python package name) and
    a name of the terraform provider this is derived from, in the case of providers generated using pulumi-terraform
    """
    name: str
    package_name: str
    pulumi_provider_name: str
    terraform_provider_name: Optional[str]


class Input(NamedTuple):
    """
    Input is the schema of the JSON document loaded as an input to the documentation generator. It contains metadata
    about the current project (see Project) and a list of providers that we intend to document.
    """
    project: Project
    providers: List[Provider]


class Context(NamedTuple):
    """
    The context is some state kept around during the transformation process.
    """
    template_env: Environment
    tempdir: str
    outdir: str
    mdoutdir: str
    input: Input


class CreateMarkdownInput(NamedTuple):
    """
    The CreateMarkdownInput is the input to create_markdown_file.
    """
    title: str
    title_tag: str
    linktitle: str
    """
    Sphinx output file, to be used as the source of data to derive a Markdown file. It is technically
           JSON but in reality it's a JSON object with a "body" property that's filled with HTML.
    """
    file: str
    """
    The output file to write the Markdown to.
    """
    out_file: str


def read_input(input_file: str) -> Input:
    """
    read_input produces an Input from an input file with the given filename.

    :param str input_file: Filename of a JSON file to read inputs from.
    :returns str: An Input representing the current run of the tool.
    """
    with open(input_file) as f:
        input_dict = json.load(f)
        project = Project(**input_dict["project"])
        providers = []
        for provider in input_dict.get("providers") or []:
            providers.append(Provider(**provider))
        return Input(project=project, providers=providers)


def render_template_to(ctx: Context, dest: str, template_name: str, **kwargs):
    """
    Helper function for rendering templates to the context's temporary directory.

    :param Context ctx: The current context.
    :param str dest: The destination path relative to the root of the output directory.
    :param str template_name: The name of the template to render.
    :param **kwargs: Passed verbatim to the template.
    """
    template_instance = ctx.template_env.get_template(template_name)
    out_path = path.join(ctx.tempdir, dest)
    with open(out_path, "w") as f:
        rendered = template_instance.render(**kwargs)
        f.write(rendered)


def generate_sphinx_files(ctx: Context):
    """
    Generates Sphinx input from the list of packages given to this tool. The Sphinx input is saved in the temporary
    directory created by the context (ctx.tempdir).
    """

    # Sphinx expects a conf.py file at the root of the folder - render it.
    render_template_to(ctx, "conf.py", "conf.py", input=ctx.input)

    # We're also shipping a Sphinx plugin to hack our docstrings.
    render_template_to(ctx, "markdown_docstring.py", "markdown_docstring.py")

    # Sphinx begins at index.rst and walks it recursively to discover all files to render. Although we're not using the
    # output of index.rst in any way, we must still render it to refer to all of the provider pages that we intend to
    # document so that Sphinx knows to recurse into them.
    render_template_to(ctx, "index.rst", "index.rst", input=ctx.input)
    create_dir(ctx.tempdir, "providers")
    create_dir(ctx.tempdir, "_static")  # Sphinx complains if this isn't there.

    # Render pulumi.rst - it's special since it's not really a provider.
    pulumi_doc_path = path.join("providers", "pulumi.rst")
    render_template_to(ctx, pulumi_doc_path, pulumi_doc_path)

    # Render all providers that we've been asked to render.
    for provider in ctx.input.providers:
        generate_module(ctx, provider, "", "providers",
                        use_provider_metadata=True)


def generate_module(ctx, provider, import_path, output_path, use_provider_metadata=False):
    """
    Generates Sphinx input for a particular module that is a member of the given provider. This function recursively
    walks the module tree of a given import path and produces reStructuredText files that will ultimately be given to
    Sphinx.

    :param Context ctx: The current context.
    :param Provider provider: The provider that we are generating.
    :param str import_path: The import path for the module that we intend to generate documentation for. If it's the
           empty string, this module is treated as the root module.
    :param str output_path: The root of the output directory that this function will write RST files into.
    :param bool use_provider_metadata: If true, uses the provider's metadata for the title of a page instead of the
           raw name of the module. Useful for presenting human-readable titles for top-level packages.
    """
    # Some templates we're going to be using.
    without_module_template = path.join(
        "providers", "provider_without_module.rst")
    with_module_template = path.join("providers", "provider_with_module.rst")

    # Try to import the module. It might fail; this is always a bug in tfgen. Since there are a few outstanding bugs
    # in tfgen, ignore the failed imports for now and emit a warning.
    try:
        module = importlib.import_module(
            import_path or ".", package=provider.package_name)
    except ModuleNotFoundError:
        print(
            f"warning: skipping {provider.package_name}{import_path}, failed to import")
        return

    # Construct the "metadata" for this module. This metadata bag is passed verbatim to the template engine.
    module_name = module.__name__.split(".").pop()
    if use_provider_metadata:
        meta = {
            "name": provider.name, "package_name": provider.package_name, "directory_name": provider.package_name,
            "pulumi_provider_name": provider.pulumi_provider_name, "terraform_provider_name": provider.terraform_provider_name,
        }
    else:
        meta = {
            "name": module_name, "package_name": module.__name__, "directory_name": module_name,
            "pulumi_provider_name": provider.pulumi_provider_name, "terraform_provider_name": provider.terraform_provider_name
        }

    # If this module doesn't have any submodules, we're going to generate all of the type documentation in a single file
    # and not proceed any further.
    if not should_generate_multimodule(module):
        render_template_to(ctx, path.join(
            output_path, f"{module_name}.rst"), without_module_template, provider=meta)
        print(
            f"{provider.package_name + import_path: <50} -> {output_path}/{module_name}.rst")
        return

    # If there are submodules, run through each one and render module templates for each one.
    all_modules = getattr(module, "__all__")
    # Skip the "config" submodule - it can't be imported.
    all_modules = list(filter(lambda mod: mod != "config", all_modules))
    print(f"{provider.package_name + import_path: <50} -> {output_path}/{module_name}.rst")
    render_template_to(ctx, path.join(
        output_path, f"{module_name}.rst"), with_module_template, provider=meta, submodules=all_modules)
    for mod in all_modules:
        # If a module is a keyword, we won't be able to import it. Append a _ at the end of it. This is again almost
        # always a bug in tfgen if a package contains a module that can't be legally imported without hacks.
        if keyword.iskeyword(mod):
            mod += "_"

        # Recursively render all submodules of this module.
        create_dir(ctx.tempdir, output_path, module_name)
        generate_module(ctx, provider, import_path + "." + mod,
                        path.join(output_path, module_name))


def should_generate_multimodule(module):
    """
    Returns whether or not we should generate a multi-page page tree for this particular module or if we should fit
    everything on a single page.

    :param Any module: A module object to inspect.
    :return True if we should generate a multi-page page tree for this module.
    :rtype bool
    """
    if not hasattr(module, "__all__"):
        return False

    # Even if this module does define __all__, if its only submodule is config, treat it as a single-page module.
    # Config is not a "real" submodule - Sphinx can't import it and there are no docs to generate for it.
    all_modules = getattr(module, "__all__")
    return all_modules != ["config"]


def build_sphinx(ctx: Context):
    """
    build_sphinx invokes Sphinx on the inputs that we generated in `generate_sphinx_files`.

    :param Context ctx: The current context.
    """
    check_call(["sphinx-build", "-j", "auto", "-b",
                "json", ctx.tempdir, ctx.outdir])


def transform_sphinx_output_to_markdown(ctx: Context):
    """
    Transforms the Sphinx output in `ctx.outdir` to markdown by post-processing the JSON output by Sphinx. The directory
    structure written by this function mirrors the `reference/pkg` directory in the docs repo, so that `reference/pkg`
    can serve as an output directory of this script.

    :param Context ctx: The current context.
    """
    out_base = create_dir(ctx.mdoutdir, "python")
    base_json = path.join(ctx.outdir, "providers")
    pulumi_pkg = Provider(name="Pulumi SDK", package_name="pulumi",
                          pulumi_provider_name="pulumi", terraform_provider_name="")
    for provider in ctx.input.providers + [pulumi_pkg]:
        provider_path = create_dir(out_base, provider.package_name)
        provider_sphinx_output = path.join(base_json, provider.package_name)
        # If this thing has submodules, provider_sphinx_output is a directory and it exists.
        if path.exists(provider_sphinx_output):
            create_markdown_input = CreateMarkdownInput(title=f"Package {provider.package_name}",
                                                        title_tag=f"Package {provider.package_name}",
                                                        linktitle=provider.package_name,
                                                        file=f"{provider_sphinx_output}.fjson",
                                                        out_file=path.join(provider_path, "_index.md"))
            create_markdown_file(create_markdown_input)
            # Recurse through all submodules (all fjson files in this directory) and produce folders with an _index.md
            # in them.
            for file in glob.iglob(path.join(provider_sphinx_output, "**/*.fjson"), recursive=True):
                rel_file = path.relpath(file, start=provider_sphinx_output)
                directory, filename = path.split(rel_file)
                module_name = path.splitext(path.basename(filename))[0]
                # If this globbed file is in a subdirectory of provider_sphinx_output, be sure to preserve the directory
                # in the output directory as well.
                if directory:
                    module_path = create_dir(
                        provider_path, directory, module_name)
                else:
                    module_path = create_dir(provider_path, module_name)

                create_markdown_input = CreateMarkdownInput(title=f"Module {module_name}",
                                                            title_tag=f"Module {module_name} | Package {provider.package_name}",
                                                            linktitle=module_name,
                                                            file=file,
                                                            out_file=path.join(module_path, "_index.md"))
                create_markdown_file(create_markdown_input)
        else:
            create_markdown_input = CreateMarkdownInput(title=f"Package {provider.package_name}",
                                                        title_tag=f"Package {provider.package_name}",
                                                        linktitle=provider.package_name,
                                                        file=f"{provider_sphinx_output}.fjson",
                                                        out_file=path.join(provider_path, "_index.md"))
            # Otherwise, just drop an _index.md in the provider directory.
            create_markdown_file(create_markdown_input)


def create_dir(*args):
    full_path = path.join(*args)
    if not path.exists(full_path):
        mkdir(full_path)

    return full_path


def create_markdown_file(input: CreateMarkdownInput):
    """
    Derives a Markdown file from the Sphinx output file `file` and saves the result to `out_file`.

    :param CreateMarkdownInput input: The input containing the source file and the output file names.
    """
    with open(input.file) as f:
        contents = json.load(f)

    with open(input.out_file, "w") as f:
        # First, write some empty front-matter at the beginning of the file.
        f.write("---\n")
        f.write(f"title: {input.title}\n")
        f.write(f"title_tag: {input.title_tag}\n")
        f.write(f"linktitle: {input.linktitle}\n")
        f.write(f"notitle: true\n")
        f.write("---\n\n")
        # The "body" property of Sphinx's JSON is basically the rendered HTML of the documentation on this page. We're
        # going to slam it verbatim into a file and call it Markdown, because we're professionals.
        f.write(contents["body"])


def main():
    if len(sys.argv) != 2:
        print("usage: python -m pydocgen <output_dir>")
        exit(1)

    output_directory = sys.argv[1]
    input = read_input("pulumi-docs.json")
    env = Environment(
        loader=PackageLoader('pydocgen', 'templates'),
        autoescape=select_autoescape(['html', 'xml']))

    tempdir = tempfile.mkdtemp()
    outdir = tempfile.mkdtemp()
    mdoutdir = output_directory
    ctx = Context(template_env=env,  input=input,
                  tempdir=tempdir, outdir=outdir, mdoutdir=mdoutdir)

    try:
        print("Generating Sphinx input...")
        generate_sphinx_files(ctx)
        print("Running Sphinx...")
        build_sphinx(ctx)
        print("Transforming Sphinx output into Markdown...")
        transform_sphinx_output_to_markdown(ctx)
        print("Done!")
    finally:
        if path.exists(tempdir):
            shutil.rmtree(tempdir)
        if path.exists(outdir):
            shutil.rmtree(outdir)
