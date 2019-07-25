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
RUN apt-get install -y jq

# Copy the Pulumi infrastructure definition to a well-known location. Because the image
# will immediately begin running Pulumi commands, also switch the working directory.
COPY ./infra /infra
WORKDIR /infra
RUN npm install

# GitHub Actions will mount the repo source code at this volume.
VOLUME [ "/app" ]

# Copy the entrypoint script and use it as this container's entrypoint.
COPY ./pulumify /usr/bin/pulumify
ENTRYPOINT [ "/usr/bin/pulumify" ]
