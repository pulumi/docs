---
title: AI Reference Architecture
meta_desc: Reference architecture for high scale AI applications
type: page
layout: ai-arch

overview:
    title: Pinecone + AWS Reference Architecture
    image: /images/solutions/ai-arch/pinecone-refarch-logo.png
    description: |
        This reference architecture demonstrates microservices scaling, data processing pipelines, infrastructure segmentation through networking and security groups, and UI and database synchronizations. It serves as a reference point for you take an idea in a notebook to an application handling real-world traffic. The reference architecture is built with the best practices for how to use AWS and Pinecone. It is designed for production, and it is easily modifiable to fit most use cases.

diagrams:
    title: Architecture Details

    items:
        - title: Infrastructure
          image: /images/solutions/ai-arch/pinecone-refarch-diagram.png
          content: |
            On the infrastructure side, the reference architecture uses a Pinecone index as a vector store, a message queue to pass information between microservices, and security groups to appropriately secure the traffic among the different components. The application uses Elastic Container Service (ECS) services for the frontend and backend microservices, and has autoscaling configured to expand the worker pool up and down elastically in response to system load.

        - title: Application
          image: /images/solutions/ai-arch/refarch-semantic-search-flow.png
          content: |
            On the application side, the reference architecture provides a semantic search interface over a Postgres database of product records, leveraging Pinecone’s vector database for queries and instant index updates. There is a frontend microservice to supply the user interface, and a pair of backend microservices that manage changes to the database as well as embeddings and updates to the Pinecone index.

benefits:
    title: Why Pulumi?
    benefits:
      items:
        - title: Easy and Intuitive
          icon: code
          icon_color: yellow
          description: |
            Easy to author IaC with standard programming languages like Python. 

        - title: Ship Faster with Guardrails
          icon: global
          icon_color: yellow
          description: |
            Eliminate infrastructure engineering and data scientist silos.

        - title: Total Visibility & Control
          icon: puzzle
          icon_color: yellow
          description: |
            Always know and enforce what's going on in your organization. 


get_started:
    get_started:
        title: Get Started
        description: |
          Schedule some time with our customer engineering team, and we will help you scale your AI infrastructure with Pulumi.
        cta_text: Schedule now
---
