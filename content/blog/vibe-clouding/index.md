---
title: "Vibe Clouding: Give In, Forget That Cloud Infrastructure Even Exists"
allow_long_title: True
date: 2025-04-01T00:00:00-00:00
draft: false
meta_desc: Today we're excited to announce vibe clouding support in Pulumi with LLM language support and a new and improved watch mode. Also, make sure to check the date.
meta_image: meta.png
authors:
    - joe-duffy
tags:
    - pulumi-news
    - april-fools
---

By this point in 2025, we've all heard about "vibe coding": the AI-fueled craze that enables even my 2 year old nephew to build new applications by simply giving into the vibes, embracing exponentials, and forgetting that the code even exists. Vibe coding enables anybody who can type on a keyboard or speak to a computer to build IPO-worthy software businesses overnight. Today we are excited to introduce vibe coding's similarly revolutionary close cousin: **"vibe clouding"**. By giving into the vibes, you can now spin up cloud infrastructure anywhere and everywhere, all by just saying stuff, copy and pasting stuff, and vibing. And even better, it _mostly_ works! Read on to learn more, or just watch the video below.

<!--more-->

## The Code Vibes

In just two months, vibe coding has transformed the entire coding profession. If you aren't familiar with the concept, this post by Andrej Karpathy introduces the idea:

<a href="https://x.com/karpathy/status/1886192184808149383"><img src="VibeTweet.png" width="600" alt="There's a new kind of coding I call 'vibe coding', where you fully give in to the vibes, embrace exponentials, and forget that the code even exists. It's possible because the LLMs (e.g. Cursor Composer w Sonnet) are getting too good. Also I just talk to Composer with SuperWhisper so I barely even touch the keyboard. I ask for the dumbest things like 'decrease the padding on the sidebar by half' because I'm too lazy to find it. I 'Accept All' always, I don't read the diffs anymore. When I get error messages I just copy paste them in with no comment, usually that fixes it. The code grows beyond my usual comprehension, I'd have to really read through it for a while. Sometimes the LLMs can't fix a bug so I just work around it or ask for random changes until it goes away. It's not too bad for throwaway weekend projects, but still quite amusing. I'm building a project or webapp, but it's not really coding - I just see stuff, say stuff, run stuff, and copy paste stuff, and it mostly works." style="padding: 3px; filter: drop-shadow(3px 3px 3px #aaaaaa);"/></a>

## Enter the Cloud Vibes

**Today we're announcing an entirely new way of managing your infrastructure, _vibe clouding_**. The vibes are no longer limited to application developers; as a platform engineer, you too can now vibe like the best of them. The combination of natural language support thanks to LLMs and an improved `pulumi watch` command put you in the flow and the cloud at your fingertips.

## Infrastructure as Code in *Any* Language. No, Really

**Today we're introducing the ability to write declarative IaC in natural language**. No code necessary.

[IaC](/product/infrastructure-as-code/) is now table stakes for anybody doing anything in the cloud. Pulumi's unique approach (which is [open source](https://github.com/pulumi/pulumi), by the way) allows you to use any programming language to declare cloud infrastructure, such as Python or TypeScript, and its declarative model brings you desired goal state into existence as if by magic.

### Declaring Cloud Infrastructure in Natural Language

Now you can express infrastructure in _any_ language, programming or otherwise. For example, this IaC "program" written in English creates a Python webserver in AWS that's accessible over the Internet:

```
An AWS EC2 instance running a Python web server.

It accepts traffic over the Internet on port 80 and simply responds "Hello, World."

Capture and export its auto-assigned IP address and DNS name.
```

We save this in a `*.pai` file (`pai` = Pulumi AI), and then deploy it with `pulumi up` like normal. The new language host asks Pulumi's AI Copilot to figure out the infrastructure we've requested and then shows us a preview of what it will do:

```bash
$ pulumi up
Previewing update (dev)

     Type                      Name               Plan       Info
 +   pulumi:pulumi:Stack       vibeclouding-dev   create     2 messages
 +   ├─ aws:ec2:SecurityGroup  webSecurityGroup   create
 +   └─ aws:ec2:Instance       webServerInstance  create

Diagnostics:
  pulumi:pulumi:Stack (vibeclouding-dev):
    🧠 Thinking...
    🧠 I am happy with this, let's go!

Outputs:
    InstanceDNS: output<string>
    InstanceIP : output<string>

Resources:
    + 3 to create

Do you want to perform this update?  [Use arrows to move, type to filter]
  yes
> no
  details
```

We can select "yes" and it will deploy our cloud stuff:

```
Updating (dev)

     Type                      Name               Status
 +   pulumi:pulumi:Stack       vibeclouding-dev   created (17s)
 +   ├─ aws:ec2:SecurityGroup  webSecurityGroup   created (2s)
 +   └─ aws:ec2:Instance       webServerInstance  created (12s)

Outputs:
    publicDns: "ec2-54-189-144-3.us-west-2.compute.amazonaws.com"
    publicIP : "54.189.144.3"

Resources:
    + 3 created

Duration: 18s
```

Seconds later, after it completes, we've got a Python webserver on the Internet:

```bash
$ curl 54.189.144.3
Hello, World.
```

### Not Just English

This is a new language runtime just like Pulumi's other supported languages (`python`, `go`, `java`, `yaml`, etc). We almost called this new language `english`, except that we can use other languages:

Spanish:

```
Una instancia de AWS EC2 que ejecuta un servidor web Python.

Acepta tráfico de internet en el puerto 80 y simplemente responde "Hola a todos".

Captura y exporta su dirección IP y nombre DNS autoasignados.
```

Mandarin Chinese:

```
运行 Python Web 服务器的 AWS EC2 实例。

它通过端口 80 接受 Internet 上的流量，并简单地响应“Hello, World”。

捕获并导出其自动分配的 IP 地址和 DNS 名称。
```

Hawaiian:

```
ʻO kahi hiʻohiʻona AWS EC2 e holo ana i kahi kikowaena pūnaewele Python.

ʻAe ʻo ia i ke kaʻa ma luna o ka Pūnaewele ma ke awa 80 a pane wale ʻo "Aloha, World."

Hopu a hoʻokuʻu aku i kāna helu IP i hāʻawi ʻia a me ka inoa DNS.
```

The LLM is happy to accept any language known to us humans. So we are simply calling it `ai`. You just specify `runtime: ai` in your `Pulumi.yaml` and all other Pulumi features work as normal:

```yaml
name: py-webserver
runtime: ai
```

### It Is Feature Rich and Works for Real Workflows

If you change your mind and want it to use a Node.js web server ... or listen on port 8080 ... or run on Azure instead of AWS ... with a different response ... Simply change your prompt:

```
A virtual machine in Azure running a Node.js web server.

It accepts traffic over the Internet on port 8080 and simply responds "Hello, Vibe Coders!"

Capture and export its auto-assigned IP address and DNS name.
```

We then rerun `pulumi up` and it knows how to evolve your infrastructure towards the new goal state.

Your prompts can be as imprecise or specific as you'd like. For example, "Run a joke of the day application on Google" needn't tell the LLM what sorts of infrastructure you want -- it will just intelligently decide between a GCE VM, Docker container in Google Cloud Run, GKE app, etc.

You can also spread your prompts across any number of `*.pai` files: so you can stick your webserver into `webserver.pai`, your database in `database.pai`, and so on, and you can even cross-references resources between files, and the LLM will figure it out. Just vibe and out pops cloud infrastructure!

## Watch Mode for Rapid Iteration and ... Vibing

This is already amazingly cool, but we haven't begun _vibing_ just yet. We are halfway there.

**Today we're also introducing a vastly improved watch command to properly unlock the vibes.**

The little-known `pulumi watch` command sits there waiting for changes to any parts of your Pulumi IaC and in response to you hitting save will redeploy the changes. It turns out that this combined with native LLM language support yields the magical combination that unlocks vibe clouding.

Let's take our original example above but use the `pulumi watch` command to trigger the deployments:

{{< youtube "h-CHD5nTZDo?rel=0" >}}

Just write specifications fluently and hit save whenever it's convenient. Pulumi incrementally deploys what it can, when it can, reports on status interactively, and summarizes what it did afterwards.

If your thought is half-baked, exploratory in nature, or you hit an unexpected hiccup, thanks to the declarative nature of IaC, it can always pick up safely where it left off. Don't worry, just vibe.

## This is Just the Beginning

By now, I hope you've realized what date it is today: April 1st. April Fool's Day. We just couldn't help ourselves. So this is all just a joke. Sort of.

Much of this is actually becoming reality thanks to the intersection of multiple factors:

1. Pulumi use of "code" pairs well with the LLMs' ability to produce correct code.
1. Pulumi language extensibility enables adding "natural language" as a language provider.
1. Pulumi Copilot, launched less than a year ago, gives us skills that make the LLMs even better at infrastructure tasks.
1. The LLM models are getting so darned good ... and will get even better still.

The improvements to `pulumi watch` are real and already in the latest Pulumi release. The `pulumi-language-ai` language host is, of course, just an early prototype of what's possible, but we look forward to hearing your feedback if you have the chance to kick the tires. Even more exciting things are on their way throughout 2025 and they won't be launched on April 1st next time.

## Get Started Vibing

If you want to get started, simply:

* [Download Pulumi](/docs/iac/download-install/)
* [Download the `pulumi-language-ai` host]() and ensure it's on your `PATH` (coming soon)
* Set `OPENAI_API_KEY` to a valid OpenAI key
* Run [`pulumi watch`](/docs/iac/cli/commands/pulumi_watch/), begin typing, copy and pasting, and vibing

We highly recommend playing this video on repeat in the background as you do so:

{{< youtube "WmL00oXSC6k?rel=0" >}}

Happy vibe clouding.
