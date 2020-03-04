---
title: "BigData Boutique uses Pulumi to Test and Optimize Elasticsearch"
date: 2020-03-05
meta_desc: "BigData Boutique uses Pulumi to determine optimal Elasticsearch configurations for their customers"
meta_image: bdbq-pulumi.png
authors:
    - sophia-parafina
tags:
    - BigData Boutique
    - Elasticsearch
    - testing
    - optimize
---

**Guest Article:** [Itamar Syn-Hershko](https://twitter.com/synhershko), Founder and CTO of [BigData Boutique](https://bigdataboutique.com/) shows how they use Pulumi to benchmark Elasticsearch configurations across cloud providers. Pulumi enables BigData Boutique to test deployments in parallel and gather metrics to produce performant and cost-effective solutions for its customers.

<!--more-->

- - -
## How Pulumi Drives Our Elasticsearch Capacity Planning and Cost Optimization Service

*Capacity Planning and Cost Optimization of Elasticsearch clusters requires a special level of expertise and automation. Here is how we use Pulumi to launch long-running benchmarks to correctly identify the right configuration for our customers’ Big Data clusters.*

<div class="flex-container mt-3">
<div class="md:flex">  
<div class="flex-auto px-0">
{{% md %}} 
![Itamar Syn-Hershko](portrait.PNG)
{{% /md %}}
</div>
<div class="flex-auto px-5">
{{% md %}} 
At [BigData Boutique](https://bigdataboutique.com/), we are continually challenged by our customers—whether it’s complex Big Data challenges we are asked to solve, reducing costs for sophisticated systems holding mountains of data, improving performance for high-demand systems, or challenges faced in building a data-driven system.
{{% /md %}} 
</div>
</div>
</div>

One of the main challenges our customers are facing with Big Data systems is deploying the right hardware at the right scale. They need to know how to correctly estimate the number of servers required to run their compute workloads and databases, so they don’t pay more than they should, while still keeping those services running without interruption and within the defined [KPI](https://en.wikipedia.org/wiki/Performance_indicator)s.

To support our customers and help them succeed in their Big Data projects, we provide an array of advanced services, and our unique cost-optimization service addresses this challenge directly. This article outlines how we use long-running benchmarks to correctly identify the right configuration for our customers’ BigData clusters by using the [infrastructure as code tool Pulumi]({{< relref "/docs" >}}) for automating the creation of complex infrastructures with conditionals and highly tunable configurations to orchestrate those benchmarks at scale.

### Elasticsearch Cost Optimization

Let’s take Elasticsearch as an example. [Elasticsearch](https://www.elastic.co/elasticsearch) is a real-time search and analytics engine. It is built to ingest huge amounts of data and to allow one to search through and visualize them in real-time. But to be able to sustain the required amount of data on ingestion and the desired number of queries per second, the right hardware has to be used.

To do this, we have to make some decisions: which disks to use (SSD disks? local, or network storage?), the number of servers (scaling up or out?), CPU and RAM ratios, index mappings, various cluster configurations, and more. These are not easy questions to answer, and that is where our [Elasticsearch expertise](https://bigdataboutique.com/services/elasticsearch) comes into play. But answering those questions correctly with a high level of certainty also requires rigorous testing for validating assumptions.

Whether our customer is running on-prem or on a cloud, our [Elasticsearch Capacity Planning Service](https://bigdataboutique.com/services/elasticsearch/capacity-planning) exists for one purpose: to find the hardware solution with the optimum balance between cost and performance, and do it scientifically, so the answers are as accurate and as precise as possible.

### Elasticsearch Sizing Process

Our process begins with a sample data request. We ask the customer for their data (or a large sample of it), existing index mappings, expected queries, and finally known KPIs and SLAs. Our goal in the initial discovery phase is to reduce the number of free variables as much as possible because the more such variables, the more permutations we will have to test. Ideally, we want very few dimensions of freedom—usually in terms of hardware and configurations—so the number of permutations to test is on the order of dozens and not thousands.

Once the initial framework has been decided, we run fully automated benchmarks to test some of the permutations our experience tells us are the most promising to deliver good results. The benchmarking process is smart enough to omit long tales and outliers, so the results are not going to lie as to the true nature of the configuration that was selected and tested.

Between benchmark iterations, our team uses its years of experience to create more test configurations that optimize various configurations we decide are important based on the results of the previous benchmarks. After several iterations of benchmarking on various configurations, we send the preliminary findings to confirm our results and proposed direction to the customer. The purpose is to communicate the results and validate the trade-offs we decide on during the sizing procedure. Finally, we provide a summary session with our team of Elasticsearch experts and customer technical and business contacts to present the results and recommendations, and to explain the reasoning behind the analysis.

Finding the best Elasticsearch configuration requires careful benchmarking and tech expertise. Yet trade-offs will come into play. For instance, it might seem that the only way to gain another 100ms of performance improvement for a certain specific query would be to spend another $500 per month on hardware. But there may be other options. Our Sizing Service takes the guesswork out of the process. We automate the entire benchmarking procedure in order to make it an exact science.

To do all this, we needed a way to launch and run numerous independent Elasticsearch clusters, each with different configurations (however nuanced), let the tests run the entire duration (usually many hours), and then plot graphs of the results of all benchmarks.

To fully automate the benchmarking process, we use [Pulumi]({{< relref "/product" >}}).

### Using Pulumi for State-of-the-Art Infrastructure Automation

[Pulumi]({{< relref "/" >}}) is an infrastructure-as-code tool that allows us to define and run infrastructures using code, as opposed to doing this manually or using other tools that use configuration-based syntax. This lets us create complex infrastructures with conditionals and highly tunable configurations. The Pulumi program we created can be run numerous times with different parameters. Each result is a cluster that is built and configured differently, sometimes even on completely entirely different clouds.

At BigData Boutique, we use that concept to launch multiple infrastructures in parallel, benchmark them, and show a report that highlights which config is better along with the various trade-offs for each. After the benchmark process, the cluster is destroyed, and the “provisioner” instance reports all logs, metrics, and the benchmark report, which we then analyze and visualize.

Generating, visualizing, and analyzing dozens of reports in parallel gives us, the Elasticsearch Engineers, the ability to understand which knobs to turn and what configurations to change to make our customers succeed in their project without spending more than they are willing to.

### Conclusion

In sum, leveraging Pulumi helps us to create highly configurable infrastructures to orchestrate benchmarks at scale. As one of many advanced services that we offer, the [Elasticsearch Capacity Planning and Cost Optimization Service](https://bigdataboutique.com/services/elasticsearch/capacity-planning) continues to meet our customers’ most important planning and optimizations needs in an as scientifically rigorous manner as possible. You can read more about it [HERE](https://bigdataboutique.com/services/elasticsearch/capacity-planning).

The original article was published on their [company blog](https://blog.bigdataboutique.com/2020/03/how-pulumi-drives-our-elasticsearch-capacity-planning-and-cost-optimization-service-jx8qlu).