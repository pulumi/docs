---
title: "Deploy Clawdbot to AWS and Hetzner with Pulumi"
date: 2026-01-26
meta_desc: "Deploy Clawdbot, an open-source AI assistant, to AWS and Hetzner using Pulumi with Tailscale for secure private access."
meta_image: meta.png
authors:
    - engin-diri
tags:
    - aws
    - hetzner
    - ai
    - hetzner-cloud
    - clawdbot
    - pulumi-esc
    - typescript
    - tailscale
    - security
social:
    twitter: |
        Everyone's buying Mac Minis to run Clawdbot. Here's the thing: you don't need one. A Hetzner VM costs $7/month and a single pulumi up gets you there. Plus Tailscale so your AI assistant isn't hanging out on Shodan.
    linkedin: |
        The Clawdbot craze has people buying Mac Minis just to run an AI assistant. But you can deploy it to AWS or Hetzner for a fraction of the cost.

        I wrote up how to do it with Pulumi - one command to deploy, one command to tear down. The post also covers securing it with Tailscale, because a lot of Clawdbot instances are showing up on Shodan with zero auth.
---

Clawdbot is taking the tech world by storm. The open-source AI assistant [gained 9,000 GitHub stars in a single day](https://news.aibase.com/news/24901), received public praise from former Tesla AI head Andrej Karpathy, and has sparked a global run on Mac Minis as developers scramble to give this "lobster assistant" a home. Users are calling it "Jarvis living in a hard drive" and "Claude with hands"—the personal AI assistant that Siri promised but never delivered.

The Mac Mini craze is real: [people are buying dedicated hardware just to run Clawdbot](https://medium.com/@orami98/why-ai-enthusiasts-are-racing-to-buy-mac-minis-inside-the-clawdbot-phenomenon-16263ae0aa0a), with some enthusiasts [purchasing 40 Mac Minis at once](https://eu.36kr.com/en/p/3655411080568966). Even Logan Kilpatrick from Google DeepMind couldn't resist ordering one. But here's the thing: [you don't actually need a Mac Mini](https://dev.to/sivarampg/you-dont-need-a-mac-mini-to-run-clawdbot-heres-how-to-run-it-anywhere-217l). Clawdbot runs anywhere—on a VPS, in the cloud, or on that old laptop gathering dust.

With all this hype, I had to try it myself. But instead of clicking through the AWS console or running manual commands on a VPS, I wanted to do it right from the start: infrastructure as code with Pulumi. Why? Because when I inevitably want to tear it down, spin up a new instance, or deploy to a different region, I don't want to remember which buttons I clicked three weeks ago. I want a single `pulumi up` command.

[Dan](https://x.com/d4m1n/status/2015335493886493056) got the assignment right:

![Dan's tweet suggesting Hetzner VMs instead of Mac Minis for Clawdbot](dan-hetzner-tweet.png)

In this post, I'll show you how I deployed [Clawdbot](https://clawd.bot/) to both AWS and Hetzner Cloud using Pulumi—and how to secure it with Tailscale so your AI assistant isn't exposed to the public internet.

<!--more-->

## What is Clawdbot?

Clawdbot is an open-source AI assistant created by [Peter Steinberger](https://x.com/steipete) that runs on your own infrastructure. It connects to WhatsApp, Slack, Discord, Google Chat, Signal, and iMessage. It can control browsers, generate videos and images, clone your voice for voice notes, and run scheduled tasks via cron. There's a skills system for extending functionality, and you can run it on pretty much anything: Mac Mini, Raspberry Pi, VPS, laptop, or gaming PC.

The difference from cloud-hosted AI? Clawdbot runs on your server, not Anthropic's. It's available 24/7 across all your devices, can schedule automated tasks, and keeps your entire conversation history locally.

## Prerequisites

Before getting started, ensure you have:

- [Pulumi CLI](/docs/iac/download-install/) installed and configured
- A [Pulumi Cloud account](https://app.pulumi.com/signup)
- AWS account (for AWS deployment)
- Hetzner Cloud account (for European deployment)
- Anthropic API key
- Node.js 18+ installed
- Tailscale account with [HTTPS enabled](https://tailscale.com/kb/1153/enabling-https) (one-time setup in admin console)

{{% notes type="info" %}}
This guide uses Anthropic's API, but Clawdbot works with other providers too. Check the [providers documentation](https://docs.clawd.bot/providers) if you'd rather use OpenAI, Google Gemini, or a local model via Ollama.
{{% /notes %}}

## Understanding Clawdbot architecture

Clawdbot uses a gateway-centric architecture where a single daemon acts as the control plane for all messaging, tool execution, and client connections:

| Component | Port | Description |
|-----------|------|-------------|
| Gateway | 18789 | WebSocket server handling channels, nodes, sessions, and hooks |
| Browser control | 18791 | Headless Chrome instance for web automation |
| Docker sandbox | - | Isolated container environment for running tools safely |

The Gateway connects to messaging platforms (WhatsApp, Slack, Discord, etc.), the CLI, the web UI, and mobile apps. The Browser component lets Clawdbot open web pages, fill forms, scrape data, and download files. Docker sandboxing runs bash commands in isolated containers so your bot can execute code without risking your host system.

## Setting up ESC for secrets management

Before deploying, let's configure [Pulumi ESC (Environments, Secrets, and Configuration)](/docs/esc/) to securely manage our credentials. Create a new ESC environment:

```bash
pulumi env init <your-org>/clawdbot-secrets
```

Add your secrets to the environment:

```yaml
values:
  anthropicApiKey:
    fn::secret: "sk-ant-xxxxx"
  tailscaleAuthKey:
    fn::secret: "tskey-auth-xxxxx"
  tailnetDnsName: "tailxxxxx.ts.net"
  hcloudToken:
    fn::secret: "your-hetzner-api-token"
  pulumiConfig:
    anthropicApiKey: ${anthropicApiKey}
    tailscaleAuthKey: ${tailscaleAuthKey}
    tailnetDnsName: ${tailnetDnsName}
    hcloud:token: ${hcloudToken}
```

{{% notes type="info" %}}
To find your Tailnet DNS name, go to the [Tailscale admin console](https://login.tailscale.com/admin/dns), look under the **DNS** section, and find your tailnet name (e.g., `tailxxxxx.ts.net`). This is the domain suffix used for all machines in your Tailscale network.
{{% /notes %}}

Then create a `Pulumi.dev.yaml` file in your project to reference the environment:

```yaml
environment:
  - <your-org>/clawdbot-secrets
```

This approach keeps your secrets out of your codebase and passes them directly to Clawdbot during automated onboarding.

## Securing with Tailscale

By default, deploying Clawdbot exposes SSH (port 22), the gateway (port 18789), and browser control (port 18791) to the public internet. This is convenient for testing but not ideal for production use.

[Tailscale](https://tailscale.com/) creates a secure mesh VPN that lets you access your Clawdbot instance without exposing unnecessary ports publicly. When you provide a Tailscale auth key, the Pulumi program:

1. **Removes gateway and browser ports** from public access
1. **Keeps SSH as fallback** for debugging if Tailscale setup fails
1. **Installs Tailscale** on the instance during provisioning (after other dependencies)
1. **Enables Tailscale SSH** so you can SSH via Tailscale without managing keys
1. **Joins your Tailnet** automatically using the auth key

{{% notes type="info" %}}
The Pulumi program installs Docker, Node.js, and Clawdbot first, then configures Tailscale last. This ensures that even if the Tailscale auth key is invalid or expired, you can still SSH in via the public IP to troubleshoot.
{{% /notes %}}

To generate a Tailscale auth key:

1. Go to [Tailscale Admin Console](https://login.tailscale.com/admin/settings/keys)
1. Click "Generate auth key"
1. Enable "Reusable" if you plan to redeploy
1. Copy the key and add it to your ESC environment

## Deploying to AWS

Let's walk through the complete AWS deployment. Create a new Pulumi project:

```bash
mkdir clawdbot-aws && cd clawdbot-aws
pulumi new typescript
```

Install the required dependencies:

```bash
npm install @pulumi/aws @pulumi/tls
```

{{% notes type="warning" %}}
Do not use `t3.micro` instances for Clawdbot. The 1 GB memory is insufficient for installation. Use `t3.medium` (4 GB) or `t3.large` (8 GB) instead.
{{% /notes %}}

### The Pulumi program

Replace the contents of `index.ts` with the following:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as aws from "@pulumi/aws";
import * as tls from "@pulumi/tls";

const config = new pulumi.Config();

const instanceType = config.get("instanceType") ?? "t3.medium";
const anthropicApiKey = config.requireSecret("anthropicApiKey");
const model = config.get("model") ?? "anthropic/claude-sonnet-4";
const enableSandbox = config.getBoolean("enableSandbox") ?? true;
const gatewayPort = config.getNumber("gatewayPort") ?? 18789;
const browserPort = config.getNumber("browserPort") ?? 18791;

const tailscaleAuthKey = config.requireSecret("tailscaleAuthKey");
const tailnetDnsName = config.require("tailnetDnsName");

// Generate a random token for gateway authentication
const gatewayToken = new tls.PrivateKey("clawdbot-gateway-token", {
    algorithm: "ED25519",
}).publicKeyOpenssh.apply(key => {
    const hash = require("crypto").createHash("sha256").update(key).digest("hex");
    return hash.substring(0, 48);
});

const sshKey = new tls.PrivateKey("clawdbot-ssh-key", {
    algorithm: "ED25519",
});

const vpc = new aws.ec2.Vpc("clawdbot-vpc", {
    cidrBlock: "10.0.0.0/16",
    enableDnsHostnames: true,
    enableDnsSupport: true,
    tags: { Name: "clawdbot-vpc" },
});

const gateway = new aws.ec2.InternetGateway("clawdbot-igw", {
    vpcId: vpc.id,
    tags: { Name: "clawdbot-igw" },
});

const subnet = new aws.ec2.Subnet("clawdbot-subnet", {
    vpcId: vpc.id,
    cidrBlock: "10.0.1.0/24",
    mapPublicIpOnLaunch: true,
    tags: { Name: "clawdbot-subnet" },
});

const routeTable = new aws.ec2.RouteTable("clawdbot-rt", {
    vpcId: vpc.id,
    routes: [
        {
            cidrBlock: "0.0.0.0/0",
            gatewayId: gateway.id,
        },
    ],
    tags: { Name: "clawdbot-rt" },
});

new aws.ec2.RouteTableAssociation("clawdbot-rta", {
    subnetId: subnet.id,
    routeTableId: routeTable.id,
});

const securityGroup = new aws.ec2.SecurityGroup("clawdbot-sg", {
    vpcId: vpc.id,
    description: "Security group for Clawdbot instance",
    ingress: [
        {
            description: "SSH access (fallback)",
            fromPort: 22,
            toPort: 22,
            protocol: "tcp",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    egress: [
        {
            fromPort: 0,
            toPort: 0,
            protocol: "-1",
            cidrBlocks: ["0.0.0.0/0"],
        },
    ],
    tags: { Name: "clawdbot-sg" },
});

const keyPair = new aws.ec2.KeyPair("clawdbot-keypair", {
    publicKey: sshKey.publicKeyOpenssh,
});

const ami = aws.ec2.getAmiOutput({
    owners: ["099720109477"],
    mostRecent: true,
    filters: [
        { name: "name", values: ["ubuntu/images/hvm-ssd-gp3/ubuntu-noble-24.04-amd64-server-*"] },
        { name: "virtualization-type", values: ["hvm"] },
    ],
});

const userData = pulumi
    .all([tailscaleAuthKey, anthropicApiKey, gatewayToken])
    .apply(([tsAuthKey, apiKey, gwToken]) => {
        return `#!/bin/bash
set -e

export DEBIAN_FRONTEND=noninteractive

# System updates
apt-get update
apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh
systemctl enable docker
systemctl start docker
usermod -aG docker ubuntu

# Install NVM and Node.js for ubuntu user
sudo -u ubuntu bash << 'UBUNTU_SCRIPT'
set -e
cd ~

# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Load NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Install Node.js 22
nvm install 22
nvm use 22
nvm alias default 22

# Install Clawdbot
npm install -g clawdbot@latest

# Add NVM to bashrc if not already there
if ! grep -q 'NVM_DIR' ~/.bashrc; then
    echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
    echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> ~/.bashrc
fi
UBUNTU_SCRIPT

# Set environment variables for ubuntu user
echo 'export ANTHROPIC_API_KEY="${apiKey}"' >> /home/ubuntu/.bashrc

# Install and configure Tailscale
echo "Installing Tailscale..."
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --authkey="${tsAuthKey}" --ssh || echo "WARNING: Tailscale setup failed. Run 'sudo tailscale up' manually."

# Enable systemd linger for ubuntu user (required for user services to run at boot)
loginctl enable-linger ubuntu

# Start user's systemd instance (required for user services during cloud-init)
systemctl start user@1000.service

# Run Clawdbot onboarding as ubuntu user (skip daemon install, do it separately)
echo "Running Clawdbot onboarding..."
sudo -H -u ubuntu ANTHROPIC_API_KEY="${apiKey}" GATEWAY_PORT="${gatewayPort}" bash -c '
export HOME=/home/ubuntu
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

clawdbot onboard --non-interactive --accept-risk \
    --mode local \
    --auth-choice apiKey \
    --gateway-port $GATEWAY_PORT \
    --gateway-bind loopback \
    --skip-daemon \
    --skip-skills || echo "WARNING: Clawdbot onboarding failed. Run clawdbot onboard manually."
'

# Install daemon service with XDG_RUNTIME_DIR set
echo "Installing Clawdbot daemon..."
sudo -H -u ubuntu XDG_RUNTIME_DIR=/run/user/1000 bash -c '
export HOME=/home/ubuntu
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

clawdbot daemon install || echo "WARNING: Daemon install failed. Run clawdbot daemon install manually."
'

# Configure gateway for Tailscale Serve (trustedProxies + skip device pairing + set token)
echo "Configuring gateway for Tailscale Serve..."
sudo -H -u ubuntu GATEWAY_TOKEN="${gwToken}" python3 << 'PYTHON_SCRIPT'
import json
import os
config_path = "/home/ubuntu/.clawdbot/clawdbot.json"
with open(config_path) as f:
    config = json.load(f)
config["gateway"]["trustedProxies"] = ["127.0.0.1"]
config["gateway"]["controlUi"] = {
    "enabled": True,
    "allowInsecureAuth": True
}
config["gateway"]["auth"] = {
    "mode": "token",
    "token": os.environ["GATEWAY_TOKEN"]
}
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
print("Configured gateway with trustedProxies, controlUi, and token")
PYTHON_SCRIPT

# Enable Tailscale HTTPS proxy (requires HTTPS to be enabled in Tailscale admin console)
echo "Enabling Tailscale HTTPS proxy..."
tailscale serve --bg ${gatewayPort} || echo "WARNING: tailscale serve failed. Enable HTTPS in your Tailscale admin console first."

echo "Clawdbot setup complete!"
`;
    });

const instance = new aws.ec2.Instance("clawdbot-instance", {
    ami: ami.id,
    instanceType: instanceType,
    subnetId: subnet.id,
    vpcSecurityGroupIds: [securityGroup.id],
    keyName: keyPair.keyName,
    userData: userData,
    userDataReplaceOnChange: true,
    rootBlockDevice: {
        volumeSize: 30,
        volumeType: "gp3",
    },
    tags: { Name: "clawdbot" },
});

export const publicIp = instance.publicIp;
export const publicDns = instance.publicDns;
export const privateKey = sshKey.privateKeyOpenssh;

// Construct the Tailscale MagicDNS hostname from the private IP
// AWS private IPs like 10.0.1.15 become hostnames like ip-10-0-1-15
const tailscaleHostname = instance.privateIp.apply(ip =>
    `ip-${ip.replace(/\./g, "-")}`
);

export const tailscaleUrl = pulumi.interpolate`https://${tailscaleHostname}.${tailnetDnsName}/`;
export const tailscaleUrlWithToken = pulumi.interpolate`https://${tailscaleHostname}.${tailnetDnsName}/?token=${gatewayToken}`;
export const gatewayTokenOutput = gatewayToken;
```

## Deploying to Hetzner

Hetzner Cloud is a solid choice if you need European data residency or want to spend less money. Spoiler: it's a lot less money.

Create a new project for Hetzner:

```bash
mkdir clawdbot-hetzner && cd clawdbot-hetzner
pulumi new typescript
```

Install the Hetzner provider:

```bash
npm install @pulumi/hcloud @pulumi/tls
```

{{% notes type="info" %}}
The default server type `cax21` is an ARM-based (Ampere) instance with 4 vCPUs and 8 GB RAM. ARM instances offer excellent price-performance. If you need x86 architecture, use `ccx13` or similar CCX series instead.
{{% /notes %}}

### The Hetzner Pulumi program

Replace `index.ts` with the following:

```typescript
import * as pulumi from "@pulumi/pulumi";
import * as hcloud from "@pulumi/hcloud";
import * as tls from "@pulumi/tls";

const config = new pulumi.Config();

const serverType = config.get("serverType") ?? "cax21";
const location = config.get("location") ?? "fsn1";
const anthropicApiKey = config.requireSecret("anthropicApiKey");
const model = config.get("model") ?? "anthropic/claude-sonnet-4";
const enableSandbox = config.getBoolean("enableSandbox") ?? true;
const gatewayPort = config.getNumber("gatewayPort") ?? 18789;
const browserPort = config.getNumber("browserPort") ?? 18791;

const tailscaleAuthKey = config.requireSecret("tailscaleAuthKey");
const tailnetDnsName = config.require("tailnetDnsName");

// Generate a random token for gateway authentication
const gatewayToken = new tls.PrivateKey("clawdbot-gateway-token", {
    algorithm: "ED25519",
}).publicKeyOpenssh.apply(key => {
    const hash = require("crypto").createHash("sha256").update(key).digest("hex");
    return hash.substring(0, 48);
});

const sshKey = new tls.PrivateKey("clawdbot-ssh-key", {
    algorithm: "ED25519",
});

const hcloudSshKey = new hcloud.SshKey("clawdbot-sshkey", {
    publicKey: sshKey.publicKeyOpenssh,
});

const firewallRules: hcloud.types.input.FirewallRule[] = [
    {
        direction: "out",
        protocol: "tcp",
        port: "any",
        destinationIps: ["0.0.0.0/0", "::/0"],
        description: "Allow all outbound TCP",
    },
    {
        direction: "out",
        protocol: "udp",
        port: "any",
        destinationIps: ["0.0.0.0/0", "::/0"],
        description: "Allow all outbound UDP",
    },
    {
        direction: "out",
        protocol: "icmp",
        destinationIps: ["0.0.0.0/0", "::/0"],
        description: "Allow all outbound ICMP",
    },
    {
        direction: "in",
        protocol: "tcp",
        port: "22",
        sourceIps: ["0.0.0.0/0", "::/0"],
        description: "SSH access (fallback)",
    },
];

const firewall = new hcloud.Firewall("clawdbot-firewall", {
    rules: firewallRules,
});

const userData = pulumi
    .all([tailscaleAuthKey, anthropicApiKey, gatewayToken])
    .apply(([tsAuthKey, apiKey, gwToken]) => {
        return `#!/bin/bash
set -e

export DEBIAN_FRONTEND=noninteractive

# System updates
apt-get update
apt-get upgrade -y

# Install Docker
curl -fsSL https://get.docker.com | sh
systemctl enable docker
systemctl start docker

# Create ubuntu user (Hetzner uses root by default)
useradd -m -s /bin/bash -G docker ubuntu || true

# Install NVM and Node.js for ubuntu user
sudo -u ubuntu bash << 'UBUNTU_SCRIPT'
set -e
cd ~

# Install NVM
curl -o- https://raw.githubusercontent.com/nvm-sh/nvm/v0.40.1/install.sh | bash

# Load NVM
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

# Install Node.js 22
nvm install 22
nvm use 22
nvm alias default 22

# Install Clawdbot
npm install -g clawdbot@latest

# Add NVM to bashrc if not already there
if ! grep -q 'NVM_DIR' ~/.bashrc; then
    echo 'export NVM_DIR="$HOME/.nvm"' >> ~/.bashrc
    echo '[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"' >> ~/.bashrc
fi
UBUNTU_SCRIPT

# Set environment variables for ubuntu user
echo 'export ANTHROPIC_API_KEY="${apiKey}"' >> /home/ubuntu/.bashrc

# Install and configure Tailscale
echo "Installing Tailscale..."
curl -fsSL https://tailscale.com/install.sh | sh
tailscale up --authkey="${tsAuthKey}" --ssh || echo "WARNING: Tailscale setup failed. Run 'sudo tailscale up' manually."

# Enable systemd linger for ubuntu user (required for user services to run at boot)
loginctl enable-linger ubuntu

# Start user's systemd instance (required for user services during cloud-init)
systemctl start user@1000.service

# Run Clawdbot onboarding as ubuntu user (skip daemon install, do it separately)
echo "Running Clawdbot onboarding..."
sudo -H -u ubuntu ANTHROPIC_API_KEY="${apiKey}" GATEWAY_PORT="${gatewayPort}" bash -c '
export HOME=/home/ubuntu
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

clawdbot onboard --non-interactive --accept-risk \
    --mode local \
    --auth-choice apiKey \
    --gateway-port $GATEWAY_PORT \
    --gateway-bind loopback \
    --skip-daemon \
    --skip-skills || echo "WARNING: Clawdbot onboarding failed. Run clawdbot onboard manually."
'

# Install daemon service with XDG_RUNTIME_DIR set
echo "Installing Clawdbot daemon..."
sudo -H -u ubuntu XDG_RUNTIME_DIR=/run/user/1000 bash -c '
export HOME=/home/ubuntu
export NVM_DIR="$HOME/.nvm"
[ -s "$NVM_DIR/nvm.sh" ] && . "$NVM_DIR/nvm.sh"

clawdbot daemon install || echo "WARNING: Daemon install failed. Run clawdbot daemon install manually."
'

# Configure gateway for Tailscale Serve (trustedProxies + skip device pairing + set token)
echo "Configuring gateway for Tailscale Serve..."
sudo -H -u ubuntu GATEWAY_TOKEN="${gwToken}" python3 << 'PYTHON_SCRIPT'
import json
import os
config_path = "/home/ubuntu/.clawdbot/clawdbot.json"
with open(config_path) as f:
    config = json.load(f)
config["gateway"]["trustedProxies"] = ["127.0.0.1"]
config["gateway"]["controlUi"] = {
    "enabled": True,
    "allowInsecureAuth": True
}
config["gateway"]["auth"] = {
    "mode": "token",
    "token": os.environ["GATEWAY_TOKEN"]
}
with open(config_path, "w") as f:
    json.dump(config, f, indent=2)
print("Configured gateway with trustedProxies, controlUi, and token")
PYTHON_SCRIPT

# Enable Tailscale HTTPS proxy (requires HTTPS to be enabled in Tailscale admin console)
echo "Enabling Tailscale HTTPS proxy..."
tailscale serve --bg ${gatewayPort} || echo "WARNING: tailscale serve failed. Enable HTTPS in your Tailscale admin console first."

echo "Clawdbot setup complete!"
`;
    });

const server = new hcloud.Server("clawdbot-server", {
    serverType: serverType,
    location: location,
    image: "ubuntu-24.04",
    sshKeys: [hcloudSshKey.id],
    firewallIds: [firewall.id.apply(id => Number(id))],
    userData: userData,
    labels: {
        purpose: "clawdbot",
    },
});

export const ipv4Address = server.ipv4Address;
export const privateKey = sshKey.privateKeyOpenssh;

// Construct the Tailscale MagicDNS hostname from the server name
// Hetzner servers use their name as the hostname
const tailscaleHostname = server.name;

export const tailscaleUrl = pulumi.interpolate`https://${tailscaleHostname}.${tailnetDnsName}/`;
export const tailscaleUrlWithToken = pulumi.interpolate`https://${tailscaleHostname}.${tailnetDnsName}/?token=${gatewayToken}`;
export const gatewayTokenOutput = gatewayToken;
```

You can find both programs in the Pulumi examples repo under `clawd-code/`:

{{< github-card repo="pulumi/examples" >}}

## Cost comparison

Before deploying, let's compare the costs between AWS and Hetzner for running Clawdbot 24/7:

| | AWS (t3.medium) | Hetzner (cax21) |
|---|---|---|
| **vCPUs** | 2 | 4 |
| **Memory** | 4 GB | 8 GB |
| **Storage** | 30 GB gp3 (+$2.40/mo) | 80 GB NVMe (included) |
| **Traffic** | Pay per GB | 20 TB included |
| **Architecture** | x86 (Intel/AMD) | ARM (Ampere) |
| **Hourly price** | $0.0416 | €0.0104 (~$0.011) |
| **Monthly price** | ~$33 (with storage) | €6.49 (~$7) |
| **Annual cost** | ~$396 | ~$84 |

The numbers speak for themselves: Hetzner gives you double the vCPUs, double the RAM, at less than a quarter of the price. The trade-off? ARM architecture instead of x86. But Clawdbot doesn't care - it's just Node.js and Docker.

{{% notes type="info" %}}
Prices are for on-demand instances as of January 2026. AWS prices are for us-east-1; Hetzner prices exclude VAT. Both include standard networking and storage. Check [AWS EC2 pricing](https://aws.amazon.com/ec2/pricing/on-demand/) and [Hetzner Cloud pricing](https://www.hetzner.com/cloud/) for current rates.
{{% /notes %}}

## Running the deployment

With your ESC environment configured in `Pulumi.dev.yaml`, deploy with:

```bash
pulumi up
```

After deployment completes, you'll see outputs similar to:

```text
Outputs:
    gatewayTokenOutput   : "786c099cc8f8bf20dbebf40b8b51b75cf5cdab25..."
    privateKey           : [secret]
    publicDns            : "ec2-x-x-x-x.compute-1.amazonaws.com"
    publicIp             : "x.x.x.x"
    tailscaleUrl         : "https://ip-10-0-1-x.tailxxxxx.ts.net/"
    tailscaleUrlWithToken: "https://ip-10-0-1-x.tailxxxxx.ts.net/?token=786c099..."
```

The `tailscaleUrlWithToken` output provides the complete URL with authentication token—simply copy and paste it into your browser to access the Clawdbot web UI.

{{% notes type="info" %}}
Output names vary slightly between providers: AWS uses `publicIp` and `publicDns`, while Hetzner uses `ipv4Address`. The Tailscale hostname is derived from the instance's private IP (AWS) or server name (Hetzner).
{{% /notes %}}

## Automated onboarding

The Pulumi program runs Clawdbot's non-interactive onboarding during instance provisioning. It uses your Anthropic API key from ESC, binds the gateway to loopback with Tailscale Serve as the HTTPS proxy, generates a secure gateway token (exported in Pulumi outputs), installs the daemon as a systemd user service, and configures `trustedProxies` and `controlUi.allowInsecureAuth` to skip device pairing when accessed via Tailscale.

The cloud-init script runs `clawdbot onboard --non-interactive` with all necessary flags, then configures the gateway for secure Tailscale access. Your instance is ready as soon as provisioning finishes.

### Access the web UI

The easiest way to access the Clawdbot web UI is to use the `tailscaleUrlWithToken` output from Pulumi:

```bash
# Get the full URL with token
pulumi stack output tailscaleUrlWithToken
```

Copy and paste this URL into your browser. The URL includes both the Tailscale MagicDNS hostname and the authentication token, so you can access the web UI directly.

{{% notes type="info" %}}
**Finding your Tailnet DNS name**: Go to the [Tailscale admin console](https://login.tailscale.com/admin/dns) and look under the **DNS** section for your tailnet name (e.g., `tailxxxxx.ts.net`). You can also find your machines and their MagicDNS hostnames in the [Machines tab](https://login.tailscale.com/admin/machines).
{{% /notes %}}

{{% notes type="info" %}}
Token-based authentication provides an additional layer of security on top of Tailscale's network-level authentication. Only devices on your Tailnet can reach the URL, and the token prevents unauthorized access if someone gains access to your Tailnet.
{{% /notes %}}

From the web UI, you can connect messaging channels (WhatsApp, Discord, Slack), configure skills and integrations, and manage settings.

### Verify the deployment

After deployment completes, SSH into your instance to verify everything is running:

```bash
# Check your Tailscale admin console for the new machine
ssh ubuntu@<tailscale-ip>

# Check Clawdbot gateway status
systemctl --user status clawdbot-gateway
```

### Test your assistant

{{% notes type="info" %}}
The cloud-init script needs a few minutes to finish. It installs Docker, Node.js, Clawdbot, and Tailscale, then runs onboarding and starts the daemon. If you hit the URL right after `pulumi up` completes, the gateway probably won't be ready yet. Give it 2-3 minutes.
{{% /notes %}}

Open the gateway dashboard using the `tailscaleUrlWithToken` output and use the built-in chat to test your assistant:

![Clawdbot gateway dashboard showing a chat conversation](clawdbot-chat.png)

Your personal AI assistant is now running 24/7 on your own infrastructure, accessible securely through Tailscale.

## Security considerations

When self-hosting an AI assistant, security matters. Clawdbot's rapid adoption meant thousands of instances spun up in days, and not everyone locked them down. The community noticed:

![Tweet warning about exposed Clawdbot gateways with zero auth](clawdbot-security-tweet.png)

The tweet isn't exaggerating. A quick Shodan search shows exposed gateways on port 18789 with shell access, browser automation, and API keys up for grabs:

![Shodan search showing exposed Clawdbot instances on port 18789](shodan-18789.png)

Don't let your instance be one of them.

| Concern | Without Tailscale | With Tailscale |
|---------|-------------------|----------------|
| SSH access | Public (port 22 open) | Public fallback + Tailscale SSH |
| Gateway access | Public (port 18789 open) | Private (Tailscale only) |
| Browser control | Public (port 18791 open) | Private (Tailscale only) |
| API keys in transit | Exposed if gateway accessed over HTTP | Protected by Tailscale encryption |
| Attack surface | 3 open ports | 1 open port (SSH fallback) |

{{% notes type="info" %}}
SSH remains accessible as a fallback even with Tailscale enabled. This allows you to troubleshoot if Tailscale fails to connect. Once you've confirmed Tailscale is working, you can manually remove the SSH ingress rule from your security group for maximum security.
{{% /notes %}}

My recommendations: always use Tailscale for production, rotate your auth keys periodically, use Pulumi ESC for secrets instead of hardcoding, enable Tailscale SSH to avoid managing keys manually, keep an eye on your Tailscale admin console for unauthorized devices, and remove the SSH fallback after confirming Tailscale works if you want zero public ports.

## What's next?

Now that Clawdbot is running, you can install skills (voice generation, video creation, browser automation), set up scheduled tasks with cron, invite colleagues to your Tailnet for shared access, or connect additional channels like WhatsApp and Discord.

## Conclusion

Deploying Clawdbot with infrastructure as code means you can reproduce your setup anytime, version control it, and tear it down with a single command. Adding Tailscale keeps it private - no exposed ports, no hoping you configured your firewall correctly at 2am.

If you run into issues or have questions, drop by the [Pulumi Community Slack](https://slack.pulumi.com/) or [GitHub Discussions](https://github.com/pulumi/pulumi/discussions).

New to Pulumi? [Get started here](/docs/get-started/).
