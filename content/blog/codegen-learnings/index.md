---
title: "Learnings from building AI-based code generator"
date: 2024-12-31T20:00:00-05:00
draft: false
meta_desc: Learnings from building a RAG for Pulumi code generator
meta_image: meta.png
authors:
    - artur-laksberg
    - simon-howe
tags:
    - Copilot
    - ai
    - iac

---
## Reliable code generation in the age of AI

When asked about his research process, Anthony Bourdain would describe how he'd blend his formal culinary training with deep dives into local food culture - from market stalls to family recipes. Modern AI code generation follows a similar path: it can't just rely on what it knows - it must tap into continuously evolving, domain-specific knowledge bases. Just as Bourdain would combine his classical French training with techniques learned from local kitchens, AI code generators blend their built-in knowledge with retrieved code snippets and type definitions to generate code that accurately represents user's intent.

This fusion of base knowledge with contextual understanding is especially valuable for Infrastructure as Code (IaC), where rapidly evolving cloud providers and libraries make manual development challenging, traditional debugging cycles impractical, and errors catastrophically expensive.

The role of IaC won't diminish in the age of AI - if anything, it will become even more central as systems grow increasingly complex and automated. Trustworthy code generators will be a key ingredient in the recipe for modern infrastructure management.

In this post, we want to share the learnings from developing code generation for Pulumi, based on both our production IaC generator powering the [Pulumi AI](www.pulumi.com/ai) and the Pulumi Copilot, as well as features and approaches we're still exploring.

## Using RAG for code generation

Pulumi supports over [120 providers](https://www.pulumi.com/registry/), including major cloud providers such as AWS, Azure, Google Cloud, and Kubernetes, as well as many other services and platforms. New providers are being added continuously, and the existing providers change as their capabilities grow.

Our goals is to to generate the most accurate code for every provider -- code that is not only correct but also reflects their latest capabilities.

LLMs are great at generating code however they are limited to what they have learned before their knowledge cutoff date. This means that the latest changes in the providers will not be reflected in the generated code. This also could lead to hallucinations when the model struggles to answer a question that requires up to date knowledge.

To help us solve this, we rely on the technique known as the _Retrieval Augmented Generation_ (RAG). RAG helps code generation by integrating information retrieved from external data sources. In Pulumi, we call this data source the _Registry_ - it's the database we maintain that containing type schema and usage information for every provider.

At a high level, using RAG involves following steps:

1. Analyze user's question.
2. Look up the pertinent information from the Registry.
3. Format that information in a system prompt that LLM can understand.
4. Make the LLM call asking it to generate the code using the additional information in the prompt.

There is lot of fascinating details here, so let's dig in!

## The anatomy of Pulumi Copilot RAG

Before going into the details, let’s consider a simple yet essential insight: for a RAG to be useful, it must meet two key requirements:

1. It must _contain_ the necessary information.
2. The information must be easily _searchable_.

Let's take a sample user query:

> "Generate code for S3 Bucket"

To fulfil the request, the system needs to intuit the following:

- The **cloud provider**. This can be determined based on the fact that S3 is a common storage solution in AWS, and possibly the fact that the user's [organization has stated](https://www.pulumi.com/blog/copilot-system-prompts/) AWS as their preferred cloud provider.
- The **programming language**. This information can again come directly from the organizational preferences, or from the user's prior conversations.
- The information about the **type** (or types) that must be created - its name and schema, the package it is in, and the capabilities it supports.

While all three of the above can be conceptually called the RAG, only the last information is actually stored in the Registry. We can now expand the original user query into the following system prompt that is going to guide the code generation:

> "Generate TypeScript code for S3 Bucket, the AWS resource defined in package `@pulumi/aws`, type `aws.s3.Bucket`
> with its schema defined as follows: ...

While we had to rely on some guesswork to come up with this prompt, fortunately this process can be iterative - if we don't get all of it right the first time, we can try again with additional information that will help us refine the results. This is an important point we return to later in the post. <!-- ref to self-debugging -->

### Assessing search quality using recall and precision

To assess how good our RAG is, we need to first understand the two fundamental concepts used in the information retrieval systems: the _precision_ and the _recall_. Imagine that you're looking for an apple pie recipes in one of Jamie Oliver's cookbooks. The book has a recipe for a classic American apple, a Dutch apple pie and a modern take on a French apple tart. Due to the book's narrative approach with the recipes woven into the stories and context, you've managed to retrieve only the first two recipes but failed to consider the French apple tart. Having succeeded in retrieving 2 ouf 3 relevant documents, you have achieved a **66% recall**.

Because you were looking for the word "pie", you also retrieved a recipe for a Shepherd's pie, which, while delicious, does not qualify as an apple pie. Another document that came up was a fish pie - a classic British dish that, alas, does not contain apples or even a pastry crust. Since only 2 of your 4 retrieved documents can be legitimately classified as apple pies, you have achieved a **50% precision**.

Now let's formalize this a bit. Recall measures the ratio of the relevant documents retrieved to the total number of relevant docuemtns in RAG:

$$Recall = \frac{N(Retrieved \cap Relevant)}{N(Relevant)}$$

Where

- $N(Retrieved \cap Relevant)$ is the number of documents that are both retrieved and relevant.
- $N(Relevant)$ is the total number of relevant documents in the database.

Good recall means that many documents relevant to the query were retrieved.

$$Precision = \frac{N(Retrieved \cap Relevant)}{N(Retrieved)}$$

Where $N(Retrieved)$ is the total number of documents that were retrieved.

High precision means that many of the retrieved documents were relevant.

Naturally, an effective RAG maximizes both the recall and the precision. It's [been said](https://buduroiu.com/blog/rag-llm-recall-problem) that high recall is essential to ensure relevant content is available to the code generator while precision is the parameter you want to optimize for to avoid hallucinations.

### Practical concerns

Precision and recall are essential in understanding the information retrieval quality, but they are quite hard to measure in practice. Unlike a cookbook, Pulumi registry contains thousands of ever changing documents, and evaluating how many of them are relevant for every user-submitted query is impractical making recall evaluation for live traffic next to impossible. Things a little easier with precision, where we're dealing with a small number of documents, but even that metric requires a non-trivial evaluation of relevance, which requires an LLM call or a human judge where the number of documents is small.

Fortunately, other metrics that often can effectively estimate retrieval quality have been developed. We have found a metric that can predict, with some degree of accuracy, whether the generated code will successfully compile. For this metric, we compare the _tokens_ present in the prompted produced by the LLM with the number of tokens present in the actually generated code. (By token here we understand a compiler token - an identifier such as the name of a class, method or a field and not a traditional LLM token concept),
Intuitively, if a token present in the prompt also appears in the generated program, we can assume that the token effectively contributed to the generated program. Tokens in the generated program that were not part of the prompt are not necessarily wrong but they are less trusted (they can come from the LLM built-in knowledge or were, ahem, hallucinated)

$$prompt \ coverage = \frac{N(\text{Tokens in prompt} \cap \text{Tokens in code})}{N(\text{Tokens in code})}$$

<!-- Note: our documents call is Recall, which is not how industry uses this term (see above) -->

Prompt coverage is a metric we can observe in production, and it's one of several metrics we use when updating providers to ensure we haven't regressed the quality of the RAG.

### Semantic search with vector embeddings

Semantic search is based on the conceptual similarity of the term you're looking for with the elements in the data store. For example, searching for "dumplings" can return terms like pierogi and gyoza - words with different spelling but both representing different types of filled dough preparations.

A common way to determine the similarity between the two strings is to first turn these strings into _vector embeddings_ - arrays of floating point values representing the semantic meaning of each string - and then calculate the _cosine similarity_ between the two vectors, which is the cosine of the angle between the vectors. [Various methods](https://huggingface.co/blog/matryoshka) of producing vector embeddings are fascinating but cannot be covered here in depth.

For Pulumi code generation we are using the OpenAI's [Ada-002 embedding model](https://medium.com/@siladityaghosh/a-deep-dive-into-openais-text-embedding-ada-002-the-power-of-semantic-understanding-7072c0386f83) which at this moment represents a good balance between performance and cost, but is by no means the only model available.

Producing vector embeddings from the user query is the standard approach in this situation, however for Pulumi code generator we added a little twist - to increase the odds of getting more relevant information from the Registry (i.e. to increase the recall, see above) we first make an LLM call to generate a small set of relevant search terms that will produce an array of vector embeddings.

<div style="text-align: center; width: 50%; margin: 0 auto;">
    <img src="flow-embeddings.png" alt="" style="width: 100%;">
    <figcaption>
        <i>Getting vector embeddings from user query</i>
    </figcaption>
</div>

We then use the array of vector embeddings to retrieve the set of relevant documents from the Registry.

### Full text vs semantic search

While semantic search is essential for any "intelligent" information retrieval system, we must not forget that there exist simple and effective methods for text search. The "S3 Bucket" part of the user search happens to be easily searchable using traditional text search operations (such as SQL `LIKE` operator).

To be effective, our RAG must be able to handle queries that require semantic understanding (such as "simple storage service in AWS") as well as the traditional text search to support situations where the user knows exactly what they are looking for. To that end, the industry has adopted an approach known as the "hybrid search", in which the results of full-text search and semantic search are combined to provide the final result.

For each of these search terms we generate a query that combines the full text search with the semantic search. The resulting documents are then evaluated based on the following parameters:

- _Dense score_: Vector similarity using cosine distance between query embedding and stored embeddings
- _Sparse score_: Text search relevance using PostgreSQL's full-text search (ts_rank_cd)

Both the dense and the sparse scores contribute to the final score that is used to sort the documents. Even though the final score is the average of the two in our current implementation, it would not be correct to say that they have the same weight, or the influence on the end result. This is so because the normalization of the scores must take into account their distribution in the real-world queries and calculating that is quite complex.

Boosting the influence of one score relative to the other is an area we're actively exploring, and achieving the optimal result depends highly on what parameters we decide to optimize for - we will touch on that later in the post.

Finally, we apply the rank-based decay process - a scoring technique where results are penalized based on their position in the ranking. This creates separation between results that might have similar initial scores and gives preference to results that appear earlier in the ranking.

### Pruning the results

The approach we've taken for Pulumi code generator is to first get as many relevant documents as possible (thus increasing the recall) and then reduce that set to only retain the most relevant documents (thus increasing the precision).

Filtering out irrelevant documents is important because many providers have similarly-named types and adding them to the prompt would confuse the LLM leading to hallucinations. There is also a practical concern - large prompts are slow and expensive, even within the limits of the supported context window limits.

In Pulumi registry search, we limit the number of documents to 10 based on their relevance score, and limit the total number of tokens for the prompt to 20K. These numbers are something we continue to experiment with and represent something we've seen good results with, but likely are not optimal.

### Prompt generation

We're now ready to create the system prompt for the LLM! We've already discussed some of the elements needed to build the effective prompt - the original user query, the search terms and the vector embeddings that produce the set of documents that will guide the code generation process.

There is another element that goes into the prompt - a concise set of instructions produced by an LLM call based on the original user's query. The approach when the output of one prompt is used as input for another is known as "prompt chaining", and we used it to guide the code generator to produce the code that satisfies the requirements of the user and their organization. For our query, this set of instructions can look as follows:

> Create an S3 bucket using Pulumi in TypeScript using the following steps:
>
> 1. Import the necessary Pulumi AWS package.
> 2. Define a new S3 bucket resource with basic configuration.
> 3. Export the bucket name as an output.

<div style="text-align: center; width: 50%; margin: 0 auto;">
    <img src="retrieval.png" alt="" style="width: 100%;">
    <figcaption>
        <i>Composition of the system prompt for code generation</i>
    </figcaption>
</div>

Finally, we use the resulting prompt to call the LLM and ask it to generate the code. We're done!

### Self-debugging

Unfortunately, this isn't always the final step of the process. Despite our best efforts, the code produced by the LLM will not always be correct.

At this point, it's worth pondering what "correct code" means. The generated program might have following problems:

- It might be syntactically or semantically incorrect, i.e. it might not compile or fail to typecheck.
- It might fail at runtime - for example if refers to a non-existing resource, a region and so on.
- It might run "successfully" but not do what the user intended - either because the user did not express themselves clearly or because their request was misunderstood.
- Finally, the code might run and do exactly what the user wants, but the user's intent leads to an undesired outcome, for example a loss of an asset or a security vulnerability.

Most of these problems can be solved but many solutions go well outside of the domain of code generation. The first of these problems can be addressed by the approach known as "self-debugging": we try to typecheck the generated program, and if it doesn't compile, feed the errors back into the prompt and ask the LLM to try again. We repeat the process until the program typechecks, or until the final number of iterations has been reached.

In our experience with Pulumi code generator, many generated TypeScript programs that fail to typecheck contain only a few errors, and can be fixed in one or two self-debug iterations.

Monitoring these typechecking errors in production can also provide valuable insight into the quality of the RAG, and even suggest specific solutions. For example, failure to typecheck a member-access expression is a likely indicator of a missing type schema (a recall problem), or a "wrong" schema brought in by an irrelevant document (a precision problem).

Self-debugging can also be extended to include the `pulumi preview` command, which is a "dry run" operation before the actual deployment and can detect many real or potential problems such as destructive actions, incorrect configurations that cannot be detected at compile time, dependency conflicts and policy violations.

## Running Pulumi code generator in production

TODO

### Evaluate code quality in production

When dealing with an inherently probabalistic system, no amount of pre-production testing can guarantee the correct behavior of the tool when it runs in production. The testing is necessarily a defense in depth. What's needed is:

1. Experimentation framework to run "what if" scenarios against a large enough test bed.
2. Local evals - "it works on my machine" but it's better than nothing.
3. Consistent and repeatable results (use 0 temperature).
4. Component testing to test RAG quality, such as recall, precision and prompt coverage.
5. Production monitoring
6. Customer reports and anecdotal data. TODO: we look at every "thumbs down" report

<!--raw material 

1.2. get multiple "Pulumi Registry schema" elements (40 in our case, 29 unique) - some of them less relevant. 
(We call them tokens internally but they are really type names)
This search uses vector embeddings

Resource metadata:

{
  "name": "aws-native",
  "version": "0.90.0",
  "token": "aws-native:s3:Bucket",
  "kind": "resource"
}

AWS native looks like this:

```
{
  name: "aws-native",
  version: "0.90.0",
  token: "aws-native:s3:Bucket",
  dense_score: 0.8639781475067139,
  sparse_score: 0,
  score: 0.3887901663780213,
  dense_score_boosted: 0.7775803327560425,
  sparse_score_boosted: 0,
  kind: "resource",
  text: "Create an S3 Bucket on AWS Native (preview)",
  definition: {
    ...
```

They include the Definition structure that defines the JSON schema type for every such token.

Less relevant providers like yandex:

```
{
  name: "yandex",
  version: "0.13.0",
  token: "yandex:index/storageBucket:StorageBucket",
  ...
```

They are then sorted by their density score.

Resulting generated prompt can be 1K or more lines of Yaml

4. Full text search and BM25

BM25: 
- Inverse Document Frequency: how rare is the query term
- Term frequency in the document: how often does the term appear in the document
Detailed explanation: https://emschwartz.me/understanding-the-bm25-full-text-search-algorithm/

5. Vector embeddings, combine the two
similarity metrics like cosine similarity.

6. Reranking 

6.1. It's good to have good recall - you can throw everything and the kitchen sink at the LLM - but too much information can actually be counterproductive:

- Context window limitation: LLMs have limits on how much text they can process, known as the “context window.” Even though modern LLMs support bigger context window, there is always a limit.
- Accuracy: recall relevant information.
- Cost: we pay by the token.

We need to pare if down.
Reranker analyzes the documents and assigns it a relevance score. It may consider additional features such as organizational preferences or user's prior history that can make the document more relevant.

## Evaluate quality of code generation

1. Does RAG even help? For many common providers, LLMs can already produce reasonably good code. How do we know that RAG adds value?
Ultimately, the only measure of quality that matters is whether the generated code correctly represents the user's intent. However, this is hard to test in an automated way.
One measure is recall: <TODO: define>

What about precision?

2. Evaluate generated programs

How do we assess the quality of our RAG? Intuitively, we want two things to be true:
- Useful information must be in the database
- We must have effective ways of finding that information

- Recall
- Typecheck
- `pulumi up` - a "dry run" before the actual deployment and can detect many real or potential problems such potentially destructive actions, incorrect configurations that cannot be detected at compile time, dependency conflicts and policy violations. 

-->
