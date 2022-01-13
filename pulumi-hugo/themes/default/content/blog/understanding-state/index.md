---
title: "Understanding State"
date: 2021-12-13
draft: false
meta_desc: |
    Do a quick dive into state and state management via some real-life physics.
meta_image: meta.png
authors:
    - laura-santamaria
tags:
    - state
---

Let's talk about state, shall we? State is the collective properties of the
system from one point in time. Think of it effectively as a snapshot of a
system. State in computer science is actually a lot like state in physics, so
let's start with something that's a bit easier to understand.

We're going to examine a physical system: A ball dropping from my hand to the
ground one meter (1m) below. The ball starts out at one point in time where it
is at rest in my hand. It has no velocity, no motion. It has properties like
color, texture, etc. that do not and will not change. The _state_ of the ball
can be thought of as a position of 1m off the ground, with a color, texture,
etc., and no velocity. Each of these variables has a specific value at that
point in time.

Now I open my hand. At the instant the ball leaves my hand, the ball has moved
some distance to the ground, and its velocity has increased. Its state,
therefore, has changed. If we imagine capturing the ball's motion with a
slow-motion camera, we see a single frame for each position of the ball. Each
frame is a single state of the system, and the difference between the frames is
a change in state. When our state changes, one or more variables change. In this
case, the variables of speed and direction (combined as velocity) and distance
from the ground

When we think about our infrastructure that we manage with systems like Pulumi,
we're thinking about states of the infrastructure system. How we move from one
state to another, which variables change from state to state, and what the
starting state and ending state are would all be considered and tracked. Most
infrastructure-as-code systems track state in some fashion, though most rely on
you, the user, to manage that state tracking with state files or other systems
that you have to manage and choose. For this deep dive, though, I'm going to
focus on how the hosted Pulumi service manages state.

When considering the state of your infrastructure over time, we need to think
about the transition of the infrastructure's state between one point in time and
another. Our program for any infrastructure-as-code platform defines the ideal,
final state of the system. As the code executes, the infrastructure goes through
a sequence of states, which we call the behavior of the system. For each tick of
processing of the code, there is a defined state. Therefore, during the
execution of the code, we see transitions in state. That state change needs to
be tracked so that, at any point in time, we know how the behavior of the system
changed. That's important for having multiple programs trying to execute at
once, debugging system changes, and other important considerations for working
in teams across a remote, cloud-based environment. In short, it's good to know
what changed! When you use Pulumi, you have access to that change information
through [audit logging](https://www.pulumi.com/docs/intro/pulumi-service/audit-logs/)
and can use [webhooks](https://www.pulumi.com/docs/intro/pulumi-service/webhooks/) to
feed those changes into other systems for observation, like a shared monitoring
system with your security team or a distributed team that can't look over your
shoulder as something deploys.

Now, code execution doesn't always happen *exactly* as we want it to due to all
kinds of environmental factors from different chipsets to varying network
connectivity and more. If you *really* want to go down the rabbit hole here, I'm
going to point you to formal methods, especially TLA+. Formal methods are a
great way to model state for distributed, concurrent systems to identify race
conditions, poor assumptions, and other common flaws in temporal logic. For now,
though, we're going to keep talking about state in the more abstract sense.

Putting all of the states together along with the transitions they can have so
that we have pathways from initial states to next states in a clean pattern, we
get what's called a state machine. When working with concurrent distributed
systems, or systems that can have multiple things happening simultaneously that
are spread out over many machines&mdash;basically, any cloud system created
ever,&mdash;knowing the various states, changes, and combinations thereof is
extremely important to ensuring that the one path we *want* the system to take
to a final desired state is the one that is taken.

When using Pulumi, you don't have to worry about the state machine. The Pulumi
Service tracks all of those states for you once the infrastructure's initial
state is declared by importing the infrastructure to or creating it with Pulumi.
You declare the desired state in code in the language of your choosing, and then
that code tells the Pulumi CLI what you want. The CLI does all of the state
computation, requesting and defining the pathway to the infrastructure final
state defined in the program, and the Pulumi Service stores the state at each
moment in time. The Pulumi dashboard, by extension, is your window into the
Pulumi Service where you can see current state, desired state, and the behaviors
of the system.

I hope this short introduction to how state works, especially with
infrastructure-as-code platforms, helps get you on your way! If you want to read
more about state with Pulumi (and get some nifty diagrams), head to
[State and Backends]({{< relref "/docs/intro/concepts/state" >}}). Until
next time!

---

Leslie Lamport has some fantastic, free resources and videos about the formal
specifications in TLA+, which he created, at [his site on
TLA+](http://lamport.azurewebsites.net/tla/tla.html). I'm a huge fan.

Also, if you want to watch a short video on state to get a better sense of the
physics example, head on over to
[PulumiTV](https://www.youtube.com/c/PulumiTV/videos) for [episode
3](https://youtu.be/u2C71uF0rdM) of our [Quick Bites of Cloud Engineering
series](https://youtube.com/playlist?list=PLyy8Vx2ZoWlohOiedbaQqT5xYRkcDsm10)
all about state.
