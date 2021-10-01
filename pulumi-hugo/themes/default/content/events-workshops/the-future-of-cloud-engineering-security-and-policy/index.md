---
# Name of the webinar.
title: "The Future of Cloud Engineering: Security and Policy"
meta_desc: "Join Pulumi Co-founder, Eric Rudder and security experts from Tigera, GitHub, Auth0 and GitLab to learn about emerging security challenges and best practices."

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
url_slug: "the-future-of-cloud-engineering-security-and-policy"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Future of Cloud Engineering: Security and Policy"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "The Future of Cloud Engineering: Security and Policy"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/72Wfb-R_4lM"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "53 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Join Pulumi Co-founder, Eric Rudder and security experts from Tigera, GitHub, Auth0 and GitLab to learn about emerging security challenges and best practices

    # The webinar presenters
    presenters:
        - name: Maya Kaczorowski
          role: Senior Director, Product Management, Software Supply Chain Security, GitHub
        - name: Amit Gupta
          role: VP Business Development and Product Management, Tigera
        - name: Johnathan Hunt
          role: VP of Security, GitLab
        - name: Eric Rudder
          role: Co-founder and Executive Chairman, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    **Eric Rudder**

    Well, welcome and thanks for being here. We're going to talk a little bit about security and policy and I thought I'd kick it off with just a few introductions. I'll let you guys introduce yourself. We can start with Maya.

    **Maya Kaczorowski**

    Sure. I'm Maya Kaczorowski. I'm a product manager working on software supply chain security at GITHUB.

    **Eric Rudder**

    Nice. Amit.

    **Amit Gupta**

    Hello. My name is Amit Gupta. I run a product management and business development at TIGERA. We are a company behind project Calico. We do networking, network security, observability for [inaudible 00:00:48].

    **Eric Rudder**

    Nice. And Johnathan.

    **Johnathan Hunt**

    Hi, I'm Johnathan Hunt, VP of information security at GITLAB.

    **Eric Rudder**

    Awesome. I thought with the debates going on in America, lots of interesting. I thought we'd start with a controversial topic. I'll go back. I'll start with Jonathan. Tabs or spaces?

    **Johnathan Hunt**

    Oh. I guess I'd have to go with spaces.

    **Eric Rudder**

    Spaces. This is interesting. We have GITLAB and GITHUB so we'll get the official corporate point of view on it. Amit, tabs or spaces?

    **Amit Gupta**

    Tabs.

    **Eric Rudder**

    Oh, wow. Already a controversial panel. This is good. And Maya?

    **Maya Kaczorowski**

    I don't know what the official point of view is, but I use spaces.

    **Eric Rudder**

    Well, two to one on spaces. This is terrible. Oh, my God. We're going to split the Supreme Court, we're going to split here too. That's all. Okay, so we're warmed up now. I thought we'd just start with an interesting thing. I saw in the news yesterday that Universal Health Services had a breach yesterday. It's actually the largest healthcare breach of medical records ever in the US. So security is definitely on the mind of everybody's topic.

    I just thought we'd start with an open ended question and talk about really what are some of the emerging threats that people see around security and policy. If you were building a team today, from scratch and you could design your all-star dream team to think about security and policy from the beginning and lock it into your culture. What are some of the things that you'd look for? I'll start with Maya.

    **Maya Kaczorowski**

    Yeah. I think there is certainly a shift and I hate already using this term, but around adding security to DevOps. So exactly almost what you were just saying around making security part of your culture, the idea of having a separate security team and a separate set of people who's responsible for implementing sort of certain controls, it's changing right there.

    Obviously, you still have a security team, you still have application security reviewers or InfoSec people or whatever, but everyone is involved in your security decisions. Everyone's involved in actually improving the security of your organization. One of the emerging trends I would say in that space is just embedding security as part of it and having all developers have some of that knowledge and tooling.

    **Eric Rudder**

    Amit, anything to add or build on?

    **Amit Gupta**

    Yeah, absolutely. Eric, I agree with you that the security landscape, specifically the threat landscape is getting more and more sophisticated, as the applications are being rearchitected to Maya, your point. The security as a function has to be involved as part of the DevOps pipeline as early as possible in the build pipeline. Security has to evolve as an enabling function and as a reserve, the security teams, they really just have to provide all enablement and everything needed for these ops teams, the DevOps teams to be able to enforce, refine and implement those security controls. So, absolutely agree with what Maya, you mentioned that security has to be part of the DevOps function and you've got a hire for talent that actually has some level of education and experience. Building, designing, implementing some security controls in addition to the ops functions.

    **Eric Rudder**

    Johnathan?

    **Johnathan Hunt**

    Yeah. I'm going to take a bit of a different perspective on this question. What I can tell you is that, what I've seen is that from 10 years ago to today, I'm seeing a lot less, we're going to try to break into your network through brute force attacks, and we're going to try to hack our way in and move laterally across to your database and export all this data out. What we're seeing and what I've seen over the last several years, is more by ways of abusing or misusing or exploiting the services that you actually provide legitimately. What we're seeing is an increase in abuse of CI writer, crypto mining, other ways to exploit our platform.

    You kicked off the question by asking about the dream team. What I can say is, much like the other companies being represented on this panel, we take security very seriously. I'm fortunate enough to have been able to build out a significant sized security organization at GITLAB. The two things that I did, in which might be helpful to some of you is, I've built a security research team and a red team to address two different ways of approaching the same problem.

    The security research team is designed to identify the latest threats, the latest zero days, the latest exploitations. Determine how they can be used to affect our service and then drive those to mitigation. Whereas, the red team then is continuously planning on launching complex multi chain campaigns against our service and platform using these threats and techniques that are being discovered by the security research team. Their attempt is to move the theoretical into reality. So far, it's really led to building a trust with our customers, building trust with the community and hopefully mitigating a lot of real threats and vulnerabilities that gets our platform.

    **Eric Rudder**

    Nice. One thing I thought that would come up in the first round of answers, but I'll make it explicit, is one of the changes now is that the cloud, at least in my career, has changed how we think about certainly the security perspective and how we construct teams. I'll throw out a softball like questioning. What things has the cloud changed? What things has the cloud made easier? What things has the cloud made harder? I'll toss it over to Maya.

    **Maya Kaczorowski**

    Sure. I think lots of things have changed and also nothing has changed. I think a lot of the threats and things that we see are not notably different than before. Be it your infrastructure like application issues that you might have, basics that everyone's annoyed with, but we still have cross site scripting. Those are still around for some reason. Untouched servers, whatever it happens to be. I think what changes for me with the cloud and as people move towards newer architectures in general, is a lack of understanding of what's actually in your environment.

    I think that makes a huge difference in terms of like, if you went from having a data center that you ran and you knew exactly what was running there, because somebody had to provision it and worked on your team, versus you have different sets of developers running in different clouds, using different architectures, using different frameworks. It's a lot more for one security team to understand.

    The first part is understanding what you actually have. That's much harder with the cloud and that's, I would say, a negative in some sense for security. In the sense that you don't initially understand your risk, because you don't actually understand what you have. Conversely, I think where the cloud does really well is arguably, short of a handful of very large companies, your cloud provider is more secure than you are. Choosing to move a workload to a data center run by one of the large cloud providers, probably actually gets to a lot of benefits that you wouldn't have.

    Otherwise, you'd have some automated patching of your hardware, some maintenance that's taken care of for you. Notifications, if there's security issues that are taken care of for you. Lots of things that are automated on your behalf. You get that all in one bundle where a lot of that specialized knowledge, your team doesn't need anymore. Again, the problem being that now you have two or three sources for that knowledge, rather than one source for that knowledge in your environment.

    **Eric Rudder**

    That's great. Amit, building on some of the things that Maya brought up, are there some unique strengths of the cloud that we can build on and use to our advantage?

    **Amit Gupta**

    Yeah. Just teeing off from what Maya here explained. In a cloud security model, obviously from a shared responsibility perspective, a whole bunch of things are going to be taken care of by the cloud provider so a whole lot of things, the user doesn't have to worry about. But as a user running applications in the cloud, you're obviously responsible for securing your applications, you use it for the services and so on. Some of the cloud providers, they do provide a whole bunch of capabilities around how you can leverage some of those knobs to secure your application.

    Specifically to question Eric, one of the things that I believe cloud creates a good architecture and a model is, it takes a very workload centric model. What it forces security professionals to think about is, move their security architecture and approach closer to the applications, closer to the workloads. We suddenly see that from a network security perspective, particularly working with our users. The traditional network security models are not as effective as you go deploy your applications in the cloud. As a reserve, designing a security approach that is more tied to your applications and your workloads is actually a good security architecture and more effective security architecture. Some of the cloud based deployments help in that model.

    Just one additional thing I would highlight is, it's very likely that if you're deploying cloud based application, that you've already moved to an architecture approach where you build resiliency in the application closer to the application. These are newer architectures. In my opinion, is actually a good part done. You should design your security to that approach as well. Not really just rely on infrastructure components where you put gates are gateways or proxies or appliances to secure the architecture.

    **Eric Rudder**

    I think just to paraphrase Maya in lighthearted way, her answer was also like, the more things change, the more they stay the same, in terms of, everything's changed, nothing's changed. I think some things have changed for dev Op team or devops. In the past when we did releases, and if you remember released checklists of all these things we were supposed to think about before release. Now, we're releasing many of us multiple times per day. It's certainly less of a checklist approach. As teams think about automating their approach, what are some things that are really top of mind that replace the final quality checks and how we think about our modern CICB pipelines in this way? I'll toss it to Johnathan.

    **Johnathan Hunt**

    Yeah. Honestly, I recommend really working closely with your QA development orgs to identify areas where automation can be a significant benefit. This can happen in multiple ways. Static and dynamic analysis, dependency scanning, all of these things are easily automated at the developer level, on their local host or during the SDLC pipeline. These tools are not only designed to run very quickly, but also speed up your deploy times versus running manually. Arguably, you're more secure as you prevent releasing harmful vulnerabilities which are obviously exploitable by malicious actors.

    **Eric Rudder**

    I think the other things to think about also, we've spent most of the time thinking about security, but there's also policy implications too, as we make changes. Things like GDPR affecting companies and other type things. There are other specific considerations around policy that people should think about, Amit?

    **Amit Gupta**

    I would agree with you Jonathan. In fact, to add to that, I think when you're defining your policy controls or any regulated regulatory framework that you're subjective for your applications running in cloud or elsewhere. I believe a very effective mechanism is to define these policies or controls or requirements in a declarative model. You define your policies, could be as simple as, "Thou shall not run privileged mode containers in production." Or, "Thou shall not allow egress traffic [inaudible 00:14:06]." Whatever those policies, regulatory frameworks that you follow and you have translated that into specific technical security requirements.

    The more effective approach is, you write those controls in a declarative model and then have governance controls around it. It really depends on the organization. We have seen some organizations very effectively do continuous audits around these policies. If they see violations, they could be actions like, "Hey, we are going to kill all deployments that are running containers in privilege." That can be one policy requirements. Or, "We would kill all deployments that are not encrypting traffic inside the cluster." If that's one of the control requirements you're following from a regulatory framework. Or, you can go as far as saying that we would have controls in place that if you do have a privileged mode container, we won't even let you deploy it in the infrastructure.

    That will be blocked much earlier right in your pipeline and your QA processes and so on. I think it's very important and it's also effective, you take those regulatory requirements from GDPR or whatever framework your organization is subject to, define those into technical requirements, and then figure out collaboratively working with your dev teams and security teams what approach you're going to take to enforce those requirements. Are those guidelines or hard frameworks that you need to adhere to? Because without that, you're subject to some significant violations or penalties.

    **Eric Rudder**

    Yeah. I'd like to build on that. All of us have talked about how it's really important to work together and bring in various team members, whether they're security experts or QA experts. But when the rubber hits the road, I'll toss this one to Maya, what is the actual best way to engage security and policy stakeholders in the group? They may not be as technical as some of the developers and yet, we need to work together. What is the best way to actually make sure that everyone's point of view is represented?

    **Maya Kaczorowski**

    I don't know that I have the best way. I think that there's a need to obviously separate requirements from the controls that you put in place. There are some regulations that have very strict controls that define very explicitly what they need to be. Like HIPAA, for example, if you were to lose healthcare information that was not encrypted, that would have consequences. HIPAA doesn't say, "Encrypt health care information." It says, "If you lose it and it wasn't encrypted, then there's a different penalty than if you lost it and it was encrypted." You have to translate that set of requirements into what's actually important for your organization and then what that actually means for your organization. I see that for things like dual control, encryption requirements, key management is a really common one, a couple of their controls.

    There's so many different ways that you can make this work. It really matters in terms of your organization figuring out what's practical and your auditors agreeing with you. [inaudible 00:17:24] control making sense for your particular organization. How to engage between those different teams? I think having a lot of clarity as to what your exact requirements are, documenting them. A common thing to do in a large company would be a risk register where you actually go and see what all those controls are and then verify that those are being met. But to go back to what Amit was saying, I think that's the reality of 20 years ago. It's still far from the reality where people are today with the cloud and wanting to have declarative policies that automatically apply to their environments and automatically enforce everything they want in their environments.

    That's what we all want. The reality is I don't see anyone there yet. I see people hoping to get there. I guess what I would say in that regard, to me the first step, obviously, like I said, understanding the controls between your different teams, but centralizing and having a common way of doing of some of the things that you want to do in your organization. One of the most powerful security controls, isn't a security control, it's just having a consistent way that your team writes, builds, tests and deploys code. Because then, you have somewhere to apply any of the controls that you can imagine in your environment. Rather than having to apply in five different places. So engaging, yes, your policy auditors, et cetera, developers, but also your dev ops team or your infrastructure team to make sure you can actually implement what you're setting out to implement.

    **Eric Rudder**

    Yeah. Anything to add, Johnathan, in terms of how to actually engage the key policy holders?

    **Johnathan Hunt**

    Yeah. We have a pretty interesting approach at GITLAB. We as a company, some people may know this, we are radically transparent. I don't know if I'm allowed to use that terminology, but that's how I phrase the way the company operates. Radically transparent. What that means is, our entire handbook is on the web. We live stream company meetings out to YouTube. We have all these procedures and processes around ensuring that the tickets and the issues and the projects we're working are open for company visibility. What I think is important is, first... I think Maya did a good job at touching on most of this.

    The one thing I would add is, I think that one thing you can do is, as best as you can, work... Rather than synchronously, like in a meeting, everybody has to get on a call at 12:30 and we're going to invite 17 people to that call, is try to work as asynchronous as possible. GITLAB itself, we have 1300 people in over a hundred countries. We can't possibly get everybody on to a meeting, all of our stakeholders on a meeting at the same time. It's literally impossible. What we try to do is, try to work as asynchronous as possible. Also, how many times have you been in a meeting and come away with direction and requirements and tasks and all of a sudden, "Oh, we forgot to invite Maya. We forgot to invite Amit to that meeting and now we've got to start from scratch."

    First and foremost, work the best that you can asynchronous. Opening up the information, the documentation to all parties, even to the company if you can, because you may not properly identify all the stakeholders from the beginning. Allowing people the visibility to access those documents, to access those tickets, to access those issues and be able to provide feedback on their time, during their workday, I think is highly advantageous. The other thing I would say is, I think it's important to, for people to become better communicators.

    I think a lot of times people jump into meetings and they don't have a real agenda set. They don't have, "This is what's expected out of this meeting." They'll go into a meeting and they'll say, "Hey, this is the problem. What do you all think?" Then it becomes a, pardon my terminology, but a waste of 30 minutes or a waste of an hour and of everybody's time. I think you have to come in and set expectations and understand what the ask is and what you're intending to accomplish with that meeting and come away with actionable items and events. I think that's the best approach to engaging stakeholders and progressing on issues of concern.

    **Eric Rudder**

    Yeah, that was good. You got some good examples on good things to do and less good things to do, shall we say. I'll build on that going forward. I'd say the easiest way to ask the question is, I think we've all seen many companies moving to the cloud and modernizing their application portfolios. What are some of the biggest mistakes that you see customers make as they go into this transition? Any words of advice on how to avoid these things going forward for the benefit of sharing our experience?

    **Amit Gupta**

    Yeah, absolutely. If there's one thing I would pick where users trip off or organization trip off is, they put security as an afterthought and it's not big then as part of the architecture. I'll take a couple of examples to decide how it gets really complex, particularly in a modern application infrastructure or architecture. You start with one cluster, a few notes, four or five services, it's relatively okay at that point. But as you start to become successful and you're moving to four or five clusters and you are hundreds of microservices running, many applications, potentially in different clouds, at that time for you to go back and put security controls in place and rethink about the infrastructure, you're just asking for massive amounts of trouble, rework, real estate time and energy and so on.

    If there's one thing I will tell you, I've seen this many, many times working with many users and customers that, they're hitting outages, they are hitting service incidents to fix some security requirements, but it's too late to start thinking about that. It's a massive overhaul of the infrastructure. If there's one thing I would say is, if folks can think about security, like secure by design principles, pick whatever principles your organization want to follow. You want to minimize attack surface? You will have multiple layers of difference, you will follow the least privilege model.

    Whatever those principles you want to follow in your design cycle, think about security at that stage. It's going to create a lot more value for you as you further evolve your infrastructure, your application, you're furthering your journey. You'll actually be able to address evolving security requirements in an effective way if you have thought about those principles early on. I would say that, that's one of the most important thing that we have seen our users trip off. Those who do think about that early on definitely benefit from it.

    **Eric Rudder**

    Maya, any other classes of mistakes that you see besides designing security and policy controls upfront?

    **Maya Kaczorowski**

    One is in terms of rollouts, different parts of the organization or different levels of control, I would say. I haven't seen anyone successfully turn on enforcement from day one. Not to say it's not possible, but I'd love to see it. The way that I'd be able to typically do those would be, it was almost like a dry run, like what's going on in my organization? Where am I not passing policy? Okay, let me go follow up with those teams, understand why they're saying that they should be in scope or understanding if they need more help becoming in scope or actually addressing the control, whatever it happens to be. Then I can go ahead and enforce that requirement going forward. It's not something you can just turn on without going to engage all of the people who might have that control affect them directly.

    **Eric Rudder**

    Yeah, I agree. I think that's important. We actually added a soft enforcement specifically so that people can turn it on day one, even if it's only reporting. I agree. The better you get the visualization of what's going on, the sooner you can figure out how to address it. What are some considerations for organizations in terms of, should you use the cloud, should you go with third party, should you actually host your own? How do people make that decision? What's your best prescriptive guidance of them?

    **Maya Kaczorowski**

    I think it really depends where your data is and what you're trying to control. If you're using three different cloud providers, using three different policy systems, one for each cloud, doesn't seem like the best plan. Again, you can tell me otherwise that you've tried it out and it worked, but I haven't seen anyone really do that successfully. People will turn to third party tools, configures code, infrastructure's code tools. We're talking about the declarative models that people are going towards. Sometimes also people don't care in some sense.

    Like if the core part of my application is running some compute workload, and I really care about what's happening at the application layer, but I am a little bit more relaxed to what's happening other layers, I might not put in place a strict controls because I don't give my developers direct access to that. It's about also controlling the things where you have people who have access to change those controls. If you only have one person who handles compute provisioning, and that person knows what they're doing, maybe you don't need to enforce controls there and they can just go update things themselves. It's more about being smart with what you have and how big your team is than anything else.

    **Eric Rudder**

    Yeah. Johnathan, any thoughts on that topic or?

    **Johnathan Hunt**

    Yeah. Honestly, to add to what Maya said, I tend to get a little prescriptive in the very beginning. She referenced, there's not really a one size fits. There's not just a right and wrong answer to this. What I tried to do is from the beginning, when I'm thinking about managed versus self-managed or third-party service provider, whatever, I think about three things really. I think the first thing I'm doing is, I think about who can do it better. Can we do it better? Does the hosting provider do it better? Is there a third party service or a third-party that does it better? What I'm doing in that scenario is, I'm considering buying expertise. That's what I'm buying, is expertise.

    The second thing I'm thinking about is honestly, unfortunately, costs. You have to think about the cost of a managed service or the hosting provider provided service versus total cost of ownership, of running your own solution. That isn't just the cost of building, but operating and maintaining and updating, all that goes into what you would consider a TCO. The last thing I think about is, can my team's time be better spent on more complex issues versus what might be considered the trivial routine of work. Essentially, what is the opportunity cost.

    **Eric Rudder**

    Anything to add to this topic as well or? Amit?

    **Amit Gupta**

    No. I agree with what he said. Johnathan, you mentioned, one of the things that we do see is, depending on a user's environment. If they have heterogeneous infrastructure, if they have complex environments, they may not be able to rely on the cloud native tools available. They may choose to a third-party solution and design and architecture that's agnostic to cloud providers.

    **Eric Rudder**

    Yeah.

    **Maya Kaczorowski**

    There's also a difference to add on to what you're all saying between the controls that I can use versus what I actually templatize or implement. Like if a cloud provider does not make a particular control available, accessible via an API, you are limited, unfortunately, in terms of how you can use that particular control. Versus you might choose to buy the expertise of someone who's already implemented a PCI. That doesn't necessarily mean using a particular solution, but using that expertise as to what might work across the streams, the solutions that you have. You are going to be limited also by the nature of what's possible based on whatever environment you're choosing to run in.

    **Eric Rudder**

    Fair point. Let's switch it around a little bit. Let's say you've worked together, you've made great tools choices, and you have a security issue. What are things that corporations should think about in terms of responding? When an issue comes up, it may be your first time facing a security issue or policy issue. I don't know if you remember the first time in your career Maya, when this came across your desk. It's that email you don't want to open in your mailbox. But what's some advice that you have for people watching, that the first time that they actually encounter an issue, how do they deal with it? What steps should they take?

    **Maya Kaczorowski**

    Hopefully, you have an incident response team whose job it is to deal with these kinds of issues. A couple things to point out. There's a difference between an issue, that's a vulnerability. That's something that is a problem with your environment, your configuration, et cetera, that no one's actively exploiting. And a security incident where someone's actually doing something bad actively in your environment, or you know that you've lost data or you know that you've eroded customer trust, et cetera. One is more urgent than the other. It might seem urgent to patch critical vulnerability and it is, but that's a different reaction and a different team and a different model than, "Hey, I've lost customer data." They're different scenarios.

    I'm going to assume we mean the security incident, the shit's on fire, let's go deal with that right away. Again, hopefully you have an incident response team if we're working on the cloud because I'm assuming that's the situation that we're in today. Make sure you understand the responsibility model of the cloud. There's probably some information that the cloud provider can give you for that incident as well. The first phase you're going to be in, is going to be in collecting information phase, finding all the logs, events, audit history of what happened in that area and figure out what's actually affected, what's the scope of the problem.

    You might be doing that simultaneously while you're trying to stem the bleeding. Whether that's change firewall rules or kill the service or whatever happens to make sense in that particular situation. Apply patch, et cetera, to address the issue. Collect information while you stem the bleeding. Once you have information, you might have a better idea as to how to actually go address and fix that problem and then you can go do so. Again, depending on what ended up happening, you might have to notify customers. There might be rotating passwords within your environment, et cetera, depending on what information was compromised. I think it's really important also after the fact to do a post-mortem and understand why this happened and what happened so that you can put in place different controls or second layers of controls to help prevent this from happening again in the future.

    **Eric Rudder**

    Yeah. Johnathan, anything to add for when your hair's on fire?

    **Johnathan Hunt**

    I honestly cannot put it any better than what Maya just did. I would say this, everything she said, please try to do it before an event actually happens. Try to figure out who you need to go to, what teams do what, who's responsible, what the on-call numbers are, what your third party, if you need to get a... The worst case scenario, you need the forensic investigator. Either reach out to this whatever agency. Have all that in place, ready to go. Do tabletop exercises, run through scenarios, know what your DR strategy is, know what your BC strategy is. Disaster recovery, business continuity in case people aren't familiar with those acronyms.

    Know how to get in touch with your tams at your hosting provider. Do that ahead of time. When the events happen, ensure people have access to that information, that document if it's an a handbook or some other location. Just make sure engineering and support and IT and security and infrastructure and development, everybody has access to that information, knows where it's at and knows how to get there. Then do exactly what Maya just said.

    **Maya Kaczorowski**

    To add to that, have some redundancy. If part of your proud problem might be like, you operate Slack ops and Slack is down and Slack is also how you communicate with anybody else in your team, maybe you need another way to communicate with everybody else in your team during an emergency.

    **Eric Rudder**

    Yeah. All right. We all agree [inaudible 00:34:43]. Amit, anything you want to pile on and add on it?

    **Amit Gupta**

    I would say hopefully people are taking notes. Those are two good examples. Pretty good playbook to how you manage your incidents. I have nothing to add to that.

    **Eric Rudder**

    Yeah. Maya, you brought up something in your answer too. I want to come back to you. You brought up the concept of review or postmortems. We have this concept of blameless postmortems. I'll throw out the provocative question. Do blameless postmortems really exist in the real world? What are the lessons that people could take away? What is the best advice we have to to people when they're doing these reviews and trying to take the learnings and apply them going forward?

    **Maya Kaczorowski**

    Yeah. I think they do exist. That being said, I'm biased. I used to work at Google, which I think invented the concept of blameless postmortems. Now I'm a GITHUB. They do exist in the real world and they apply both to security and also to operational incidents and that thing. I think it's particularly important to realize that humans make mistakes. When a mistake happens, the human can say sorry and can change their behavior and can learn how to do it differently. But a new human is going to come along and do the exact same thing unless we fix the actual system.

    I had an incident that I remember, where we accidentally made some customer data public that shouldn't have been public. We contacted the customer and told them. The person who was responsible for this said, "Let me personally apologize." I was like, "No. This is not your fault. The fault is the system that you make the data public. We should go fix the system." That to me is the learning and the takeaway from this. Is like, how can you make everything easier for your humans? Because you have a limited number of humans and they're going to keep making mistakes. How do you make the system prevent them from doing things that they shouldn't be doing?

    **Eric Rudder**

    Yeah. Wise words. Anything you want to build on in the reviews and actions to take on it?

    **Amit Gupta**

    I agree with Maya. The couple of things I would say is, as you're doing your postmortems for security or operational incidents, review the entire workflows, do a very comprehensive evaluation of your tools and systems. Don't just restrict the evaluation or the postmortem to where you actually saw the symptoms. The chain of a reaction or flow could be for systems downstream or upstream in the process. Take an approach where... I would say, just don't go with the prejudice or then go over there with the mindset that, "Hey, here's one way to solve the problem so we got to go around here." These systems are complex. They're already connected. Go with an open approach and look deeper elsewhere for the root cause. Because if you just fix the symptom, you can two months later, be end up in the same situation and may not be able to recover then.

    **Eric Rudder**

    Well, I think that's a good point. One of the things that... Also, I'll share a personal anecdote on my side. We actually got to test some of our business recovery plans because of COVID, because no one was in the office and because we have different set of tools and we got to check our redundancy tools. Some of our planning wasn't something we intended. We probably would've run a different style of fire drill. It was a test so took advantage of it. We hinted around it in the beginning. Johnathan, in preparing, I looked at some of the work that you guys have done. A lot of us are working from home now. I can tell by some of your backgrounds. They don't look very, TIGERA-ish or GITHUB-ish or GITLAB-ish. I'm sure a lot of people watching this now are watching from their homes.

    Is there anything that people should think about in terms of protecting their infrastructure and services? When I did my searches preparing for the thing, I noted that GITLAB did a phishing test on their employees when they were working from home. And actually one in five employees actually fell for the phish. I don't know if people were happy or unhappy. But that type of auditing and stuff is like a concrete action that we can take. But any advice to organizations that are working remotely and haven't thought about the security and policy implications, Jonathan?

    **Johnathan Hunt**

    Yeah. The first piece of advice and granted, I may be with a disclaimer. I may be a bit rusty. I've been working remotely for six years now so this is pre pandemic. If I could give a piece of advice for companies that have moved remote for obvious reasons, one thing that they may have not thought about or forgotten is, ultimately one significant part of security is threat landscape and reducing that threat landscape. If you think about the infrastructure that's still running in a data center somewhere, where you had this network domain and all this access to your 80 servers and app servers, I would consider disabling or suspending services that are no longer being utilized inside the network that was once connected from a desk or an office somewhere inside your building.

    That said, working remotely this day and age, most people have created external access to their production environments. Teams go on call. People go on vacation, teams are on call 24/7. Events happen in the middle of the night. They have to get up. Their cert engineers, their infrastructure engineers, the IT teams have to connect remotely. In the most simplistic form is, obviously make sure you're thinking about a couple of the best practices. I certainly recommend using an encrypted VPN. I certainly recommend the principles of least privilege. Ensure that in addition to that is MFA. Make sure you have multifactor authentication turned. As their workforce has moved remote, it adds a layer of complexity from connecting in an office to connecting in everybody's homes, on personal networks. Using what could potentially be insecure methods or insecure Wi-Fi. Maybe they're in their Starbucks. I think VPN, I think MFA is really important and ensuring you're reviewing access from the external parties.

    **Eric Rudder**

    Amit, anything to add to Jonathan about us all working remotely?

    **Amit Gupta**

    I think those are good. Those are definitely good tactics. I would add that, if we just stay with the example, Eric, you were mentioning that one out of five employees fell for the phishing attacks. The other thing to account for is, as you're designing your security architecture for this new way of working, think about your blast radius, think about the trust domains for the users. Just like a good developer, you think about your fault domain for the application similarly from a security perspective. That user falls for a phishing attack, what's the blast radius for that compromise in the environment? If you follow some of the things Jonathan, you mentioned, you can easily contain those compromises and have literally no exposure to your infrastructure or your environment, even if one of those users get compromised.

    **Maya Kaczorowski**

    Yeah. To add onto some of that, the 20% fishing rate is pretty good. I think that's industry standard, roughly. That's not something for people to be upset if they see something similar in their environments. The two strongest things I would do there are obviously, MFA and just make it okay to ask questions. For someone who was working from home and who doesn't have contact with the security team, where do they go ask a question of like, "Hey, someone called me claiming to be from IT." It's the same commotion that we have for people working from home is what we're going to have with the US election, where someone calls you up and tries to scam you into doing something.

    Everything has changed for everyone. We know that. Make it okay, make it easy for someone to get information. I think it's also the opportunity is, anyone who had a beyond corporate plan on the backlog was probably picking it up and dusting it off and going, "How do I do beyond corp again?" So it's the idea of, instead of using a VPN, having different trust levels for your internal applications and using things like IP addresses and times and machine identities, et cetera to then access to determine if a user should be able to access a particular application. I think that's also a trend that I'm seeing picked back up. Not that it ever went away, but pick up back up and force for more modern corporations.

    **Johnathan Hunt**

    If I could add one more thing too. I think what we can do better as security leaders, as security orgs is, let's not just wait for once a year to have this little 15-minute security awareness training video and check a box and now we're SOC compliant, everything's good. Check the box items rarely... I think research has shown that that rarely improves an organization security posture. Just keep security top of mind. What I try to do at GITLAB, at past companies is I send out just email updates. I sent out Slack channel updates like, "Hey, just a reminder to take a quick look at this phishing handbook page or something and how you can protect yourself." I tried to send something out around the holidays. I tried to send something out when there's a trend or an increase in the industry of certain types of attacks or malware or phishing attempts or whatever it is, or spear phishing.

    Just trying to keep security top of mind, is important. If you can manage it, I know it's difficult to do, but if you can manage it, it'd be nice if you could maintain regular security training versus just like, "Oh, go watch this video 15 minutes." And you're done for the year. Maybe figure out a way to incorporate security training into other types of policy refresher. Maybe when you do a GDPR video or is that where you have to do some sort of GDPR training, it'd be nice if there was some security step into that. Or code of conduct policy, it'd be nice to throw some security stuff into that. "Oh, take a look at the acceptable use policy, by the way. You have to sign off on that as well. Let us know if you have questions." I just think keeping it top of mind is important.

    **Eric Rudder**

    Yeah. Definitely good advice. We're running out of time. Let me close with one last question in a different vein in terms of our responsibility. The thing I think is fun to speculate on is, there's all this new technology coming. I'll just like to throw out, what are some future technologies and trends that you see cloud vendors and the industry taking advantage of, to make all of our jobs easier with respect to security and policy going forward? I'll start with Maya. I'll run down the panel one more time and then we'll wrap it up.

    **Maya Kaczorowski**

    That's a tough one. I'm thinking of it right now. I have more problems. I don't know that I have more solutions for you immediately.

    **Eric Rudder**

    That's okay. You could articulate the order in which we should work on them. That's okay.

    **Maya Kaczorowski**

    Some of the other problems that I see people starting to care about that they didn't care about before, things like firmware security or it's like, "Oh, I had all this hardware and it was great when I knew what all my machines were, but now that we're working from home and now that I have things in three different data centers and a private cloud, and and and. There's this layer across my entire organization that I know nothing about." That's an interesting problem I think for me, that I'm like, "Huh, I wonder if they're going to be doing in that space."

    **Eric Rudder**

    Yeah. Trusted supply chain, provenance, all important topics. Amit, any feature trends that excite you or you think that users will benefit from, shortly?

    **Amit Gupta**

    We come from the commodity world so suddenly I'm closer to those environments. It's a great infrastructure. It's a great architecture approach, building your application in a microservices based environments. I think the one thing I would say that users should definitely plan on their roadmap is, bringing security closer to the workload specifically in a network security environment. You will see if you're not already there, in your deployment that your workloads are going to grow and you will be beyond just that two, four, five clusters that you're running. As you grow and become successful, it's going to become harder and harder to design security.

    If you're following what we call as a traditional, in clay model, where there are gates in places and everything has to pass through those gates. Go away from those approach, bring it as closer to the workloads. I understand, it may not be as straightforward or as easy for you. So, taking pre-mental approach but definitely start moving in that direction because that's really the most scalable and most effective and most cloud native way to secure your environments.

    **Eric Rudder**

    Yeah. Jonathan?

    **Johnathan Hunt**

    Yeah. Two words, world domination. No, but for real though, honestly, the trend we're seeing all across the world, regardless of industry, regardless of professional personal space, is an aggregate like a complete solution and aggregated services. What do I see? I see AWS. I see GCP. I see Microsoft Azure. I see these companies adding more and more solutions to their platform. That's going to be a one-stop shop. Isn't that what we're trying to do? Many of us are trying to do with the product and services that we offer. Amazon started off as a bookstore and look where it's at today. That's what I see happening in the next 10 to 20 years, is just an increase in an already expansive set of service solutions and embed it into the hosting platform.

    **Eric Rudder**

    Nice. Well, thank you all for-

    **Maya Kaczorowski**

    I have a positive one now.

    **Eric Rudder**

    Oh, one more. Okay.

    **Maya Kaczorowski**

    The use of open-source. I got it, but it didn't get it until a couple of years ago where it's like, you can really put in... Say your team is three applications security people. You can spend one person's worth of time. And if they can treat that time to an source project and use that open source project, they get back 10 engineers worth of time. Based on people building the features that they need that work with their environment, et cetera. Again, assuming you don't go down a super, super bespoke path, the rise of open source security tools. Everyone's going to be, "We don't have that many in the grand scheme of things that do security, but we're going to have more and more and more open source security tools."

    **Eric Rudder**

    Yeah. I just want to cover myself just in case AI overlords are reviewing this video in 20 years. I'm totally on your side and respectful of you. That insurance is in my pocket. I want to thank you guys for spending some time on this, sharing your thoughts and best practices overall. I wish you all a good day. Thanks for spending some time with us.

    **Johnathan Hunt**

    Thank you.

    **Voice Over**

    Pulumi is the modern infrastructures code platform that empowers cloud engineering teams to define cloud resources using their favorite programming languages, including JavaScript, TypeScript, Python, .Net, and Go. By using familiar programming languages instead of templates or domain specific languages, teams can now manage cloud resources using the same tools, libraries and workflows that they use to write their applications. This means Pulumi works with your preferred source control management system and IDE with full linting, debugging, testing and code review capabilities at your fingertips. Pulumi integrates with popular CI/CB platforms so that your infrastructure deployments can be gated and deployed in the same pipeline as your applications, ensuring your infrastructure is ready to support new application features before you push them to production.

    Pulumi has over 40 integrations with leading software tools and popular SAAS platforms so you can stand up all of the capabilities your team needs in the cloud, on communities and on prem. It even supports sophisticated hybrid deployments. Pulumi provides an open source SDK and CLI for your development team and offers both free and commercial SAAS products to help you manage infrastructure state, user roles, infrastructure policies and more. With Pulumi, you can deliver quickly, deploy confidently, operate securely and scale easily. Try it today at pulumi.com.
aliases:
  - /resources/the-future-of-cloud-engineering-security-and-policy
---
