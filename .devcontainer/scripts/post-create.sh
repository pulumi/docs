#!/bin/bash
set -e

# Install gcloud CLI (official apt repo)
sudo apt-get update -y
sudo apt-get install -y apt-transport-https ca-certificates gnupg
echo "deb [signed-by=/usr/share/keyrings/cloud.google.gpg] https://packages.cloud.google.com/apt cloud-sdk main" \
  | sudo tee -a /etc/apt/sources.list.d/google-cloud-sdk.list
curl -fsSL https://packages.cloud.google.com/apt/doc/apt-key.gpg \
  | sudo gpg --dearmor -o /usr/share/keyrings/cloud.google.gpg
sudo apt-get update -y
sudo apt-get install -y google-cloud-cli

# Install TypeScript
npm install -g typescript

# Install Vale (required by scripts/ensure.sh for prose linting)
VALE_VERSION="3.14.1"
VALE_SHA256="ff2b49ffaa9dcd246fd5008f03ff67746d2790b75bf4d3657e2fb9530fb96db3"
curl -fsSL -o /tmp/vale.tar.gz "https://github.com/errata-ai/vale/releases/download/v${VALE_VERSION}/vale_${VALE_VERSION}_Linux_64-bit.tar.gz"
echo "${VALE_SHA256}  /tmp/vale.tar.gz" | sha256sum -c -
sudo tar -xz -C /usr/local/bin vale -f /tmp/vale.tar.gz
rm /tmp/vale.tar.gz

# Install Pulumi CLI
curl -fsSL https://get.pulumi.com | sh
echo 'export PATH=$HOME/.pulumi/bin:$PATH' >> ~/.bashrc
echo 'export PATH=$HOME/.pulumi/bin:$PATH' >> ~/.profile
export PATH=$HOME/.pulumi/bin:$PATH
pulumi version

