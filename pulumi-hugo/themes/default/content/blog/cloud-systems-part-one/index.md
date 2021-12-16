---
title: "Cloud Systems Part One: Static Sites and AWS S3"

date: 2021-15-10T09:44:47-08:00

draft: false

meta_desc: In this series, learn modern cloud engineering practices and tooling, starting with using Pulumi to deploy a static site to AWS S3!

meta_image: meta.png

authors:
    - kat-cosgrove

tags:
    - 101
    - tutorials
    - cloud-engineering
---

Cloud engineering is taking over software development. In a lot of ways, this is great; it allows us to build and deploy more complicated applications with less difficulty, and maintaining those applications becomes less troublesome too. We can release smaller updates more quickly than ever, ensuring that we can stay on top of feature requests and security issues. That said, the rise of cloud engineering has also introduced a lot of complexity in the form of dozens of services even within just one cloud provider. Figuring out where to start can be tough, so let’s take a practical tour! In this series, I’ll walk you through building a personal website and deploying it using modern cloud engineering practices.

<!--more-->

The simplest website you can build is a static site. That means no web server, just HTML, CSS, and maybe some front-end JavaScript. Static sites can still be beautiful and interactive though, and for many people, they’re more than enough.

[Amazon S3](https://aws.amazon.com/s3/) (Simple Storage Service) is an AWS service that provides cloud storage for files, stored as objects in buckets. You can think of it like an external harddrive: plug it into your computer, and you have more storage space for your files, photos, and movies that you can unplug at will and move to another computer. An S3 bucket behaves very similarly in that you can throw just about anything in it, from data lakes to images to logs, and connect it to an application. This also means that you can use it to host a static website! Let’s look at how.

## Prerequisites:

- An AWS account

- [Pulumi account](https://app.pulumi.com)

- [Pulumi installed and configured for AWS](https://www.pulumi.com/docs/get-started/aws/begin/)

- Python3

- NodeJS (optional if you want to preview the site locally)

There are a lot of ways to provision an S3 bucket and set its permissions, but for this I’m going to use Pulumi, an Infrastructure as Code tool that allows you to provision, configure, and deploy a variety of cloud services and tools programmatically, without learning a new language. That way, we can stay in our code, and the syntax will be more familiar for developers. It also saves us the headache of going through the AWS Console. All of the code for this, both the website and the infrastructure code, can be found in the [GitHub repository](https://github.com/katcosgrove/cloud-systems-101) for the series, although I'll be walking you through everything here too.

## Building a Static Site

Create a new directory called `s3-tutorial` and navigate into it. From there, `run pulumi new python -y` to create a new Pulumi project using Python. You’ll see Pulumi create a few files for you, but the one we’ll be touching is `__main__.py`.

Before we move on, we need to build out our website. Create a subdirectory and call it `website`. In that directory, add `index.html`, `style.css`, and `normalize.css`.

This one is built using only HTML and CSS, plus one background image file. Replace the name and bio with your own, as well as the social links in the header.

`index.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello world!</title>
    <link rel="stylesheet" href="style.css">
    <link rel="stylesheet" href="normalize.css">
</head>
<body>
    <header>
        <div class="logo"><i class="fas fa-cat"></i></div>
        <ul class="social">
                <li><a href="http://github.com/katcosgrove" target="_blank"><i class="fab fa-github-alt"></i></a></li>
                <li><a href="http://twitter.com/Dixie3Flatline" target="_blank"><i class="fab fa-twitter"></i></a></li>
                <li><a href="http://linkedin.com/in/katcosgrove" target="_blank"><i class="fab fa-linkedin-in"></i></a></li>
            </ul>
    </header>
<div class="banner">
    <h1>Your Name</h1>
    <h3>Job Title at Company</h3>
    <p>Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nam blandit tristique arcu, sed commodo ligula. Ut ullamcorper velit non luctus mollis. Sed placerat quam sed tellus aliquam, ac eleifend quam lacinia. Praesent bibendum velit at metus auctor, vitae feugiat quam luctus. Morbi eu imperdiet metus, et tincidunt tellus. Aliquam non ullamcorper justo. Cras ornare nulla vel pellentesque vulputate. Mauris in elit neque. Aliquam tempor aliquam libero, elementum luctus nisl imperdiet sit amet. Praesent urna ante, scelerisque non tellus mollis, laoreet sodales felis.</p>
</div>
</body>
<script src="https://kit.fontawesome.com/b4747495ea.js" crossorigin="anonymous"></script>
</html>
```

`style.css`

```css
@import url('https://fonts.googleapis.com/css?family=News+Cycle|Teko&display=swap');

ul {
    list-style-type: none;
}

ul li {
    display: inline-block;
}

a {
    color: white;
    -webkit-transition: color .5s ease-out;
    transition: color .5s ease-out;
    text-decoration: none;
}

a:hover, a:active {
    color: rgb(255, 157, 112);
}

header {
    background-color: rgba(0, 0, 0, .8);
    height: 80px;
    position: absolute;
    top: 0;
    width: 100%;
}

header li {
    color: white;
}

.active a {
    color: rgb(255, 157, 112);
}

.social {
    position: absolute;
    right: 50px;
    top: -5px;
    font-size: 30px;
}

.social li {
    margin: 0 5px 0 5px;
}

.logo {
    position: absolute;
    left: 10px;
    margin-left: 20px;
    font-size: 60px;
    color: white;
}

body {
    background: url('./background.jpg');
    background-size: cover;
    background-repeat: no-repeat;
}

.banner {
    width: 60vw;
    font-family: Teko;
    font-size: 2vw;
    text-align: center;
    margin-top: 15vw;
    margin-left: 20vw;
}

.banner p {
    font-family: News Cycle;
}
```

Your `normalize.css` can be copied from [this respository](github.com/necolas/normalize.css), and the expected `background.jpg` can be downloaded from [this repository](https://github.com/katcosgrove/cloud-systems-101/blob/main/part-one/website/background.jpg).

To see what this looks like before we deploy it, we're going to use a tool called `live-server`. This isn't a real, functional webserver, but it's a useful tool during development for static websites. It will reload automatically when a change is detected, so you don't have to wait for deploys.

Install it with this:

`npm install -g live-server`

And run it from the same directory as your `index.html` file:

`live-server`

Your browser should automatically open to localhost:8080, but if it doesn’t, navigate there yourself and you’ll see your website.

## Configuring an S3 Bucket

It’s time to deploy this thing to S3. From your project’s root, run `source venv/bin/activate` to make sure we’re in a virtual environment, and run `pip3 install pulumi-aws`. From now on, we’ll be working in `__main__.py`

For imports, we need the following:

```python
import json
import mimetypes
import os

from pulumi import export, FileAsset
from pulumi_aws import s3
```

We’re going to be reading files from the operating system and working with JSON, so we need the first three packages from the standard Python library. We’re also going to be using Pulumi. You will already have the `pulumi` package installed, but we also need the AWS provider, which we just installed.

```python
web_bucket = s3.Bucket('s3-website-bucket',
    website=s3.BucketWebsiteArgs(
        index_document="index.html",
    ))
```

Here, we are instantiating an s3 Bucket object and assigning it to the `web_bucket` variable. S3 buckets are capable of hosting websites, but we have to tell the bucket that’s what it’s going to be doing and what it should expect the index document to be called. Ours is just called `index.html`.

```python
content_dir = "website"
for file in os.listdir(content_dir):
    filepath = os.path.join(content_dir, file)
    mime_type, _ = mimetypes.guess_type(filepath)
    obj = s3.BucketObject(file,
        bucket=web_bucket.id,
        source=FileAsset(filepath),
        content_type=mime_type)
```

This codeblock defines our content directory (the `website` folder containing your site files, from earlier) and reads each of them in, before creating using the Pulumi AWS module to create an S3 bucket object for that file. We are also including a little bit of metadata for each file.

```python
def public_read_policy_for_bucket(bucket_name):
    return json.dumps({
        "Version": "2012-10-17",
        "Statement": [{
            "Effect": "Allow",
            "Principal": "*",
            "Action": [
                "s3:GetObject"
            ],
            "Resource": [
                f"arn:aws:s3:::{bucket_name}/*",
            ]
        }]
    })
```

This function sets some permissions for our bucket. Since this should be publicly-accessible, we need to allow anyone the ability to read the files.

```python
bucket_name = web_bucket.id
bucket_policy = s3.BucketPolicy("bucket-policy",
    bucket=bucket_name,
    policy=bucket_name.apply(public_read_policy_for_bucket))
```

Now we assign the ID of our bucket as the bucket's name, then create a policy for it that includes its name and the policy we defined in the previous step. We're almost done!

```python
export('bucket_name', web_bucket.id)
export('website_url', web_bucket.website_endpoint)
```

These last two lines are using Pulumi to export some data for us to interact with. The first is the ID of the bucket so we know which one we're working with, and the second is the website endpoint created by S3 once the bucket is online, so we know where to go to see our site!

## Deploying

All that's left to do is deploy! From your project's root directory, define the AWS region you want to work in by running `pulumi config set aws:region us-west-2`, then run `pulumi up`!

Pulumi will first give you an overview of the expected changes and ask if you want to perform the update. In my case, it looks like this:

```bash
     Type                    Name                Plan
 +   pulumi:pulumi:Stack     static-site-s3-dev  create
 +   ├─ aws:s3:Bucket        s3-website-bucket   create
 +   ├─ aws:s3:BucketObject  index.html          create
 +   ├─ aws:s3:BucketObject  style.css           create
 +   ├─ aws:s3:BucketObject  normalize.css       create
 +   ├─ aws:s3:BucketObject  background.jpg      create
 +   └─ aws:s3:BucketPolicy  bucket-policy       create

Resources:
    + 7 to create

Do you want to perform this update?  [Use arrows to move, enter to select, type to filter]
> yes
  no
  details
```

If everything goes smoothly, you'll see more feedback from Pulumi showing each resource that was created:

```bash
     Type                    Name                Status
 +   pulumi:pulumi:Stack     static-site-s3-dev  created
 +   ├─ aws:s3:Bucket        s3-website-bucket   created
 +   ├─ aws:s3:BucketObject  index.html          created
 +   ├─ aws:s3:BucketObject  style.css           created
 +   ├─ aws:s3:BucketObject  normalize.css       created
 +   ├─ aws:s3:BucketObject  background.jpg      created
 +   └─ aws:s3:BucketPolicy  bucket-policy       created

Outputs:
    bucket_name: "s3-website-bucket-89f0341"
    website_url: "s3-website-bucket-89f0341.s3-website-us-west-2.amazonaws.com"

Resources:
    + 7 created

Duration: 6s

```

Notice the `Outputs` section there. Those are the two things we exprted at the very end of our `__main__.py`: the ID of the bucket, and the website URL. Click on the website URL, and you'll see your personal site, deployed to AWS S3 and publicly accessible by anyone! If you don't want to keep this up, run `pulumi destroy` to tear down all of these resources, and you're done!

We're not quite done yet, though&mdash;this site is a little slow, and it's not very interactive. Maybe we want some kind of database associated with it, or the convenience of containers, or the scalability of Kubernetes. Stay tuned for the next tutorial in this series, where we'll keep building on this website to introduce more modern cloud engineering tools until it looks like something you'd happily call production!
