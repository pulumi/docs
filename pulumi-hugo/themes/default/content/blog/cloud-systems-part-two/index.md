---
title: "Cloud Systems Part Two: Containerizing a Website"

date: 2021-12-27T12:26:10-08:00

draft: false

meta_desc: In this series, learn modern cloud engineering practices and tooling, continuing with expanding our personal website and containerizing it!

meta_image: meta.png

authors:
    - kat-cosgrove

tags:
    - cloud-systems
    - tutorials
    - docker

---

Cloud engineering is taking over software development. In a lot of ways, this is great; it allows us to build and deploy more complicated applications with less difficulty, and maintaining those applications becomes less troublesome too. We can release smaller updates more quickly than ever, ensuring that we can stay on top of feature requests and security issues. That said, the rise of cloud engineering has also introduced a lot of complexity in the form of dozens of services even within just one cloud provider. Figuring out where to start can be tough, so let’s take a practical tour! In this series, I’ll walk you through building a personal website and deploying it using modern cloud engineering practices.

<!--more-->

In part one of this series, we built a personal website and deployed it to AWS S3. That works perfectly well for a static, single-page application with minimal interactivity, but if you want server-side routing or database interactivity, things have to get a little bit more complicated. In part two of this series, we’ll be adding a couple more pages to our personal website, adding server-side routing, and containerizing it with Docker.

## Containers

So, what’s a container and why would you want to use one? You can think of a container here the exact same way you think of containers on a shipping barge. On that barge is a bunch of shipping containers, and inside each shipping container is a bunch of packages. The barge itself is your computer (or your cloud environment), and the shipping containers house your applications.

It may also help to think of them as smaller, more lightweight incarnations of virtual machines. While a virtual machine virtualizes the machine’s physical hardware through the use of a hypervisor, a container virtualizes only the operating system. A virtual machine is usually several gigabytes in size, whereas a container is usually less than a gigabyte. The small size and speed of deployment as compared to a traditional virtual machine has given rise to the popularity of designing applications as collections of microservices (several single-purpose services running in containers that, when working together, make up your complete application) instead of monoliths (all of your application code and services running as a single unit, often within a single file).

Deploying your application using containers allows you to package your application code alongside everything required to run it, including its dependencies and an operating system. You know how sometimes you hand code off to someone else, but it doesn’t run for them, so you go “Well, it works on *my* machine,” and just shrug? Using a container is pretty similar to just deploying your machine. The most popular container engine today is Docker, so that’s what we’ll be using today.

## Prerequisites:

- [Docker](https://www.docker.com/products/docker-desktop)

- Python3

Before we go into containerizing and deploying our website, let’s make it a little bit more useful. For this, we’re going to be using Flask, a lightweight web framework for Python. Fork and clone [this GitHub repository](https://github.com/katcosgrove/cloud-systems-101) to get the full sample code for part two of this series.

## Expanding the Website

Our file structure gets more complicated now that we are building a more dynamic website with server-side routing and throwing it into a Docker container. You will have something like this:

```
container-tutorial
├── Pulumi.yaml
├── requirements.txt
├── __main__.py
└── website
    ├── Dockerfile
    ├── requirements.txt
    └── app
        ├── server.py
        ├── static
        │   ├── normalize.css
        │   ├── style.css
        │   └── background.jpg
        └── templates
            ├── base.html
            ├── index.html
            ├── portfolio.html
            └── about.html
```

Everything contained within the `app` directory is the website itself. We now have server-side routing, and a few different pages. To run it locally and see what the new website looks like, `pip3 install flask` to install the Flask web framework and then run `python3 server.py` from the `app` directory. Flask will return an IP address where your website is running; navigate there in your browser and click around a bit!

`server.py`

```python
from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route('/portfolio')
def portfolio():
    return render_template("portfolio.html")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=True)
```

Where before our entire website was made up of a single HTML file, we now have several, and we're using Flask to handle the routing between them. In this server file, three routs are defined: home, about, and portfolio. Flask handles serving these up for us, and associating a route with a particular HTML file. This way, we get a nice `www.mywebsite.com/about` URL instead of something like `www.mywebsite.com/about.html`. Building a website this way also means we have the ability to apply some logic to each of these routes, such as adding database interaction, user login, and passing conditional variables from the server to the templates that will be rendering each page. We aren't doing any of that yet, but we will!

At the bottom, we're binding the Flask application to `0.0.0.0:80`. You can change that to any other unoccupied local IP address and port you like.

## Templating

Flask can make use of a templating engine called Jinja2 to make adding pages to your website a bit less repetitive. You start with one template, in this case called `base.html`, that contains any HTML you want to exist on every single page.

`base.html`

```html
<!DOCTYPE html>
<html>
<head>
    <meta charset="utf-8">
    <title>Hello world!</title>
    <link rel="stylesheet" href={{ url_for('static', filename='style.css') }}>
    <link rel="stylesheet" href={{ url_for('static', filename='normalize.css') }}>
</head>
<body>
    <header>
        <div class="logo"><i class="fas fa-cat"></i></div>
        <nav>
                <ul>
                    <li {% if request.path == url_for('home') %} class="active" {% endif %}>
                        <a href="{{ url_for('home') }}">Home</a>
                    </li>
                    <li {% if request.path == url_for('about') %} class="active" {% endif %}>
                        <a href="{{ url_for('about') }}">About</a>
                    </li>
                    <li {% if request.path == url_for('portfolio') %} class="active" {% endif %}>
                        <a href="{{ url_for('portfolio') }}">Portfolio</a>
                    </li>
                </ul>
            </nav>
        <ul class="social">
                <li><a href="http://github.com/katcosgrove" target="_blank"><i class="fab fa-github-alt"></i></a></li>
                <li><a href="http://twitter.com/Dixie3Flatline" target="_blank"><i class="fab fa-twitter"></i></a></li>
                <li><a href="http://linkedin.com/in/katcosgrove" target="_blank"><i class="fab fa-linkedin-in"></i></a></li>
            </ul>
    </header>
{% block content %}{% endblock %}
</body>
<script src="https://kit.fontawesome.com/b4747495ea.js" crossorigin="anonymous"></script>
</html>
```

This file includes some metadata, stylesheets, the header, navigation, and any Javascript we want to link in. All of the content in this file will exist on every page. Below the header, in the body, you'll see `{% block content %} {% endblock %}`. That's where additional, page-specific content will be added.

`index.html`

```html
{% extends 'base.html' %}

{% block content %}

<div class="content">
    <h1>Your Name</h1>
    <h3>Job Title at Company</h3>
</div>

{% endblock %}
```

This is all that exists in our `index.html` now. The first directive tells Jinja2 that this bit of HTML goes in the `base.html` template, and the remaining two wrap the content we want to insert. The same thing is happening in `about.html` and `portfolio.html`. Neat, right? Jinja2 is not unique to Flask, so you can use this templating engine with another web framework if you prefer.

While we could deploy this as-is, it's a bit unwieldy. Let's wrap it up into a container.

## Dockerizing our Website

In the `website` directory, we have something called a Dockerfile. Dockerfiles tell the Docker engine what to do with your application, how your container should behave with respect to the wider internet or other containers, and what needs to be done inside of the container for your application to run. Ours looks like this:

```bash
FROM ubuntu:20.04

COPY app /app

WORKDIR /app

EXPOSE 80

RUN apt-get update && \
    apt install -y gcc python3-dev python3-pip python-markupsafe

COPY requirements.txt /app

RUN pip3 install -r requirements.txt

ENTRYPOINT [ "python3" ]

CMD [ "server.py" ]
```

This Dockerfile says that our container should be running ubuntu:20.04 as its operating system. It will pull the Ubuntu image from Docker Hub, their public image registry, though you can pull from another registry here as well. The `COPY` directive moves our website’s files (the `app` directory) into the container. We then set our working directory for all future commands run inside of the container to `/app` to reduce the amount of typing we have to do later on, update Ubuntu, and install some dependencies using both apt and from the requirements.txt file we also copy over. Lastly, an entrypoint and command to actually start our application are defined. There is a slightly less verbose way to start the application, but this way of defining an `ENTRYPOINT` and `CMD` is fairly common, so it’s worth seeing here.

To see this run locally, we first need to build and tag the image. From the same directory as your Dockerfile, run the following command:

`docker build --tag container-tutorial:latest .`

We are calling the docker CLI, telling it we want to build a container, and indicating that we want to tag it at the same time. The tag isn't strictly necessary for the container to run, but it does make the container easier to identify and interact with. We're also assigning it a version of `latest`. Note the trailing dot at the end of the command, which is the part of the command that indicates the location of the Dockerfile we want to build.

Run `docker images` to see a list of all images you have built. Something like this should be in the list:

```bash
cloud-systems                                                       latest                                                             0ce569ac0360   10 days ago    408MB
```

Now the container is built, we need to run it and forward the container’s port to a local port so we can see our site.

`docker run -d -p 80:80 container-tutorial`

There's a lot going on in that command, so let's take a closer look. the `-d` flag is short for `--detach`, and it tells the Docker engine that we want to print the container's ID and run it in the background. The `-p` flag is short for `--publish`, and it tells the Docker engine to publish the container's port to the host. In this case, port 80.

Run `docker ps` to get a list of all running containers, and you'll see something like this:

```bash
CONTAINER ID   IMAGE                COMMAND               CREATED       STATUS       PORTS                                       NAMES
f95362faf3cd   container-tutorial   "python3 server.py"   7 days ago    Up 7 days    0.0.0.0:80->80/tcp, :::80->80/tcp           affectionate_jackson

```

That's our website! You can see the container ID, the image tag, the commands that ran for it to start the application, its host, the container port, and the port it forwarded to. Go to `localhost` in your browser, and the website is up!

We're hosting this locally, though. It's not accessible by the wider internet, and even if it was, our machines would be dealing with all of the traffic. There's nothing in place to distribute traffic or restrict access. Worry not, cloud services exist for that, too. In the next in this series, we'll take our containerized website and deploy it to AWS Elastic Container Service, complete with AWS networking configuration, IAM roles, and AWS Fargate!
