ARG NODE_VERSION=14
FROM mcr.microsoft.com/vscode/devcontainers/javascript-node:0-${NODE_VERSION}

ARG VARIANT=hugo
ARG VERSION=latest

# Download Hugo
RUN apt-get update && apt-get install -y ca-certificates openssl git curl yarn && \
    rm -rf /var/lib/apt/lists/* && \
    case ${VERSION} in \
    latest) \
    export VERSION=$(curl -s https://api.github.com/repos/gohugoio/hugo/releases/latest | grep "tag_name" | awk '{print substr($2, 3, length($2)-4)}') ;;\
    esac && \
    echo ${VERSION} && \
    wget -O ${VERSION}.tar.gz https://github.com/gohugoio/hugo/releases/download/v${VERSION}/${VARIANT}_${VERSION}_Linux-64bit.tar.gz && \
    tar xf ${VERSION}.tar.gz && \
    mv hugo /usr/bin/hugo

# Install go
ARG GO_VERSION=1.16.9
RUN rm -rf /usr/local/go && \
    wget -O ${GO_VERSION}.tar.gz https://golang.org/dl/go${GO_VERSION}.linux-amd64.tar.gz && \
    tar -C /usr/local -xzf ${GO_VERSION}.tar.gz && \
    rm ${GO_VERSION}.tar.gz

ENV PATH=$PATH:/usr/local/go/bin

# Hugo dev server port
EXPOSE 1313
