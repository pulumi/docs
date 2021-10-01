---
# Name of the webinar.
title: "The Future of Cloud Engineering: Architectures and Platforms"
meta_desc: "Join Pulumi CTO and expert panelists Joe Beda, Al Sene, Jason Warner, and Corey Scobie as they discuss how architectures and platforms are evolving."

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
url_slug: "the-future-of-cloud-engineering-architectures-and-platforms"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Future of Cloud Engineering: Architectures and Platforms"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "The Future of Cloud Engineering: Architectures and Platforms"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/JoWznwb1-xE"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "47 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Luke Hoban, CTO of Pulumi, and expert panelists Joe Beda, Al Sene, Jason Warner, and Corey Scobie as they discuss how architectures and platforms are evolving and how that will impact the role of Cloud Engineers in the future.

    # The webinar presenters
    presenters:
        - name: Joe Beda
          role: Principal Engineer, VMWare
        - name: Al Sene
          role: VP of Engineering, Digital Ocean
        - name: Jason Warner
          role: CTO, Github
        - name: Corey Scobie
          role: CTO, Chef

# This section contains the transcript for a video. It is optional.
transcript: |
    **Luke Hoban**

    Welcome everyone to today's panel on the future of cloud engineering architectures and platforms. My name is Luke Hoban. I'm the CTO of Pulumi and I'm joined today by an incredible set of panelists with deep insights from across the industry who hopefully can share some of their insights on what they're seeing both today and into the near future in terms of the architectures and platforms that are being adopted in the cloud. So to get started I wanted to sort of invite each one of our panelists to introduce themselves. Tell us your name, what you're working on right now and just for fun maybe share your favorite database technology. So Corey, do you want to kick us off?

    **Corey Scobie**

    Sure. Thanks Luke. I'm Corey Scobie. I'm CTO at Chef software. Most people will know Chef for Chef but we're also the proprietors of InSpec and Habitat projects as well in the security and application management space. My favorite database management software is none.

    **Luke Hoban**

    I'm wondering how many good wrong answers we'll have here. I think that is [inaudible 00:01:12]. Great. All right. So maybe AL do you want to introduce yourself next?

    **Al Sene**

    Yeah. Hello everybody. My name is Al Sene. I am VP of Engineering at DigitalOcean. My responsibilities are infrastructure as a service. I manage all the software teams that develop our compute network storage products. I also have teams that are responsible for infrastructure management as well. My favorite database management tool I would have to say MySql I guess.

    **Luke Hoban**

    It's a good safe default answer.

    **Al Sene**

    Spend way too much time in there and are way too invested in MySql.

    **Luke Hoban**

    Great. All right, Joe do you want to go next?

    **Joe Beda**

    Yeah. Hi, everyone. I'm Joe Beda. I'm a principal engineer at VMware. I came to VMware through the Heptio acquisition. We're doing this thing called Tanzu which is bringing together all of VMware's Kubernetes and sort of modern application investments. Previous to that I was at Google and helped start the Kubernetes project. My favorite database software, I got two answers here. I'll give you two flip answers. I think... Number one is CSV. Number two is Excel. I think in general, I'm not smart enough to run a database. We'll just say that.

    **Luke Hoban**

    Great. Yep. Awesome. Then Jason.

    **Jason Warner**

    Hi Everybody, I'm Jason Warner. I'm the CTO of GitHub. Before that, I was the VP of Engineering at Heroku and I would say that my flippant answer is blockchain for the database. See if anyone's going to [inaudible 00:03:03] me for that. But I have to say that MySql treated us well at GitHub. Postgres treated us incredibly well at Heroku so I'm going to have to go with those two.

    **Luke Hoban**

    Awesome. All right. So yeah, to get over it then I think what we want to cover today is really sort of where folks see the cloud engineering platforms of the current and the future and just what you're doing inside your organizations and what you're seeing with the customers that you're working with and where you're seeing companies going.

    One thing to start us off maybe, at Pulumi I'd say really across the industry we've seen a tremendous uptake of cloud native infrastructures and a lot of that driven by Kubernetes. Would love to hear how folks think about the impact they're seeing Kubernetes having on the architectures and platforms that are being adopted inside organizations today. Maybe Jason do you want to start off on this one?

    **Jason Warner**

    Sure. But I'd like to correct that. I hear it's pronounced Kubernetes. Joe is that right? Is that how we're supposed to do that.

    **Joe Beda**

    Well, when we picked the name, we read it and we pronounced it and we went with it. But then you'll give a talk to folks who actually speak Greek and they'll start correcting you and it gets pretty embarrassing pretty fast. But I think Kubernetes, something like that is correct. I'm sure I'm butchering it now also.

    **Jason Warner**

    So to answer the question directly, I see a lot of adoption of Kubernetes and I see people what they're really trying to do is they understand that abstractions are real in the world and that is the most valuable one we can have in our architecture at the moment. They're trying to figure out... Everyone is talking about hybrid strategies and cross cloud and all of that sort of stuff but they don't fully understand why they need that yet so they're trying to hedge a little bit.

    But Kubernetes is very clearly the front runner of that and what they're really trying to do now and where we sit in the world, where GitHub sits in the world, we're seeing a lot of demand for what I basically call protecting the future self. They don't want to find themselves into any really bad decisions at the moment but they want to also keep themselves open for future optionality and we try to show them how to do that.

    **Luke Hoban**

    Al, how are you seeing things at the infrastructure provider level?

    **Al Sene**

    It's big. We have been using Kubernetes internally for our control plane for a number of years. We ended up creating a Kubernetes as a service product that we released about a year and a half ago. We're seeing a lot of adoption from that and interacting with those customers are using that product. You learn a lot about some of the flexibility that they have for their environments and they're able to deploy their containers just about anywhere they want.

    Certainly we'd love to have them all but we realized that the multi cloud strategies is facilitated by Kubernetes by so much. It just makes everything so much easier. Abstracts everything, simplifies application management, scaling, and all the goodies that cloud native developers just don't have to worry about. It just that next level of abstraction and simplification of application development. We're seeing a very, very big uptake in that option. Internally, we use it as well so it definitely helps to have that internal expertise as well and be able to have those features being used internally to manage our infrastructure as well.

    **Luke Hoban**

    Great, Joe, Corey, either of you. Joe I'm sure has lots of thoughts on this.

    **Joe Beda**

    Yeah, I mean I think... There's a bunch of impacts that we've seen with Kubernetes. For me the most interesting thing is when we talk to customers, it's everything from very small companies all the way up to sort of huge financials. When you get to these larger customers, what you find is that, "Hey, which cloud do you use?" And they're like, "All of them." "Where do you run?" "Everywhere." The name of the game these days for those types of users is that they're just looking for any way to start bringing a layer of consistency, a way of actually starting to approach this sort of intrinsic complexity that they have to deal with.

    I mean, hopefully, fingers crossed Kubernetes ends up being a net positive there in terms of hey, if you can get teams working on a platform that's Kubernetes based, you have a certain level of consistency across different environments. It's not going to be exactly the same between DigitalOcean and Amazon and on prem, but there's enough commonality there that it's not a total retraining, as teams, as skills, as people need to move between these different areas.

    Then the next impact that I think is really interesting is that the distributed control models that Kubernetes embodies have proved useful for managing containers and managing sort of application level stuff. We're starting to see folks use the Kubernetes infrastructure and sort of distributed system patterns in new ways that go beyond just containers. I think that's... We're still early on in that journey but I think it's a really, really exciting journey to be on.

    **Luke Hoban**

    Definitely. Corey any thoughts on the impact you're seeing from Kubernetes?

    **Corey Scobie**

    Yeah, I think obviously the industry impact is indisputable in terms of how it's affecting, not just the way that hyper scale web companies thought about getting applications to their computer infrastructure but the way now that enterprises are doing it as well. It has its both upsides and its downsides. We see companies that have decided that if it's right for Google, it's right for us and may or may not have the capability to be able to actually pull that off at the end of the day.

    I think there's no question that Kubernetes is the most impactful infrastructure compute technology of the modern era. Also, it comes with an operational paradigm that is wildly different than the operational paradigm that many of those same customers have experienced over the last 20 years and so there's a learning curve associated with that as well. But to just echo what others had said, the abstraction is really obvious and it helps decouple the development process from the operations process and I think those things are all good things.

    **Luke Hoban**

    Definitely. I think we talked a little bit about Kubernetes there. I think one of the other trends we've seen sort of in that sort of computing platforms layers [inaudible 00:10:00] have been serverless over the last several years. Curious if anyone here has thoughts on what they're seeing with serverless and how their sort of views on the serverless approach have changed over the last several years. I know this is something that for many people it has evolved in interesting ways. So curious what this group thinks about serverless.

    **Joe Beda**

    I'll go first. I think with respect to things like Kubernetes, I don't think it's an either or. I think serverless the easy place to start is things like function as a service. But honestly, I think that's the least interesting part of what we think about with respect to a serverless model. I think most usage of serverless would be what I would call glue. I mean, if you look at why are people using Lambda, they're taking an event coming from S3 and putting an entry into DynamoDB. This ends up being a cloud bash to some degree in terms of being able to just glue some stuff together.

    The interesting thing for me is that the power of glue goes with the square of the number of things you have to glue together. The reason why something like Lambda is so interesting on AWS is because there's a whole heck of a lot of events and there's a whole heck of a lot of services that you can glue together. The opportunity as an industry though I think is to actually find a way so that we can have a set of events and a set of services that are open and actually stretch across providers. Because I think we're going to find that if we can develop a thriving ecosystem that crosses these sort of mega cloud boundaries, it's going to be a richer world for everybody. It'll be bigger than any one single company can deliver.

    **Jason Warner**

    Let me jump in and say I agree with Joe entirely. I think that the intellectual possibilities of serverless are amazing and that they're completely out there. We can have a lot of fun with it. I love the glue way that he describes it, I would say that our current usage and expectations and how we engage with it is just horrendous. It's a terrible experience and in fact it borders on almost neglect to a degree.

    **Luke Hoban**

    You were so nice about Kubernetes.

    **Jason Warner**

    I think this has less to do with any one person and more of a feel for why this is important in the first place and just throwing it out there and seeing what happens with it. I think that we as an industry probably should agree that it's now time for it to mature from the experience perspective. I know Serverless.com is trying to do something and Amazon's trying their own thing. But to your point Joe, I think if it was a little bit more across the cloud, if we think of it that way as an ecosystem would be a better experience.

    Right now I feel like you have to buy into a camp. I think that that is my real issue. As an open source enthusiast through and through, someone who talks about developer experience across everything, I don't really want to buy into any singular camp.

    **Al Sene**

    Yeah, I definitely echo the same sentiments. There's definitely a feeling of you have to get it right. It seems to me that there are lots of opportunities in the future in terms of how we use it. The idea of having a repository of a bunch of functions that you can run or something of that matter would actually be very cool in terms of how you take open source and just have it be ready to go in some ways as a service. So far the usage I've seen has been tied to particular application being very specific, but there's definitely a general sense that we're still learning how do we use this? How do we make the most of it?

    And obviously, as a vendor it would be something that we're approaching and looking at how do we provide something that people can use? I mean, that's who we serve. But certainly as a company that is built on open source and champions open source we would like to see a larger adoption for sure.

    **Luke Hoban**

    Definitely. All right. So maybe switching gears to another kind of topic, I think one of the things that I'd say we've seen is a lot of organizations and probably that we've talked to, that I'm sure a lot of you guys talk to are today building their own sort of platform as a services for their organization on top of either Kubernetes or on top of the other cloud native technologies like serverless framework or things like that.

    We'd love to hear your thoughts on why are we seeing so much reinventing of the wheel in this platform layer? Why is every organization building their own one of these. Why haven't we as an industry helped to move that layer of abstraction up? Maybe I'll throw it to Jason to start since I know you've had experience working in one of the platforms that has made some progress.

    **Jason Warner**

    So at Heroku obviously is one of the platform as a service in the world. We used to joke that every time we walk into an organization we're going to see some variant of the platform as a service inside that organization. I think that people build it just to be honest with you because it's easy and it's fun to do it to a degree. It's the 80% versus 100% probability. 80% of this is likely, quite fun and rather easy to do. You can get going really quickly. Kubernetes is a good example of where in the past two, three, four years it's made it incredibly easy to get to that point.

    It's the refinements in the last 20% that make it incredibly difficult to get right. Now, do I think that organizations should do this? I'm definitely not against them doing it. I just think that they should go into a wide eyed. It's the equivalent of making a database. The first 80% of a database is really straightforward and easy to do. The last 20% if you're going to throw it into production and shard and scale it across multi [gios 00:15:49] is going to be a nightmare. You're going to have to invest billions of dollars into that. Is that what you actually want?

    **Corey Scobie**

    Yeah, you know it depends... It's funny Jason you mentioned the database analogy. I have this very fun memory of a long time ago in my career being at eBay and having the CTO of eBay at the time tell me that if you could make one change about eBay's distributed web architecture it would be that he would have his own database because for every dollar that they took in, eBay had to give their database vendor 30 cents of it.

    I'm not going to call out anybody in particular. But also, that's a super valid business reason to do it. To your point on pass right, We've gone through this period of democratization of decision making and enterprise IT where basically the CTOs and CIOs of the world have taken the chains off their teams and said go and make decisions. There's this incredible world of software that's available out there and parts and pieces but it's all a bunch of Lego kits and people are forced to pull it together and so they pull it together in a pattern that they think fits for them.

    The big challenge that many of the customers that we see at Chef having right now is that they have so many patterns in their organization that they can't operationalize anything at scale because everything's a unicorn. Everything is a pet and there's no cattle left anymore. I think the power of being able to pull all this open source software together and build your past that fits your organizational dynamics and everything is so alluring to folks. But the downside of it is that this democratized decision making has created sort of enterprise chaos at some level.

    We believe that there is a period of... A correction period that we're entering now where people are looking at ways to simplify the number of patterns that they have to manage at scale operationally. Whether that's to build a pass of your own or buy somebody's kit out of the box or whatever there's an opportunity there in the industry for sure.

    **Jason Warner**

    I would like to add one thing what you said there Corey. I think interestingly, the size and scale and sophistication of your organization is one of the more crucial questions to answer inside this. I can't tell you how many organizations I see that are two people and they said, well we'll get our product out the door once we fix XYZ about our infrastructure and I just don't understand why they're not so thrown into Heroku or DigitalOcean and use rails right out the door or something like that. Then work on getting the product market fit and then going to it.

    EBay building their own database makes more sense. With that two person startup making their own database doesn't make any sense. It has to do with where you are in that growth function too.

    **Luke Hoban**

    Corey you mentioned the period of correction. I'm curious if others have thoughts on what that period of correction might look like. First if you agree that we're sort of entering that period where there might be some more consolidation here inside organizations and if so, what do you think it would look like?

    **Joe Beda**

    I think a key part of the story there around correction comes down to security and compliance. It's all fun and games until you have some sort of breach. We do a lot of work with financials. There is a certain level of where's that sweet spot around empowering developers and application teams with a cloud like model where they can... I like to call cloud like. Not talking to a sales guy as a service. The key part of cloud is that I can get my job done without having to file a ticket or talk to anybody.

    I think the holy grail here is how can we have that experience for app teams so they can run hard but how can we do it in the context and the constraints that are often very unique to each enterprise? You end up with... I cut my teeth at Microsoft back in the day where it's like why does Word have all these features that I don't use? The answer is that they did studies and the average person uses maybe 20% of the features of word. Everybody uses a certain 10% and then everybody else uses a different 10%.

    I think this is one of the things that makes it difficult in complex scenarios to end up with any sort of one size fits all solution for deploying and managing infrastructure. Those are some of the things that I think drive people to want to create their own experiences. But it's not easy and I agree with Jason that you got to go in eyes open and know what you're getting yourself into.

    **Al Sene**

    Yeah, the complexity is... I don't know if we're entering a period of correction but the complexity is continuing to increase. At the same time we're getting more abstraction. There's this contradiction that is happening in the industry right now where every time you turn around, there's a new package out there that is doing something specialized but it is abstracting things in many ways. Nobody's a true computer scientists anymore. Everybody's operating at a much higher level than they were before.

    I don't know. For me, it is exciting to continue to see the simplification of software engineering, that we're building stuff much faster with an increasing level of complexity. There are lots of great advances and things that you can spin up today within a few minutes. It's mind boggling in terms of what it used to take to actually deliver value in the past. I'm wondering if maybe what is to happen is more of a meta architecture where there are these big types of building blocks that we all end up grabbing from and there's some variety there to match our specific application.

    But I agree that there's... That the increasing complexity overall is ripe for some methodology or some way of thinking that would actually simplify it a little bit or make it more tangible.

    **Luke Hoban**

    All right. The next question we've mentioned a few times. I think both Jason and Joe mentioned multicloud earlier in the conversation. Love to get folks thoughts on sort of what they see the future of multicloud looking like. Will we see the increased levels of consistency across the cloud providers? Will it be Kubernetes that is the level of consistency? Do we think specific industries will see more penetration around multi cloud architectures? Where do you see multi cloud going over the next few years?

    **Al Sene**

    As a cloud vendor, I like to believe that multi cloud is going to continue. What I see with a lot of our customers they use multiple clouds as a way to manage availability, as a way to deal with pricing, as a way to deal with pops around the world. I mean, there's a number of different ways that people use multi cloud technology to actually... The approach to architect the application. Certainly Kubernetes has been super helpful in facilitating that kind of approach. Deploying an application for sure.

    Whether there's consolidation in the future, who knows? But I think variety is good. Variety increases innovation, increases competition and frankly, it just makes things more interesting.

    **Corey Scobie**

    I'd like to add on there that I think... I don't see a real compelling reasons that cloud vendors would choose to standardize their interfaces or their service offerings across the cloud, at least in today's landscape. For the foreseeable future I think they'll continue to be drift in the different types of service offerings and the implementation of those service offerings over time. I do think that the abstractions that are coming along, in terms of how developers interact with the cloud services and resources underneath are going to continue to put the actual location of your workload further and further away from sort of the tip of the spear with developers.

    What I mean by that is that the most advanced organizations that focus on things like zero trust are not actually going to care where a developer chooses to put a function or a workload because they'll have a level of security consistency and access controls across the various different environments and so therefore the business is going to care less ultimately about this physical location that things operate in and they're going to care more about being able to leverage across different environments.

    That means both things that they place... Investments that enterprise makes in their own cloud architecture and also the investments that they may make in public cloud providers as well. I think we're ways away from seeing material paradigm shift because today most enterprises view it as Look, I'm going to be an AWS customer and I'm going to get a virtual private... A VPC in that environment and I'm going to go and put my stuff in there. I think in the future, with the right work on the security side, with the right work on the operational side, they're going to have less opinion about where things operate and more opinion about the efficacy and the efficiency of what they get at the other side of the transaction.

    **Jason Warner**

    I would say my thought here is there's a way in which I maybe think things should go and the way they're likely to go and also what you mean by multicloud too. I mean, we talked about the big three and how they provide compute or we can talk about what's going on with some of the CDN networks and what they're doing with computed edge is the transition there. Or there's a theoretical thought exercise where all the compute, the big three compute more like meet up internet providers in the future and the innovations happening on the other side of the line. I don't know what's going to happen.

    I'm an optimist and a builder so I think it should go a certain way because you want to give developers and organizations a certain thing, but I also don't think it's going to move as fast as I would hope it does as well. I think the industry will actually look a lot more like it does today in five years just with better tooling and operations.

    **Corey Scobie**

    Jason when I said abstractions I was looking at you and thinking actions.

    **Joe Beda**

    I think if we rewind the clock five or six years, everybody thought that there was going to be one big cloud and everybody is going to run in there be like one data center per continent and we're going to be done. Clearly that's not where we're at. I think what I see is that the infrastructure footprint for enterprises is just getting more and more complex. Whether you're talking about data sovereignty or sort of geopolitical issues, that's a force that's causing people to actually go wide.

    For specialized workloads, whether you're doing machine learning or graphics rendering or what have you, there are certain cases where it does make sense to manage your own data center. Then I think there's the whole thing around edge and all its various different types of things. I love the idea of the CDN as being a low latency cloud and we're seeing that start to evolve. But you take a look at... Amazon's doing these stores with cameras everywhere. If you've been to one of these Amazon ghost stores, you look up and it's just a layer of cameras.

    I don't think every retail establishment is going to look like that but it's going to be somewhere on that spectrum and they're going to need compute to be able to do that. Because you can't always get the back haul that you want to your data center to be able to handle that. Whether you're talking telcos, CDNs, retail edge, shippers want to be able to have infrastructure at their distribution centers so that they can actually download stuff to their trucks and stuff. This world is just getting more and more complex and I think that multi cloud as a term I think stands in for just dealing with the full complexity of the entire IT estate.

    **Jason Warner**

    Can I have one more thing to pile on to what Joe said there which is I think security and compliance is really going to have an impact on this whole conversation too. The whole geopolitical thing is it's super complex. I mean I have a premise that the rise of Chief compliance officers is going to become a thing because it is super difficult to navigate this landscape and changes all the time.

    **Luke Hoban**

    Yeah. All right. I think we just talked about a few of the sort of technology shifts especially around the edge and things like that. I'm curious going down a layer. In terms of the hardware, obviously the hardware that we have available has shaped significantly what the cloud looks like today and how we're building out modern cloud technologies. Curious if folks have any thoughts on any interesting shifts they're seeing in the hardware landscape they are going to have an impact on the platforms and technologies that we're using in the next few years.

    **Joe Beda**

    I think machine learning and devices is going to be a big change. I think being able to shift some of the stuff that you could only do in data centers with big models to something that can be done on devices is going to be a big change. I think 5G is going to be a big change in terms of orders of magnitude, more bandwidth and accessibility to connectivity. I don't think anybody knows exactly what that change is going to look like. It's just going to be different.

    **Jason Warner**

    I'll [inaudible 00:30:26]. Sorry.

    **Corey Scobie**

    Go ahead.

    **Jason Warner**

    I was going to say, the 5G was the one I was going to key in on and say I think that's going to have an impact. I don't know if it will but you're going to, at some point have mobile. All the cars that we have running around. The Tesla's running around. All the other EV's [inaudible 00:30:43] mobile units. Who knows what's going to happen there. Their phones are just getting more powerful. Obviously the machine learning is the big... The 5G, machine learning are the two big ones we're going to see. The rise of GPUs and the rise of what's going to happen over there with 5G. Other than that, I'm not a hardware guy.

    **Corey Scobie**

    I think what we're seeing though, there's an interesting inversion that's happened. Because if you think back and I'll age myself here, but if I think back 15 or 20 years in this industry what you had was hardware defined what was happening on the software and services side of the world. I actually think that we're... The hyper scale web companies pioneered the idea that hardware doesn't just come in one shape and size and that you could specialize it into specific workloads and the work that Facebook and Google have done in their own data centers to build hardware that was fit for the kinds of operations that they need.

    I think what we're going to continue to see now is increasingly specialized hardware that's coupled to the software side of the house as opposed to being hardware driving what's on the software side of the house. Nobody speaks about Moore's Law anymore because nobody cares about what the compute capacity of an individual processor is because we don't think about the world in that way anymore.

    As software architects, we think about there's an unlimited amount of compute out there. All I need to do is figure out how to interface that with the software that I'm building for the workload that I'm building. I think we'll continue to see hardware evolve as being the trailing function of requirements that are coming out of the cloud world. Out of the software world, out of the compute world as opposed to the opposite.

    **Al Sene**

    I just want to add that the advances we're seeing with GPUs and certainly on the networking side as well with regards to smart NICs, I mean those are technologies that are actually going to make a lot of difference. The speed to which the GPU world is evolving where every year and a half they have a whole new generation. I mean things are advancing so fast that it is bound to have huge impact on what we can do from an ml standpoint or data sciences and things of that nature.

    Those are going to enable a wave of innovation like we've never seen before. With 5G you're effectively going to have a machine learning device next door right. Your car's going to have so much power in terms of what it can do. It's really interesting how the innovation that we're seeing today is really accelerating. It's amazing.

    **Luke Hoban**

    Great [inaudible 00:33:40] I think Corey talked about how software is really taking a even more driver's seat role here in the cloud the way that's exposed to the cloud vendors and things. I'm curious what folks are seeing in terms of cloud native and modern cloud technologies and projects that you think are having a big impact today and that are going to have a big impact over the next few years in terms of the ultimate experience that the cloud engineers have with these platforms.

    **Joe Beda**

    I'll get started here. I think we're going to see an evolution of sort of application architectures on how people actually build applications that can take advantage of the extended capabilities that we see. Back in the day it was all three tiers sort of crud apps. It was like you got a database, you got a presentation layer, maybe you were using rails to get this stuff going. Then we had this whole sort of evolution around big data. I think now we're seeing a merging of these things where we now have some standard patterns for how you actually deal with fire hoses of data in a sane way.

    Being able to make these sort of reactive type of programming models work and making that be easy and accessible where you don't have to have a computer science PhD to build distributed systems. I think that's something that's really enabled and empowered with Cloud. I think one of the fascinating things when I was at Google was that we would talk with research scientists in research labs and they didn't have nearly the resources that we had just sort of between the couch cushions at Google.

    I think the accessibility of scalable infrastructure for everybody, I think we're still... That was an early result of cloud when early EC2 usage was New York Times scanning its back catalog and doing OCR. We're still I think early in terms of understanding and building consumable, accessible ways for building distributed systems.

    **Al Sene**

    On that front I think service mesh type architectures are actually being very helpful in simplifying that distributed system paradigm. That you can deploy an application out there and have it all be managed for you and scale up and down and so on. It seems to me that the simplification is continuing. That it is becoming easier and easier to do some of these things. I think a lot of the setup today is a little too complex still for people that are not hardcore developers.

    But I can foresee a time where it'll be super easy to just deploy an application and have it be distributed and worldwide and have CDN's involved. All of that is just a few clicks of a button for a developer.

    **Jason Warner**

    I agree with what both of them said. I think that there's a natural evolution that happens in software over periods of time. We've all gone through various versions of this. But when a new technology comes out, a new paradigm, a new shift, and it explodes and a whole bunch of things happen and complexity rains everywhere. And then it gets consolidated back down to a core set of principles and [inaudible 00:37:19].

    I think we're essentially in the explosion phase for a bunch of different things and it'll get consolidated back down here soon on a couple of different concepts. A good example of this is I cannot program in Java anymore, too much scar tissue from J2ME and Java server faces and all that sort of stuff. The complexity from the early 2000s that exploded and then when I found rails and Ruby and just fell in love with because brought some simplicity back. Well, we're having very interesting explosions happening in frameworks and things of that nature. But also services.

    Services have now gotten easier to write services, the complexity of managing services. If you look at it, there's an interesting thing that's happening at the moment which are... A lot of the 2008, nine and 10 unicorn, decacorn startup companies and Google's another example plays in here, is they wrote internal systems or services or things to manage the complexity of their business because it didn't exist. A lot of those people are actually spinning out and making new companies or products. This is largely what's happening with the cloud foundation landscape. They're bringing some of that simplicity to everyone else. Well, we're still I think in an explosion of complexity phase before the back to simplicity rains in.

    **Corey Scobie**

    Yeah, I agree with that Jason. It's starting to come back together. The big bang has happened and the expansion happened. You could definitely see it starting to come back together. I think when I look at... We were talking about serverless earlier and for all of its good and bad and everything else, the fact that you could take an engineer of virtually any experience level and say build me a massively scalable data Ingress system out of serverless and a cloud database capability is so democratizing to the companies that aren't the hyperscale web companies of the world. That don't have an unlimited amount of resources and don't have an unlimited amount of money to throw at those problems. Right?

    What I think is going to happen particularly with CNCF is the goodness that has come to building those kinds of interfaces, those kinds of interactions in the public cloud. Is going to become available to enterprises to run in their environments as well as Jason described, the explosion starts to come back together and reform into more operationalizable technology.

    **Luke Hoban**

    Definitely. Just to wrap up, would love to give everyone a chance just to give any parting thoughts they have. As you think about cloud engineering and the future of what people are going to do with architectures and platforms. What are your last parting thoughts for folks in this space?

    **Corey Scobie**

    I'll start. At Chef we have a hypothesis that one of the things that's going to happen in cloud engineering in general and in infrastructure management and software development is that most companies are going to start to go through again this period of consolidation. Ultimately what it means is to reduce the number of patterns that they have for operationalizing the various different things that they have to a smaller number of patterns.

    If you look at the way that the big technology players operate at scale and velocity, like the Amazons and the Googles and the Facebook's and the Netflix's of the world, they have hundreds of thousands of software developers working on 10s of thousands of projects simultaneously, but they only have a small number of ways that those projects actually get to operational state. The funnel gets narrow very quickly and there's a small number of patterns that they operationalize that.

    Our advice to enterprise customers that are looking to try and get that kind of efficiency and effectiveness out of their IT organizations is that you have to try and reduce the number of patterns that you're going to support in the long term. We see that happening now but I couldn't give that advice enough times to enough CIOs out there which is, if what you want is web scale efficiency and output, what you have to do is reduce the number of patterns that you're supporting at any given time. That's my parting piece of advice.

    **Al Sene**

    So Corey touched on very large enterprises and customers. I'll go to the other side. I think for people that are coming out of school, future developers, future entrepreneurs, there's going to be discontinued simplicity and simplification and abstraction of the development environments and tools. Standing up applications of massive complexity will be something that people will be able to do at the drop of a hat. We'll see people have an idea and get it spun up super quickly in ways that it would have taken years in the past years for somebody to develop.

    For me, I'm certainly very excited to see all these developments in computer science because it is actually allowing a lot of people to have access to technologies for standing up and creating businesses and developing new innovations and so on. I went to a conference in Africa, in Ghana, back in December before the world went on lockdown. There was just this huge energy. There was 3000 people at this conference. A lot of them were still at school and building enterprises. They were all super excited about Kubernetes. I can only imagine where something like this would be in five years or 10 years from now.

    That simplification, that abstraction, that innovation in the tools is really going to provide access to a lot of people. We'll see a lot of innovation over the coming years for sure.

    **Jason Warner**

    I think it would only be fair that we let Joe have the last word on this topic so I will go next. I think that if I can offer any parting advice for folks is it's almost inevitable that you get to complexity in what you're building and where you get to but don't do it too soon. Don't do it too early. Graduate into it. I think that with what we see out there, it's a great time, one, to be an infrastructure tech [inaudible 00:44:02] infrastructure tech I think is a lot of fun. Two, it's having its own renaissance in terms of everywhere is being innovated.

    If you're a large enterprise, I would say also don't buy all the hype you hear, ask your developers internally and ask other developers about what's happening actually in the market. Because there is a lot of stuff that will be said in the next five to 10 years about things that you likely don't need. Then developers don't get saddened or frustrated or upset about things that are happening of.... Other parts of the stack. I can't navigate the JavaScript frameworks anymore. It used to be vanilla JavaScript all the time. It's just not my thing anymore. It's had its own Cambrian explosion. I can't follow it. I'm not that upset by it. I just know there's a lot of smart people caring after and that's what I really care about.

    **Joe Beda**

    There's two things that I want to leave with. The first is I'm fundamentally I think an optimist. It's hard to be during this time but I think I'm fundamentally an optimist. I think there's a bit of a nihilistic view that we're just moving complexity around and that, hey, if we do this thing we're making this more complex but we're making this thing easy. It ends up being a zero sum game. I keep reminding myself that old [inaudible 00:45:22] we taught sand to think.

    There is so much complexity in our stack that we're not even cognizant of. We've done amazing things as an industry and there's no reason to think that that won't continue and we won't find ways to innovate and find ways to just fundamentally make things simpler and it's not a zero sum game around moving complexity around. Then the last thing is, I think it's got to be about community. I think we got to work to build ecosystems that again, create positive some environments for everybody.

    Such that as an industry, we're bigger than any single vendor, we're bigger than any one company. The work that I'm trying to do, working with a lot of folks at VMware around Tanzu is, you look at this complex, confusing... I call that CNCF landscape diagram. Beautiful chaos, right? That's a sign of innovation. We want to partner with our customers so that we can give them an on ramp into this environment so that they can benefit from it but not cut them off from it. I really want to see everybody embrace. How can we work together to build something that's bigger than any single one of us could?

    **Luke Hoban**

    Very well said and couldn't agree more. Thank you very much to all of the panelists here. I think it's been a great conversation and lots of really good insights from all of you. Thanks again and thanks everyone for joining us today. Bye.

    **Corey Scobie**

    Thank you.
aliases:
  - /resources/the-future-of-cloud-engineering-architectures-and-platforms
---
