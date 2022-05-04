---
# Name of the video.
title: "Walkthrough of building container-based AWS Lambda Functions"
meta_desc: "In this week's episode of Modern Infrastructure Wednesday, we go in-depth on the container-based AWS Lambda functions demo."

# A featured video will display first in the list.
featured: false

pre_recorded: true
pulumi_tv: true
unlisted: false

# Gated videos will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

external: false
block_external_search_index: false

# The url slug for the video landing page. If this is an external
# video, use the external URL as the value here.
url_slug: "walkthrough-of-building-container-based-aws-lambda-functions"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Walkthrough of building container-based AWS Lambda Functions"

# Content for the left hand side section of the page.
main:
    # Video title.
    title: "Walkthrough of building container-based AWS Lambda Functions"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/4RC37yZJakM"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2020-12-01T10:00:00-07:00
    # Duration of the video.
    duration: "7 minutes"
    # Description of the video.
    description: |
        In this week's episode of Modern Infrastructure Wednesday, we go in-depth on the container-based AWS Lambda functions demo.

        We walk through each line of code, showing how it works as well as what's in the `Dockerfile` to build the image.

        Code for this episode available [here](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-12-02).

        Today's example is in TypeScript, but Pulumi makes it easy to stand up infrastructure in your favorite languages including JavaScript, Python, C#, Go, and Java - saving time over legacy tools like CloudFormation and Hashicorp Terraform.

    # The video presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, and welcome to another episode of Modern Infrastructure Wednesday. Today, we're going to be going over the demo that I built for showing how to use container-based Lambda functions. And so we're going to walk through that code in depth. Since in the video, it was like kind of a quick take on just how to build an application and kind of show the demo of the application, but it never really walked through it in depth. And so we're going to do that in this video today. If we kind of start at the beginning, we import a couple of libraries. We're building a TypeScript application today. Pulumi obviously does support Go, .NET as well as Python in addition to Node.js. So, but here we're using TypeScript. So I create this bucket you know, simply just call, you know, a new bucket. Here, we just name it bucket, but obviously that's just the, the name we're using within Pulumi. With Pulumi's auto naming capabilities these actually end up being transformed into suffix names and the actual cloud provider in this case AWS. This next line here, we're using this convenience library, AWSX, this is a Crosswalk for AWS.

    It's a convenience library from Pulumi. And then here we just build and push image and it builds the image and pushes it into a repository within ECR. And so actually, if we go to our console, the Pulumi console, we can actually see those resources here in our stack. And if I open this up we can actually see the name of the bucket is, you know, is suffixed like this. And then same thing with I, if I go look at the sample app repository, we can actually see this particular repository in ECR.

    Sorry, I updated something without publishing it, but here we can see that the repository names as well as the images, that's what I meant to do as long as the images that have been pushed into that repository. So that's kind of how that works. And so again, this is all auto named as part of Pulumi. And so yeah, so we, we have the bucket, we have the image in order to execute a Lambda function, obviously that Lambda function needs to have an IAM role and permissions. And so we create that role here, thumbnail role, and we attach a policy called the AWS Lambda full-access policy. So actually here, we using a managed policy ARN that AWS provides. You'll note that this is actually an enum, you know and so, so that's how this is how we actually bring this in here.

    So that's kind of, or access to any of them, rather, it's a set of constants, so that's how we bring that into there. And so once we have those, we just create the function. That's what this line is here on line 20. And so the function takes that image, a URI. So we have that image URI from above and this is an output of this particular image. And then we also give it the role that we created. So those things combined allow us to create the function that actually executes. And I'm going to go into how that function works in a second. After that, the rest of the code is actually fairly simple as well. We create a onObjectCreated. This is again a convenience in the Pulumi AWS library where we hook up the S3 bucket notifications to our function.

    And so every time there's a new object created in that bucket. And in this particular bucket, we will the name of the handlers on new video. This could be any name. And then we give it the function that we want to execute whenever a new bucket object is created. And then we specifically filter for this MP4 suffix. And then finally, just to kind of, you know, for the sake of the demo, I also throw in an additional function that we create here. So again, we can create another onObjectCreated notification so that you can see it's actually the same thing, but here we can give it a new handler name in this case. Instead of giving it an existing function, I created a new function inline actually, and my inline function is simply just a TypeScript code I create here, and you can see the inline function is fairly simple.

    All it's doing is providing some additional information about what's actually being processed. And again, we give it a policy. So that's, that's pretty much it here. And you can see this is, this is looking for that JPEG thumbnail that gets written once it gets written. And so, nothing too crazy here. So instead of a role, I just give it a policy because this actually creates a role on its own as well. So that's kind of how all that works. And so really the only code left to look at is how do we build that container image and what is the code running within that container image? So if we go over here, we can look at our Docker file and you can see up here, I'm basing this image off of the image that AWS has published.

    This is actually using their new public ECR. And so we're grabbing that image from there. And then we're just adding a few things that weren't present in the image already. So we're including a few utilities. We need those to install a couple other things. So we need unzip to install the AWS CLI where we just grabbed this CLI and then we unzip it and install it. And then we similarly need 'tar xz' to install FFmpeg. So we also grab that file unpack it, and then move that binary into somewhere on the path. And then once all that's done you know, finally we just copy this handler and then set the entry point to be this handler. And so if we look at this handler it's fairly simple.

    This is exactly the same code you would write in a Lambda function. And so here, all we're doing is we have this simple run wrapper that does an 'exec'. And so that's simply a shelling out to take the file that came in and copy it to the local disk. We run FFmpeg against it with the correct FFmpeg parameters to grab the thumbnail that outputs to the thumbnail. And then we finally copy that thumbnail that we create back into S3. And so that's how all this is wired together fairly simple and straightforward. And so that really that's how the entire example works, and like I said in the short video, it really is just a few dozen lines of code to wire everything together pulling me makes it super simple and easy to get started doing this. So yeah, I hope you enjoy this video. Be really curious to see what you do with the Lambda functions using container-based functions. And I hope to see you next week on Modern Infrastructure Wednesday. If you liked this video, please leave a comment below. Would love to hear what other content you would like to see as well as please make sure you hit that like and subscribe button so we know you're enjoying the content here. Thanks.

---
