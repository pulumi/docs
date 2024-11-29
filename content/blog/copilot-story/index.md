---
title: "Copilot Story"
date: 2024-11-29T13:56:13-05:00
draft: false
meta_desc: Learn key engineering lessons from building Pulumi Copilot, including how to minimize LLM workload, validate outputs, and deal with hallucination.
meta_image: meta.png
authors:
    - artur-laksberg
    - adam-gordon-bell
tags:
    - copilot
social:
    twitter: 🚀 Building Pulumi Copilot taught us key AI engineering insights – Minimize LLM workload, validate outputs rigorously & use "skills" for modular tasks. Plus, sometimes when AI hallucinates features, it reveals exactly what users want! 
    linkedin: 🚀 Building Pulumi Copilot taught us key AI engineering insights – Minimize LLM workload, validate outputs rigorously & use "skills" for modular tasks. Plus, sometimes when AI hallucinates features (like a "--force" flag), it reveals exactly what users want! 
---
*Artur Laksberg and others have been working hard on Pulumi Copilot, an AI assistant for cloud engineeinfrastructure. Having worked extensively with conversational AIs at Microsoft before Pulumi, he brings unique insights into building with LLMs. Today he shares his key engineering lessons and an unexpected discovery he's learn along the way.*

## When Your LLM Hallucinates Missing Features: Engineering Lessons from Building Pulumi Copilot

Since joining Pulumi back in June, I've spend my mornings reviewing user feedback for Copilot, our AI assistant. Recently, one message caught my eye: "Your tool doesn't know anything!", except with some spicing langauge in the mix. Having just updated our code database and refined our prompts, I braced for the worst. But the evals we run were still looking strong so what was going on?

<!--more-->

The user was trying to force-delete a stack that still had resources. Copilot confidently suggested using a "--force" flag - a perfectly logical solution, except this flag doesn't exist in Pulumi.

After years in conversational AI, I thought I understood the challenges of chat interfaces but confidently wrong information still gets me every time. This is a day in the life of building on LLMs. Dealing with hallicinations to the user is just a fact of life but this one, this is a specific type of hallicination that I now have a solution to and now that we've launched our REST API and Copilot has been running in production, I want to share how we're handling that particular hallucination, along with key engineering lessons we've learned building with LLMs. Let's start with the fundamental tension between software engineering and prompt engineering...

## Engineering for Reality: Software vs Prompt Engineering

When building LLM-powered applications, the temptation is to throw every task at the model. After all, modern LLMs are remarkably capable - they can generate code, format text, and even create clickable links. But this approach comes with hidden costs.

The core principle we've learned building Pulumi Copilot is this: minimize LLM workload whenever possible by favoring traditional software engineering. Let me explain.

Early in Copilot's development, we had a seemingly simple feature: listing a user's Pulumi stacks with clickable links based on data from a backend api. Our first implementation used a complex prompt instructing the LLM to construct URLs in the format `app.pulumi.com/org/project/stack`. The prompt explained the format, provided examples, and asked the LLM to generate these links from JSON data it had.

It worked - most of the time. But we were seeing occasional malformed URLs and a prompt that complex feels like technical debt. More importantly, we were burning tokens (and money) having an AI construct strings that could be deterministically generated.

The solution was straightforward: generate the full links in the backend service and include them directly in the context. The LLM then needs no instructions on how to creat them. Simple stuff, but it gave us faster responses, perfect URLs, and lower costs.

This pattern - identifying deterministic components and moving them out of the LLM - has become central to our engineering approach. When you find yourself writing elaborate prompts to handle structured data transformations, stop and ask: could traditional code do this better? Could this be decomposed?

One of the ways we decompose this is through what we call skills.

## Skills

To manage the increasing complexity and enable Copilot to handle a wide range of user queries, we extended this decomposition to what we call skills. Each "skill" represents a modular unit of functionality, designed to perform a specific task or access a particular data source. For example, the Insights Skill handles queries about resource usage and configuration ("How many S3 buckets do I have?"), the Cloud Skill interacts with the Pulumi Service API to manage infrastructure ("Create a new project to deploy Metabase on Azure."), the Code Skill generates Pulumi code snippets ("Write a Typescript program..."), and the Docs Skill retrieves information from Pulumi documentation ("How do I use update plans?").  

When a user asks a question, the LLM analyzes the query, determines the user's intent, and selects the appropriate skill (or sequence of skills) to invoke. This function-calling approach, orchestrated by a component we call the "outer loop," allows Copilot to access and process information beyond its internal knowledge base.

Early in development, we faced the challenge of ensuring Copilot could effectively interpret the diverse ways users might phrase their questions. To address this, we undertook a skill mapping exercise, analyzing a large sample of real user queries and categorizing them based on the underlying Pulumi functionality required. This exercise,  allowed us to refine Copilot's intent recognition capabilities and ensure it could accurately route user queries to the appropriate skills. For example, a question like "Show me my untagged EC2 instances" would be mapped to the Insights Skill, with parameters specifying the resource type (EC2 instance) and the tag filter (untagged). This structured approach enabled us to develop a more robust and nuanced system for understanding user intent.

## Debug

Let's talk about another optimization opportunity we identified: the Debug button workflow.

Currently, when users click "Debug with Copilot" on a failed update, we send a text query like "Analyze this update and explain any errors." The LLM then:

1. Determines the user wants to analyze an update
2. Identifies which API to call
3. Calls the API
4. Summarizes the results

But we already know the user's intent - they clicked a debug button. Having the LLM determine intent is unnecessary processing that adds latency and cost. Instead, we directly call the analysis API get the results and use the LLM solely for what it does best: summarizing technical output into clear, actionable explanations.

This exemplifies our broader approach: ruthlessly identify where LLMs add unique value versus where traditional software patterns suffice. Combining deterministic backend logic with LLM-powered natural language understanding - consistently delivers better results.

## Latency

This optimization mindset is crucial because latency remains one of our biggest challenges and whenever you introduce an LLM things slow down. You can mask the speed with streaming, but fastest is not using them at all.

The core lessons from our engineering journey:

* Use LLMs only where they provide unique value
* Understand User Intent
* Move deterministic operations to traditional code
* Implement streaming for better user experience

But even with all that, you can still hit problems.

## The Illusion of Correctness

Large language models excel at generating well-structured, grammatically correct output. They can format tables, craft compelling narratives, and even mimic human conversational styles. But this polished presentation can mask underlying flaws in the information itself, creating a false sense of confidence for users.

One of our early testers, Pablo, encountered this firsthand. He posed a query to Pulumi Copilot, asking for a summary of resources within a specific project. The response he received was impeccably formatted, neatly categorizing resources by type and providing counts for each. It *looked* right, and for us humans sometimes looking right carries a lot of weight.

However, a closer inspection revealed that the numbers were way off. Copilot had asked for the wrong data and then summarized in a way that looked correct. The dissonance between the correct retrieving of the data, the polished presentation and the underlying inability to count was striking. So don't be fooled by polished output. The only way to keep an LLM in production honest is exstenvie set of Evals and tests that get constantly augmented based on real-world user feedback.

## Testing the Untestable: Validating LLM Outputs

When testing traditional code, we expect deterministic outputs. With LLMs, even successful outcomes can vary significantly. Here's how we tackle this challenge.

### Keyword Validation: Start Simple

Our initial approach focused on keyword checking. For example, when testing our update analysis feature, we have a specific test case where a security error occurs. Our test validates that the LLM's response mentions "security" and describes the specific error condition.

This approach works well for basic validation but becomes brittle with complex responses. An LLM might correctly analyze the problem without using our expected keywords.  Furthermore, simply knowing *what* to test is a challenge in itself.

### Learning from Real Users

Early internal dogfooding, where we analyzed logs of real user queries, was crucial for shaping our initial test suite and for understanding what questions users were actually asking. And sometimes user-testing highlighted areas we needed to improve in our documentation.

### Using LLMs to Test LLMs

We evolved to using LLMs themselves for validation. We use Promptfoo for automated testing and LangSmith for monitoring. Our test suite runs against every code change, validating both response content and format.

For streaming responses, we collect chunks into a complete response before validation. While this doesn't test the streaming itself, it ensures content quality.

Here's a concrete example from our test suite:

```python
def validate_update_analysis(response):
    prompt = f"""
    Does this response contain:
    1. Reference to security system error
    2. Explanation of cause
    3. Suggested solution
    Response to evaluate: {response}
    Return YES only if all criteria met.
    """
    result = evaluate_with_llm(prompt)
    return result.strip() == "YES"
```

This approach provides more flexible validation while maintaining reliability. We've found that LLMs are remarkably consistent at this type of evaluation, even when their original outputs vary.

The key is keeping validation criteria specific and responses binary.

## Copilot in Action: Real-World Dog-Fooding

Before launching Copilot publicly, we extensively tested it internally at Pulumi. This phase was invaluable for uncovering bugs, refining our prompts, and, most importantly, understanding how real users would interact with the tool. Here are a few examples of how Copilot proved helpful, even in these early days:

**Debugging Deployments:** One of the first questions our internal users asked was, 'Why did my latest deployment fail?' Copilot successfully pinpointed the cause of the failure in a user's stack and even suggested the CLI command pulumi cancel to stop the problematic update. This early success demonstrated Copilot's potential to streamline debugging workflows.

**Understanding Complex Infrastructure:** Copilot helped our engineers gain insights into our own infrastructure. One user asked, 'How many resources are in production?' Copilot responded with a detailed breakdown, categorizing resources by type, project, and stack. This demonstrated its ability to summarize complex data into actionable insights.

**Generating Code:** Even internally, the demand for code generation was strong. One of the first queries logged was, 'I want a static website on AWS behind a CloudFront CDN.' In a particularly impressive example, one of our Solutions Engineers, tasked with demonstrating Pulumi's CrossGuard policy engine to a prospect, asked Copilot to generate a policy. It worked flawlessly on the first try, highlighting Copilot's unexpected ability to assist with policy as code.

These early successes, observed during our internal dogfooding phase, gave us confidence in Copilot's potential and helped us prioritize development for the public launch. As we continue to gather feedback and iterate on the product, we expect Copilot to become an even more powerful and versatile tool for all cloud engineers.

## Reality is Broken

But yeah, back to that angry user feedback about the "--force" flag. Well that led to an unexpected insight. The hallucination wasn't wrong - it was revealing what users intuitively expect from our CLI.

We're implementing the "--force" flag for stack deletion because our LLM accidentally showed us what was missing. When you think about it, it makes perfect sense: force deletion is a common pattern across developer tools. The LLM, trained on vast amounts of documentation and code, was simply reflecting established conventions.

This has fundamentally changed how we view hallucinations. While we constantly work to minimize them – a frustrated user is something we take very seriously – some of them are clearly potential product signals. When our LLM consistently hallucinates a feature, especially one that exists in similar tools, it's worth investigating. The LLM becomes an unexpected source of user research, drawing on its training across thousands of developer tools and experiences.

Today, we're launching the Pulumi Copilot REST API in preview, built with these lessons in mind. You can now integrate these same capabilities into your own tools and workflows. Whether you're building CLI extensions, chat integrations, or automated deployment checks, the API provides the contextual understanding we've engineered into Copilot.

Try it out at docs.pulumi.com/copilot-api.
