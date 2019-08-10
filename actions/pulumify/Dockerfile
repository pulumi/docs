FROM pulumi/pulumi

# Label things so it lights up in GitHub Actions!
LABEL "com.github.actions.name"="Pulumify"
LABEL "com.github.actions.description"="Deploy static websites to your favorite cloud!"
LABEL "com.github.actions.icon"="cloud-lightning"
LABEL "com.github.actions.color"="purple"
LABEL "repository"="https://github.com/joeduffy/pulumify"
LABEL "homepage"="http://pulumi.com/docs"
LABEL "maintainer"="Joe Duffy <joe@pulumi.com>"

# Install some tools we'll need.
RUN apt-get update -y
RUN apt-get install -y jq wget make

# Install content generation tools.
# TODO(joe): this should eventually get factored out to be pluggable, so that the
# "pulumify" image is agnostic to the specific content management system being used.
RUN wget https://github.com/gohugoio/hugo/releases/download/v0.55.4/hugo_extended_0.55.4_Linux-64bit.deb && \
    dpkg -i hugo_extended_0.55.4_Linux-64bit.deb && \
    rm hugo_extended_0.55.4_Linux-64bit.deb

# Copy the Pulumi infrastructure definition to a well-known location. Because the image
# will immediately begin running Pulumi commands, also switch the working directory.
COPY ./infra /infra
WORKDIR /infra
RUN npm install

# GitHub Actions will mount the repo source code at this volume.
VOLUME [ "/app" ]

# Use the pulumify script as this container's entrypoint -- it will get the job done.
ENTRYPOINT [ "/infra/pulumify" ]
