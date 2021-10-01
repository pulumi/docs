---
# Name of the webinar.
title: "All-Remote Teams at Scale"
meta_desc: "Learn how GitLab, the largest all-remote employer, has perfected building remote teams. From hiring remote workers to reducing distractions for your team."

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
url_slug: "managing-all-remote-teams-at-scale"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "All-Remote Teams at Scale"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "All-Remote Teams at Scale"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/NKxtz9cUqa0"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2020-10-08T10:00:00-07:00
    # Duration of the webinar.
    duration: "22 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Learn how GitLab, the largest all-remote employer, has perfected building and scaling remote teams. You'll learn how to hire remote workers and ways to collaborate without creating new distractions for your team.

    # The webinar presenters
    presenters:
        - name: Christie Lenneville
          role: VP of UX, GitLab

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi, my name is Christie Lenneville. And this talk is about Managing All-Remote Teams at Scale. This topic is near and dear to my heart because I lead the U-X department at GitLab the world's largest remote first company for anyone who isn't familiar GitLab is an end-to-end dev-ops platform that enables teams to plan, manage, deploy, monitor and secure the software they're building. I feel so privileged to have had the opportunity to both hire and lead one of the largest all-remote U-X teams in the world Today I want to talk about my team's one-year Journey from 16 to 60 U-X leaders, product designers, researchers and technical writers including how we work remotely both with our developer and product peers and how we collaborate within our own U-X department.

    I'll start by talking about what I learned from hiring so many amazing remote professionals over the last year. When I joined GitLab in February of 2019, we had 16 U-X practitioners, 10 designers, two researchers and four technical writers Today, we have over 60 U-Xers who are located all around the world. It was an incredible investment in U-X and our product has definitely seen the benefits of having such a strong U-X team. We talked to a lot of amazing people as we grew the team and I want to share with you a few things that we found to be important for hiring people who’ll succeed in an all-remote environment While my focus was on U-X. I think these learnings are true for many. If not most remote roles First, we tend to hire people who have at least some experience working remote. After the events of the past few months. that will be almost everyone.

    Candidates don't have to have worked all-remote, but we found that experience working at least with a distributed team really helps. All remote isn't the right fit for everyone and that's okay. Some people really prefer working face-to-face and they don't realize it until they try things a different way. We also conduct all of our interviews remotely. A remote interview shows how well the candidate can communicate over video. Not everyone is comfortable with this. Some people really thrive when they can engage with the energy in a room. We also ask candidates to share a case study of work they've done that they're proud of.

    We found that this is a good proxy for how they'll share work with their team for U-X. It's important for us to understand do they only share their end result because if so, what we're really interested in is their process not just their final output, but how they got there. This context helps the entire team have a better understanding of why they're building what they're building. It also allows them to give critical input early in the process so that they can move faster and end up with a better result. We also want to understand how they share their day-to-day work with their team.

    Do they document their work and share it broadly where others can find it and comment on it? That asynchronous communication is really important when you're working with an all-remote team. Without it people naturally make assumptions which can really slow things down. It also means you can lose the historical context of the decisions you've made, either because that context is in a few people's heads, or maybe they've left the company. We also look for people who are great collaborators.

    Do they proactively bring their cross-functional partners into their process as early as possible or do they throw their work over the wall and expect someone to understand and implement it? In an all-remote company this is especially important because your peers can't just walk over to your desk to ask a question or give feedback When collaboration happens early and often a team can move much faster and again achieve better results. Now I think humility is always important but it's especially important in an all-remote company. You want people who are proactive about encouraging input. At Gitlab we call this having ‘short toes’ because it's unlikely that someone can step on them. We want people who seek out different opinions and probe to find where their own ideas might fail. Facilitating this type of cross-functional conversation is how you end up with a great product.

    And lastly while we hire all over the world and our teams are widely distributed across time zones. we do think about a candidate's team and working hours to make sure they won't feel isolated. Many of these are traits that are important in any role but we found them to be especially important in all remote. Very quickly, if you're wondering how our UX department works, we’re a matrixed team that reports through the engineering department. That means we have a cohesive U-X team with functional leaders who support their teams career growth and our overall U-X strategy, but every U-X practitioner is embedded in a larger cross-functional team of product managers, developers and quality engineers who they work with on a day-to-day basis.

    This is a great model for us because we support a complex product that requires deep subject matter expertise. It would be very difficult for our team to solve technical problems that they don't deeply understand. Now, let's talk about managing all remote at scale. When I joined GitLab almost two years ago, I knew that our team would be rapidly expanding. It was important for me to quickly understand both what was working well and where we had opportunities for improvement. So, I spent my first month mostly listening to the team. I didn't want to make assumptions based on previous experience because every team and its culture are different. The worst thing I could have done was to begin changing things that I didn't understand but were actually working well.

    Instead, I wanted to focus on uncovering my team's pain points. So it was basically an internal research project. Based on those conversations, here are some themes I uncovered. First, they wanted more design collaboration. They were getting good feedback from their product managers and engineering partners, but it was different than the feedback they knew they'd get from other U-Xers. Also, they wanted more collaboration with their product managers. They often felt like they were missing context that would help them better understand the business problem they were attempting to solve.

    In a company where we frequently communicate asynchronously. It was easy for important tech details to get obscured. They also wanted more context about work that was happening in other product areas. It's always easy to get siloed in your own little part of the product and this is especially true when you're all remote, but when you're designing end-to-end workflows, you really need to understand the larger problem that's being solved. You also need a way to understand possible dependencies and areas where you need to maintain consistency. And lastly, even though they were all remote, they still wanted to feel like they had work friends because the social aspect of work is important, too. So, my approach was this: most importantly we would keep the good things.

    This was really critical to making sure the team was working effectively, but, it was also key to building their trust. They needed to know that I wasn't going to come in and mess around with the good things they were already doing. Also, we agreed to run everything new as a pilot and I actively invited feedback from the team about how well changes were working. We also agreed that we would stop doing anything new that didn't show a clear improvement in their day-to-day jobs, and we would go into any new initiative assuming that at least part of it was wrong. This encouraged us to continue iterating to make it better.

    Before we move on, I want to take a moment to talk about one of the good things that GitLab does as a company that we had to make sure not to lose in the U-X department and that's trust our team. At GitLab, we work hard to hire real, good people and we expect them all to be a manager of one, meaning themselves. When you're working remote, it can be easy to fall into a micro-management trap, because you don't physically see people working. But at GitLab, we assess our team based on outcomes not the hours they put in. They can work whatever hours they want as long as they're meeting their commitments and communicating asynchronously both with questions and updates. We can see everyone's progress in the work they produce and because we trust them to manage themselves, they do.

    Usually the biggest problem we have is making sure that people don't overwork. So, as leaders we stay up to date on their personal velocity and the expectations from their team. And, when we see someone starting to work too many hours, we find out why and help them and their extended team adjust. As an all-remote company GitLab is very focused on asynchronous communication. What's interesting is that GitLab runs on GitLab. We use our own tool to get our daily work done. That means we communicate mostly in issues which are what other tools often called tickets and merge requests, which other companies make all pull requests. But synchronous communication can have a lot of value. It can be much faster and more successful to understand and ideate on problems face-to-face.

    What I learned was that my team needed a little more of this synchronous communication, but, the challenge was not to over-correct. We needed to remain primarily asynchronous while giving them more of the verbal conversations they felt they were missing. So, we brainstormed together and came up with a few ideas. One of the first initiatives we rolled out was a pair designer program. This was to address the team’s concern that they weren't getting the amount of feedback and collaboration that they wanted from their functional peers. For designers who work in an office, they can look across the aisle and have a pretty good idea of whether they would be interrupting someone's workflow with a question. But, in an all-remote team, they had no idea.

    So instead they felt cautious about reaching out. So, we took a cue from pair programming and began a paired design program where every designer is assigned to another designer who is their go-to person for ideation and feedback. We make sure to assign pairs in compatible time zones, but we also try to partner people who wouldn't normally work together. This gives everyone an opportunity to see product areas that they wouldn't otherwise. Every six months we switch the pairs up so that we get to know new people better and also experience other product areas more deeply. There are no constraints on how the pairs work together. Some like to meet ad-hoc while others have a regularly scheduled sync. This time is for them, so it's really about what works for their partnership.

    As you can see, in the quote from Alexis on this slide, the designers really like the program because they get a perspective that they wouldn't have gotten from working alone, and they learn more about what's happening across our entire product. Like I mentioned before, we base this initiative on the idea of pair programming. So it's a great approach for many roles, not just U-X. We also started holding a U-X showcase for one hour, every other week, again to increase everyone's visibility into work that was happening in other product areas. Everyone in the company is welcome to attend, but outside of U-X it's especially helpful for product managers and developers. In a U-X showcase four designers share for 15 minutes each and we record the conversation and post it on YouTube so that anyone who isn't available at that time can still take advantage.

    That also lets us share the recordings broadly with the rest of the company, so they know what we're up to. In fact, anyone in the world can review the showcases, because we upload them to YouTube. This is important in an open-source company like GitLab where millions of people may be interested in the work you're doing. The U-X showcase is one of my favorite activities because I always learn so much from my team. What I might have absorbed from just being around my team in an office, we take the time to to intentionally share.

    Because we record it, we can also look back over time to see the progression of work that we've done If you'd like to see an example, I’ve added a short link to a U-X showcase by Jeremy our brilliantly talented visual design lead In it, he talks about our upcoming migration from sketch to Figma, our newly updated color palettes, and our new U-X foundations team that focuses on design ops and our design system, which is called pajamas. At GitLab, teams try to work as asynchronously as they can. That's a core philosophy at our all-remote company because not everyone is in a time zone that allows them to be in the same place at the same time. But, we have found that at the beginning of a project it's often helpful to get the team together for a face-to-face discussion.

    These kickoffs are cross-functional because it's important to have U-X, the product manager, and engineers all on the same page. It offers an opportunity for the P-M to clarify the business goal and the engineers to note any known constraints. But more importantly, it allows the team to brainstorm together about potential solutions. The key to these kickoffs is to keep them short, usually 30 minutes or an hour. Make sure the team comes in with context about the problem to be solved and clearly set the scope of the problem that the team is solving. Also, we make sure to document both the discussion and the outcome so that we have a record of the decisions we've made and anyone who can't attend can easily catch up. And, as with every other meeting, we record these kickoffs and post them to YouTube for anyone who wants to see everything that happened.

    It's always easy to fall into silos at work, where you work with the same people all of the time, but when you work all-remote, this can become even more of a problem one way our U-X research and design system teams overcome this is with open office hours. They hold them every two-to-four weeks and everyone in the company is welcome. There's a standing invitation on the company calendar, but they also advertise in Slack as a reminder. People are invited to come with literally any question they may have It's an opportunity for people to learn more about the teams, but also to bring up thought-provoking ideas. This works really well for our UX team, but it can be helpful for nearly any kind of role. As technologists, we all have our own areas of deep expertise to share.

    Now that I've covered how we infused a little more synchronous communication into how we work, I'd also like to share some asynchronous activities we added that the team really values. First, some of our designers record video walkthroughs of their design work to keep their teams up-to-date. Prior to this, they likely shared low-fidelity sketches or wire frames with their team in issues. The video walkthrough is most appropriate for when a design is getting ready to move into development. The point of the walkthrough is to step the cross-functional team through a prototype, sharing the end-to-end workflow and rationale for the intended solution. They also talk about options that they thought about, but discarded for whatever reason.

    This is a great way to make sure the product manager and engineers all understand the design. This is the same thing that designers in a traditional company might do face-to-face, but in an all-remote company, we have to make an effort to ensure that everyone has access to the information they need. But, this isn't just useful in the context of designs. Our engineers and product managers create video walkthroughs too, that cover their own strategic decisions. As always, we post the video to YouTube, but we usually post a link to the video in the issue too, so that anyone can leave comments or questions. If you visit the short link on this slide, you can see an example from Kyle, one of our designers for the security section of our product.

    The last activity I'll talk about is asynchronous sketching. As designers we’re used to getting our cross-functional teams in a room with a whiteboard, sticky notes, and markers to brainstorm together. But when you're all-remote, you have to get creative about how you lead these collaborative activities. It's still possible though. Most importantly you want to start by documenting clear, simple instructions for the team to make sure they understand what's being asked of them. Then you need to offer them a space to collaborate. We often use a tool called Mural, but we also use GitLab issues. You can see example of that in the slide. You can see that a variety of people contributed sketches to this activity including developers and product managers.

    The designer made sure to remind her team that good drawing is not the point. She even pointed out that her own drawings were going to be ugly too. If you're interested, you can visit the short link on this slide to see the asynchronous sketching session that Sun Jung facilitated recently for her team. It's important to remember that when someone shares an idea asynchronously, they aren't going to get the same feedback, they’d naturally get in an in-person session, through body language or facial expressions, and that can be really nerve-racking. So, as the facilitator you have to make sure to encourage them with supportive comments.

    Emojis are a great way to give feedback too and as always make sure the results are documented someplace where everyone can find them. Everything I've talked about so far has been a more formal activity, but often times people want informal collaboration too So, one of our team members set up a Slack channel just for this purpose. When a designer wants to some ad-hoc feedback and their pair designer isn't available, or if they have some extra time to give feedback, they pop a note into the U-X co-working channel. I also see them posting designs there for quick a-sync feedback.

    The last thing I want to leave you with is a core principle at GitLab, which is: document everything. You may have noticed that throughout this presentation I frequently brought up the idea of documenting both your discussions and your outcomes. In an all-remote company, that's probably the single-most important thing you can do, because when you're remote you have to be intentional about sharing information. At GitLab, we document absolutely everything. In U-X, we document our designs and rationale in issues and videos and we document our research findings in a searchable repository that's accessible to everyone in the company.

    Throughout the company for literally every meeting. we have a Google Doc with an agenda and everyone helps document the discussions we make. This is an incredibly democratized and empowering way to work, because anyone can add a topic to the agenda. And lastly, we document our team processes in the company handbook which is accessible to anyone in the world. The handbook is kind of amazing. It has over 7,000 pages and we update it dozens of times every single day. Everyone in the company is responsible for keeping it up-to date because it's a real-time view into how we work.

    If you're interested, you should check it out at the link on this slide. The last thing I'll mention is that even though we work together through technology, we're all still human and it's important not to forget it. That's why we schedule hangouts that are purely social. In an office you'd have these conversations at lunch or when you pass someone in the hall, but in an all-remote company, you have to set aside time for the fun stuff. We also try to check on each other just to say hi.

    Slack can be a good way to quickly reach out. It's also important to remember to give positive feedback for the good work that your peers do. At GitLab, we have a dedicated Slack channel just for this purpose and it gets many, many messages every day. Also, anyone can nominate a pear for a discretionary bonus of $1,000 and our company goal is for 10% of the company to receive a bonus each month. And, lastly we actively remind each other that we don't have to hide our families from our work. Kids and pets are always welcome in our calls and when someone apologizes for the interruption, we invite an even bigger interruption. T

    his is a picture of my own two kids and they've definitely participated in a few meetings. So in conclusion, all-remote works, you just have to be intentional about it. Be proactive about reaching out. Reach out again, when you don't get the information you need. Record and share everything and document everything. And lastly, be human, be kind to yourself and others, because work is just another part of life. Thanks for joining me today. I hope you enjoyed our time together because I did. Feel free to connect with me on LinkedIn if you're interested. Take care.
aliases:
  - /resources/managing-all-remote-teams-at-scale
---
