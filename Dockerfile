FROM ruby
COPY Gemfile /src/Gemfile
COPY Gemfile.lock /src/Gemfile.lock
WORKDIR /src
RUN apt-get update 
RUN apt-get -y install curl
RUN curl -sL https://deb.nodesource.com/setup_8.x | bash 
RUN apt-get install -y nodejs
COPY Makefile /src/Makefile
RUN make ensure
COPY . /src
CMD make serve