---
# Name of the event, <= 60 characters
title: Pulumi and Kubernetes - Better Together
meta_desc: Learn how to use Pulumi's integrations with Kubernetes to ensure that your clusters and containerized workloads are managed with maximum ease and efficiency!
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: true

# The layout of the landing page.
type: webinars

# External webinars will link to an external page instead of a webinar
# landing/registration page. If the webinar is external you will need
# set the 'block_external_search_index' flag to true so Google does not index
# the webinar page created.
external: false
block_external_search_index: false

# The url slug for the webinar landing page. If this is an external
# webinar, use the external URL as the value here.
url_slug: pulumi-kubernetes-better-together

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Pulumi and Kubernetes - Better Together

    event_type: workshop # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url:

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-11-18T13:00:00-04:00

    # Duration of the webinar.
    duration: 60 minutes

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        Explore the powerful combination of Kubernetes and Pulumi for modern cloud-native application deployment and management.
        
        Kubernetes has become the de facto standard for container orchestration, offering scalability, portability, and efficient resource utilization. However, organizations often face challenges in managing complex Kubernetes configurations and integrating with various cloud services. This is where Pulumi steps in, providing a revolutionary approach to infrastructure as code.
        
        Pulumi empowers developers to define and manage Kubernetes resources using familiar general-purpose programming languages, eliminating the need for lengthy YAML configurations. This workshop demonstrates how Pulumi's unified platform enables teams to manage not only Kubernetes resources but also cloud provider services and SaaS offerings through a single, consistent toolchain.
        
        Participants will gain hands-on experience using Pulumi to deploy and manage Kubernetes applications and learn best practices for creating maintainable and scalable infrastructure code. You will learn how, by using Pulumi, organizations can streamline their infrastructure management, improve collaboration between development and operations teams, and accelerate their cloud-native journey.

    learn:
        - How to use the Pulumi Kubernetes provider and the Pulumi Docker provider to build and run containerized workloads all with a single tool.
        - How the Pulumi Kubernetes provider can integrate seamlessly with your existing Kubernetes resources, whether plan YAML manifests or Helm charts.
        - How to use the Pulumi Kubernetes Operator to enable Pulumi IaC programs to run in a GitOps fashion.
    # The webinar presenters
    presenters:
        - name: Josh Kodroff
          role: Sr Solutions Architect, Pulumi
          photo: /images/team/josh-kodroff.jpg

    # case-sensitive
    tags:
        level: Intermediate # Beginner, Intermediate, Advanced
        topics: ["Kubernetes", "Docker", "GitOps"]
        languages: []
        clouds: []

# The right hand side form section.
form:
  hubspot_form_id: 7fa54625-9e6e-4133-8ea6-4e82df69c767
  salesforce_campaign_id: 701PQ00000JthRBYAZ

event_data:
  name: "Pulumi and Kubernetes - Better Together"
  start_date: 2024-11-18T13:00:00-04:00
  end_date: 2024-11-18T14:00:00-04:00
  url: "https://www.pulumi.com/resources/pulumi-kubernetes-better-together/"
  description: |
    Explore the powerful combination of Kubernetes and Pulumi for modern cloud-native application deployment and management.
        
    Kubernetes has become the de facto standard for container orchestration, offering scalability, portability, and efficient resource utilization. However, organizations often face challenges in managing complex Kubernetes configurations and integrating with various cloud services. This is where Pulumi steps in, providing a revolutionary approach to infrastructure as code.
        
    Pulumi empowers developers to define and manage Kubernetes resources using familiar general-purpose programming languages, eliminating the need for lengthy YAML configurations. This workshop demonstrates how Pulumi's unified platform enables teams to manage not only Kubernetes resources but also cloud provider services and SaaS offerings through a single, consistent toolchain.
        
    Participants will gain hands-on experience using Pulumi to deploy and manage Kubernetes applications and learn best practices for creating maintainable and scalable infrastructure code. You will learn how, by using Pulumi, organizations can streamline their infrastructure management, improve collaboration between development and operations teams, and accelerate their cloud-native journey.
---
