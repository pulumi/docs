---
# Name of the webinar.
title: "Certificates as Code with Pulumi and Cert-Manager"
meta_desc: "In this lightning talk, Jake Sanders will show you everything you need to know about deploying apps with mutual TLS automated using cert-manager."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: ""

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "certificates-as-code-with-pulumi-and-cert-manager"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Certificates as Code with Pulumi and Cert-Manager"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Certificates as Code with Pulumi and Cert-Manager"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/_PUsRJi5yEw"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "11 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        In this lightning talk, Jake Sanders, Software Engineer from Jetstack, will show you everything you need to know about deploying apps with mutual TLS automated using cert-manager.

    # The webinar presenters
    presenters:
        - name: Jake Sanders
          role: Software Engineer, Jetstack

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello everyone. My name is Jake Sanders and I work on the Cert-Manager Team at JetStack. And JetStack is all about cloud native engineering. So I'm very happy to be speaking to you all today at the Cloud Engineering Summit. Today I'm going to be talking about Certificates as Code with Pulumi and Cert-manager. So what is cert-manager? Cert-manager is a kubernetes controller that manages the complete lifecycle of X-509 certificates or T-L-S certificates in kubernetes.

    Being cloud native means that cert-manager extends the kubernetes A-P-I with custom resources that represent certificates, certificate requests, and certificate issuers. When you create a certificate with cert-manager, it will automatically get renewed on time, and therefore you don't need to worry about anything. We support the A-C-M-E or ACME Protocol, which means that any publicly-trusted certificate authority that implements this A-P-I can issue certificates to cert-manager, but we also support internal-only certificates with a number of pluggable issuers including Vault or an internal SelfSigned one, or even our new parent company Venafi’s trusted platform solution.

    So, before cert-manager, your internal P-K-I may have looked something like this. Signing a C-S-R, preparing it. Getting a signed C-S-R by your internal C-A, having it valid for a year or so, and then setting a reminder to yourself in calendar for next year to make sure we renew our certificate or our service will go down. However, with cert-manager you can create a certificate to custom resource. Inside the kubernetes A-P-I you can consume this from a standard kubernetes secret that's mounted inside your pod. Just like any other kubernetes secret.

    Behind the scenes, cert-manager creates another of its custom resources called The Certificate Request. And then this is picked up and signed by either an issuer in a single namespace or a cluster issuer, cluster-wide and this will go off to sign the certificate using either internal private P-K-I or off to a A-C-M-E server. So how does it integrate with Pulumi? Well as we know, Pulumi lets you write infrastructure as code in your preferred language, and as of May or early this year, Go Support was fully added, which is cool for us in JetStack. We’re mostly a Go shop.

    Pulumi’s kubernetes providers supports the full kubernetes A-P-I, but an advantage for us is that you can import your custom resource definitions, which are kubernetes, YAML, that describe to kubernetes the correct spec for custom resource and Pulumi will generate properly type-checked libraries for you to just import infrastructure.as code. And so compared with just hand-editing deployment manifests with and for— or text templates with other deployment tools, you get the full advantage of creating C-R-Ds that are checked by your language’s in-built type-checker.

    So because this is going to be a live demo, I'll start it rolling now if you want to follow along. I know it's a remote video presentation. So I put the link to the code, but also a Q-R code that you can scan with your phone. And while it's— while it’s going on, we will set this going. And I'll explain what's going on while it's running. So, the contents of the demo is we're going to create a private C-A and deploy cert-manager, create the cert-manager issuer with our private C-A inside, then create the cert-manager certificate resources at which— at which point cert-manager will automatically sign and maintain the lifecycle. And then will create two deployments that talk to each other using mutual T-L-S signed by this.

    And this is all happening behind the scenes with a Pulumi Stack as you can see here. So I'll talk through what it actually looks like in Pulumi. So using Pulumi's built-in T-L-S provider, we no longer need to do any kind of certificate wrangling with open S-L on the command line. I’m gonna say I want a private key and a certificate that's allowed to be a C-A and self-signed. We’ll then create a secret inside kubernetes using the Pulumi kubernetes provider. And this is using the Core V-1 A-P-I and the Meta V-1 A-P-I and we're pulling the data from our existing signed and private key. Using the help of a converter to base64 because kubernetes secrets have to be base64 encoded. This is where the magic happens. So using the C-R-D to Pulumi Tool that you can find on Pulumi’s website, I've taken our cert-manager custom resource and converted it into a library that I can just import and deploy along with my— the rest of my Pulumi stack.

    So we're creating a new issuer, cert-manager V-1, and it's going to be called C-A in the main space default and it will pull from the secret that we created earlier in the stack called C-A. Now we'll deploy certificates for each of our apps so we can have a ping certificate and a pong certificate signed for the service addresses of those services— those deployments rather. And by creating this certificate resource, we're signaling to cert-manager that we want it to sign certificates that are valid for 1 hour and 30 minutes before they expire.

    I want cert-manager to automatically renew them and this is really useful because no longer need a calendar invite to remember to renew your certificates. Cert-manager takes care of it and because we're using extremely short lived certificates, if any of these credentials were to leak, it shouldn't really matter because they have a very short lifetime. And probably most of the people watching have already seen a kubernetes deployment so I didn't include the entire code because it wouldn't fit on the slide, anyway.

    We're deploying a ping-pong container that mounts certificates from a secret and these— this secret will exist because cert-manager has put it there. So transitioning over to my terminal, we should be able to see— We created our, issuer. We created our certificates. Which created some secrets. And we created our deployments that are all talking to each other using a secret.

    So hopefully our stacks finished deploying. You can see cert-manager, all of the R-BAC commission's that cert-manager needs to work our C-A issuer, our services, and deployments. And I got the— I got Pulumi to output the U-R-Ls of the resulting services so we can go and look at them and show that, well, ping service has managed to communicate with our pong service and authenticated with a certificate issued by our private C-A. So that's our lightning-quick demo.

    I'll just put the slide back up for people to quickly check if they want to— if they missed it the first time. And that's it for our quickly deploying a completely managed internal private P-K-I solution with a few lines of Pulumi and cert-manager. And thanks very much and hope you enjoy the rest of the conference.
---
