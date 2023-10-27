---
title: "Unlocking the Benefits of LangChain AI for Dev, Sec and Ops"
date: 2023-10-26
meta_desc: "Learn LLMs and GenAI using LangChain AI, with key lessons for DevOps broken down into Development, Operations, and Security."
meta_image: langchain-ai-gen-ai-workshop-llm-devops.png
authors:
    - sara-huddleston
    - kat-morgan
tags:
   - pulumi-events
   - community
   - ai
   - devops
   - langchain
   - ml
---

The emergence of DevOps revolutionized software development. Now, with AI powered tools like LangChain, these transformations are being accelerated. Unsurprisingly, our distinguished speaker at the launch of Pulumi's in-person AI Talks, Patrick Debois, who coined the term "DevOps," has recently tuned into LLM and GenAI Ops using the Langchain framework.

<!--more-->

This article unwraps the topics addressed during our "Generative AI, Apps, and DevOps | AI/ML Talks" event in Seattle, focusing on Langchain and GenAI for DevOps. You'll be able to watch Patrick Debois teach LangChain to learn LLMs and GenAI, with code examples and lessons that are easily understood by traditional software engineering.

## What is LangChain used for?

LangChain is an open-source Python framework designed to empower developers to construct robust generative AI applications. It facilitates the integration of advanced AI models such as OpenAI's GPT, Google's BARD, and Meta's LLaMA. This versatile tool finds application in developing retrieval-augmented chatbots and other personalized assistants, utilizing technologies like ChatGPT. Furthermore, it enables tasks such as question-answering (GQA), summarization, code comprehension, API interactions, data cleansing, and much more.

## Why is LangChain becoming popular?

The landscape of AI development is rapidly evolving, and LangChain is packed with incredible features for building LLM applications and tools. Developers with a wide range of expertise use LangChain for tasks such as managing interactions with language models, establishing seamless connections between diverse components, and integrating external resources like APIs and databases effortlessly.

The LangChain platform hosts a diverse collection of APIs seamlessly integrated into applications. This enables developers to incorporate advanced language processing functionalities without the need for laborious construction from scratch.

## LangChain Accelerating DevOps

{{< figure alt="Patrick Debois at the Seattle Pulumi User Group, with a monitor showing OpenAI LangChain and code in Python" src="./patrick-debois-langchain-ai-workshop.png" caption="Patrick Debois presenting the workshop Dev, Sec & Ops meet LangChain" width=100% >}}

LangChain can streamline the integration of large language models and data sources. By helping bring in AI capabilities, DevOps can revolutionize software development life cycles by making it easier for teams to handle challenges while optimizing resource allocation and usage through their cutting-edge, AI-powered solutions. This makes the [automation of manual processes easier](https://www.pulumi.com/docs/using-pulumi/automation-api/) and the development of new resources far more accessible with faster utilization rates by leveraging artificial intelligence. Significantly important as "[Developer Velocity and Productivity](https://www.pulumi.com/product/internal-developer-platforms/)" become business performance metrics across various industries.

The features included in LangChain include chain interface memory functions for scalability within apps, control over dataflow, as storage – making code quality more reliable, plus seamless machine learning models integration, which allows them to build custom automated AI programs quickly. Thus providing users with an advanced but easy way of creating sophisticated solutions by combining their knowledge of coding and machine training models together.

## How to Use LangChain to Learn LLMs and GenAI for Dev(Sec)Ops

Patrick teaches in the way he would like to be taught. The workshop mainly uses the Langchain framework and basic Python knowledge. OpenAI will also need to be installed. You'll learn essential skills in multiple use cases, applying Langchain for LLM application Development.

{{< youtube "iIl1bQnVwEs?rel=0" >}}

You can see the breakdown of the lessons per role below, and find the code examples on this repo: [https://github.com/jedi4ever/learning-llms-and-genai-for-dev-sec-ops/tree/main](https://github.com/jedi4ever/learning-llms-and-genai-for-dev-sec-ops/tree/main)

### Developer

- Calling a simple LLM using OpenAI
- Looking at debugging in Langchain
- Chatting with OpenAI as a model
- Using prompt templates
- Use Docloader to read your local files and prepare them for the LLM
- Explain the calculation and use of embeddings
- Understand how splitting and chunking are important
- Loading embeddings and documents in a vector database
- Use a chain for Questions and Answers to implement the RAG pattern (Retrieval Augmented Generation)
- Show the use of OpenAI documentation to have the llm generate calls to find real-time information
- Implement an Agent and provide it with tools to get more real-time information

### Operations

- Find out how many tokens you are using and the cost
- How to cache your calls to an LLM using exact matching or embeddings
- How to cache the calculation of embeddings and run the calculation locally
- Run your own local LLM (using Ollama)
- Track your calls and log them to a file (using a callback handler)
- Impose output structure (as JSON) and have the LLM retry if it's not correct
  
### Security

- Explain the OWASP top 10 for LLMS
- Show how simple prompt injection works and some mitigation strategies
- How to detect prompt injection using a 3rd party model from Hugging Face
- Detect project injection by using a prompt
- Check the answer LLMs provide and reflect if it is ok
- Use a Hugging Face model to detect if an LLM output was toxic
- Show a simple prompt for asking the LLM's opinion on Kubernetes and Trivy vulnerabilities

## Real-World Applications of LangChain AI in DevOps

{{< figure alt="Vector similarity search in a RAG application" src="./langchain-vector-similarity-search-in-a-rag-application.png" width=90%  caption="Vector similarity search in a RAG application. Credit to LangChain and Neo4J team" >}}

LangChain AI has practical applications in DevOps, particularly related to question-answering using documents as context, extraction, evaluation, and natural language processing tasks, all powered by AI tools. An interesting scenario is implementing [a knowledge graph based RAG application with LangChain](https://blog.langchain.dev/using-a-knowledge-graph-to-implement-a-devops-rag-application/) to support the DevOps team.

ChatGPT based on LLMs enabled with these AI tools is one of the foremost implementations at present. Tracking capabilities through LangChain enables developers to determine which prompts are more effective, thus supporting what artificial intelligence offers when integrated into development operations.

## Monitoring and Anomaly Detection with LangChain AI

{{< figure alt="Monitoring LLM performance with LangChain and LangKit" src="./monitoring-llm-langchain-whylabs.png" caption="Monitoring LLM performance with LangChain and LangKit. Credit to WhyLabs" width=90% >}}

LangChain AI provides an efficient approach to DevOps through continuous monitoring, and anomaly detection. LangChain's integration in DevOps allows for intelligent monitoring of various system parameters, application performance metrics, and log files. It can process large volumes of data generated by applications and infrastructure components. Through natural language processing (NLP) techniques, LangChain can interpret logs, error messages, and system alerts in real-time.

LangChain's AI-driven anomaly detection capabilities are pivotal in identifying deviations from expected behavior in the monitored data. By analyzing historical data patterns, LangChain can learn the normal behavior of the system and its components. When the system encounters an unusual event or behavior, LangChain can promptly detect it as an anomaly. These anomalies could be security threats, performance bottlenecks, code quality, or any irregularities within the system.

Keep in mind that monitoring LLM performance is important to ensure you can rely on the model's accuracy and relevance in real-world applications. Our customer [WhyLabs](https://www.pulumi.com/case-studies/whylabs/) has a great article showing the significance of [monitoring LLMs performance with LangChain and how to get started](https://whylabs.ai/blog/posts/monitoring-llm-performance-with-langchain-and-langkit) with monitoring.

## Future: AI, Apps, and DevOps

[Platform engineering](https://www.pulumi.com/product/internal-developer-platforms/), DevOps, or MLOps may be the next steps in the AI-driven software development future. AI tools are the gateway to giving developers access to big language models that allow them to create highly sophisticated solutions.

### Accelerating Development with AI-Powered Tools

AI-powered tools are revolutionizing the development process, enabling DevOps teams to access intelligent recommendations and improve code quality or obtain suggestions on new ways to accomplish goals. An example is the usage of [Pulumi AI](https://www.pulumi.com/ai).

Tools like LangChain, Amazon CodeGuru, and Pulumi AI provide actionable insights for efficient resource utilization while enforcing policy and compliance best practices. An [IaC that leverages AI empowers teams](https://www.pulumi.com/blog/pulumi-insights-ai-cli/) to automate and more effectively manage infrastructure.

Developers can reap multiple benefits from higher quality assessment of code lines, instantaneous detection of policy and security issues, useful cues on how to resolve problems, and improving code quality, productivity, and time management.

AI has greatly impacted optimization during the review stage, providing developers with better insights into performance issues, code effectiveness, and [resource utilization](https://www.pulumi.com/blog/property-search/) without any extra effort.

### Security and Vulnerability Management with AI

The marriage of AI, machine learning, and DevOps/DevSecOps practices revolutionizes security and vulnerability management in software engineering. AI-enabled tools technologies not only strengthen the defenses of software systems but also enable organizations to stay one step ahead in ensuring successful deployments by removing manual processes through automation, using single sources of truth, enforcing least-privileged access through role-based access controls, and [automated remediation to correct configuration violations](https://www.pulumi.com/blog/remediation-policies/) like auto-tagging, removing Internet access, and enabling storage encryption.

DevSecOps can foster collaboration between developers, security, and operations and still enhance security and compliance best practices using Artificial Intelligence (AI) and Machine Learning techniques.

### Leveraging Machine Learning in DevOps

![MLOps (Machine Learning Operations) meets DevOps Infinity Loop as part of the software development lifecycle](./ml-dev-ops-cycle.png "MLOps (Machine Learning Operations) meets DevOps Infinity Loop")

Applying Machine Learning in DevOps is a game-changer. Not only does it automate and enhance various processes but also brings an intelligent, predictive, and adaptive dimension to development workflows. By embracing these technologies, development teams can achieve higher efficiency, improve code quality, optimize performance, and seamlessly integrate with artificial intelligence, thereby shaping the future of software engineering.

ML models can evaluate past outcomes from compilation/builds plus performance metrics within an operation so that developers may leverage these insights when writing code accordingly with machine learning algorithms, allowing them to identify vulnerabilities or issues faster through root cause analysis while ameliorating system security against outside attacks like hackers or DDOS activity thus boosting overall system productivity thanks to AI implementation into existing processes.

### Implementing AI models into DevOps: Key Considerations

When considering AI, it's essential to assess data quality, integration complexity, cost savings, and ethical/legal considerations:

- Ensuring the data used for training these AI tools are precise, exhaustive, and up-to-date will help gain more reliable results.
- An important aspect of the implementation process is integrating existing DevOps instruments and guaranteeing scalability, depending on the company's necessities.
- Ensuring that all laws applicable when working with such technology.

## Conclusion

AI and ML are rapidly becoming a necessity, which can greatly enhance and benefit Development, Security, and Operation teams. At first glance, it may appear daunting or out of reach, but tools like Langchain and Pulumi can make it easier to get started. Follow the Pulumi Python + AI/ML series to upskill and get ahead:

- [The Real AI challenge is Cloud, not Code!](https://www.pulumi.com/blog/mlops-the-ai-challenge-is-cloud-not-code/)
- [Deploy AI Models on Amazon SageMaker using Pulumi Python IaC](https://www.pulumi.com/blog/mlops-huggingface-llm-aws-sagemaker-python/)
- [Deploying Your AI/ML Chatbot Frontend To Vercel Using Pulumi](https://www.pulumi.com/blog/deploy-ai-ml-vercel-app/)

---

## Frequently Asked Questions

### Who is Patrick Debois?

Patrick Debois is a highly accomplished technologist whose expertise spans the domains of Development (Dev), Security (Sec), and Operations (Ops). Acknowledged as a respected confidant within the developer, security, and operations communities, Patrick is presently deeply engrossed in the realm of Artificial Intelligence and Machine Learning, continually pushing the boundaries of his technical acumen.

He was the organizer of the inaugural DevOpsDays in 2009. He is credited with coining "DevOps" and co-authoring the renowned DevOps Handbook. In the past, Patrick has collaborated with esteemed technology organizations such as [Atlassian](https://www.pulumi.com/case-studies/atlassian/) and Snyk. Currently, he wears dual hats as the Vice President of Engineering and a Distinguished Engineer at Showpad.

### Is LangChain Free?

Yes, LangChain is an open-source framework, free to use and modify.

### How Does LangChain Work?

LangChain is a meticulously designed open-source framework tailored to simplify the creation of applications powered by large language models (LLMs). First, you will need to have a language model or you can use a public language model or train your own.

Once you have a language model ready, you can start building applications. The framework offers an array of tools and APIs, simplifying the process of connecting language models to diverse data sources, interacting with their environment, and constructing intricate applications.

LangChain operates by linking together various components, referred to as links, to establish a workflow. Each link in the chain performs a task and is connected in a sequence, enabling the output of one link to serve as the input for the subsequent one. This sequential linking allows the chain to execute intricate tasks by combining simple tasks seamlessly.

See [LangChain's get started](https://python.langchain.com/docs/get_started/introduction) docs for more information.

### Does ChatGPT use LangChain?

ChatGPT utilizes LangChain to create custom artificial intelligence (AI). This allows for an individualized experience.
