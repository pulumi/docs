---
# Name of the video.
title: "Building container-based AWS Lambda Functions in Python"
meta_desc: "In this week's episode of Modern Infrastructure Wednesday, we port last week's example of using container-based AWS Lambda functions to Python."

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
url_slug: "building-container-based-aws-lambda-functions-in-python"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Building container-based AWS Lambda Functions in Python"

# Content for the left hand side section of the page.
main:
    # Video title.
    title: "Building container-based AWS Lambda Functions in Python"
    # URL for embedding a URL for ungated videos.
    youtube_url: "https://www.youtube.com/embed/o-_pDWaGDNw"
    # Sortable date. The datetime Hugo will use to sort the videos in date order.
    sortable_date: 2020-12-08T10:00:00-07:00
    # Duration of the video.
    duration: "8 minutes"
    # Description of the video.
    description: |
        In this week's episode of Modern Infrastructure Wednesday, we port last week's example of using container-based AWS Lambda functions to Python.

        We walk through each line of code, showing how it works as well as what's in the `Dockerfile` to build the image.

        Code for this episode available [here](https://github.com/pulumi/pulumitv/tree/master/modern-infrastructure-wednesday/2020-12-09).

        Today's example is in Python, but Pulumi makes it easy to stand up infrastructure in your favorite languages including TypeScript, JavaScript, C#, and Go - saving time over legacy tools like CloudFormation and Hashicorp Terraform.
        [Get Started](/docs/get-started/)

    # The video presenters
    presenters:
        - name: Lee Zen
          role: VP of Engineering, Pulumi

# This section contains the transcript for a video. It is optional.
transcript: |
    Hello, and welcome to another episode of Modern Infrastructure Wednesday. I'm your host, Lee Zen, and today we're going to be covering how to build container-based AWS Lambda functions using Python. So we actually did a very similar walkthrough last week using Node, specifically TypeScript in Node. This week we're going to be going over it in Python. A user comment suggested, "Hey, can you cover some of these examples in Python and Go?" And, oh, you ask and you shall receive. So here we are covering an example in Python.

    So, yeah, we start off by importing some of our libraries that we're going to use. We're going to be using Pulumi obviously, SDK along with AWS and Docker. Docker you'll see why in a minute. So, fairly simple. We create a bucket and this is where we're going to... We're going to go through the thumbnail example again just like last time. So the objective here is to create a Lambda function that has a container as the underlying image where the container has FFmpeg in it. So we don't have to figure out how to get that uploaded into Lambda as a layer or anything like that. It's just part of the container image. And then we're going to upload videos into this bucket and then those videos will get a thumbnail created as a result of that upload.

    So, yeah, we create this bucket that's going to host our videos when we upload them, and then we're going to create a repository for hosting our container images. So that's all these first two lines are doing. And then we grab an authorization token from ECR and we use that to feed into this image resource. And what this image resource is doing is you can see it has a build parameter, and this is taking... This is a context we're going to build. So later on I'll show you this Docker context, this exact same one I showed last week, but I'll show briefly here as well. And then we give it the image name, which is just going to be the URL of the repo, and then the registry information. So here, this is where I need the credentials, where I need the username and the passwords that we can actually Docker log in to push our image.

    After that, you kind of... At this point of the program, what will have happened after we run 'pulumi up' is we'll have created the bucket, we'll have created the repo, and then we will have pushed this image into that repo. Next, we want to create the function that's based on this image. So we create a role and a policy attachment for that role. So you can see we're using very simple AssumeRole policy here, and then actually here we're kind of showing off some of the new enum support we have across all our languages. So this enum is projected into all of the languages and it's available in C# and Go and Python here and obviously Node as well.

    So we get to use this, which is great. So that's a nice convenience. So here we're using the full access managed policy ARN. And then we finally create the function specifying the image package type along with the actual image name, which is the fully qualified URL for the image that we uploaded earlier. So combine all that together, we have this function now.

    And the final thing to do is to really just wire up that Lambda function we created with S3 bucket notifications. And this is also fairly simple. All we're doing here is first giving permissions for the bucket to invoke the function. And so here you can see we have this permission where we allow invoke function from S3, from that bucket that we created as the source, and then it's going to invoke this function that we just defined. And then we have to define how we actually want to invoke. And so we create this bucket notification. And in the bucket notification, again, we provide the bucket that we're actually going to invoke from along with the functions that are going to be invoked off that notification.

    And so here you can see we give it this function ARN and then we give it this event. This is for object creation because obviously we care about any videos that get created, and then we filter on this MP4 suffix since we're looking for specifically video files. Just because it's easier, we actually write JPEGs into the same bucket. So we obviously want to make sure we're not infinitely recursing on ourselves. And so we're just looking at the video files. And this depends on having this permission obviously. So we have this explicit dependency we define here.

    So that's how this all gets this wired up. And then we finally export the bucket name for convenience. And so I actually ran this earlier. So I ran 'pulumi up'. It provided all the resources, shoved them all into AWS. And when I run this copy of the sample file into the bucket, if I show the output, this is running Pulumi logs, I'm just tailing the logs from CloudWatch. And you can see here, this is the thumbnail or task or function that's getting invoked. And here it's copying the file from S3 into the temporary directory on the container, and then it's running FFmpeg to extract that image. So you can actually see this thumbnail is getting saved here in the sample that JPEG. So you can see here it's copying as well. So let's actually copy this locally and see that it actually worked. And if we open up that sample, there's the thumbnail. And this is a video of a waterfall. So great success. It all worked.

    I mentioned I would take a quick look at the Docker build context here. And this is just a Docker file. Exact same one as last time. Didn't touch anything here. So actually one of the cool things I'm showing here is that we authored our Pulumi program in Python, but our Lambda function and the Docker file that you can see is building off this Node.js base Lambda image. So actually the function is written... The Lambda function itself is still written in Node. And so here, the critical line here, we're installing FFmpeg and then copying it, copying this actual function handler. And the function handler is very simple. It's really just shelling out to copy to S3, running FFmpeg, and then copying the result of the thumbnail file back into S3.

    So yeah, really, again, it's super easy to get running with Pulumi and it's super easy to use Pulumi to create your container-based Lambda functions in AWS. So hopefully you enjoyed this video. As always, love to hear your feedback. Please leave them below in the comments. And if you liked this video, please make sure you like...hit the like button. Make sure you subscribe to PulumiTV for more updates. And yeah, like I said, this was the result of viewer feedback. So open to more feedback and willing to make more videos that you guys want to see. Thanks for watching, and we'll see you guys next week.
---
