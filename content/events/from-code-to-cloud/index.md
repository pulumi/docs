---
# Name of the webinar.
title: "From Code to Cloud"
meta_desc: In this workshop, you'll learn how to leverage GitHub to make code CloudOps ready without learning new tools or collecting new certifications.

cloud_engineering_summit:
    track: keynote

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
url_slug: "from-code-to-cloud"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "From Code to Cloud"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "From Code to Cloud"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/tDq0XXpMG6k"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2021-10-20T11:20:00-07:00
    # Duration of the webinar.
    duration: "21 minutes"
    # Description of the webinar.
    description: |
        As the need for well-designed cloud infrastructure increases, front end developers and early career developers may be feeling the pressure to learn CloudOps and DevOps practices. Commonly, software developers are on time crunch and don't always have extra time to study more.

        The good news is if you may already have the necessary skills!

        In this workshop, I'll discuss how I leveraged GitHub to make my code CloudOps ready without learning new tools or collecting new certifications.

    # The webinar presenters
    presenters:
        - name: Rizel Scarlett
          role: Junior Developer Advocate, Github

# This section contains the transcript for a video. It is optional.
transcript: |
    Hi, everyone. I hope you're having an amazing time at Pulumi's Cloud Engineering Summit. I know that I am. I want to take this time to personally thank the team at Pulumi for giving me the space to talk about my learnings, my experiences in code. So, let's jump straight into it.

    My talk is entitled Code to Cloud.  I'm kind of just going to give an overview of how I got my code to be hosted on the cloud with very little cloud engineering experience and how you can do that too.  So, I'll start with a quick story of a time that I worked at a company that did releases at night.  And there was a reason we did this.  We did them like, Friday night at nine.

    Or like, Saturday night between like, eight, nine, starting.  These could end at up to like, midnight, depending on how many- how well things went.  How smoothly things went.  And the reason we did this is because we didn't have a great CI/CD pipeline in place.  So, it was all hands on deck to make sure that nothing broke before, during, or after the release.

    I found this extremely nerve-racking. One, I wanted to like, hang out on my weekend nights.  I'm young, so I wanted to have fun.  And then two, I just don't trust myself to find every single bug and to know what's broken, because I'm human.  So, most of the time, majority of the time, I would come in on Monday and things would be on fire.

    So, that was to be expected because like I said, we're human. So, we couldn't pick out and predict every single error.  On the flip side, after I worked at that company, I worked at another startup, but they use GitHub Actions to automate their release workflow.  I was actually very impressed. I'd never like, encountered or used GitHub Actions before that. And I was like, "Oh my gosh.  So cool." Like, the release takes like, five to 10 minutes. We can do it during the day. And if anything goes wrong, you can easily revert it.

    I was very impressed. And I think both of those experiences were valuable for me because they allowed me to see how important it is to have some kind of strong DevOps or CloudOps structure in your project. And to, at the very least, implement a CI/CD pipeline.  And I made it a goal to have a CI/CD pipeline for my personal projects and my freelance projects, just to get better practice and to get into the habit of doing that. So this talk, as you can probably tell, it's going to be for front end developers, early career developers, open source maintainers or contributors who are like, "Hmm, maybe I should implement some kind of CI/CD pipeline."

    Or, anyone who doesn't do cloud engineering for their day-to-day work. I know this is a cloud engineering summit.  So, a lot of y'all are cloud engineers. I'd advise you to still stick around because I want feedback. I want to know how I could've done things better, or more easily.

    I'm sure I made things hard for myself. I also think it'll be cool for you to see from this perspective of someone who is a little bit more front-end heavy. So, before I dive into that, you have no clue who I am. Right? So, my name is Rizél. I am a junior developer advocate at GitHub, and I was trained as a Full Stock Software Engineer three years ago. I've moved around the stack, but I've mostly been heavy in... On the front end. And I'm also a program director at G{Code} house, which is a nonprofit organization aimed at training women of color and people of color to code.

    And as you can see, I am very passionate about empowering and educating others, especially within the tech industry. I am passionate about my own learning journey, and I am addicted to Twitter. So, because I'm addicted to Twitter, I would definitely tell you to follow me on there. I'll follow back. I'll interact with you. My handle is @blackgirlbytes. That's my handle on Twitter, Hashnode, GitHub, Dev. to.  I will soon-to-be on TikTok and YouTube. So, if you want some awkward black girl content about code, definitely look out for me there.

    So, like I said, because this talk is for people who don't have that much cloud engineering experience or DevOps experience, you've heard me throwing around the words, or the term CI/CD pipeline.  Maybe you're wondering, "What does it mean?" and "Why does it matter?" CI/CD stands for Continuous Integration, and the CD part of it can stand for Continuous Delivery or Continuous Deployment.  I think it is all about, and it matters for like, these five reasons.  So, essentially it allows you or through CI/CD pipeline, you're creating automated test, code, builds.  You're encouraging your team to make small incremental changes, and check them in frequently.

    Because nobody likes that person who is checking in like, a long PR.  Like, 90 files changed.  Now you're affecting the whole team.  Now they have to all re-base off of you and get sidetracked from their actual task.  It's also automating the delivery of these applications to production, to staging, to dev, and whatever other environments you have.

    It's also just enabling teams to catch bugs more easily and more frequently because you have these automated processes in place.  And therefore, improving the code quality overall and improving the team morale.  Because now they have a reduced workload.  They can focus on collaboration, having fun, and coding.  So, of course, with these talks, someone tells you about a new tool or something you should be using, and you're like, "Yeah, this is cool.

    But now I have to learn something new and I don't have time to learn something new." I feel that pain, I feel that pain.  That's why I built my application with the intention that I am going to use familiar tools to put- to host my project on the cloud and to implement CI/CD pipeline.  So, I'm going to kind of show you guys my application very quickly.  I built a Git Emoji search app with Next.js, Tailwind CSS, and Fuse. js.  I've never used these technologies before, but they were very familiar to me because I'm like, familiar with React and I'm familiar with CSS.  Let me show you the app very quickly.  So, here's my app hosted locally.

    I'm calling it CuteMoji.  It's nothing crazy.  Very simple interface so far.  I'm sure it'll grow.  It shows the first couple of emojis and this is... this is calling GitHub's emoji API.  And essentially, I can do a search for whatever I'm looking for.  So, let's say I'm looking for yellow. It shows me like, a yellow circle, yellow heart, yellow square.  Let's say if I searched the word girl, it shows me a bunch of girls.  If I misspell something.

    Oh, what can I misspell? Maybe moon, or start to spell something.  We got mooncake, boo, book.  So, as you can see, this is the start of my application and it is using fuzzy search.  I kind of want to show you guys how I'm using fuzzy search because I thought it was cool.  So, I was able to do fuzzy searching within my app using Fuse.

    js, which is an open source project.  I thought this was a great lifesaver because I was considering writing my own algorithm for this, which would have been a lot of work.  Or, using a different tool that I would eventually have to start paying for as my project grew.  So, I didn't really want to do all of that.  I was able to implement this with like, very little lines of code. So, let's look at it over here.  As you can see, I have an options object and I'm passing in a keys property.  And in this keys property, I essentially am passing in all the...

    I guess, property names of that object that I passed in, or the data that I'm passing in.  And I'm saying like, I want my user to search by emoji name.  And the includeScore's line is essentially saying like, return the results that are most relevant.  So, it scores it in some way saying like, Oh, this is like, most relevant to least relevant.  I don't want to see the least relevant.

    Hide those or don't show those first.  Then I pass in, I create a new fuse objects instance, and I pass in the API data and this options object that I just created.  And then, I call a method called fuse. search.  And depending on whatever query that the user typed into the input bar, it'll call that search method on it and return the results.  It was so easy.  Like, what is this? Like, just a few lines of code, and I was able to do fuzzy searching.

    Okay.  Back to cloud and CI/CD stuff.  Like I said, my goal was to implement CI/CD pipeline and to get it hosted on the cloud.  Very simple stuff.  I just want to do this as a teaching tool for myself. And I expect my app to grow beyond what it is right now.  This is, this is to me, very simple or very simple for me.  So I wanted to be...  Have it be able to scale and to be maintainable. So, I also said I'm not trying to learn anything new.

    I'm trying to focus on using familiar tools, and languages, and platforms.  So, I decided to go for GitHub actions because I've been on GitHub for like, ever since I learned to code, so I'm very familiar with it.  And GitHub actions has open source, automated workflows.  I was thinking maybe I don't have to start from scratch.  Plus, actions are very well documented.

    Also, I went to go- I decided to go with Pulumi to deploy my code to the cloud.  One of the benefits of Pulumi is I don't have to like, learn how to use AWS, or Google Cloud Provider, or whatever you may have.  I just have to write in my favorite coding language, or the coding language I'm most familiar with, which is JavaScript.  So, I started off by creating an S3 bucket.  And here's like, my little Pulumi JavaScript that I wrote to create a new S3 bucket.

    And I told it to point to the index. html file and a 404. html file to say like, this is the index document of the website, and then this is the error page.  And then I ran Pulumi up.  That's kind of how you deploy your changes. I was like, "Wow, this is so easy.  I'm having fun." The only little problem I had is that I realized, "Wow, this is a next JS project and I don't have an index. html file." So, when I did pull Pulumi up and I went to go check if it got loaded to the S3 bucket, I saw an error.

    And, I realized the error was pretty easy to fix.  I was able to generate both an index. html file and a 404. html file by running "next build && next export" I added this as a script to my package. json, that way I'll just have to run npm run export. And then as you can see, it created an outfolder with all of these files in it.  So, it generated a website URL for me.  I could've given it a more specific name, and I probably will.  But this was my first attempt.  So, I just went with S3 website bucket.

    Let's check it out.  So, now we are on that URL that says S3 website bucket.  Bunch of random numbers.  And we're seeing the same thing that we saw that I had locally.  You type in words, you're getting emojis. So, everything's working.  Everything's good over here.  So essentially, I got it on the cloud.  It's on AWS.  Check to that one goal that I had. Then, my next goal was trying to lay the foundations for starting up like, a CI/CD pipeline.  I do want to warn y'all, this isn't like, the whole thing.  It's not the whole shebang.  It's just like, a very simple start.  And I realized Pulumi has GitHub action.

    So, I don't really have to write my own.  I was very excited about that.  So, here's how I initially set everything up to be able to use Pulumi's GitHub actions.  First, I enabled my applications to talk with each other.  So, I wanted Pulumi's GitHub action to be able to talk to GitHub, and that required some authentication. So, Pulumi needed the GitHub action needed to like, call my AWS access key, AWS region and all that.  And instead of like, saving that in my repo for other people to access, I used GitHub secrets and now it's encrypted.  No one knows, but my applications can speak to each other.  I also installed the GitHub Pulumi application.

    This was a little tool that they made to allow the GitHub action to actually leave comments on my PR's or whatever event that I used for GitHub actions.  And then I just copied Pulumi's GitHub action code, they're YAML, and I modified it to work for me.  So, first they had two GitHub actions that I found.  The first one allowed me to see the activity that happened in my Pulimi stack.  So, if I like, made any changes in that stack, it would like, print out like, "Hey, these are the three things changed." or like, "A small error happened." This way I would gain like, a little visibility into why something happened rather than like, going into the Pulumi console.  We can take a really quick look at like, what the action looked like.  Essentially, this is the name of that action.  We're saying we want this to happen on poll request.

    We're doing like, a couple of things that you need to do for GitHub actions which is like, just checking out the code and setting up node, configuring like, my AWS credentials for it.  And then I think right here uses pulimi/actions@v3, is where we're using Pulumi's GitHub action.  And it does all the magic behind the scenes.  So, on each of my poll requests now, I get a little comment.  I'm not actually doing this. This is automated.  And the comment essentially shows what things changed.  For this specific PR, nothing changed.  There was two unchanged resources for my Pulumi stack, and I thought that was cool. All right.

    So, the other Pulumi action or GitHub action that I implemented, showed me a live preview of my website which is something I wanted.  I don't really have tests on my applications yet, but I wanted that every time I do a PR, I can get a quick live preview before I merge it into production.  Because I've had many times in my life where something's working locally for me, it's working on my machine.  I'm like, "Wow, everything's all good." And then I merge it to production, or whatever like, the main branches.

    And I realized it doesn't work at all, and I have no clue why.  So, I decided live preview might be a really great and easy way for me to do some manual testing.  Okay.  So, let's have a look at my repo.  I am in the poll request and I opened up a PR of me just changing the background gradient.

    If you could remember, I had like, pink and then it like, went over to like, a little bit of a bluish color.  So, let us see.  Basically again, here we have the first like, automated PR, or sorry, automated comment from the GitHub action.  And then we have the second one, which gives me a live preview of the site.  So, let's click on it and see what it looks like. Cool.  There, we have it, we got a blue to pink to green gradient, which is what this PR was all about.  Let's have a look at the actual like, code for the GitHub action.  I modified this a little bit just to fit my use case.  But basically, what they had worked for me.

    First, I checked out the code.  I essentially did npm run export again because it was looking for an index. html file and I needed to generate that for the action.  And then, I use this update live preview called Pulumify that Pulimi created.  I pass it all my environment variables that it needs and the magic happens.

    So, I want to make this disclaimer that I'm not done yet with the project, I'm near done with the talk.  There's lots of stuff to do in terms of like, implementing a strong CI/CD pipeline.  But I think this is definitely a good start for me to lay the foundations.  And it really only took me about like, an hour or two to do all of this.  So, this is me saying like, go ahead, try it out.

    Try out GitHub actions.  Try out Pulumi.  I hope this was interesting and edifying for y'all.  Thank you for listening to me speak and definitely check out my repo.  It's https://github.com/blackgirlbytes/git-emojis.  Definitely download it.  Play around with it.  Suggest some things for it for me to make it cooler because I'm still thinking of like, what I could do with it.  Thank you!
---
