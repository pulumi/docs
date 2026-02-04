---
title: "Neo: Share Tasks for Collaborative AI Infrastructure Operations"
date: 2026-02-04
draft: false
meta_desc: "Collaborate on infrastructure operations by sharing Neo tasks with teammates for review and assistance."
meta_image: meta.png
authors:
    - neo-team
tags:
    - neo
    - ai
    - features
schema_type: auto

# Optional: Social media promotional copy (for reference only, does not auto-post)
social:
    twitter: |
        Neo now supports task sharing.

        Share any task with your team: the original prompt, Neo's reasoning, the actions it took, and the outcome. Full context preserved.

        Viewers see everything but can't trigger actions. Sharing context doesn't mean sharing access.
    linkedin: |
        **Neo Task Sharing: Collaborative Infrastructure Operations**

        One of Neo's defining characteristics is transparency. You see the reasoning behind every decision, the steps considered, and why actions were taken. But until now, that context was locked away with the person who initiated the task.

        **The Problem**
        Platform engineering is collaborative, but when Neo's work is trapped with individual users, collaboration breaks down. Describing a task in Slack loses detail. Screenshots fragment context.

        **The Solution**
        You can now share any Neo task with anyone in your organization. Click share, send the link, and your teammate sees the complete picture: original prompt, reasoning process, actions taken, and outcome.

        **Secure by Design**
        Task sharing preserves RBAC guarantees. Viewers see the conversation but cannot trigger actions. Links to stacks or resources still enforce the viewer's existing permissions. Sharing context does not mean sharing access.

        Available now in Pulumi Cloud.
---

Neo shows its work, but until now that context was locked away with you. When you wanted a teammate's input on a decision Neo made, you had to describe it in Slack or screenshot fragments of the conversation. Today we're introducing task sharing: share any Neo task with anyone in your organization, full context preserved.

<!--more-->

To share a Neo task, click the share button to generate a read-only link, then send it to a teammate. They see the complete picture: the original prompt, Neo's reasoning process, the actions it took, and the outcome. Full context preserved. Instead of writing up what happened and losing detail in the retelling, you share the task itself.

{{< video title="Sharing a Neo task" src="neo-task-share.mp4" autoplay="true" loop="true" >}}

We built this with security as a core constraint. The original task system enforced strict RBAC, ensuring users could only see and act on resources they had permission to access. Task sharing preserves these guarantees. Viewers can see the conversation with Neo, but they cannot trigger any actions, and links within the shared task to stacks or resources still enforce the viewer's existing permissions.

The feature is available now. The next time you want a second opinion or need to show a colleague how you solved something, share the task. You're no longer working alone.
