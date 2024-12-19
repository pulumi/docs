---
# Name of the webinar.
title: "The Future Should Be Uneven"
meta_desc: Let's talk about how we can provide more power to users to customize, configure, streamline, and understand what they are getting from us.

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
url_slug: "the-future-should-be-uneven"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "The Future Should Be Uneven"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "The Future Should Be Uneven"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/fhCtfzeYNeM"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T10:50:00-07:00
    # Duration of the webinar.
    duration: "23 minutes"
    # Description of the webinar.
    description: |
        "The future is here, it's just unevenly distributed" is something we say about why people on instant connection devices walk past people sleeping on sidewalks.

        We don't want a homogenous web, we want an accessible, personalized web. What I want and need is different than everyone else. And although the Dominos ruling mandates that everyone make their sites accessible, it's a non-trivial problem because different kinds of accessibility solutions can conflict with others.

        Let's talk about how we can provide more power to users to customize, configure, streamline, and understand what they are getting from us. Let's explore some accessibility settings that turn out to be just good universal design.

        You're going to leave this talk inspired to build an infrastructure that can support the glorious diversity of the future, instead of assuming that everyone is the same.

    # The webinar presenters
    presenters:
        - name: Heidi Waterhouse
          role: LaunchDarkly

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi, my name's Heidi Waterhouse. I'm a transformation advocate at LaunchDarkly. We're a company that does feature management, as a service and that means it's about delivering people, what they want, when they want it, in the way that they wanted it. This talk is actually about accessibility, but not just the accessibility that you're probably thinking of right now. It's about how to make the web more of what it should be and more of what it was before.

    I call this talk, "The future should be uneven". In 2003, William Gibson, the author of Neuromancer and a bunch of other cyber punk that probably you know about, said, in The Economist, "The future is here it's just not evenly distributed". And the more I think about that, the truer it gets because that's what we keep futurists around for, is to tell us what the future could be and is going to be and how it may yet be avoided. All of those things are in a futurists brain all the time. The dominant image that I had when I decided to put this talk together, was this one.

    This particular version of it was created by the Center for Story-Based Strategy, which is an Oakland company, just like us and they had a lot of great resources. I got stuck doing the research. I'm like, "Oh, I want to learn more about this". What we have is a portrayal of the difference between equity, equality, and justice or liberation. Equality means everyone gets the same thing, no matter what they need.

    Equity means that everyone gets exactly what they need, making it more or less difficult to access that. And liberation is when we take apart all of the barriers to access and make it easy for everyone to have what they want and what they need. When we think about the internet, we are the privileged people. We are pretty much the assumed user of the internet. We think of the internet as fast, like we're going to complain if it takes more than a few minutes to download something.

    We're going to be able to watch streaming. We think of it as, essentially free. It's not entirely free, I do pay a bill for my internet access, but that bill is a fraction of my daily earnings, not a multiple of it. At a lot of parts of the world that's not the direction it goes. So when I say the internet is free, it's not entirely free, but I don't have to think about what I'm doing on the internet because it's paid for and it's not painful for me to do one thing over the other, like this download is not going to cost me an appreciable amount of money.

    I think of it as usable. I can mostly do what I want on the internet, when I want to do it. And I think of it as useful. It brings me the things that I want when I want them, but the internet isn't like that for everyone. The internet can be really slow.

    My parents live in a cell phone dead spot. There's no cell reception up there, tiny mountain valley, but less than two hours from Seattle, still not a thing. I just drove through the Intermountain west and it was a lot of what we didn't have in connection. And sometimes there isn't more than one internet provider. And sometimes when we go back to my parents for the holidays, all the kids and technology come home, we all have this moment where, oh yeah, the internet that the rest of people have.

    And let me tell you folks, that is not great, the internet the rest of people have, if you're not living in San Francisco or a major American metropolitan area or a major European metropolitan area, even in Australia. And even then, slow American internet is maybe faster than a lot of people have because that's how it works. But it's really expensive. Like I said, sometimes we're talking about multiple days of pay to access the internet. It's broken.

    It's not useful. It's not accessible. It's something that causes frustration and difficulty when people are trying to use it. And it's hurtful. Not talking about the personal hurtfulness of users interacting with each other, that's a different problem and I'm not going to step into that today.

    What I'm talking about, is that it's hurtful to realize that someone has forgotten to foresee your existence, that somebody has never thought about how it would feel if they were the person in the situation experiencing this. No one has thought how they would feel about having lost a wanted pregnancy and still getting automated baby updates. How would that feel? We don't very often ask ourselves that question because there isn't an obvious A to B connection with money and we're paid to build the internet. And we think a lot about how much things cost and what they're worth. John Rawls came up with this concept that he called, the "Veil of Ignorance", which I really love.

    Basically what he's saying is, "How would you design society if you didn't know what position you would have in it?". We all know how we would design society for the people that we are now. But if you wanted to design society to be equitable, it would be different. So if we designed for what we have now, middle-aged women would get a lot more respect and cyclists would have a much better experience. I'd put in a lot more bike lanes and make driving a little more difficult because these are the things that matter to me.

    What he's saying is that you can design any kind of society you want, but you don't know who you'll be in it. Will you be a wheelchair user? Will you be a black man? Will you be someone who is oppressed by the society that you create? "Stop and think", he says, "About how your society that is ideal for you, is not ideal for somebody else". This is all very high flown philosophy. We're in the philosophy section of the talk here, but you're going to be okay. I like to think of this as the cake problem.

    Maybe your parents did this too. My mom would say, "Okay, you're going to divide. One kid is going to cut the thing in half and the other kid is going to pick which half they want". This optimizes everyone's experience because one child is going to do the very fairest job that they can because game theory says, the other child is going to pick the biggest piece of cake, right? So we can think of Rawls' "Veil of Ignorance" and designing society or we can think about how we would slice the cake that we have, knowing that we don't get to pick which slice of cake we get. I think it's a nice concrete way to think of it.

    So, what would make all of that philosophy apply to the internet? How could we make it work better in our modern connected world? I told you that the internet is slow and broken and hurtful. So how do we make that better? We give people consistent access. When we talk about accessibility, we frequently talk about it on one device or one browser or one application. One of the ways we can make the web better is to make all accessibility cross device and cross browser and make it really reliable and bandwidth aware. The idea of meeting extra bandwidth in order to access some accessibility setting, seems really counter-intuitive, but it would be really easy to have happen.

    So when I'm thinking about this problem consistently, it isn't just access to the internet, but also access to the things that we need to use the internet, whatever those are. I have a million repetitive motion injuries, and like I'm basically put together with floppy rubber bands and because of that, I need a split keyboard that allows tenting and lets me set my keyboard settings. So I don't have to use a mouse because mice are pretty much the devil. I went and bought myself this new toy. Well, I didn't buy it myself, my company bought it for me because I, the internet privileged, get that kind of consideration.

    I bought this new toy and it's really making me think about how accessibility is something we could be building into more things. It really is called the Ultimate Hacker Keyboard. The exclamation points are my own. So when we're thinking about how to make the internet better, let's talk about configurability. Let's talk about multiple inputs, fine-grain control because control of your inputs and your outputs and being able to choose your workflows and your settings and your meeting configurations, all of that takes a ton of cognitive load off what you're doing.

    I think of this as the difference between hunt and peck typing and touch typing. If I don't have to think about it, like where I'm going to put my fingers to make something happen, I can just think and the words come out of my fingers. We want that kind of seamless experience for everyone, but it isn't actually that seamless for everyone because we don't have an internet that's fully supporting that. So when I'm talking about multiple preferences, I'm not just talking about appearances, but the things that we can do deeper like adding no motion. I have ADD and maybe I'm distracted by flashy things on the side of my screen.

    It's not that I don't want people to get ad revenue from me, it's that I can't work if there's something going like this in my peripheral vision. So I really want to be able to control my experience of being on a computer and being in the world. They're the same thing right now, aren't they? Input sources are a great way to think about this. I type funny. I'm a Dvorak typer and this is what my key cap layout looks like.

    Actually it doesn't, it actually says, "Cordy", but it knows in its heart that it's actually a Dvorak. When I sit down at a computer, the first thing I do is change it over to Dvorak because that's what I touch type in. Everything else is this painful hunt and peck process. This configuration has been around for a long time. I remember in '97, '98, being able to sit down at a summer job and change their Mac keyboard to type Dvorak and I thought, "Oh, that's pretty cool".

    I didn't have to bring in a special keyboard or anything. I can just change the keyboard mapping and it knows what I'm saying. And then I want to talk about persistent customization because there's this thing, I have to change my keyboard at every computer I sit down at. I have to change my device settings, every time I get a new device. I used to love new technology day, like new phone day because it was a chance to get to use new, exciting technology.

    I was so excited. Yeah, now I hate it because it's so much work for me to port everything that I'm expecting over and get it to work the way that I expect. It's not exciting. It's just tedious to try and teach it when I want alerts and when I don't want alerts. So I think one of the things that we could be doing and thinking about is, persistent customization.

    Mozilla made a stab at this with their personas, the user profiles. I think we will begin to see more of a movement toward having portable pseudonymous profiles, that lets us experience the web and the world in the way that is most useful for us and I think it's going to have to be a portable language. My guess is, it will probably be an XML extension, but I guess we'll see. The reason I want this is because changing the input source of my keyboard is actually pretty late in the workflow of logging into a new computer. So I have to log in, looking at the keyboard and then I have to use a mouse because I haven't taught it that I'm not a mouse person, to get to the settings and then, maybe I have to log in, looking at the keyboard again, to get past security settings.

    And once that's all done, I can get down to the keyboard settings and change what I want to change. But if I had a way to take all of that information with me, something that said, this person types Dvorak and really likes it when her Windows go dark, when it goes dark outside, I'd be able to get to work that much faster and the web would feel that much more seamless for me. Let's talk about future vision because I'm telling you about this thing that doesn't exist. The pseudonymous preferences profile. When we're talking about accessibility, we're not just talking about disability.

    We're talking about giving people access to exactly what they need, exactly when they need it, with precision, without having to do a lot of work to get it and allowing people to set that up is going to make them feel so much more invested in what you're doing, because it's also them. Everything that people customize, they get attached to. It's pretty much psychology. If you made something yourself, it's more valuable to you, even if it's lumpy or weird-looking than something that you could buy. That said we are also all only temporarily able-bodied.

    Sometimes disability is situational. Sometimes it's permanent. So, when I'm thinking about this, Microsoft put out this amazing kit of things that you can do to think about disability. And they talk about the difference between permanent, temporary and situational disabilities. For instance, a new parent can only type with one hand because they have a baby in the other hand.

    That's a real thing, I've been there. That's why large phones are such a trial for me because I don't have small hands, but phones are very big and they expect that you have two hands to use them. And if you don't have the thumb adaptation turned on, it's very difficult, at least for me, to reach the whole screen with my thumb. That's an accessibility consideration. Like, maybe people don't have two hands to use their phones for any reason.

    I think that there's a lot of things that we could do with understanding that people are going to access our stuff in different ways and I'm excited about it. The web was born accessible. When you look at the RFC's of the very early web, this thing was born accessible. It was meant to be accessible and sometimes we screw that up. Sometimes we get it wrong.

    Sometimes we think that something is so beautiful that it deserves to overwhelm accessibility. I don't think that's actually true. I think it's possible to make beautiful things that are accessible if we actually work at it. When I was thinking about this, what I realized was that, prescribing how a webpage appears is like fixed mindset thinking. It says, "This is what my page is and this is how it should be".

    I have this argument all the time with all sorts of products. I don't always want my screen to be the full width of the monitor. Sometimes I would like it to be a third of the width of the monitor and even on a super wide monitor, some people aren't set up to reflow their applications like that. And when they don't give me that option, they're saying, "I believe my application is so important, it deserves at least half your screen real estate". And if you don't want to give me the chance to move that around, I'm going to make you really uncomfortable.

    So now I have to scroll to try and see everything or it's not going to wrap well, whatever it is that you do to adapt to that. Their vision of how the application appears, is more important than my experience. What I want for the web is, growth mindset. When we code semantically, the semantic web, which I'm not going to get into because it's super interesting but when I try and describe it, I'm like two steps away from pictures on the wall and red string connecting them all cause it's super cool, but it's also complicated. Anyway, the semantic web says, "We don't label things by how they look.

    We label them by their meaning". If I say something is an H1, a level one heading, maybe that's bold and in larger print, that's a typical H1 treatment, but maybe somebody says it louder, maybe it's bigger braille, the keys are raised higher. I'm not sure how it works, I'm not sure if it does work, but I think it would be possible, if there was a semantic interpreter. So when we're designing around using the semantic web to do what we're trying to describe and inserting that layer of abstraction, it allows people to take the instructions in directions that we didn't know they needed. We can't even imagine right now, like maybe at some point each one will be, each heading one will be holographic or 3D or augmented reality.

    I don't know. It could. If you've designed a webpage that doesn't constrain it, that is designed for growth, has things that are semantic, that are composable, you can take them apart and put them together out of all the parts. You want to design things that are opinionated, but not dictatorial. You don't want to lock people in divs that say, "This is the container and I guess, good luck figuring out what's in the container".

    You want to say, "Here's how I think webpage should go but if you have a better idea, please, here's the API, here's the CSS, I'd love to see what you do with it. I've given you the content, presentation can be your choice". But I've come to realize, that the whole point of talking about technical debt, isn't that debt is inherently bad, it's that we're making trade-offs that we're borrowing from future work in order to make this capital investment and that's a really exciting way to think of it because it gives us a lot more latitude to say, "What am I borrowing for? What is the future that I'm building for? How do I anticipate this going?". What I want to keep saying about accessibility and access in the semantic web, everything comes down to empowerment. I want to give users choice in their input and some of the choices that we give users already are, typing and speaking and eye trackers and mouse free movement.

    We think about as many things as we can, but because we're not all accessibility experts and even accessibility experts have different specialties, we can't know them all. So we're using that semantic abstraction layer as an API so that other people can access what we're trying to say. We want to give people a choice in how things are presented to them. I'm not great at watching videos. It's better now that I figured out I can speed them up, but some people really want visual input.

    Some people really want audio input or tactile input. We all want different things. Some people are deaf/blind and they want to be able to touch it. I want to choose whether I want to look at the whole thing or have it unveiled step-by-step. There are different learning styles that work differently for different people on different topics.

    Sometimes it's overwhelming to see all 27 steps of a procedure and so people want a smaller chunk revealed at a time. And some people want to understand the whole, so they understand where the steps fit in it and they want to see it all at once and having it revealed slowly would be irritating and annoying. One of the things that I think of, is I used to say, "I don't like anything animated on the web", but that's not true. I really love diagrams that are animated because then I can see how things relate to each other. But other people find the motion really distracting or even nausea inducing.

    So I think it would be great if we could have choices in how information was presented to us. I want choices in action. I want to be able to say, "Here's how I want to do things" and I want that accepted. I want to be able to say, "This is my workflow". For instance, G-Mail has a really opinionated way to handle email.

    It thinks that you should immediately sort something and either answer it or archive it. I've read this and I don't need to do anything about it or respond. But now by default, they've added a thing that says respond and archive. So if I just want to respond to get this out of my inbox, I can. G-mail is obviously built by people who ideally want you to clean your inbox out and yet there's all of this room for us to have thousands of unread messages or read messages in our inbox.

    So it's a little opinionated, but also gives us a lot of room to do things in a different way. I want to say, "These are the things that I approve, this goes with that workflow". When I say, "Yes, I've checked out your code, it seems good, thumbs up, you can go ahead and deploy it", I don't necessarily want to be the one who does deploy it. I'm not the one who wrote it. I want to give that back to whoever wrote it or onto the next person in the chain of approval.

    Blocking is so core to so many things and we don't really think about it because it seems negative to us. So there's blocking in workflows. That's like a thumbs down on your code, go back and fix it, here's what I found out, but it's also being able to block people. I think it's really interesting that slack hasn't implemented a blocking feature because they think of themselves as a workplace thing. And they don't imagine a workplace scenario where you would be harassed by a coworker to the point that you don't want to hear from them anymore.

    It's a kind of privilege, isn't it. And finally, personal optimization. When I think about my fancy keyboard or how I have my monitor set up or how I feel about my podcast, recording microphones, what it is that I want, is the thing that's best for me, my world, in the way that's useful to me. And I want to be able to accept and appreciate your world in a way that I can understand. And the more we understand that communication is both of these things, I think the more we're going to be able to build a web that allows us to translate between different modalities.

    That's really exciting for me. I really want the web to be more flexible, really want us to get out of this constraining idea of the page and the browser and the app and start thinking about what we could do when we combine these elements. What we could do when we combine them with different input and output devices. How is it, we could build a better world for everybody's experience? Here's what I want you to remember, build for your unimagined future. It's already around here somewhere.

    The future is here, it's just unevenly distributed and unfair. We don't want equity. We want something closer to equality or liberation. We can still work toward making the web more distributed, more powerful, more inclusive, more accessible. That's the thing that seems worth striving for.

    So, if you enjoyed this talk and want to learn more about LaunchDarkly and how we can help you build a web that has different modes of access and different ways to deliver, follow this link and look us up. Otherwise you can get some downloads. I'll be around for questions after this and the rest of the day. It's so great to talk to you and I hope you have a great day. Stay safe.
---
