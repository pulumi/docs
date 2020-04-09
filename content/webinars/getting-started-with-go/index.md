---
# Name of the webinar.
title: "Getting Started with Infrastructure as Code using Go"
meta_desc: "Pulumi makes it easy to manage any cloud using Go. Pulumi engineer, Evan Boyle, shows you how to define, test, provision, and verify resources."

# A featured webinar will display first in the list.
featured: false

# If the video is pre-recorded or live.
pre_recorded: true

# If the video is part of the PulumiTV series. Setting this value to true will list the video in the "PulumiTV" section.
pulumi_tv: false

# The preview image will be shown on the list page.
preview_image: "/images/webinar/pulumi_tech_talk.jpg"

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page.
external: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: "getting-started-with-go"

# The content of the hero section.
hero:
    # The title text in the hero. This also serves as the pages H1.
    title: "Getting Started with Infrastructure as Code using Go"
    # The image the appears on the right hand side of the hero.
    image: "/icons/containers.svg"

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: "Getting Started with Infrastructure as Code using Go"
    # URL for embedding a URL for ungated webinars.
    youtube_url: "https://www.youtube.com/embed/s91qF5MLy14"
    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2019-04-03 10:00:00 -07:00
    # Duration of the webinar.
    duration: "39 minutes"
    # Datetime of the webinar.
    datetime: ""
    # Description of the webinar.
    description: |
        Pulumi makes it easy to manage any cloud using infrastructure as code and Go. Pulumi engineer, Evan Boyle, shows you how to define, test, provision and verify resources.

    # The webinar presenters
    presenters:
        - name: Evan Boyle
          role: Software Engineer, Pulumi

    # A bullet point list containing what the user will learn during the webinar.
    learn:
        - "Provisioning: Treat your infrastructure as cattle not pets."
        - "Architecture: Using abstraction and encapsulation to share best practices across teams."
        - "Testing: Unit and integration tests that give you the confidence to move quickly and deploy often."
---

### Transcription

I'm excited to talk to you tonight about
cloud infrastructure and go with Pulumi
so tonight I had set up a couple of
poles interaction with the audience just
want to hear what you all have to say
along the way so you go to this URL here
pull every comm slash Evan Boyle 164 you
should be able to answer these polls and
see live results excited to see who can
get there first and answer the question
so I'm just kind of curious from the
room what is your what is your
background are you an engineer a DevOps
background manager I key student maybe
just curious getting started
okay others some DevOps some engineering
anyone from the other category wanna
curious to hear in chat what background
you come from so things are gonna be
covering today first provisioning and
this is you know treating our
infrastructure as cattle not pets we
want to be able to manage this stuff in
Mass we don't want to give things names
we want to spin it up we want to spin it
down we want every developer to be able
to have their own stack we want to be
able to experiment second we're gonna
cover architecture using things that we
would traditionally use in software
design abstraction encapsulation sharing
these best practices across teams
creating architectural components then
the last thing we're gonna cover is
testing so this is unit and integration
tests to give you confidence to move
quickly deploy software often give you
the confidence to hit that green button
and not have to babysit your deployments
so prerequisites some of this material
was sent out ahead of time but if you're
still curious and want to follow along
and you haven't done this yet I'll leave
this up here for a second you can walk
through Pulumi comm slash doc slash
getting started this will help you
download the Pulumi CLI and get set up
with the AWS CLI we have installation
instructions for Mac Linux windows etc
then all of the content that will be
coming covering tonight is from the
Pulumi examples repo so if you want to
clone this repo into your go path you
can follow along run the examples as we
go and there will be live demos at
almost every step so I'll leave this
here for just a moment in case anyone
wants to enter those URLs and their
browser real quick and also if you
google Pulumi getting started and or if
you just search for Pulumi examples
github you will find this content on
there okay so
one more question for everyone before we
get going here if you could head back
over to the poll I want to know where
are you and your cloud rate so some of
us have no experience at all maybe we're
developing web applications and we have
another team who manages the
infrastructure for us maybe we're just
getting started we're hobbyists on the
side we're excited to move into this
area maybe yeah we're already managing
cloud services in production we're on
call maybe we're deploying some lambdas
or ec2 instances or we're gonna use
clusters awesome Wow so quite a quite an
experienced crowd tonight very cool so
you want to go to the cloud go to the
cloud well how do you get there there's
an awful lot of choices and it's fairly
confusing you know you could start by
creating a VM in seven easy steps in the
AWS console or use the AWS COI or the
SDK or cloud formation or terraform
or chef or puppet or ansible or wow that
hurts right an abundance of choice so
let's just slow down for a minute and
take a step back what do we want out of
our cloud development process
you
develops Wild West yes so what do we
want out of our cloud development
process we want maintainable correct
system first and foremost now a tooling
process that works for the whole team's
like software doesn't exist in isolation
right we have to be able to you know
work with others we want confidence
making changes you know we don't want to
babysit our deployments and we want to
be able to iterate don't want to have to
spend lots of time constructing a
developer environment that needs to be
babysat and upgraded and patched and you
know are these goals really any
different from traditional software
development I don't think so so you know
why not use the same developments we'll
chain that we're using elsewhere same
tools that we love and that good old
gopher so let's start out with a demo I
want to create a simple web server so
that's gonna involve creating a security
group with public looking arrests on
port 80 then looking up the latest
Amazon Linux ami create an ec2 instance
using those two values and we're just
gonna specify to start a simple launch
script that sets up a server on port 80
and export that Public DNS but here this
is the part where you can grab your
computer so what we did here was just
make der - P go path source github
bloomin see into that directory and then
get clone github.com Pulumi examples
okay and so now proceeded into if I just
do a PWD here we're seeded into go path
source github flew me examples AWS Co
web server and I ran this command Pulumi
stackin it this is going to create a new
ephemeral developer environment for me
to deploy into and organize my resources
with I went ahead and set the AWS config
so let me do that real quick Bloomington
fixed at a mus region and I'm in u.s.
West too because I'm on the west coast
so that's where I wanted to point my utq
instances into and then from there I can
do lumia and while that's going I'm
going to go ahead and switch over to the
presentation and here these
steps here so that you can so that you
can follow along yourself if you want to
and I know we haven't looked at any
other code yet we know where we're going
we're deploying a web server and we're
using this command line tool called
Pulumi but we don't really know much
more than that yet well folks are
getting this set up for themselves and
happy to answer a few questions here in
the meantime yep I will walk through the
code okay so why don't I go ahead and
get started doing doing that so let's
break it down what do we have here so
this is a arch this is our show just
just to show you all with what the code
looks like in its entirety you know it's
about 50 lines here but I'm gonna break
it down piece by piece for you so we
start off with just a simple import to
the paluma core engine go bindings and
these just define a set of types some
convenience functions a context object
that is very similar to the context
object you might use in your normal go
program and we have here this Pulumi dot
run function which gives us a context in
which to create cloud resources attach
cloud resources etc so inside of there
we're now going to start actually
creating cloud resources so we've
imported a set of bindings to the AWS
SDK here the Pulumi AWS SDK and we're
creating a new security group and you
can see this security group defines
simple ingress over TCP from port 80 to
port 80 and defines a Sider block
spend just a second here in case anyone
wants to read through this looks fairly
similar to other go code you might see
the Pulumi dot string and Pulumi Don it
may look a little strange but we'll get
to that in just a couple of slides from
there we're gonna go and look up the a
my so we have a utility to do this where
we can use this this pattern expression
here hvm dash star to look up the most
recent Amazon Linux am I
from there we're going to use that ami
and that security group ID here to
create a ec2 instance and our webserver
is a fairly low tech it's just a bash
script it's gonna echo hello world and
do an index.html file and then we're
gonna run Python in be in the background
we're just gonna run a simple HTTP
server on port 80 which we've already
exposed through the internet for ingress
so let's go back to our window here and
see what happened while we previewed our
update it showed us that we created this
new stack this container for our
resources we created a security group
and our ec2 instance great and it looks
like we also exported some resources
here so let's go back and look at that
context export public IP and hosting so
we can take these results off of the
server that we created and export them
which gives access to tooling either
through the command-line other polluting
programs can now reference and import
these values this allows you to break up
your infrastructure into manageable
chunks so that when you do a deployment
you don't necessarily have to worry
about updating you know a hundreds of
pieces of infrastructure so if we go
ahead and do a curl on this we see hello
world great and the other thing that's
really cool about this is we can
actually do some commands to Pulumi so
Chloe has a Clooney stack output command
we can say what was the name of that
that was our public hostname so if we do
a sub command here that still works
Clemmy goes and retrieves the value and
your curl reads that in and hits the
server so ya stack outputs are great
because they're highly composable highly
toolable allows you to create automation
you know DevOps to learn things like
that so let's go ahead and stop here for
some questions
I saw one question right off the bat
which was is Pulumi like Heroku and the
answer to that is no paluma is not a
it's not a pass balloony is is a set of
libraries and an engine and a CLI that
allows you to interact with like any
cloud so you can deploy resources to
we have all the resources of asher AWS
GCP modeled vSphere from vmware lots of
other things like that
so paluma is a is a sdk for building and
defining your cloud applications in any
plan
ah larger font for code okay perfect any
other any other questions before we
before we move on here
how is state managed so there's two
options here so state is either managed
in the Pulumi sacs so we have a free SAS
back-end it's it's free to individuals
free to open-source community for anyone
to use and there's obviously like paid
plans if you have like a you know larger
enterprise or something like that but we
also have open-source backends for you
to store your state either locally just
on disk or you can store your state s3
Google Cloud Storage as your storage so
we have pluggable backends the that you
can use for different cloud storage but
by default it is managed to intercept so
here's a pop quiz for everyone and what
I want to know is is paluma based on
what you've seen is it imperative or is
it a declarative desired state
configuration trick question a-all right
yeah why not both yep anyways the answer
is both so let's go ahead and take a
look at this real quick we're gonna do a
plea stack edge work okay and so this is
gonna go ahead and grab that desired
state configuration that we were looking
at so let's see what we can find here so
this is an ec2 instance it's a our web
server dub dub dub and so you can see
this is a type AWS ec2 instance we have
our inputs here so this is what was used
to create and we allowed some defaults
to get specified here here's the ami
that we wound up looking at they got
resolved at runtime
here's that user data that we specified
we also have some outputs and things
that were created by AWS and then
returned to us awesome so what does that
mean we write imperative code Pellini
execute it produces a declarative
desired state file
and then drives to that desired state so
ephemeral environments Pellini creates
reproducible isolated instances of your
projects we call these stacks so each
developer can spin up and teardown
environments at will you can create
stacks and multiple cloud accounts you
can have stacks in your production
account or you can have your development
in a separate account that's completely
isolated and this allows you to treat
your resources like cattle not pets you
can spin them up and down as you please
if your stack becomes pork you can just
blow it away create a new one so the
workflow for this looks something like
pulling me snacking it which is where we
create an isolated environment pollute
me up is where we deploy to it and
Pulumi destroy is where we clean up all
of those cloud resources so that we
don't continue to charge for them when
we're not using it then if you want to
remove that stack and delete all of the
history associated with it all the
config Pelini staff RM so I'm gonna
actually go ahead and do that real quick
because I want to keep getting charged
for those resources so I encourage
anyone else who may be following along
at home
gloomy destroyed after - yes and this
will get your resources toward them ok
any questions is it possible to use
multi cloud for a stack yes you can
create stacks that deploy to multiple
clouds absolutely you can even create
stacks that deploy to multiple different
AWS accounts we have this notion of
something called a provider so if you
want to create a provider that goes into
separate AWS accounts you can do that
and figure them with different
credentials and then when you create a
resource with a given provider
explicitly it gets placed inside of that
account how feature complete is this
compared with cloud specific solutions
extremely feature complete so the Pulumi
the Pulumi providers actually are
currently based off of the terraform
providers so that means that with like
you know there's communities of
thousands of developers contributing and
using these things across the globe so
oftentimes within days if not hours of
feature is being announced that there's
support in the providers so some of the
providers we've actually built ourselves
like we use the open API spec for
kubernetes and so this past past week
when a 0.18 came out for kubernetes we
actually had our update released before
kubernetes had their branch cut which
was which was pretty cool as the whole
provider is a is code generator what is
my take on the AWS CDK how do you think
this will impact Pulumi development from
official supported frameworks yeah so I
think cdk is a is a great tool one thing
that we're seeing with you know our
largest customers and a lot of our
customers is that these days you know
companies are not just taking advantage
of one cloud it's it's not necessarily
the in one stack they're deploying to
multiple clouds but you know they want
to be able to take advantage of the
machine learning assets in GCP or they
don't want to be tied in on price we
have a lot of kubernetes workloads where
people want to be able to lift and shift
to clouds and don't want to be locked
into a particular vendor cdk is a great
tool but you use cdk for your ad of AWS
development and then what are you gonna
use for your after developmen what are
you gonna use for your what are you
going to use for your CCP development
anyways Pulumi pull
because it gives you and your teammates
a consistent programming model allows
you to use the tools you're familiar
with across clouds and if your company
decides that they want to keep that
option open you don't have to retrain
relearn okay so now we're gonna do a
little bit of Pulumi one-on-one I kind
of brushed aside some of those things
that we saw there like these strange
types right what is a Pulumi dot int a
Pulumi dot string yeah this TCP port 80
what's going on here right so
fundamentally cloud deployments are
asynchronous right some values are are
static didn't we know them at a you know
authorship time right for web servers we
want to always want to expose that port
80
but others only resolved at runtime so
what is that public IP of our ec2
instance well you don't really know
until AWS creates it for you and returns
it back so we have this notion of inputs
and outputs in flew me so we're gonna
just get into some very light kind of
type theory if you haven't seen this
before it's okay it's you know it's will
explain it every step of the way so you
know let's just think T is symbolically
is like some type so T is maybe it's a
string or maybe T's an int or maybe it's
an array of strings or perhaps it's a
stretch right so T is just some raw
concrete value an output of T something
that maybe is produced by a cloud
resource right so an output of T is an
asynchronous object that resolves with
the value of type T so for us we could
think of our public DNS name as an
output of type string it doesn't exist
when we write our program but we know
that when we run it eventually it's
going to resolve with a string so it's
kind of like a promise for any of those
of you who are familiar with javascript
in the web and you know when we create
that ec2 instance it's not just that
public dns it's every member of the
results object is an output so it has to
be a sink we really you know can't know
these values ahead of time and we want
to be able to propagate these values you
know from our ec2 instance or from our
security group into our HT 2 instance so
we have to model use these outputs
asynchronously and now an input an input
of type T is either an output of T which
is that that future that we were talking
about so an input of T it either
promises to eventually give you a T or
currently has a tea so it either says I
will give you back an inch eventually or
I have an INT right now it's either one
and you know this allows us to support
both promptly available arguments like
our port is always a tea or something
that's maybe computed like we're gonna
create this resource group and that
resource group is going to have an ID
and we're gonna need to wait for that ID
to be created for us to give to our ec2
instance right allows us sort of this
this coordination so every input when
creating a plaque loud resource is going
to be an input of tea and every output
is an output it's a little little
repetitive so why all of these custom
types right we have Pulumi string Polly
nyan what is this what does this have to
do with prompt and available values
right well halloumi uses generics over
Union types to represent inputs and
other languages so input of tea is the
union of tea and outputs you right go as
we all know lacks generics for now so we
must define our own custom types so for
Pulumi a combination of these custom
types using interface and reflection
under the hood allow us to represent
this type system while still offering a
strongly typed API on the consumer
facing side of things
so you know we have these asynchronous
values these outputs right and sometimes
we need to manipulate them very common
to take a protocol a hostname a port
that's returned want to construct a
fully qualified URL well you can't just
you know printf of a future right like
that's a complex structure right you
can't just printf that thing in and you
may not you may not have that those
values available when this statement of
code executes civ runtime right these
are features that they resolve when
they're resolved may also want to for
instance set a value of a struct based
off of something that comes back from an
output yeah
what if these values are racing well
that's why Polly has something called
apply and apply allows us to specify a
phone call back function that
manipulates the underlying value when it
becomes available and produces a new
output so we can call apply on our port
and then return a URL that contains that
port after the fact here's a great
example here so we've created a V PC and
that V PC has an output which is a DNS
name so this DNS name is a is an output
of type string a string output in Gulu
nigo terms and we're gonna call apply
string on this and this callback
function will be called with that dns
name when it becomes available and we're
just gonna append a HTTP on the front of
it to return a fully qualified URL and
so now URL is not actually going to be a
string it's an output of type string
right because this apply string is
asynchronous and returns another
asynchronous value so it's kind of like
promises and chaining dot been together
if you've ever done anything like that
you
so sometimes we need to coordinate
multiple outputs like maybe you have a
database in the server that are getting
created and you want to create a
connection string so all is how we
coordinate multiple asynchronous output
types creating a new output right we can
combine this with a fly to manipulate
asynchronous values together right so
here we have a sequel server that's been
created and we basically call Paloma all
to await the server and the database
when we say hey when both of these are
ready execute this callback and return
me this connection string
you
and once again a connection string is
not a string connection string is an
output of type string right so that
means that connection string is an
asynchronous value that promises to
eventually resolved with a formatted
string once sequel server and database
have resolved so Pulumi trying to you
know us personally trying to create some
more idiomatic and useful go have
created a utility function so if you're
doing this just in the basic case where
you're awaiting a couple of strings this
is very common we have a Pulumi dots
printf which hides all of this from you
but now you know what's going on under
the hood questions here how can everyone
how can I wait for the output to be
ready for further usage so the way that
you handle that is you you never access
the raw out value within an output
directly when writing a Pulumi program
you always use paluma all and paluma
apply to basically schedule these so
Pelini basically builds a big dependency
graph right like every time you write a
Pulumi dot all every time you write a
Pulumi don't apply Pulumi create edges
inside of this this you know graph
basically and then eventually does a
topological sort over top of that graph
and then just looks at what is the first
node that I can pull off and start
executing and resolves those
dependencies and continues to do that
and does it in parallel wherever
possible so more or less you you have to
use all and apply because the like the
cloud just by nature is asynchronous is
the Pulumi sdk feature set identical
between go node net and python which
language implementation gets developed
first okay so the Pulumi SDK for go is
is been in preview for a little while
now and we've been working really hard
over the last quarter and we are
actually GA and launching 2.0 at the
Pulumi platform which includes GA of all
of our languages so all of our languages
are
officially supported now okay so moving
on here we're going to talk a little bit
about you know architecture is good we
hear a lot about infrastructure is code
but you know not so much about creating
reusable components and architecture
it's certainly possible to do in the
amal and ESL's but this is our bread and
butter when working with programming
languages right so we want to
encapsulate our design we want to
compose our infrastructure into useful
units we want to extract these into
functions publish them into libraries
unit test them and be able to share
these best practices across our teams
sometimes you have you know maybe a
junior engineer on your team who you
want to be able to allow them to create
a web server and maybe maybe put some
HTML inside of it but you don't want
them to necessarily change the network
configuration like maybe maybe they
don't have that expertise or you know
maybe maybe you are a security engineer
and you've set up these best practices
and you just want to hide the level of
or control the level of abstraction
that's exposed this is something that we
do all the time in software design but
something that's not so common in
infrastructure so let's take a look at
that web server example that we just had
and here we have encapsulated this into
this create infrastructure function and
create infrastructure is going to return
this infrastructure object which
contains a security group and a server
and here we've actually said hey you
know we're very happy with the
functionality of our web server we don't
want to provide any configuration to our
customers at all and so we're just going
to control the entire thing so some
things to note here instead of using a
user data stream to start up that web
server we've actually baked an ami ahead
of time so that that web server will
start up automatically
and here now our code executing the side
of our Pulumi dot run you know looks a
whole lot simpler right we just call
this create infrastructure function that
returns this info object that has our
our security group and our server inside
of there we can still export those
values as we did in our previous program
and these improvements are shared right
you know so we bake that web server like
I said into an ami instead of having to
use user data there's no worry about a
let's see you know if if I'm a if I'm an
engineer and you know I'm just getting
started I'm like hey you know I instead
of saying hello world I want to say
hello world hello mom
you know uh-oh I just made a big mistake
in my in my shell script right so we had
the ability to write abstractions that
you know we could parameter parameterize
this HTML this message that gets echoed
into this index file and build that ami
we have the ability to do that way and
you control that with views um
encapsulation so so testing let's get
into testing all right since we're in
the NGO ecosystem you know can we use
all of our favorite tools that we use
for you know go tests right the built-in
one no what about the tools we use for
mocking or code coverage tools and the
answer is of course yes yes we can use
all these things we want to use all
these things these are the things that
we're using every day so let's write a
unit test against our create
infrastructure function we want to
verify a couple of things right so we're
building some operational tooling around
tagging you know we want to make sure
that we're able to query every ec2
instance with with the webserver tag on
it so we want to verify that that name
tag is on there we want to make sure
that no one is specifying user data
right because we have already baked in
with the AMI that web server and we
don't want any conflicts there we also
want to validate SSH is disabled we
don't want any of our public facing web
servers to have SSH on them we want to
make sure that none of our user data is
at risk okay so that's another
opportunity to go ahead and grab your
computer
and once again we're still inside of
this Pulumi examples repo so if you're
inside of the Pulumi examples repo all
you need to do is CD into testing - unit - go and run go tests so let's go ahead
and do that
great and while that gets started let's
go ahead and look at some of this code
so we have this this test function here
test infrastructure that instead of
running inside of
halloumi run we run it inside a Pulumi
dot run error which allows us to specify
a set of mocks
I'm not going to go through these marks
they're not particularly interesting
it's just a couple of lines of
boilerplate but they're in there and the
examples repo if you'd like to look so
we run those marks we create a wait
group that corresponds with the number
of assertions and the number of tests
that we'd like to run here and then we
do those assertions run that way because
these assertions are going to happen
asynchronously inside of our all and
apply calls and then we assert that
there's no error at the end let's just
go back here so we see go test passed in
half a second excellent so what did
these tests actually look like so we
want to be able to check do we have a
tag with the name field right and we
want to check for each server so for now
we're only creating a single server but
we want to make sure that when we report
an error on that server we know which
server in case we add more in the future
right in case we're doing this inside of
a loop okay so we have passing the you
our end of that server and pass in those
tags wait for all those to be promptly
available or eventually available and
then execute this apply key where we
take that first value which is going to
be the you our n the second value that
map tags and we're going to check to
make sure that map contains the tag name
we're gonna call done on that wait group
okay next we're gonna text and make sure
that all of these user instances do not
have user data specified so similarly
passing in the URL and the user data and
calling all to make sure that those
values are promptly available or
eventually available once they're
eventually available this apply T
function will execute and we will assert
that the user data string is nil right
if it's not me we're going to throw this
error believable use of user data
on server server you are once again
calling done on that way through
finally we're gonna test and see if port
22 is exposed so this one is a is is you
know a little a little bit more involved
so we're gonna iterate through all of
the ingress is and check for that wide
open cider block there right and if that
wide opens if we find that wide open
cider block we know we're open to the
internet right and we're gonna break out
and we're gonna check and see is the is
the port that we just that we just found
a public cider block for 22 if so if
we're open to the Internet then we've
got an illegal ssh board we're gonna
fail the test this ensures that none of
our none of our tests are none of our
web servers are open to the Internet
it's a nice thing to be able to verify
locally so you know once again this is
unit testing we aren't verifying the
functionality of a particular cloud
service the behavior of your
infrastructure you know we don't have
this is an extensive mocking so we can't
make an HTTP query you know we're not
mocking out all of the cloud services
but what we can verify is the control
flow the logic the propagation of
expected values through your code right
the number of times the create call to a
given resource it gets made right so the
behavior of your code in isolation and
not become you know and the great thing
about this is it's blazing fast you can
do it locally without the CLI without an
internet connection you have a tight
feedback loop so you know we also
sometimes we do want that full
confidence we do want to take the time
to spin up an ephemeral stack and
execute and then we're closed right
making requests against our live
infrastructure verify like these
integration of these different pieces of
of cloud services this end and request
flow and then we want to automatically
clean up that environment whether or not
the test succeed we don't want to leak
resources we don't want to keep paying
for that right so Pulumi has a test
harness our integration test harness
that allows you to do just that and in
just a few lines of code see we
configure here a directory
says this is where my Pulumi program
exists a config map which is the list of
values that are required to inject into
the program for it to be able to run you
saw when I initially ran my program I
did Pulumi config set AWS region this
allows us to do that inside of code in
this automated test harness and then
this extra runtime validation function
is going to be run with the resulting
stack so that stack is going to be
populated with stack outputs so you will
be able to access that website URI
append it to a like turn it into a fully
qualified URL and assert that when we
make an HTTP request against it we get
that hello flew me back and then we just
do an integration dot program test
passing in the the the go testing object
and the Pulumi test configuration this
program is going to execute spin up my
web server stack do the extra runtime
validation and then tear it down
reporting the results and I don't have a
demo for this in real time you know it
can take a couple of minutes to spin up
cloud resources execute these requests
and care it down you know these these
tests are very very valuable but they
are a little bit more expensive in terms
of time they're not necessarily as great
in that tight feedback loop
but this deploys real cloud resources
and validates their behaviour so this
can catch bugs and things like I am and
access control making sure that your
requests can flow and and through the
system making sure that lambda has the
ability to pick up that file out of x/3
make sure that propagation and secrets
happens as you would expect it also
allows you to do some really interesting
things like this this integration test
option allows you to specify a directory
but it also allows you to specify an
edit directory so you could have a
second version of your program perhaps
checked out to a different revision of
the code and then simulate an update so
you could spin up your resources on the
initial flew me up and then by
specifying that editor do a second flew
me up on a new version of the code
simulating a deployment this may allow
you to measure up the uptime make sure
that you still have
database availability make sure that
none of your resources get deleted so
this is a great way if you're making
kind of a risky change and you're
concerned you want a game-day ahead of
time balloony makes it really easy for
you to do that you can also do things
like verify health checks and alarm
configuration so like I said this is
much slower than unit tests this is not
always a great thing to have in your
tight dev feedback loop but you know
before you go to make that pull request
you want to verify every core taste of
your infrastructure that maybe you
didn't touch when you were working on
this feature and you know that brings
great confidence and enables the ICD for
your intra which is you know something
that's not always that common it's
common the more common than you would
hope so have to babysit these builds and
a decent these deployments so we want to
be able to hit that big green merge
button and you know sit back to stop our
hands and and go work on something else
you don't want to have to babysit so
with that anyone have questions about
integration testing so just taking a
look here at the ecosystem so Pulumi is
tightly integrated with you know all the
source code providers all the identity
providers that you would expect we
support a suite of languages for
authorship including typescript go no
js' Python all of the dotnet languages
and with those languages comes the tools
that you're used to the package manager
is you're used to the editors you're
used to the CI/CD integrations right on
top of that we have support for all the
cloud environments AWS asher GCP
kubernetes on any cloud that you want
OpenStack VMware the list goes on so
just in summary today we talked about
how do we provision our application
treating our applications our
infrastructure apps as cattle not pets
right let me spin these things up we
spin them down we onboard a new teammate
onto the team you know use synonyms for
the Pulumi getting started flow and
there you go they're up and running and
ready to deploy your application that's
it there's there's no creating resources
through the console no complicated
custom set up we also talked about how
do we take a cloud resource and turn it
into a piece of architecture that we can
this abstraction that we can encapsulate
a best practice that we've defined
within our team
and share it share it at that at that
correct level of encapsulation at that
correct level of abstraction for that
giving consumer right expose the things
that you want to expose maybe maybe
allow them to specify the HTML that gets
rendered inside of the web server but
don't allow them to configure the the
network configuration don't allow them
to change that right Kumi allows us to
do that and then finally we talked about
testing so the unit and integration
integration testing strategies that give
us the confidence to move quickly and
deploy often
so you know I just want to say thank you
and thank you to hatch IT for setting
this all up and thank you to all of you
for coming here and talking about go and
talking about pelini tonight with me
here's some more ways for you don't
learn about Pulumi if you want to join
the community so we have everything from
slack to github where all of our work is
done out in the open so you can go and
see pull requests that I've been working
on this week or the rest of the team has
been working on in preparation for 2.0
release it's coming up in the next two
weeks we have video.you tutorials
you can always reach out to me directly
on our community slack I'm there all the
time and we have more workshops coming
up a lot of them in languages other than
go if there are those of you out there
who might be interested in learning some
other languages as well
