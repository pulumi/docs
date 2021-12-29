---
# Name of the webinar.
title: "Forecasting the Future: Creating a Radar for Risk"
meta_desc: In this presentation, we'll talk about Risk Radar, Netflix's forum to collect and make sense of emergent sociotechnical risk both from experience and risk.

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
url_slug: "forecasting-the-future-creating-a-radar-for-risk"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Forecasting the Future: Creating a Radar for Risk"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Forecasting the Future: Creating a Radar for Risk"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/J1X_VgN6mus"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T15:30:00-07:00
    # Duration of the webinar.
    duration: "22 minutes"
    # Description of the webinar.
    description: |
        In the mid-20th century, predicting the weather was still one part science, one part intuition, and one part luck. But as computers, data collection, and modeling have steadily improved, we now produce staggeringly accurate weather short-term forecasts.

        In tech, we're still early in our journey to more deeply understanding and modeling our world through learning from incidents. As we improve, what if we could start forecasting incidents?

        In this presentation, we'll talk about Risk Radar, Netflix's forum to collect and make sense of emergent sociotechnical risk both from experienced-incidents, and risk which can predict angry, incident-filled skies.

    # The webinar presenters
    presenters:
        - name: J. Paul Reed
          role: Senior Applied Resilience Engineer, Netflix

# This section contains the transcript for a video. It is optional.
transcript: |
    This is "Forecasting the Future: Creating a Radar for Risk".  Now, before we get started today, I wanted to give a shout out to Kat, Laura, Maddie and Wendy.  Those are the folks that put on the Pulumi Cloud Engineering Summit and worked really hard to do so.  I know a lot of folks think of virtual conferences is maybe easier than putting together an in-person conference.

    It's not, it's just a different type of work but it's definitely the same amount of work.  And I know a lot of us thought that we would be in-person by now.  So I'm looking forward to seeing them and you in 2022 and I just wanted to thank them for bringing us all together here today.  All right, let's get started.  So, a lot of you have heard of this idea of AIOps.

    You know, it's a game changer.  This idea that maybe, if we can teach the computers enough about our work, they'll be able to detect incidents before we can and maybe even auto-remediate them.  It's a big promise.  A lot of Ops teams kind of wondering about this, you know, hey, is it just another addition to DevOps, you know, DevSecAIOps.  And we keep adding letters to that, to DevOps.

    And rightly so, I think there's a little bit of skepticism.  You know? It may seem like we're just looking at sort of a crystal ball of sorts, and, you know, except now it's computers that are looking at this crystal ball, you know? And admittedly, it's kind of hard to trust these things because looking back at one of those AIOps articles from the previous slide, you know, the clip art that they actually used here is a tarot card, which is not particularly confidence-inspiring.  I don't know if I, might want, you know, computer auto-remediation based on a terror reading as it were.  One of my favorite guys, Dave Han, has a great quote about this.  He said: "if you're having enough incidents to train a machine learning model, you probably have more pressing problems to look at and think about."

    And there's, I think something to that.  So, for today, I'm gonna talk about AI, but I'm referring to something different, the Already-Existing Intelligence that we have on our teams.  One that we use and brain to our systems every day as expertise and how, when we interact with each other and with other teams, that intelligence is more than the sum of its parts.  When we wrangle these systems and operate them day to day, usually pretty successfully.  So, I'm talking about that expertise and that already existing intelligence within us.

    A little AIOps in that context.  So Risk Radar, what is this risk radar thing? We're gonna dig into that.  But before we do so, my name is J.  Paul Reed, for those that don't know me.  Most important thing on here is Twitter, @jpaulreed on Twitter. Background in Build/Release Engineering, I did instant consulting, and have a Master's in Human Factors and System Safety, which I mention because a lot of these ideas come from that field of study.  Now I'm at Netflix, on the Critical Operations and Reliability Engineering team.  Get asked a lot what I do on CORE at Netflix.  I once gave this answer: "I navigate the organization to observe signals of systemic socio-technical risk, so we can activate our adaptive capacity to address that risk." And somebody came back and said: "So you run around the building gossiping with people about broken computers?" Which had a reaction to, but you know, maybe there's something to that.  I don't know. I don't know.

    So, let's dig into a "Radar" for "Risk," you say, "what do we mean by that?" Well, it's good to offer a little historical context before we dig into to the benefits of risk radar and the details of how you would build your own.  So, risk radar was a repurposed meeting, originally.  The meeting was originally called the "IRL": Incident Risks and Learning Meeting, where we talked about incidents and then risks and learnings associated with those incidents.  One of the big changes that we made when we renamed and repurposed that meeting, was to go from talking about specific incidents to Risk Themes.  And so, in the previous meeting, a lot of times to folks' teams, we had asked teams to come present their incident that they had run into.

    Specific incident.  And now we shifted more to risk themes.  Incidents still play a role, we'll talk a little bit about that in a sec, but we're talking more about thematic risk in risk radar.  As I mentioned, teams would come and present.  We moved from a model of presenting to discussing.

    We found that setting up a presentation to come to that meaning, a lot of times felt like a book report.  Felt like extra work.  So we don't have teams prepare in that way anymore, and it's more of a discussion.  Also, it's less of a retrospective about, again, about specific incidents, and more focused on emergent discussions, emerging paths that come about, around these risks, themes that we talk about.  So again, even though we bring in some previous stuff to inform our discussion, we really let the conversation kind of go wherever it's gonna go.

    And it's less focused around the framing of a particular, specific incident.  Again, even though we use those.  We'll talk about the details of how we do that in a sec.  So the recipe, how would you put this together for your own organization? Well, you obviously have to have a Scheduled Forum.  A meeting to handle it in or, or conduct a risk radar in.

    We solicit and collect risks beforehand.  And so, I sent out an email a couple of times before the meeting, and ask folks to share their risks before the meeting so that we're not spending a ton of time doing that during the meeting.  There's also a benefit that we'll talk about in a second, but then we do all of this collection sorta beforehand.  We also do some incident and OOPSies analysis that we bring to the meeting.  OOPSies, by the way, is a program that was started by Lorin Hochstein, "norootcause" on Twitter, which is one of my favorite Twitter names.

    Nora Jones is involved, as well Ryan kitchens.  Started the OOPSies process.  It's really near misreporting.  It's things that could have gone very wrong, but didn't, and then people will sort of do a retro with them and their team and write it up as an OOPSies.  We'll take some of those analysis from actual incidents or OOPSies, bring those as well.

    A lot of times we'll merge the risks that folks have raised, and then look and see if, we see any of those risks patterns in the analysis of recent incidents that we've had.  Published and Distributed Minutes.  So, that's actually a really important part.  After the meeting,the meeting minutes get put together, and then we send them out for folks to look at.  We'll talk about why that's important in a sec, but that's definitely a part of the recipe to making risk radar work.

    So, some surprises, some surprises at risk radar, well, Scheduling and Cadence surprises.  We were originally doing it monthly.  We started this in 2019.  So, about a couple of years ago, actually it was October, 2019.  And we used to do it every month.

    As the pandemic came around, and we were in the thick of that, we went to every other month.  And so we played a little bit with the scheduling and where we are now, every other month seems to be a good cadence for collecting these risks, discussing them, and then, you know, disseminating them back within the organization.  So, you might find every month is not enough.  You might find it's too much.  So, that's something to play with as well.

    Radar "echoes", what do you mean by this? Well, when I would solicit risks, people were actually surprised that other people had the same concerns and risks that they had.  So, a lot of times we'd say "Hey, I don't think it'd be, you know, else is worried about this, but I'm worried about X".  And I would say "yeah, actually I got emails from four or five other people about that particular risk." And so, we would definitely dig into that one at the meeting.  But that's one of the reasons you collect things beforehand, to reduce that bias that people maybe, you know, having to say it in a meeting is very different than just emailing it.

    That was a big surprising thing.  The importance of the meeting minutes.  So I talked about this.  So, we have a lot of folks that have a conflict with risk radar or have a very busy schedule.  A lot of leaders and senior leaders may not be able to make it to the risk meeting.

    A lot of their teams might, but they don't.  And so for them, the really useful output are the correlated, crisp meeting minutes, which we put together, and those get, you know, more broadly disseminated.  Two: it's easier for people that weren't at the meeting, leaders, or ICS to actually look at the minutes.  If somebody goes in and says "Hey, weren't you just talking about this?" And so, it's an easy way to sort of keep the conversation going, but they have to be really high quality and sort of edited, so we try to make them very readable, almost newsletter articles, sort of styling is kind of where we're going.  And finally, the risks that your AI radars detect.

    Very surprising! When you don't constrain risks from an incident perspective and say "Hey, we're gonna look at all the risks in this incident." You start to get risks that aren't technical in nature.  They're about the socio parts of the system.  You know? How people are feeling, how an on-call rotation might be thin, things like that.  It may go into other parts of the organization around, you know, other teams that aren't aren't engineering.

    Maybe they're PR, maybe they're other things.  And again, it's great.  'Cause then you can follow as part of the emergent discussion, follow the thread of risk around the organization.  It's not just, you know, in the context of an incident and this single technical system failing.  So, some of those risks and where they've led us have been very surprising in a very positive way.

    And so, that's another benefit here.  All right.  Let's talk a little bit about some of the problems and challenges of risk radar that we ran into.  The radar represents a sort of probabilism, right? So, there's a probabilistic nature to the risks that people are gonna come up with.  We, you know, people are using their own heuristics and they're making a judgment call about where, how likely it is that the risk that they're bringing up is.

    So, you have to know that this radar that we're talking about, you know, it's based on how many sensors report that same risk, right? How many different radar sites report that.  And so, there's a probabilism involved.  Recency Bias is definitely involved.  So a lot of folks will actually bring up risks that were in recent incidents or OOPSies, that's okay.  One of the things that we found that are super interesting is those risks things ebb and flow over time.

    So, there may be a few incidents about a particular risk.  It kind of dies down, kind of gets tamped down.  Maybe engineers do something different, but six months later we're talking about the same risk and we might want to revisit it because it came up again.  And so, recency bias plays into that, but it's still useful there in terms of watching risk ebb and flow over time.  Some risks will never come to pass, and that's something that you just have to accept.

    One of the important things is all the risks that get brought up, whether or not, you know, they happened in a previous incident or end up happening in an incident in the near future, are a second order signal of what folks are worried about in the organization.  And so, that's actually super useful to look at like, where are people concerned and why are they concerned? There's a lot of chunky conversations that can be had there.  You might say to yourself: "ah, whatevs, this is a Netflix thing, recording thing, and I can't do this in my organization.  Well, oh, look, hey, it's Pete! Hey Pete, I'm kind of in the middle of something, I'm kind of giving a presentation for Pulimi, Cloud Engineering Summit.  Is this quick.

    Can I help you with something? Yeah yeah, I just got a couple of questions about risk radar, if you have a few minutes. Risk radar.  Well, it's funny, I'm actually talking about risk radar right now.  So, why don't you tell folks like who you are and, let's talk about your questions. Yeah, I'm Pete Shima.

    I work on the Reliability Engineering team at Epic Games, and we have started doing this risk radar thing that we found out about and, and it's going pretty well, but you know, a few things, you know, a few questions I had about it.  One is, you know, we're gathering all these risks and people, we have have really liked talking about this and we've sort of created this forum for people to talk about these things, which is great, but like a lot of folks want action out of these things.  And that's definitely a challenge for us.

    Yeah yeah.  Well, but before I answer your question, we'll get to that. 'Cause that's an interesting thing.  I mean, this comes up an incident topics, you know, incident remediation, like why would we do a retro if there's not any action items? So, it's a juicy topic.  But I'm actually really curious.  How did, I mean, how did you get started? Like how do you, I mean, how did you introduce this meeting to the crew? Like, what was that like?

    Yeah yeah.  So we have an operational meeting that we have bi-weekly now, where we talk about a lot of stuff for service ownership at Epic. So, you know, where we have the, definitely, a you build it you run it type of culture.  And hey, we're talking about a lot of operational and service ownership items there.  And we said, Hey, you know, there's not really like a place for people to talk about some of this, or so.  Ww talk about security risks and things like that in other forms, but like, Hey, one great conversation we had was about on-call problems we have with in some of our on-call rotations.

    On-call health. And we had a great discussion.  Yeah, on call health and on-call configuration, right? So, so we sort of introduced this into this, an optional meeting that people can join and sort of learn what's going on.  So, it's a pretty big audience there, and we're getting a lot of sort of feedback about, like: "Oh, hey, this thing doesn't seem right.  Or this thing doesn't seem right." Yeah.

    Yeah.  And of course, as we were talking about earlier, like that's, you know, the point of risk radar is to create sort of a forum for that, so that people, you know, people can kind of get some of those things off of their chest or off their mind around like, what's what they're worried about.  Right? One of the interesting things you asked, right? Was about action items.  And I guess, I wonder a little bit, like, did that come up because people were discussing these great risks and then it was kind of like: "oh, well, what now?" Or like, was that kind of the, the thinking there? Or Yeah. Yeah. So we've been sort of collecting these risks to sort of build our risk library.  So to speak, our risks catalog, and we're sort of going through this .

    And we have quite a lot now, which is great, but Hey, what's the next step? Hey, this is actually like a serious problem.  What do we do about it? Right? We, we shouldn't just leave this here.  And how do we sort of address that? Yeah. Yeah, definitely.  Well, so there's lots of different ways that we've done that at Netflix or dealt with that.

    Right? And one of the ways is, you can use it as a input into product discussions, right? If you have a product team.  One of the big things too, you can surface it, you can use some of those things to surface actually where teams are, right? And so, maybe there's a certain part of the product that has a lot of technical debt, and that's being expressed through incidents and the risks that people see in incidents, right? But if you kind of go to someone and say: "oh, I just have technical debt." Right? And maybe there's a technical debt in the Frogger service, right? They may say "well, that's great." But, if you can connect that to, like, there was an incident, and when we went and looked at that, the risks that got expressed are related to this technical debt, it gives you something, a bit of an anchor to do that.  So, I think you can use it in a lot of different ways, but one of the things that I think is relevant and important as part of that is you do have to have somebody driving it, right? 'Cause otherwise to your point, I bet it maybe feels like a little bit like, just complaining, right? Unless you do something about it, right.

    Yeah.  Yeah.  And I think, you know, we've developed this long list of things and then people are like "okay, we've got a list of stuff right now." And we've done a couple of voting type of things.  Hey, what's important to people? And that's been helpful, but I think, you know, finding that right driver and hey, what do we really do about this? When maybe it's not attached to even one team, it's something we're still figuring out.

    Yeah.  Yeah.  Well, and so, the one thing too, that I'll mention that's really interesting about this is that not all of the risks that folks bring up or that get discussed may have an actionable outcome in the moment.  So, one of the things that we found, and we found this at Netflix too, it's just like, it's almost trying to scale the, and I kind of referenced this earlier, scale the water cooler conversation, right?.  Engineers knowing how the system works and the sharp edges, you may not actually polish them, but you may want to know that, you know, if you use that buzzsaw in that way, the buzzsaw service in that way, it's gonna bite you, right? And so, that's useful information too, even if you don't put it in a backlog or, you know, do anything with it.

    I'm actually curious, I have a question for you.  For folks that might be interested in this whole risk radar concept, what advice do you have for getting them on their journey, doing it at, you know, an organization that maybe, you know, this is not a unicorny thing.  You can do it at Netflix.  You can do it at Epic.  You can do it at your org. What advice do you have?

    Yeah.  Yeah.  A couple of things that I've found so far, you know, we've been tracking this for a few months and getting a lot of things and, definitely finding out what is important to people has definitely been helpful for us.  We used some voting things to, to start gathering more of that and also like having a safe space.  So, some of the stuff is gonna be painful for people to talk about, right? So it's gotta be like a, a space where it's okay to talk about things like team health, like on-call, like that sort of stuff, is pretty important.

    And if people aren't comfortable about talking some of these risks, then that's gonna make it challenging.  And we've also tried to get senior folks in this meeting too, so people can actually have a dialogue with senior people directly about how they think about some of this risk, right? So, well, what is important to one person and might be a really emotional thing for one person, might actually be a really big problem for someone else, or might not as be a big of a problem for other teams.  So I think finding, getting that dialogue going and then focusing on, hey, here's actually the important stuff.  People that are passionate about this stuff, like they're gonna get together, if you can just bring them together.  So, I think that's worked pretty well for us so far.

    Yeah, definitely.  You know? We've been using the metaphor of like radar and clouds, right? Some, so sometimes clouds look very ominous, but there's no moisture in them, right? They're not actually that scary when you have a tool, like a radar to look at them and then other, you know, things, other clouds look like happy, fun clouds, and behind there's like major storms going on.  And so, that, creating that space can help take "the signal of the clouds" if you will, and make useful information about it, to explore it more.

    Yeah.  And I think people bringing up similar things or the same things over time, it's like: "oh, hey, this is a repeat." And now they have somebody to connect with on that topic. Yes. And quite often there's people like: "Hey, I wanted to solve this.  I didn't know as a problem for someone else to." "Hey, how can we sort of go solve this?" We're we're still figuring out how we can sort of facilitate some of that stuff.

    Yeah. But it's been good connecting some of the groups. Cool.  Cool.  Well, I'm gonna go ahead and finish up this talk, but I'm really glad you, you know, dialed in, you know, gave me a call and we could talk about it.  It was very serendipitous. Yeah, well thanks for a few minutes, and talk to you later. Yeah.  Yeah.  All right, I'll talk to you soon. Bye. All right.  All right.  That was great.  We now, where was I? Oh, this is a Netflix only thing.  Well, clearly it's not, anybody can do this.

    And where are the action items? Pete and I talked about that a little bit and what you can do about this, but that's one of the things too, that a lot of times people are thirsting for action items, and that can be a tricky thing to wrangle sometimes.  Again, some risks may not have clear defined action items and you'd have to do a little more work to find what is the actual action item from that risk.  So, let's talk about the three takeaways from today.  So, people communicating with each other in Sociotechnical Systems, turns out it's kind of important, right? A lot of times as engineers, we love telling stories about a near miss, this thing I did that almost took the site down but didn't.  We just talk about, we'd love to talk about ways that we kept the site up and wrangled, you know, that database back to health, without anybody noticing.

    I mean, these are water cooler conversations and they're important to organizational learning and to how we play out, what happens during high consequence, high tempo events.  This is kind of, you know, as I said, a water cooler.  So, this risk radar is a way to scale those conversations and disseminate some of those learnings outside of just what engineers are talking about that concerns them.  Fundamentally, this is what that is.  And so, play with it.

    It's a format to structure that.  Play with it, do something that works for you.  Takeaway number two: A technique to give voice to "I told you so!" Now, saying "I told you so!" is not generally very productive, but it exhibits or indicates a frustration, right? People saying: "Hey, I was really worried about this and it blew up and I told you so." So, risk radar is a way to sort of give voice to those concerns, but in a more actionable and definitely healthier way.  Hopefully if we see a lot of folks concerned about the same thing, we can take action about it.

    And, you know, it's really healthier than just saying "I told you so, hahaha!" Finally, takeaway number three: Forums like Risk Radar cultivate adaptive capacity in interpredictability, across levels of the org, right? So adaptive capacity, that's our ability to adapt to situations under high consequence, high tempo events, and this, the exchange of knowledge and exchange of what things are on, you know, risky things are on the mind of engineers, increases our ability to cope with those things during an incident.  And then the interpredictability is the concept of how can we lean on each other and other teams during these high stress, high tempo, high consequence incidents.  And this builds that, because it shares some of the context in a non-stressful way in a non-stressful forum about what they're doing, what they're worried about, all of those things.  And then of course, if you disseminate that out, as I mentioned with the minutes, that's super important, you can get some of this effect across all levels of the organization.  So, go forth, establish your own risk radar sensor network, and start finding out those risks with the already existing intelligence that you and your colleagues in your organization have. I'm J. Paul Reed, jpaulreed at Twitter.  It's all I got.
---
