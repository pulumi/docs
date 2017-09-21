#!/usr/bin/env python

import os
from os import path
import shutil
import sys

def GetDTSFiles(root):
    """Returns all DTS files under a file path."""
    dts_files = []
    for root, dirs, files in os.walk(root):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith("index.d.ts"):
                continue
            if file.endswith(".d.ts"):
                full_path = path.join(root, file)
                dts_files.append(full_path)

    return dts_files

def GenerateReferenceDocs(repo_folder, output_folder):
    """Scans a source repo for .d.ts files and generates a Jekyll compatible
    documentation file from it."""
    repo_name = path.basename(path.normpath(repo_folder))

    if not path.exists(repo_folder):
        print "ERROR: Path %s did not exist." % repo_folder
        return
    os.makedirs(output_folder)

    # Emit a placeholder for the repo.
    dest_root_index = path.join(output_folder, "index.html")
    content = """---
layout: typescript-repo
repo: %s
---
""" % (repo_name)
    with open(dest_root_index, 'w') as new:
        new.write(content)

    dts_files = GetDTSFiles(repo_folder)
    print "%s: Found %d .d.ts files." % (repo_name, len(dts_files))
    for file in dts_files:
        # Strip out everything before "/bin/" in the file path.
        # TODO(chris): Is this something we can rely on?
        i = file.find("/bin/")
        if i == -1:
            print "WARNING: Not sure what to do about %s" % file
            continue
        sub_path = file[i + len("/bin/"):]

        dest_file = path.join(output_folder, sub_path)
        dest_file_folder = path.dirname(dest_file)
        if not path.exists(dest_file_folder):
            os.makedirs(dest_file_folder)

        # Copy the source file's contents, but we add our own preamble
        # with Jekyll frontmatter.
        preamble = """---
layout: typescript-reference
repo: %s
subpath: %s
---
""" % (repo_name, sub_path)
        with open(dest_file, 'w') as new:
            new.write(preamble)
            with open(file) as old:
                new.write(old.read())
        

if __name__ == '__main__':
    # Confirm we are running from the root of the "docs" repo. We assume that
    # pulumi-fabric, pulumi-framework, and pulumi-aws are siblings of this folder.
    repos_root = path.join(os.getcwd(), "..")
    repos_root = path.abspath(repos_root)

    output_dir = path.join(os.getcwd(), "_typescript_docs")

    if path.exists(output_dir):
        print "Deleting previous output in %s..." % (output_dir)
        shutil.rmtree(output_dir)

    GenerateReferenceDocs(
        path.join(repos_root, "pulumi-aws"),
        path.join(output_dir, "pulumi-aws"))
    GenerateReferenceDocs(
        path.join(repos_root, "pulumi-fabric"),
        path.join(output_dir, "pulumi-fabric"))
    GenerateReferenceDocs(
        path.join(repos_root, "pulumi-framework"),
        path.join(output_dir, "pulumi-framework"))

    print "Complete"