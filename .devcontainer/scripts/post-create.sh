#!/bin/bash
set -e

curl -fsSL https://get.pulumi.com | sh
echo 'export PATH=$HOME/.pulumi/bin:$PATH' >> ~/.bashrc
echo 'export PATH=$HOME/.pulumi/bin:$PATH' >> ~/.profile
export PATH=$HOME/.pulumi/bin:$PATH
pulumi version
