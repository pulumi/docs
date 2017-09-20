#!/usr/bin/env python

import os
from os import path
import sys

def GetDTSFiles(root):
    """Returns all DTS files under a file path."""
    dts_files = []
    for root, dirs, files in os.walk(root):
        if "node_modules" in root:
            continue
        for file in files:
            if file.endswith(".d.ts"):
                full_path = path.join(root, file)
                dts_files.append(full_path)

    return dts_files

# Confirm we are running from the root of the "docs" repo. We assume that
# pulumi-fabric, pulumi-framework, and pulumi-aws are siblings of this folder.
cwd = os.getcwd()
if path.basename(cwd) != 'docs':
    print "cwd is not 'docs' folder. Bailing." % (cwd, os.path.dirname(cwd))
    sys.exit(1)

pulumi_repos = path.join(cwd, "..")



dts_files = []
dts_files.extend(GetDTSFiles(path.join(pulumi_repos, "pulumi-fabric")))
dts_files.extend(GetDTSFiles(path.join(pulumi_repos, "pulumi-framework")))
dts_files.extend(GetDTSFiles(path.join(pulumi_repos, "pulumi-aws")))

for file in dts_files:
    print file
