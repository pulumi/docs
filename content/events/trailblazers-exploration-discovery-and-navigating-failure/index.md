---
# Name of the webinar.
title: "Trailblazers: exploration, discovery, & navigating failure"
meta_desc: In this session, you’ll see what we can learn from trailblazers and how adopting techniques for exploration can help us build more reliable systems.

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
url_slug: "trailblazers-exploration-discovery-and-navigating-failure"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Trailblazers: exploration, discovery, & navigating failure"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Trailblazers: exploration, discovery, & navigating failure"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/wU2BGZv6VHA"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T09:00:00-07:00
    # Duration of the webinar.
    duration: "14 minutes"
    # Description of the webinar.
    description: |
        Why is it that trailblazers seem to adopt new technologies unscathed, but then mainstream adopters come along and follow published "best practices" only to experience major incidents and outages?

        Lewis and Clark's epic 8,000-mile expedition into the unknown wilds of the American Pacific Northwest led to the creation of the Oregon Trail, and along the way only lost one team member. Years later, with maps in hand, wagoners would attempt this journey, and along the way, an estimated 20,000 died.

        In this session, I’ll share what we can learn from trailblazers and how adopting techniques for exploration (even when operating in well-known territory) can help us build more reliable systems, and maybe even prevent you from dying of dysentery!

    # The webinar presenters
    presenters:
        - name: Jason Yee
          role: Director of Advocacy, Gremlin

# This section contains the transcript for a video. It is optional.
transcript: |
    In 1804 Meriwether Lewis and William Clark set out from camp to Debois near present day St. Louis, Missouri. And they'd embark on an epic expedition that would traverse over 8,000 miles. They'd catalog dozens of plant and animal species that had never been documented before. And they'd map the lands between the Plains of the Americas and the Pacific Northwest.

    Their work helped create the Oregon trail, which was used by over 400,000 people to settle in this part of the country. But one of the stark contrasts between the wagoneers and these trailblazers is that an estimated 40 to 60,000 people died on the Oregon trail. Over one in 10 people that attempted the journey. Well, Lewis and Clark's team only saw one death. Sergeant Charles Floyd died early in the trip due to a burst appendix.

    And that's not to say that the team didn't have their challenges. They certainly did. In fact at one point Lewis got shot in the butt because he was mistaken for an elk, but the differences are stark. So why is this? what is it about the Lewis and Clark team that was so different? Lewis and Clark's team wasn't made up of professional explorers. Now you could argue that they were far more skilled than any of the homesteaders.

    And there's definitely advantages to having a team with a broad diversity of skills that can tackle anything you might encounter. But I think the thing that made the biggest impact is the mindset that goes into creating teams like this. The mindset of not knowing what to expect, the mindset of exploration. The Explorer mindset is constantly asking what's next? Where can I go from here? And how can I prepare for the unexpected? The follower mindset has no vision for the possibilities of the dangers because it's been given a map. You see the thing about maps is they make us a bit complacent.

    When you're told where to go and what to do and what to expect. It makes it really difficult to step outside of that and to prepare for the unexpected. And we often see this with the complex technologies that we work with. It's so easy to use the pre-baked AMI or containers, or just install the Helm Chart, or even better use a SAS offering so you can just subscribe to the service and not even have to worry about the operations. And I'm not saying that any of these are bad.

    They're good. No, they're great. And I use a lot of these things myself to get quickly set up, but with all of this, we risk falling into that follower mindset. And it means that when we face incidents, we're more surprised and we're less prepared to deal with them. So how do we prepare ourselves? How do we regain some of that explorer mindset? I think the first thing that we can do is to try to reorient ourselves and get a better sense of the signs of danger.

    Most of us have experienced incidents and a lot of us have experienced so many that we've got weird PTSD issues from them. Incidents are like encountering a bear on the trail. Incidents are obvious problems. And if you run into enough bears, you'll eventually get really good at running away. Or maybe you won't and you'll just become another casualty on the Oregon trail.

    But constantly getting attacked by bears, doesn't help prepare you for avoiding them in the first place. You need to start in a safer place. You need to start to learn how to evaluate your environment for those signs of danger, to look for the bear tracks or scat or other telltale signs that a bear will be close by. And this is why I love chaos engineering. Chaos engineering is often described as intentional failure, but I think that can be a bit misleading.

    It's not about creating incidents. It's about building a better understanding so that we can identify problems before they become incidents. And I think chaos engineering helps us to regain that explorer mindset in part because you start by questioning what you think you know. The chaos engineering process begins with observing your systems to establish a baseline and then using that to create a hypothesis. What do you think will happen? How do you think your systems will react or behave and beyond just your application or individual services, how will this be reflected in your monitoring systems or in other dependencies? What sort of alerts should get triggered? In the chaos engineering community we often talk about starting experiments with a small blast radius and a small magnitude.

    What's the smallest number of hosts or services or containers that we can impact with the smallest amount of failure in order to derive some data to pick up on those signals of danger. We also set abort conditions. Abort conditions are guardrails, so that we can halt a failure and prevent any real damage. It's only after defining your expectations and the safety parameters that you run the experiment by injecting failure and collecting data. Afterward do analyze the data and determine if any action steps need to be taken.

    Finally, you share your findings and you iterate. Once you validate what you know, the next step is to start imagining what's possible and where potential factors can come into play. For example, if I'm validating that Kubernetes will automatically reschedule a pod when it fails, and it works as I expect, I now have a better baseline to start exploring the ways in which this might not work. For example, if the cluster didn't have enough resources such as memory. Our systems have become extremely complex and it's nearly impossible for any of us to become masters of every software and service offering out there.

    Following maps, whether in the form of pre-packaged config files or dodgy, best practice tutorials or random stack overflow how-to articles, those are all easy ways for us to get halfway down the trail, completely unprepared for the inevitable troubles that will arise. Adopting an explorer mindset and using a bit of chaos is how you can prepare. Chaos engineering is how you can confirm what you know, and safely discover, explore, and prepare for the dangers that you weren't aware of. And that's how you ensure that everybody in your party reaches the destination.
---
