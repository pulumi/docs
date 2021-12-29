---
# Name of the webinar.
title: "Taking a K8s Deployment from Default to Secure"
meta_desc: In this session we'll start with a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to go from default to secure.

cloud_engineering_summit:
    track: build

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars
layout: cloud-engineering-summit-replay

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "taking-a-k8s-deployment-from-default-to-secure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Taking a K8s Deployment from Default to Secure"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Taking a K8s Deployment from Default to Secure"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/ouj_0Yx4Mg8"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:20:00-07:00
    # Duration of the webinar.
    duration: "25 minutes"
    # Description of the webinar.
    description: |
        A Shodan search can quickly reveal over 17 million Nginx servers currently returning a 200 OK. One would think with such adoption that building a secure Nginx Kubernetes deployment would be easy. Surely one would be overwhelmed with online content!

        Whilst best practices are in abundance and security scanning tools for helm and k8s yaml are available, it can be truly difficult to find example code or solid advice on how to successfully follow security best practices. In this session I'll start with a blank canvas of a default Nginx deployment and leverage Checkov's Kubernetes yaml scanning capability to show my own experiences with the easy, the hard and the plain confusing elements of creating a secure Nginx deployment.

    # The webinar presenters
    presenters:
        - name: Steve Giguere
          role: Developer Advocate, Bridgecrew by Palo Alto

# This section contains the transcript for a video. It is optional.
transcript: |
    Okay, super happy to be here at the Cloud Engineering Summit. My name's Steve Giguere, it should show up down there. I'm a developer advocate for Bridgecrew. More about that in a moment, But let's get cracking with the subject, all right. I am going to be securing an NGINX deployment for Kubernetes using checkov, which is an open source Infrastructure As Code scanner.

    And I'm gonna try to explain why that is, like why, what was my challenge when I first started this. That is, I needed a website. This is a real challenge, for my Twitch show. I was gonna host it on Raspberry Pi. There's also challenges I've already got here, right? And it seemed obvious to use NGINX.

    The big problem I had was really just trying not to look like a total idiot because I worked for a security company that specializes in Infrastructure As Code security. And I have history in cloud native security. That's what the show's about. So it would be horrible, giant face-palm moment if I didn't pass our own checkov YAML scan. So and it wasn't secure, that'd be bad.

    So a little bit more about me. I'm a developer advocate for Bridgecrew. I'm a Raspberry Pi geek, I like the SecOps. I've worked for a bunch of places that focus on security and that's the Twitch show I was talking about. You can learn more about me at my website.

    Yeah, there we go. All right, so, this is kind of, some of the motivation. I guess, it's fair to say that NGINX is popular. And if you look up their 18 million live deployments that seem active, not all of them are containerized, of course. Not all of them, maybe on Kubernetes, maybe that first one is, it's on Digital Ocean, but it just kind of shows that if there's a weakness, some baddy out there with a bot is gonna find it.

    So I kind of feel like we should do best efforts. If you don't know what Shodan is, Shodan is like Duck Duck Go. But looking for all this stuff you can't see. So it's used by researchers and baddies alike for good and bad things. So the problem with NGINX, if compromised, what could I do, right? Well, if I took a look at the image itself, just the default image, just pulling NGINX, right? Not specifying tags, just seeing what happened.

    I jumped in there and it's got some things that if you're an unfamiliar with NSENTER, it allows me to execute commands in namespaces other than like Linux namespaces, other than my own, it's kind of odd there. It was an attack vector for a while. And thankfully, there are things in place to stop that being useful. Curl is there, so if there's nothing, anything, I basically have everything, if I have curl, I can get anything that I might be missing from an attack perspective, or I can install it. So and there's loads there.

    What was weird though noticed is that there was no PS. I thought, well, whatever I can get around that. So what I can do, the image can, as a result, I can enumerate the network. I can number environment. I can even breakout to the host, recently, there was the CV that was announced 2021-22555, that has an exploit that you can run.

    And exploit's a out of bounds right that pops you out into route. I tried it, and it does a bunch of stuff. If you get it wrong, you can actually crash the underlying node. And you can all sorts of stuff with it. So interesting, and of course, I'm on an NGINX server, so I can serve malicious content.

    I have control over what is being sent to other people. So that's bad. So I think we've established, let's just go to our happy place for a moment and let's get going, what's the plan? Well, step one of course, was go get NGINX, how I was going to do that in a containerized form. And I was actually interested recently to see that it hit number one. So I saw this graph in an article about three months ago and they were saying, oh, look NGINX is almost more popular than Apache.

    And Hey, look at that. As of about June, it is, cool. I'm going to wrap it in a Kubernetes deployment. So where do I get started? This is where I put on my newbie hat, and I thought, what would somebody do if they wanted to create a web server and from scratch And they want it to put it into Kubernetes? Well, they probably search, I would imagine Google or Duck Duck Go. It doesn't really matter, you get slightly different results.

    And so we can do that. I can click that and it's going to bring up search and there's lots of ads, okay. Some articles that are a little bit more NGINX focused App Protect, sure, great, a lot of videos. but I didn't, I know there's the blog actually, there's the blog that SEO works, I like that this talk is based on, but as I went down the first time I actually got some actual code was here. So that was a live search, and it's still, there can be applications with services.

    This is Kubernetes IO documentation. That was the link I had there just in case. And here's where I get my deployment. And then down here, I've got an example of how to create a service to connect it. Now, it serves that somebody might just cut and paste that and go well, there's my starting point.

    And I thought, well, that's what I'll do. I'll just cut and paste that. That seems good, right? So the next step was to check that it's secure. Can I use the default image, is it secure? Do I need to make changes to it? Do I need to make changes after I look at the deployment? Are my defaults in my deployment secure? That is pretty much step one or step one of securing things. So what does secure mean? When I say secure, I'm talking about I'm going to make it like a pretty old school, almost Info Sec reference to the CIA, what they call the triad of security, which when I say triad, it always sounds weird, but confidentiality, integrity and availability, generally, whatever it is you're doing can fall into these categories.

    I loosely here tried to map it to something that was a bit more cloud native or Kubernetes easy and said, all right, least privilege, immutability and resilience. This, that roughly summarizes what I'm after in terms of security in Kubernetes. And I tried to break everything down into what we're going to see in a moment. Now my tool of choice, other tools are available, was checkov. I would be remiss if I didn't say I work at bridgecrew.

    So obviously I use checkov, but independent of that, I used to use it, I just, I think, I think it's, I think it's good. It's got lots of checks, it works for Kubernetes. I can also use it for Terraform and a bunch of other stuff, right? It covers most infrastructure code languages. So why not? And it's gotta be as code plug and it's got all this stuff. Great.

    So I'm going to talk about least privilege in a moment, but just before I do that, I'm going to flick over here and I'm going to show you what I've got here. So I've got the, if I look, I've taken that NGINX and here it is, this is exactly straight out of what we just saw on the Kubernetes docs. And over here, I can scan it with checkov so I can type, compact and quiet just makes it easier to read on the screen. And I'm going to pick out the NGINX.yaml and I can see what I've got wrong.

    Now, what it's going to do is not gonna do is not show you the things that passed. We don't really care about that. That would be a whole their presentation to see what we did there. And I've got a few things, right? Specifically about, I think it's 20 things that were wrong of 90 things that it checked. 70 out of 90 sounds like a good score on a test, but, in security, maybe not right.

    And we can see making sure that I have a set comp profile I'll get into why that is. A high UID to avoid host complex, making sure I have a security context. That's when I always have an issue with, there's never a security context in there by default. And that says, well, I'm going to apply something that looks secure and you can take things away afterwards. We don't do that, we have a tendency to just give lots of examples that are technically insecure by default or easy by default so that we ease the friction of adoption.

    But I think we could probably start changing that these days. Some stuff that you might not know about, like ensuring Service Account Tokens are only mounted where necessary you might think really, is my Service Account Token mounted? I didn't do that, yeah, it is. If you don't say not to, it is. Namespace, all of these things, I've through all of these, memory limits, CPU and memory limits written requests are like the number one always missing because there's a bit of a paradox there. How do you know what there should be? And then interesting one about using digests.

    Let's go back and I've summarized a lot of these and I've categorize them, adding that set comp profile. You'd be surprised how important that is and how rarely it is done. It disables a ton of 44 system calls. I likened it to the Expelliarmus, Harry Potter spell. Getting rid of all disarming your opponent.

    Mount, Ptrace, reboot, rebooting the host, changing the namespace, the Linux namespace. There's a bunch of like, well, we talked about NS enter earlier, quotactl, messing with CPU limits, all sorts of stuff, there's tons of stuff that just gets rid of, and that you can like, you don't need to be a white hat hacker to look at that and go, yeah, I don't want any, I don't want any of that stuff. And it's a great default defense in depth. Like a lot of these features are, it doubles up when you remove capabilities like CAP_SYS_ADMIN, But why not, if I can add a one-liner that does this for me, of course, I'm going to do that, right? So that's right off the beginning. We can do that very quickly.

    Set the allow privilege escalation to false. You're probably thinking, of course, why would I want to do that? It must might be a surprise to you to learn that ping uses that, so you'll be disabling ping. Why do you need ping in a container? Most of the things you might want to use that this would disable are debugging related, debugging related. So understanding that like sudo, for example, anything that's set UID, you won't be able to use anyone. So keep that in mind, but it still should be a default.

    Don't run as root and assign inappropriate user and group ID. Now that might be harder than you think. And I'm going to show you how I did that because NGINX by default was running. I think it was running on UID and JD 101, which is really low and actually can conflict with other things. So I had to push that out and I had to do some tinkering in the Docker file to make that happen.

    So we'll talk about that in a moment. Drop all capabilities, we'll see that in a moment. There's a very, you don't have to know the capabilities, you can just say drop dash all. And then I feel like 9 times out of 10, nothing will break and that's good, right? Then you can start investigating and learning what capabilities you need after the fact. Too often, back in the old days, people would actually run as privilege, which gave you way, all that stuff, keys to the kingdom, or they would add all, cause they didn't want to sort it all out.

    So dash all is the good way to say least privilege. We'll talk about immutability. A read only file system, that sounds good. Why do I need to write to the file system? Typically containers are considered to be immutable by default. Well, in my case, actually I'm running a web server that needs to do some cacheing and have a temp file.

    So I need to find a way to be mostly read only at the very least, and we'll look at that. Unmount that Service Account Token, if you don't specify what service account you're using, it will use the default service account. And if an attacker gets in there and could get the token associated with that account, then they can impersonate that Service Account and abuse the Kubernetes REST APIs from within there, which means they can start messing with all sorts of stuff. So if you don't need it, which quite often you don't, one line gets rid of that, one line, one line security, that's what we like. Avoid supply chain attacks.

    This was the best image I can find. Sorry about that, it's kind of gross, but when we're talking about what images we're using, we often know, a lot of us know that we shouldn't use latest, right? But and then we'd start using, for example, in NGINX I would use 1.21 maybe that's one of the latest ones. But that still can be a problem from a supply chain attack perspective. Because if I get a hold of the build environment, the CI, I can build a malicious version of this.

    I can push into its destination. And I just tag it again with 1.21. Now the SHA, the digest will change, but if I'm just using the tag, I'm vulnerable, right? So let's just, let's be diligent and use the tag and we'll see how to do that. It's not hard, you can even do it in CI, you don't have to go manually do anything.

    It's not a lot of extra work. Okay, resilience, this is one of the things that is often. Well, I won't even say easily avoided. I mean, understanding what readiness and liveliness probes you need, this can be hard. It's not always totally clear which things, how, what commands will do what, but if you can come up with those letting Kubernetes know you're alive and you're ready is great because that it'll help you stay alive and it'll help that make sure that your availability is high.

    In the case of NGINX, it's actually not that hard. So we'll see how, what that looks like shortly. CPU and memory requests and limits, again, it's like a chicken or egg scenario. What should they be? If I don't know what they are, how can I set them before I start deploying? But the reality is you can come up with sensible limits. It's really quite important to have requests in there because more than just requesting a piece of CPU and memory, Kubernetes looks at that as how much of the pie do you want in comparison with other running pods on this node.

    So it's more than just me me me, it's about working as a team with other pods on the node. So I will, I will put some sensible defaults in there for NGINX and we'll see what those look like. Okay, so let's do it. Let's apply all of these security controls to our NGINX and see if we get a clean slate on checkov. That would be awesome.

    So low-hanging fruit out of the box would be here. I can just add my namespace, yep. We're going to call it Cloud Edge Summit and I really should add it here as well. So let's add it in there. That'll give me some low-hanging fruit out of the box.

    Can I add resources right now? Let's do that. So let's do it in that order. That is associated with my containers. So let's add some space there and let's add some default resources. Cool, let's talk a little bit about those.

    So I've got my limits of one CPU and 0.5 CPU. Maybe that's a little bit much, but I'm not running anything else on this one node, so this should be fine and I know that memory is pretty reasonable, but I can really, I can scale this way down if I wanted to. And it doesn't really matter. As long as I have something in there that is my portion of what we want.

    Right, I might leave my memory, I might leave my limits really high and my requests really low at the start just to be absolutely certain that I am recognized, I am part of the team, right? So those are, that's a perfectly reasonable starting point, just as long as it's there. What I can do afterwards is I can use metric server and I can do a top and I can see what I'm actually using and I can create a buffer plus or minus around that. That is what I really want to do, but let's not leave it blank to start. Right, so since I'm on resilience right now, let me add the probes and you can see what those look like. Okay.

    Probably think I'm the fastest typer in the world, right? I've worked out these beforehand and I typed, I actually programmed them into my stream deck. So I'm live in this probe. I'm just checking to see the Internet's processes live and running. And I'm doing that at a reasonable cadence and my readiness. Well, this is kind of, is it actually serving up a, some web, some of my website.

    You'll see, I've got 8080 here. And actually I'm going to go back, and this isn't something that is being checked for, and I think it might result in a new rule is that sharing a kind of a system level port directly from the pod isn't necessarily great. I should be doing that from the service down here. So I should have target port in there, and that would make a lot more sense, but we'll do that after. So that adds up, so there we go.

    I've got that done, now let's just, Let's do another track, right? So I was at 20, what am I at now? Hopefully maybe like 16 or something, that'd be, that'd be already good progress, right? All of these, a lot of these CPU limits ones like there's tons of them, they're going to go away. I'm not a one-page yet, darn. I've kind of hoping I was, but I got 12. Okay, that's not bad. Security context when I add that is really going to take care of a lot of this.

    I've already said this, it kind of upsets me, no, it doesn't upset me, but I think we don't, we don't add security context by default often enough. And it is confusing definitely, because there's two different security contexts. There's the one for the pod itself, and then there's the one for the container. So if we're looking at, for example, the pod, let's do that, right? Let's pop this here. So here's the security context for the whole, by default, this will be for all containers, so I can have multiple containers in a pod, we know that.

    I'm going to run as non root, which is important, right? Maybe I'm already running this down route, but to specify it to Kubernetes is important. I'm going to run as user 10,014 and group 10,014, and you might be thinking, how on earth is he doing that? This is I'll at the very end, I'll end by showing you what I did in the Docker file to make that happen. And I'm using the seccompProfile RuntimeDefault. See that to me is a no-brainer because it does so much. And I don't have to think it up to make up a profile.

    I can just use Docker default or RuntimeDefault, and I'm going to get a ton of good stuff from that. So just with that alone, if I save, there's nothing wrong with those defaults. Quite often, if you've already got a sensible user ID in your container, just add that information means that I've got a declarative definition of security in place. Almost on one page I bet. Eight checks, we're on the edge.

    So we're going to add the other security context now down within the container. So let's move down here and go after our probes. We're going to pop it just there. All right, well, so what am I doing within the container itself? I am establishing that it will have a read only file system. This is good, this will cause me problems for NGINX, and I will show you how I overcome that.

    I blocked allow privilege escalation and I have dropped all capabilities, but I've been specific about NET_RAW Now I don't necessarily think that's something you necessarily have to do cause it's sort of redundant. But because I have noticed the checkup has two checks. It checks for specifically for NET_RAW and for all capabilities, I added them both just cause I like to have a clean slate. And now we're going to be really close to the end. Yes, Service Account Tokens, and the secconf was covered.

    So the one-liner, that is also at the pod level. So let's go up to the top where we're doing our things for the pod. Let's pop it and just here and let's get rid of that service account. automountServiceAccountToken, false. Awesome, right? And the last two were to do with the image.

    Look at this, how often do we see this? Like in lessons or tutorials, they just say kubeCTL run my pod dash image equals NGINX. We're not encouraged often enough to have a tag or have to be specific about it. So much so that not until you get further down the line, do you suddenly go, oh, this is bad. Like I have nothing here which will default the latest, but I need to have something. If we go look at Docker Hub, we can see there's loads of tags here, I've got all the tags present.

    We're going to have our latest. And there it is, and I can actually at a glance, see that this image has already tagged multiple times. So it's tagged as main line. I also happen to know that it's 1.21.3, which is, which is one that I should really, if I was using tags and being specific, I would use this one here. But that's not really what I want to use. What I want to do is I want to come in here and I want to get this information here. I want to put that in there. It is a slightly different format, but it does make sure that I'm always, definitely use the same built image.

    It does go in there a little different. Normally you'd put colon, but in this case, you're going to put it in like that with an @ SHA 256, and then colon version. So I think we're kind of there. That wasn't too painful. And if we're done, we're done, and then I'll end by showing you how to make it actually work.

    Cause I've got my clean slate, but it's now really a bit of a tick box exercise because the reality is NGINX won't be able to write to the drive and it'll just crash loop back off, fail, in order to make that happen. I mean, I do actually need to create some volumes. So I'm going to have to do this, create some empty dir volumes and then immediately above it, mount those volumes. And those are the directories that I need. So I've just created some temporary space.

    I still have a read only file system. And I've solved that problem where this is actually going to run now, which is great. And then finally, the last thing I had to do with my Docker file was do a little bit of jiggery pokery here. You can see I'm installing something called shadow. The reason I've done that is because user mod and group mod don't exist in this NGINX Alpine.

    And that allowed me to change the NGINX's identity to a decent user ID and group ID. It does some of the permissions, but it took care of the rest of the permissions down here and being a good boy, I then deleted shadow afterwards. And that meant I was able to switch to user NGINX and work. So that is essentially all the different steps I took to secure this NGINX, which did take some time to work out, even though I just did that pretty quickly. So the key takeaways I want you to get from this is that finding secure examples sometimes can be really difficult.

    I have put all of this into a repo, which I can, I should have put it on here, but it's in my blog. So if you Google secure NGINX deployment, you'll find the blog and you'll find the repo where all of this stuff is. Basic best practices can be easy if you use tools, all of those, all of those errors I found in checkov actually refer to documentation that points you to good suggestions and good best practices, or even to the Kubernetes documentation itself. So they're available. Know that many of the defaults aren't secure and there is always an easy way to make that happen.

    All right. All right, that's the end of this talk. Thank you very much, happy to take questions. More information about checkov, you can find a checkov.io, thank you very much.
---
