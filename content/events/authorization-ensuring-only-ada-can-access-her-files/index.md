---
# Name of the webinar.
title: "Authorization: Ensuring Only Ada Can Access Her Files"
meta_desc: In this talk, you will get a high level overview of the authorization landscape and learn how Split approached these unique challenges.

cloud_engineering_summit:
    track: manage

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
url_slug: "authorization-ensuring-only-ada-can-access-her-files"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Authorization: Ensuring Only Ada Can Access Her Files"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Authorization: Ensuring Only Ada Can Access Her Files"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/WaBjJhCATWg"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T14:30:00-07:00
    # Duration of the webinar.
    duration: "22 minutes"
    # Description of the webinar.
    description: |
        When an application is small, few or even no permissions are needed.  However, as they grow larger, it is common to have increasingly complex permissions models.  While things are still small, it's easy to meet these needs through something built in-house, but as they become more complex, a better model is often needed.

        The world of authorization solves precisely this problem.  There are several common models, including ACLs, RBAC, and ABAC, which work well for different use-cases.  In addition, there are several higher level architectures for implementing one of these as well as a number of different products available.

        In this talk, I will discuss a high level overview of the authorization landscape.  I will then delve into more depth about how we approached this problem at both Box and Split and some of the things we considered.  I will include the pros and cons for the various options with regards to our use-cases and what we ultimately chose to do.

    # The webinar presenters
    presenters:
        - name: Joy Ebertz
          role: Sr. Staff Engineer, Split

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, I'm Joy Ebertz, and I'm a senior staff software engineer here at split. And today I'm going to be talking a little bit about authorization. But before we get too much into that, first of all, who am I? I like to write, I write about both running and tech stuff, so you can find my stuff on medium. I've worked at a box for quite a while, as well as Microsoft, a super tiny startup, and currently at split. I'm a backend engineer. I work mostly in Java these days but I've done a few other things.

    I've spent time at both box and Split on splitting up monoliths into microservices and microservices architecture in general. I've created API standards for both companies and rest APIs. I've also worked quite a bit on authorization again at both box and split. So today I'm going to go through, first of all, a little bit of the difference between authentication and authorization. Since a lot of people get the two confused, as well as a few definitions there. And then I'm going to talk a little bit about some of the different layers that you might have authorization within your company. And then I'm going to talk about some of the different types of access control. And then we're going to get a little bit into some of the typical architectures at the end.

    So first of all, what is authentication versus authorization? So Authentication or AutheN, is the process or action of verifying the identity of a user or process. Meanwhile, Authorization or AuthZ, is the function of specifying access rights or privileges to resources. i.e defining the access policies. So the example I like to use is if you are going into a bar and you run into a bouncer at the door, the bouncer is going to ask to see your ID.

    And first of all, they're going to check, is it a valid ID? Like, is this actually a government issued ID. Next they're going to ask, like, do you actually match the photo on the ID? Is this ID actually for you? So they are validating your credentials. They're making sure they're valid credentials and they're making sure that they in fact represent you. This is authentication. Next, they're going to check your ID for your birth date. And they're going to see if you are at least 21 years of age. And this is because they are now matching your age with the policy that the bar has about the age you need to be in order to enter.

    This is authorization, it is checking your permissions based on facts about you. Okay. So a few more quick definitions before we get into other things. Access Control, is the restriction of access. Access Management, is the process of restricting access. Identity and Access Management, is the framework of policies and technologies encompassing both authentication and authorization. This is also sometimes just called Identity Management. AWS Identity and Access Management or AWS IAM. Is Amazon's specific customer-facing authorization management feature. And I bring this up mostly because in a lot of contexts, when you see IAM, they actually mean AWS IAM. They might not actually specify to that, but that they actually mean Amazon specific customer facing feature.

    They don't mean the more generic one that I just mentioned a minute ago. So that's something to keep in mind when you're reading more about authorization. Okay, next, we're going to talk about a few of the different levels of authorization you might have. The first one is System and Infrastructure Authorization. The next one is Customer Facing Authorization features. And the last one is Application Level Authorization. So what do I mean by these? System and Infrastructure Authorization. So when you have a group of users within your company, so I work at split. So this is the split employees shown here. You're going to want to be able to restrict access to various things within your company. So for example, you want to be able to check if users should be able to access the servers, right?

    Or maybe should they be able to access to production servers, or should they be able to access the data, you know, in their databases, either MySQL, MongoDB, whatever, or so they'd be able to access specific applications. So in this case it might be Salesforce or, you know, something else. The other thing to note here is that different users within your organization are going to have different authorization. So for example, as an engineer, I can access our servers, but I cannot access Salesforce. Meanwhile, our sales folks can access Salesforce, but they can not access our databases. Right? So authorization is different by user.

    Next, I'm going to talk a little bit about the customer facing features. Which is at the totally opposite end of what authorization can mean within a company. So this is an example from box, boxes of file sharing system. So when we collaborate a file with another user, so if I own a file and I share it with you, I can specify some of the different access rights that I want to give you on that file. So for example, I can make you an editor, which means you can change it, or I can say you can only view that file, right? And so you can't actually change it. So I'm able to set authorization levels within the box application. This is what I mean by customer facing feature. Finally, we have the application level authorization, which is sort of putting together a bunch of different customers facing features and some other things into one authorization check within your application. So for example, within box, again, you might ask if Grace has access to a file, right?

    Maybe she doesn't have access, but is Grace on a team that has access, right? So we need to consider both of these things, but not just Grace's direct access on the file. So it's that user facing feature, but there's other questions as well, right? Like is Grace's organization active? Maybe they haven't paid in six months, and so we've deactivated them. So should she even be able to access box files at all right now? Or maybe this file has a specific feature related to it. And that feature is not turned on for her organization. So that's another thing we need to consider. Or maybe Grace got fired last week. And so she shouldn't be able to access any of the content for her organization at all. Her account itself is not active, right? So application authorization is putting together all of these separate questions and making a single decision about whether Grace can access that particular file. Okay.

    So that's sort of a quick overview of some of the levels of authorization and of these I'm actually going to focus on that last one. The application Level Authorization for the rest of this talk. Which isn't to say that this stuff doesn't apply to the other two, but that's going to be my main focus for today. So next I want to go through some of the types of access control. So if you do an internet search, this list is pretty exhaustive you're going to find. There might be a couple others, but as far as I could tell, they're basically not used. So this is mostly what you're going to find. It's a little daunting. We'll go through them a little bit at a time. So for the first two, these are both about who controls the access or policies.

    So the first one, Mandatory Access Control, is an operating system level access control where policies are controlled by a central administrator and users cannot override policies. Meanwhile, Discretionary Access Controls allows individual users within the system to grant access to objects. Most of the time, these implementations involve the owner of an object, granting access to things that they own to other people. Owners is not actually in the formal definition, but that's how it's most often implemented. So to use an example from box, these features can live side-by-side, they, they do need to be a little bit separate as you might be able to tell because they have sort of conflicting definitions, but they can live side-by-side.

    So again, let's say we have an organization with a box account and the administrator of that organization is Grace, right? She is the box administrator. And then Grace also has two employees within her company, Ada and Katherine. And there's also, you know, Dorthy, who's in a totally separate organization. She works for a competitor, let's say. So Ada owns a folder within her organization. Now Grace can set a policy that says that her, people within her organization, can not share content with anyone outside of her organization. This will be an example of Mandatory Access Control. Grace, as the admin is able to put a policy in place that doesn't, that prevents access to other people, and individual users cannot override this policy. Meanwhile, however, Ada can actually collaborate this folder with Katherine and now Katherine has access. Katherine previously did not have access to this folder, but now that she's collaborated, she does have access. So this is an example of Discretionary Access Control.

    ADA has granted access to Katherine as an individual user. So let's see these first two, who are, which is about who controls the POL access policies. These next three are all about how the policies are modeled. So we have who and we have how. Nor as fast as you might guess, you can actually combine these two and various permutations, right? So this Rule-Set Based Access Control is really just a combination of Role-Based Access Control and Mandatory Access Control. So I'm not really going to get into much depth about it, but it's mostly here to illustrate that you can combine these and have like pretty specific things that a lot of people use. And the final one I want to mention real fast, is this Policy Based Access Control.

    So PBAC and ABAC Attribute Based Access Control are really, I would say 99%, the same thing. There are, there are a few nuanced differences, but for all intents and purposes, for everything we're going to talk about here, you can consider them to be the same things. So we're just going to cross policy based access control off the list. But if you see that, know that it's pretty much the same as Attribute Based Access Control and everything we refer to about ABAC here.

    Okay. So now we're going to get into these three. The three about how the policies are modeled. So the first one you've probably heard of this, mostly in the context of operating systems, but the first one is ACLs. So Access Control Lists, and the idea behind ACLs is you basically have a list associated with each object in your system. And that list is going to say, give lists out the access rights for each user within your system. So you, on this folder, you might say, Ada can read or write, and Grace can read. And meanwhile, on this file, you know, Ada can read it and Grace can read it, right?

    So the big advantage to ACLs is that it's really fast lookup. So, you know, Ada is trying to see if she can read this folder, assuming you've done your indexing correctly, you can just immediately find that access control list. And then again, you should be able to immediately look up Ada, right? So really fast. Sort of, I guess the other thing that I didn't mention is this is also super fine grain control, right? You can very, very cleanly control exactly who has access to what. One of the big problems here, however, is storage explosion, right? So, you know, especially within a system like box, you're going to have, you know, not a couple of files, but a lot of files, right?

    A lot of objects in our system. So we have to have an access control list for nearly all of them, if not all of them, right? Meanwhile, we also have a lot of users. And so when you consider the combination of access between all of these users and all of these items, you can see how that gets really large, really fast. Similarly, within box, we have the ability to collaborate a group of people on a particular folder, and they automatically get access to everything underneath that folder. So everything inside that folder. Now let's say we want to move this folder into a different folder. We now have to recalculate the permissions of who should have access to this folder.

    And if we've individually written out a bunch of this information, we're going to have to both remove that as well as completely re decide what the they should have access to. And you can imagine this could be pretty complicated and slow depending on how many people, and how many folders deep, and a bunch of other questions, right? Meanwhile, similarly, if we have a user within our system who has access to a bunch of content and she leaves the company, we're going to need to remove her access from every single one of those access control lists. And again, this could take some time as we have to update each and every single record with her name in it. So slow update.

    That's a big problem. Okay. The next one I'm going to go through is our RBAC. And this is probably the most common type of access control. So RBAC has this really nice idea of roles. So the idea is you can assign users to roles and then you assign a set of permissions to the role as well. So if you have a user, Grace, who's an engineer, she gets the engineering role. And let's say, Ada is her manager. Ada is going to get both the engineering role and the manager role as an engineering manager. Now we can say that like engineers can read and write and managers can read and delete for example, right? And this is really nice because if Ada decides she doesn't want to be a manager anymore, and just wants to be an IC. We can really quickly just remove this rule from Ada.

    And she's going to lose all of the permissions that she had for only being a manager. Right? Similarly, if we suddenly realized that, oh, wait, managers, shouldn't actually be able to delete things. We can remove that permission. And every single manager is going to simultaneously lose the ability to delete. So again, it's really fast, it's really convenient. The big problem with RBAC was when we tried to fit that into the box use case. So in the box use case, we allow users, like I mentioned before, we allow users to collaborate individual items with anybody else, right? So we need this fine grain amount of control.

    And when we spent a long time trying to figure out how to map that to roles. And sort of the best that we were able to come up with was sort of just doing these permutations of who can edit, who can read, and you know, mapping things accordingly. As you can see, this really isn't any better than ACLs. In fact, it's probably the same or worse, and that we are now recording all of these permutations of who has access to what, and it has all of those same problems. We did come up with a few more fancy ways to do this, but we found that it didn't realistically save much space. And at the same time, they were really complex to make sure that they were right at all times. So long story short, this was just really hard to represent our use case. Okay.

    So the final one I'm going to talk about is ABAC, or Attribute Based Access Control. And the idea with the ABAC, is that when Ada goes in to see if she can read a particular folder, we're going to find the policy that's related to reading folders, right? And then this policy is going to go and fetch any missing attributes that it might have written into the policy. And based on all of those, it's going to make a decision and respond to Ada. So, because I was a little fuzzy, I'm going to get into an example requests and policy real fast. So an example request might be that this is again, user with ID 1, 2, 3.

    So Ada, wants to view, she wants to access this. And she wants to view this file with ID 4, 5, 6. So it's a subject wants to do an action on a particular resource. So now the policy might be something like if the action is VIEW. So that's basically saying if she's trying to view the folder and the enterprise of the resource is the same as the enterprise of the subject, then permit, access, otherwise deny. So we're just basically saying if Ada is in the same enterprise as the file belongs to, then she should be able to see it. So in this case, we sort of fill in the attributes that we have from the request.

    So in this case, the action, as we said is view. So we're going to say a views view, and then we don't actually have the enterprise of the resource, right. But we do have the resource. So we're able to take that resource information that we have, go out and fetch the enterprise, and return and fill that in now, right? And the same thing with the subject. We can go out and fetch the enterprise of Ada and bring it back and fill it into this policy. And now we should have all the information we need in order to make a decision. So the really nice thing here is that we have fast update again. Because in this case, if we go out to a service and we changed some information there, or we change how something's calculated, it'll update immediately. Same thing with the database, right?

    So we can change Ada's access instantaneously. And it can also handle pretty complex use cases. So for example, if we have a file that's locked, then we can prevent access. Or maybe there's a legal hold on it. We can prevent access. So we can take all of these completely desperate features and combine them together to make a decision about whether Ada has access. And these features don't necessarily even need to know about each other in order for them to work together for that final decision.

    The big problem you might imagine, is that this whole system can be kind of slow because you're making calls out to external systems. And it began because you're calling external systems. If one of those goes down, your authorization decisions are going to go down. So it's kind of, it's kind of a mixed bag there. So throughout all of this, our choice at both Split and box was to go with ABAC. So why ABAC? So first of all, it's an industry standard. That was something that we really wanted.

    We didn't want any homegrown solutions that nobody else knew about. Secondly, there's no permissions update lag. So that's something that was super important at both places. If a permission has changed on something, we wanted it updated immediately. We didn't want our customers to see it lag there. We wanted it to be something that was relatively space efficient. And as I've kind of outlined just going into this so far, it sort of just best fit our use case.

    ACLs and RBAC are a little bit too simplistic for some of the use cases we had. And so we wanted to be able to represent something that was a little bit more complicated. And similar to that, I'm just going to mention real fast that it is possible to still have customer facing features that are, that are simpler built on top of a more complex system underneath. It's very hard to do the opposite. So in the box use case, they have that RBAC system built on top, but then they still have ABAC solution underneath.

    So what does the typical architectures for this look like? So first of all, a typical web application might look something like this. You have a call that comes in, it's an API gateway, which calls a couple of different services. Within that, the API gateway itself might be an obvious choke point in place to put the authorization service. So you might have the API gateway call-out to the authorization service, to decide if that user should have access to whatever end point they're trying to, trying to call.

    Or you might try to save some time there even more and put it into the API gateway itself, so you save that network call. There are some API gateways out there that include authorizations. So that is an option. Another thing you might consider is having it as a separate service that the individual services call before they execute their main code. And similarly, you can do this as a sidecar. There are pros and cons to each. It's a little less obvious, which is faster than it might seem at first due to caching and a few other things.

    But those are two different options that you might have there. So what do we do at box? At box we have the API gateway, as you see, but instead we went ahead and had it at the service level. So when the API gateway sends a request to the service, we have the Pepin, the filter chain, which is going to automatically intercept the request before it goes to any of the code in the service and calls out to the authorization service, which makes the decision.

    And in boxes case, we were using Balana, which is an open source authorizations ABAC solution. And for our PEP, we built a custom library using the Jersey filter chain, like I mentioned, and Jackson annotations. So what do we have at split? It's pretty similar, a little bit different, but pretty similar. So again, we're using the PEP as a filter before we call the service. In this case, we're calling to a custom built authorization service. That's mostly just a wrapper on top of OPA.

    So OPA is another open source solution that we're using under the hood. And that's going to contain most of our policies, but we're fetching a lot of the attributes in the service itself. So it allows us to do a little bit of performance optimization there. Again, I guess I mentioned already, we're using OPA under the hood. And again, we're again doing a custom library with the Jersey filter chain and Jackson annotations. So that is a whirlwind through authorization. Thanks for sticking with me.
---
