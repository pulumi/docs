---
title: Submit a Support Request
meta_desc: Open a support request with the Pulumi support team. Tell us what you're running into and we'll get back to you by email.
type: page
layout: support-new
# Transactional form page. Keep it out of search until the Intercom cutover
# makes it the canonical support entry point.
block_external_search_index: true

overview:
    eyebrow: Pulumi support
    title: Submit a request
    description: Tell us what you're running into and the Pulumi support team will get back to you by email. Fields marked with an asterisk (*) are required.

form:
    fields:
        email:
            label: Your email address
        name:
            label: Full name
        company:
            label: Company name
        organization:
            label: Pulumi organization name
            help: https://app.pulumi.com/PULUMI_ORG_NAME
        category:
            label: "I need help with:"
            help: In what area of Pulumi are you encountering issues?
            placeholder: Choose an area
            options:
                - label: My Pulumi Account/Sales
                  value: account-sales
                - label: My Pulumi Program
                  value: program
                - label: My Pulumi Cloud
                  value: cloud
                - label: Pulumi Documentation/Blog
                  value: docs
        subject:
            label: Subject
        description:
            label: Description
            help: Please enter the details of your request. It always helps to include code snippets, current behavior, and expected behavior when encountering issues. Markdown is welcome.
        pulumi_about:
            label: Please run pulumi about in the directory containing the Pulumi project and share the output.
            help: This will print information about the Pulumi environment and is helpful for debugging.
        attachments:
            label: Attachments
            help: "Up to 5 files, 20 MB each. File contents aren't uploaded yet: we'll note what you selected and ask for the files by email if we need them."
    submit: Submit
    submitting: Submitting…
    error_banner: We couldn't send your request just now. Your entries are saved in this browser tab — please try again in a moment, or open a ticket at https://support.pulumi.com/.

confirmation:
    title: Request received. We're on it.
    description: Your request is with the Pulumi support team. Keep an eye on your inbox — replies come from Pulumi support by email.
    recap:
        - label: Organization
          field: organization
        - label: Subject
          field: subject
    steps:
        - title: Now.
          description: Your request has been logged with the Pulumi support team.
        - title: Next.
          description: A support engineer reviews it and replies by email, usually within one business day.
        - title: Then.
          description: You work the issue together over email. If we need files or more detail, we'll ask there.

help_links:
    title: Need something else?
    description: "If this isn't a support request, these get you there faster:"
    links:
        - label: Ask the community on Slack
          url: https://slack.pulumi.com/
        - label: Browse the documentation
          url: /docs/
        - label: Check Pulumi service status
          url: https://status.pulumi.com/
        - label: Talk to sales
          url: /contact/
---
