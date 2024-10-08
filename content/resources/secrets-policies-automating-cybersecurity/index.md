---
# Name of the event, <= 60 characters
title: Secrets and Policies - Automating Cybersecurity
meta_desc: Discover how to balance security with agility, automate defenses, manage secrets & secure the software supply chain in today’s evolving cybersecurity landscape.
meta_image:

# A featured webinar will display first in the list.
featured: false

# Webinars with unlisted as true will not be shown on the webinar list
unlisted: false

# Gated webinars will have a registration form and the user will need
# to fill out the form before viewing.
gated: false

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
url_slug: secrets-policies-automating-cybersecurity

# Content for the left hand side section of the page.
main:
    # Webinar title.
    title: Secrets and Policies - Automating Cybersecurity

    event_type: event # workshop | event

    # URL for embedding a URL for ungated webinars.
    youtube_url: https://www.youtube.com/embed/NJBSbZ2wpXw

    # Sortable date. The datetime Hugo will use to sort the webinars in date order.
    sortable_date: 2024-09-18T09:00:00-00:00

    # Duration of the webinar.
    duration: 1 hour

    # "virtual" will be shown under "show virtual events only", otherwise shown as City, State (seattle, wa)
    location: virtual

    # Description of the webinar.
    description: |
        In an era where digital threats are becoming more sophisticated, the need for advanced cybersecurity strategies has never been more critical. Our expert panel explored the intersection of innovation and security, offering insights into how AI is reshaping the threat landscape and how organizations can stay ahead. Discover how to balance security with business agility, implement best practices for secrets management, and leverage automation to safeguard your operations. We’ll also delve into securing the software supply chain and predicting future trends in cybersecurity. Join us for an in-depth discussion on protecting your organization in today's dynamic digital environment.

        - The Evolving Threat Landscape: A deep dive into the most pressing cybersecurity threats today, focusing on how AI reshapes attack strategies and defense mechanisms.
        - Balancing Security with Agility: Strategies for organizations to balance robust security measures with the need for business agility and rapid software delivery, ensuring innovation doesn't come at the expense of security.
        - Secrets Management Best Practices: An exploration of the critical components of a strong secrets management strategy, common pitfalls, and valuable lessons from high-profile secret leak incidents.
        - The Power of Automation: How automation can be harnessed to enforce security policies consistently, manage secrets efficiently, and enhance threat detection and response across dynamic environments.
        - Building a Secure Software Supply Chain: Approaches for detecting and mitigating supply chain attacks, evaluating third-party risks, and establishing best practices for secure software development and deployment.
        - The Future of Cybersecurity: Insights into emerging trends, including advancements in cloud security, the evolving role of AI and machine learning in threat detection and response, and the importance of adopting a proactive, forward-looking security strategy.

    # The webinar presenters
    presenters:
        - name: Arun Loganathan
          role: Sr. Product Manager, Pulumi
          photo: /images/team/arun-loganathan.jpg
        - name: Maya Kaczorowski
          role: Chief Product Officer, Tailscale
          photo: /images/pulumiup-2023/2024-speakers/maya-kaczorowski.jpeg
        - name: Jason Meller
          photo: /images/pulumiup-2023/2024-speakers/jason-meller.jpg
          role: VP, Product, 1Password
        - name: Ofir Cohen
          photo: /images/pulumiup-2023/2024-speakers/ofir-cohen.jpg
          role: CTO, Container Security, Wiz

    # case-sensitive
    tags:
        level: # Beginner, Intermediate, Advanced
        topics: ["Secrets Management", "Security", "DevOps", "DevSecOps", "Pulumi ESC", "Automation"]
        languages: []

# The right hand side form section.
form:
    # HubSpot form id.
    hubspot_form_id:
    salesforce_campaign_id:
---