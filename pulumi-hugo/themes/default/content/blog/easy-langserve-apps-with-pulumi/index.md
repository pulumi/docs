---
title: "Easy LangServe Apps with Pulumi on AWS"
ate: "2024-02-13T06:00:00-08:00"
meta_desc: "Create a LangServe app. With Pulumi, you can create, deploy, and manage Langserve apps using your favorite language."
meta_image: meta.png
authors:
- engin-diri

tags:
- ai
- langserve
- aws
---

We all know how easy it is to create, deploy, and manage any cloud infrastructure
with [Pulumi](https://www.pulumi.com/) using your favorite
programming language. With the rise of artificial intelligence (AI) more and more developers are working on [LLM-powered
applications and services](https://www.thoughtworks.com/en-de/radar/techniques/llm-powered-autonomous-agents). And with
this, the need to have the same ease of use for creating, deploying, and managing
the infrastructure for these applications is growing.

In this blog post, we will show you how to this can be achieved with combining Pulumi
and [LangServe](https://python.langchain.com/docs/langserve).

## What is 🦜️🏓 LangServe?

[LangServe](https://github.com/langchain-ai/langserve) is part of the
awesome [🦜️🔗 LangChain](https://github.com/langchain-ai/langchain)
framework. LangChain simplifies the process of creating generative AI application interfaces. Generative AI applications
are powered by large language models (LLMs) and deliver an answer to your question (called prompts) in natural
language. This becomes even more interesting and useful once you integrate with your own private data and APIs. Some
popular use cases could be:

- Ask a question over your company's internal knowledge base
- Summarize a document
- Text extraction or data labeling

Building these types of integrations often needs to build pipelines (called typically chains), starting from the prompt
and enriching the prompt with your own data. Here is where LangChain comes into play.

LangChain gives you all the abstractions you need to start building your own LLM app. It has many components ready to
use for you, like LLMs, chat and text embedding modes, and vector stores, and many more.

Once we have our prototype chain ready, we can now use LangServe to expose it as a REST API.

## Getting Started with LangServe and Pulumi on AWS

After all the theory, let's get our hands dirty and start building our first LangServe app
with Pulumi on [AWS](https://aws.amazon.com/). For this
we can use one of the [LangServe example projects](https://github.com/pulumi/examples/) from the Pulumi examples
repository.

The AWS architecture you will get out of the box will look like this:

![LangServe AWS Architecture](./architecture.png)

The Pulumi LangServe AWS architecture consists of the following components:

- Docker Image resource, to build and push the LangServe app to the AWS Elastic Container Registry (ECR).
- AWS Application Load Balancer (ALB) to expose the LangServe app to the public internet.
- AWS Fargate to run the LangServe app in a serverless manner.
- AWS Parameter Store to store the LangServe app's configuration.
- Some IAM roles and policies to allow the different components to interact with each other.
- A VPC, Subnets, and Security Groups to isolate the LangServe app from the rest of your infrastructure.

I will use the Python example (`aws-py-langserve`), but you can use any of the other supported language. The examples
are [available here](https://github.com/pulumi/examples/) and ready to
use as a base for our two demo projects.

### Create a Gandalf Chatbot App 🧙‍♂️

{{% notes type="info" %}}
Please make sure that you have `OPENAI_API_KEY` environment variable set with your OpenAI API key.
{{% /notes %}}

Our first example is a chatbot app with a twist. We will use LangChain to create chain that will answer questions
about
[Middle-earth](https://en.wikipedia.org/wiki/Middle-earth)
as [Gandalf the wizard](https://en.wikipedia.org/wiki/Gandalf). The chain will be exposed as a REST API with LangServe
and deployed with Pulumi.

First clone the example repository, and head to the `aws-py-langserve` directory:

```bash
git clone https://github.com/pulumi/examples.git
cd examples/aws-py-langserve
```

In the `app` folder create a new Python file called `chain.py` and add the following code:

```python
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

_prompt = ChatPromptTemplate.from_template(
    "You are Gandalf the Grey, with his deep knowledge of Middle-earth, 'Let me tell you about {text}'"
)
_model = ChatOpenAI()
chain = _prompt | _model

```

Here we define a new chain with a prompt and a model. We provide the prompt to the model with a surrounding text to set
up the context for the model. The model will then answer the prompt with a response.

This can be as simple or complex as you want. In our case, we will keep it simple, and tell the model that it is Gandalf
and that he has deep knowledge of Middle-earth. Then we pass the text to the model and let it answer.

Open the `server.py` file and add the following code:

```python
from app.chain import chain as gandalf_chain

# ... rest of the code

add_routes(
    app,
    gandalf_chain,
    path="/openai",
)
```

You can test the chain locally with the following command:

```bash
langchain serve
```

You can either use the `playground` or `curl` to test the chain. The `playground` is a web interface where you can test
the chain. You can access it by opening your browser and navigating to `http://localhost:8000/openai/playground`.

![Playground](./playground.png)

Or you can use `curl` to test the chain:

```bash
curl http://127.0.0.1:8000/openai/stream  -X POST -H "Content-Type: application/json" --data  '{"input": {"text": "orcs"}}'

# ... omitted output
event: data
data: {"content":"ondrous","additional_kwargs":{},"type":"AIMessageChunk","example":false}

event: data
data: {"content":" land","additional_kwargs":{},"type":"AIMessageChunk","example":false}

event: data
data: {"content":".","additional_kwargs":{},"type":"AIMessageChunk","example":false}

event: data
data: {"content":"","additional_kwargs":{},"type":"AIMessageChunk","example":false}

event: end
```

To deploy the chain with Pulumi, you can use the following command:

```shell
pulumi login # if you haven't logged in yet
pulumi config set open-api-key --secret # your openai api key
pulumi up
```

This will first give you an outline of all the resources that will be created and then ask you to confirm the changes.
If you are happy with the changes, you can confirm them by typing `yes`.

After the deployment is finished, you will get the URL of the deployed LangServe app. You can use this URL to test the
app either with the `playground` or `curl`. Same as you did locally. The URL will look like this:

```shell
https://<your-alb-dns-name>/openai/playground
```

![Gandalf AWS](./gandalf-aws.png)

If you want to destroy the stack, you can use the following command:

```shell
pulumi destroy
```

The Pulumi CLI will ask you to confirm the changes, and if you are happy with the changes, you can confirm them by
typing `yes`.

### Create a Pinecone RAG App

{{% notes type="info" %}}
Please make sure that you have the following API keys set:

- `PINECONE_API_KEY` environment variable set with your Pinecone API key. You can get it from the Pinecone console.
- `OPENAI_API_KEY` environment variable set with your OpenAI API key.

{{% /notes %}}

Our second example will show you how to create a RAG (Retrieval-Augmented Generation) app
with [Pinecone](https://pinecone.io/) vector
databases. The clue of this example here is to show you how easy you can extend the Pulumi LangServe example to deploy
additional cloud resources. In this case, we will deploy a Pinecone index to use it in our LangServe app. Pulumi and
Pinecone recently [released a dedicated Pulumi provider](/blog/pinecone-serverless/)
for Pinecone. This provider allows you to create and
manage [Pinecone indexes](https://www.pulumi.com/registry/packages/pinecone/) with Pulumi.

As an external knowledge base, we will use Wikipedia to load information
about [Gandalf the Grey](https://en.wikipedia.org/wiki/Gandalf) and ingest them into our Pinecone index.

First clone the [example repository](https://github.com/pulumi/examples/), and navigate to the `aws-py-langserve`
directory:

```bash
git clone https://github.com/pulumi/examples.git
cd examples/aws-py-langserve
```

To use the Pulumi Pinecone provider, you need to install it first:

```shell
echo "pinecone_pulumi==0.4.0" >> requirements.txt
```

Now open the `__main__.py` file and add the following code at the end of the file:

```python
import pinecone_pulumi as pinecone

# ... omitted code
pinecone_provider = pinecone.Provider("pinecone_provider",
                                      api_key=pinecone_api_key)

pinecone_rag_index = pinecone.PineconeIndex("pinecone-rag-index",
                                            name="test",
                                            metric=pinecone.IndexMetric.COSINE,
                                            spec=pinecone.PineconeSpecArgs(
                                                serverless=pinecone.PineconeServerlessSpecArgs(
                                                    cloud=pinecone.ServerlessSpecCloud.AWS,
                                                    region="us-west-2",
                                                ),
                                            ),
                                            opts=pulumi.ResourceOptions(provider=pinecone_provider))
```

Now we need to pass the Pinecone API key to the AWS Parameter Store. Open the `__main__.py` file and this following line
after line `38`:

```python
# ... omitted code
pinecone_api_key = config.get("pinecone-api-key")
# ... omitted code
```

And add line `226` a new secret to the AWS Parameter Store:

```python
# ... omitted code
langserve_ssm_parameter_pinecone = aws.ssm.Parameter("langserve-ssm-parameter-pinecone",
                                                     type="SecureString",
                                                     value=pinecone_api_key,
                                                     key_id=langserve_key.key_id,
                                                     name=f"/pulumi/{pulumi_project}/{pulumi_stack}/PINECONE_API_KEY",
                                                     tags={
                                                         "pulumi-application": pulumi_project,
                                                         "pulumi-environment": pulumi_stack,
                                                     })
# ... omitted code
```

And to the IAM policy in line `260`:

```python
# ... omitted code
"Resource": [langserve_ssm_parameter_arn, langserve_ssm_parameter_pinecone.arn, ],
# ... omitted code
```

Last but not least, change the Fargate task definition to use the Pinecone API key. Add a new element in line `338`:

```python
# ... omitted code
container_definitions = pulumi.Output.all(langserve_ecr_image.repo_digest, langserve_ssm_parameter.name,
                                          langserve_log_group.name, langserve_ssm_parameter_pinecone.name).apply(
    lambda repo_digest, langserve_ssm_parameter_name, langserve_log_group_name,
           langserve_ssm_parameter_pinecone_name: json.dumps([{
# ... omitted code
```

And add a new array element to line `349`:

```python
# ... omitted code
{
    "name": "PINECONE_API_KEY",
    "valueFrom": langserve_ssm_parameter_pinecone_name
}
# ... omitted code
```

This should create your Pinecone index and update the Fargate task definition to use the Pinecone API key; this is what
we are going to need to use the Pinecone index in our LangServe app.

To use the Pinecone index in our LangServe app, we need first to add following packages to our LangChain app:

```shell
poetry add pinecone-client
poetry add langchain-community
poetry add langchain-openai
poetry add langchain
poetry add 'tiktoken>=0.5.2,<0.6.0'
poetry add wikipedia
```

Now we can add `chain.py` in the `app` directory and add the following code:

```python
import os

from langchain_openai import ChatOpenAI
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.pydantic_v1 import BaseModel
from langchain_core.runnables import RunnableParallel, RunnablePassthrough

if os.environ.get("PINECONE_API_KEY", None) is None:
    raise Exception("Missing `PINECONE_API_KEY` environment variable.")

PINECONE_INDEX_NAME = os.environ.get("PINECONE_INDEX", "test")

### Ingest code - you may need to run this the first time
# Load
from langchain_community.document_loaders import WikipediaLoader

loader = WikipediaLoader(query="Gandalf the Grey", load_max_docs=50)
data = loader.load()

# # Split
from langchain.text_splitter import RecursiveCharacterTextSplitter

text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=0)
all_splits = text_splitter.split_documents(data)

# # Add to vectorDB
vectorstore = Pinecone.from_documents(
    documents=all_splits, embedding=OpenAIEmbeddings(), index_name=PINECONE_INDEX_NAME
)
retriever = vectorstore.as_retriever()
### End Ingest code

vectorstore = Pinecone.from_existing_index(PINECONE_INDEX_NAME, OpenAIEmbeddings())
retriever = vectorstore.as_retriever()

# RAG prompt
template = """Answer the question based only on the following context:
{context}
Question: {question}
"""
prompt = ChatPromptTemplate.from_template(template)

# RAG
model = ChatOpenAI()
chain = (
    RunnableParallel({"context": retriever, "question": RunnablePassthrough()})
    | prompt
    | model
    | StrOutputParser()
)


# Add typing for input
class Question(BaseModel):
    __root__: str


chain = chain.with_types(input_type=Question)
```

Head over to the `server.py` file and add the following code:

```python
from app.chain import chain as rag_chain

# ... rest of the code
add_routes(
    app,
    rag_chain,
    path="/rag-pinecone",
)
```

To deploy the chain with Pulumi, you can use the following command:

```shell
pulumi login # if you haven't logged in yet
pulumi config set open-api-key --secret # your openai api key
pulumi config set pinecone-api-key --secret # your pinecone api key
pulumi up
```

This will deploy create the AWS infrastructure, and the Pinecone index and then containerize and deploy the LangServe
app to AWS Fargate.

After a couple of minutes, you will see in the Pinecone console that the index has been created and the first documents
have been ingested from Wikipedia about Gandalf the Grey.

Here a screenshot of the Pinecone console:

![Pinecone Console](./pinecone-console.png)

And if you want to test the LangServe app, you can use the playground UI, where you should be able to ask questions
about Gandalf the Grey and get answers based on the documents ingested into the Pinecone index.

![LangServe Pinecone](./langserve-pinecone.png)

When you're ready to destroy the stack, you can use the following command:

```shell
pulumi destroy
```

The Pulumi CLI will ask you to confirm the changes, and if you are happy with the changes, you can confirm them by
typing `yes` and all the resources will be deleted, including the Pinecone index.

## In Conclusion

In this blog post, we showed you how easy it is to create, deploy, and manage LangServe apps with Pulumi. The
example projects from the Pulumi examples repository provide an excellent starting point to build your own LLM-powered
apps.
In the second example, we showed you how to extend the Pulumi code to deploy additional cloud resources, in this case a
Pinecone serverless index to hold custom data for our Gandalf app.

As always, we welcome your feedback and contributions in
the [Pulumi Community Slack](https://slack.pulumi.com/), [GitHub repository,](https://github.com/pulumi/pulumi)
and [Pulumi Community Discussions](https://github.com/pulumi/pulumi/discussions).

New to Pulumi? Signing up is easy and free. [Get started today](/docs/get-started/)!

Happy AI building!
