---
title: "Pulumi Cloud Adds Multi-factor Authentication"

# The date represents the post's publish date, and by default corresponds with
# the date and time this file was generated. Dates are used for display and
# ordering purposes only; they have no effect on whether or when a post is
# published. To influence the ordering of posts published on the same date, use
# the time portion of the date value; posts are sorted in descending order by
# date/time.
date: 2023-11-28T10:49:53-08:00

# The draft setting determines whether a post is published. Set it to true if
# you want to be able to merge the post without publishing it.
draft: false

# Use the meta_desc property to provide a brief summary (one or two sentences)
# of the content of the post, which is useful for targeting search results or
# social-media previews. This field is required or the build will fail the
# linter test. Max length is 160 characters.
meta_desc: Pulumi Cloud Adds Multi-factor Authentication improving Pulumi customers' security posture.

# The meta_image appears in social-media previews and on the blog home page. A
# placeholder image representing the recommended format, dimensions and aspect
# ratio has been provided for you.
meta_image: meta.png

# At least one author is required. The values in this list correspond with the
# `id` properties of the team member files at /data/team/team. Create a file for
# yourself if you don't already have one.
authors:
    - meagan-cojocar

# At least one tag is required. Lowercase, hyphen-delimited is recommended.
tags:
    - features

# See the blogging docs at https://github.com/pulumi/pulumi-hugo/blob/master/BLOGGING.md
# for details, and please remove these comments before submitting for review.
---

We are excited to announce that all users of Pulumi Cloud can now secure their account with multi-factor authentication (MFA). By requiring an additional verification step during the login process, MFA shields against unauthorized access, reducing the risk of breaches. This feature aligns with our commitment to providing robust security measures for our users. As an organization administrator, you can further protect your organization by having your members enable MFA.
<!--more-->

### How to set it up

Let's walk through the steps to enable MFA on your account:

1. Click on your account avatar in the top right corner
2. Navigate to Account Settings
3. Scroll to the MFA section
4. Press Enroll
    ![Screenshot of enrolling in MFA](mfa-enroll.png)
5. Use your authenticator application of choice to scan the QR code or paste the code
6. On your next login, you will be prompted for a passcode:
    ![Screenshot of login experience with MFA enabled](sign-in-mfa.png)

You are enrolled! When signing in you will now be asked for a one-time passcode.

### Limitations

Initially, MFA in Pulumi Cloud will support TOTP (time-based one-time passwords) and it will only be available for Pulumi Cloud-backed users. Users authenticating with a third party (such as GitHub or GitLab) will need to use MFA through those providers at this time. Some other future improvements we are considering and will prioritize based on feedback we hear from customers are extending support for WebAuthN/passkeys, Duo, SMS/Email OTP and admins enforcing MFA for their entire organization.

### Wrapping it up

We're committed to continually evolving our services to meet the needs of our diverse and growing user base. Stay tuned for more updates and features as we progress on this journey together.
