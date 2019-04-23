FROM ruby AS builder

COPY Gemfile* /src/
WORKDIR /src
RUN gem install bundler -v '2.0.1' && bundle install

RUN apt-get update && apt-get -y install \
  curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash 
RUN apt-get install -y \
  nodejs
RUN npm install broken-link-checker typedoc
COPY Makefile /src/
CMD make serve
