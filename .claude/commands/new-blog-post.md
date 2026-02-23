---
description: Create a new blog post with proper structure, frontmatter, and automatic author detection/onboarding.
---

# /new-blog-post Command

**Use this when:** You're creating a new blog post for the Pulumi website.

Creates a new blog post with proper structure, frontmatter, and author onboarding if needed. Automatically detects the author from git configuration and handles all required setup.

## Instructions for Claude

**CRITICAL**: Complete all 5 steps in sequence. Display progress as **[Step X/5]** before each step.

**Important**:

- **Always display all 5 steps**: Even when skipping a step, display it with an explanation (e.g., "[Step 2/5] Skipped - using suggested location from Step 1")
- **Minimize open-ended questions**: ALWAYS use AskUserQuestion with prepopulated suggestions whenever possible. Always provide smart defaults based on context.
- **Store decisions**: Track choices to avoid re-asking

When this command is invoked, you should:

### 1. Detect Context and Gather Information

**First, gather context automatically:**

1. Get git user information: `git config user.name` and `git config user.email`
2. Try to detect GitHub username from:
   - `git config github.user` (if set)
   - Git remote URL (e.g., `git@github.com:username/repo.git`)
   - Recent commit authors (if available)
3. Generate a suggested author ID from the git name (e.g., "Jane Doe" → "jane-doe")
4. Check if `data/team/team/{suggested-author-id}.toml` exists
5. If it doesn't exist, search for existing author files that match the git user's name or email (use grep/glob)
6. Determine if this is likely a new author who needs onboarding

**Then ask the user for the following information using AskUserQuestion:**

**Blog Post Details:**

- **Title**: The blog post title (will be Title Case in frontmatter). If the user doesn't have a title yet, ask for a working title or topic to generate a slug and suggested meta description/tags. Be clear that the user can update the title later before publishing.
- **Author ID**: The author's ID (e.g., "jane-doe"). Prepopulate with the suggested author ID from git config if detected.
- **Summary**: Suggest a concise, one-sentence meta description based on the post title (50-160 characters, optimized for SEO and social media)
- **Tags**: Suggest 1-3 relevant tags based on the post title and similar existing blog posts. Common tags include: features, product-launches, pulumi-cloud, aws, azure, kubernetes, tutorials, announcements
- **Date**: Publication date. Ask using AskUserQuestion with these options:
  - Question: "When should this blog post be published?"
  - Header: "Publish Date"
  - Options:
    1. label: "Today ({current-date}) (Recommended)" / description: "Publish immediately when merged to master"
    2. label: "Enter a specific date" / description: "Schedule for future publication (you'll provide YYYY-MM-DD format)"
    3. label: "I don't know yet" / description: "Sets placeholder date 2099-01-01 (must be updated before publishing)"
  - After getting the response:
    - Option 1: Use today's date in YYYY-MM-DD format
    - Option 2: Prompt for custom date in YYYY-MM-DD format, validate the format
    - Option 3: Use 2099-01-01 and set a flag to add TODO comment in frontmatter
  - Note: Replace {current-date} with the actual current date (e.g., "2026-02-05")
  - DO NOT display the day of the week in the date options. Use only the date in YYYY-MM-DD format for clarity and consistency.

**For New Authors Only (skip if existing author detected):**

If the author file doesn't exist, also gather:

- **Full name**: Prepopulate with git user.name if available
- **Title**: Job title (e.g., "Senior Software Engineer")
- **GitHub username**: Try to extract from git config or recent commits
- **LinkedIn username**: LinkedIn handle (without linkedin.com/in/)

**Additional Authors:**

After gathering the primary author information, ask:

- **Are there additional authors on this post?** If yes, ask for their names or author IDs (comma-separated)
- For each additional author:
  1. Try to find their existing TOML file in `data/team/team/`
  2. If found, confirm and add to the authors list
  3. If not found, ask if you should create a profile for them (gather same info as primary author)
  4. Keep track of all author IDs for the frontmatter

### 2. Create Author Profiles (if new)

For each author that doesn't exist in `/data/team/team/`:

1. Use information gathered from git config and user input
2. For GitHub username, check git remote URL or recent commit history if not provided
3. Create `data/team/team/{author-id}.toml` with this structure:

```toml
id = "author-id"
name = "Full Name"
title = "Job Title"
weight = 1

status = "active"

[social]
github = "githubusername"
linkedin = "linkedinusername"
```

Inform the user if author information was auto-populated and give them a chance to review/correct it.

**For additional authors**: Process each one separately, creating profiles as needed.

### 3. Create Blog Post Directory and File

1. **Generate slug**: Convert title to lowercase, replace spaces with hyphens, keep only alphanumeric characters and hyphens (remove all other special characters)
2. **Create directory**: `content/blog/{slug}/`
3. **Copy placeholder meta.png**: Use Bash to copy `.claude/commands/_common/images/blog-post-meta-placeholder.png` to `content/blog/{slug}/meta.png`
4. **Create index.md** with this structure:

```markdown
---
title: "Title in Title Case"
# If user selected "I don't know yet": Add TODO comment above date
# TODO: Update this date before publishing! Currently set to far future to prevent premature publication.
date: YYYY-MM-DD  # Use 2099-01-01 if "I don't know yet" was selected, otherwise use the chosen date
draft: false
meta_desc: "The one-sentence summary provided by user"
meta_image: meta.png
authors:
    - author-id-1
    - author-id-2  # Include all authors gathered during setup
tags:
    - tag1
    - tag2
schema_type: auto

# Optional: Social media promotional copy (for reference only, does not auto-post)
social:
    twitter:
    linkedin:
---

Introduction paragraph. This will appear on the blog index page.

<!--more-->

Main content goes here. Everything after the <!--more--> comment appears only on the full post page.

Avoid using images or code samples in the first 70 words, as they may not render properly in summaries.

For more guidance, see [BLOGGING.md](https://github.com/pulumi/docs/blob/master/BLOGGING.md).
```

### 4. Validation

Before finishing:

- Verify git config was readable (if not, inform user and proceed with manual entry for all fields)
- Verify all author files exist and are valid TOML
- Verify all author IDs in the frontmatter match the author IDs that were created/found (prevent typos)
- Verify the blog post directory was created
- Verify meta.png was copied to the blog post directory
- Verify index.md has valid YAML frontmatter
- Verify the user is not committing to `master` directly (if so, warn them)
- Check that all required fields are present (especially meta_desc, authors, tags)
- If information was auto-populated, remind user to double-check author profile accuracy

### 5. Provide Next Steps

After creating the files, tell the user:

1. **Location**: Where the blog post was created
2. **Author profiles**:
   - List all authors included in the post
   - If new author profiles were created, show the file paths and confirm which details were auto-populated
   - If existing author profiles were used, confirm which ones were found and used
   - If information was auto-detected, remind user to review it for accuracy
3. **Next steps**:
   - **If date was set to 2099-01-01**: Update the publication date in frontmatter before publishing! The current placeholder date will prevent the post from appearing on the live site.
   - Replace the placeholder `meta.png` with your own image (recommended size: 1200×630 pixels, optimal for social media previews). Figma templates are available for internal use, ask in `#docs` for a link.
   - Write the blog post content
   - Add any screenshots or images to the blog post directory
   - **Optional but recommended**: Run `/add-borders` on the blog post to add 1px grey borders to PNG images for better visual presentation
   - Preview locally: `make serve` and visit <http://localhost:1313/blog/{slug}/>
   - **Recommended**: Run `/docs-review` on your blog post to check for style issues before committing
   - Run `make lint` before committing
   - **Important**: If your post is merged to master but not showing on the live site, check the date in frontmatter - posts only appear in deployments built after their publish date.

## Important Notes

- **Publishing workflow**: Blog posts go live when merged to master, but only appear on the site after their publish date. There is no draft mode - make sure content is ready before merging.
- **Directory naming**: Use just the slug (e.g., `my-awesome-post`), not date-prefixed (e.g., `2026-01-23-my-awesome-post`)
- **Images**: All images go in the same directory as `index.md`
- **Author array**: The `authors` field in frontmatter is an array. For multi-author posts, add additional author IDs to the array (e.g., `- jane-doe\n    - john-smith`)
- **More marker**: The `<!--more-->` comment marks where the excerpt ends on listing pages
- **Style guide**: Remind users to follow `STYLE-GUIDE.md` (Heading style: H1 = Title Case, H2+ = Sentence case)

## Example Usage

```markdown
User: /new-blog-post
Claude: I'll help you create a new blog post. Let me first check your git config...
[Reads git user.name and user.email]
[Checks if author file exists for suggested author ID]
[If new author: "I see you're Jane Doe (jane.doe@pulumi.com). I couldn't find an existing author profile, so I'll create one for you."]
[If existing author: "I found your existing author profile: jane-doe"]
[Asks: "Are there additional authors on this post?"]
[If yes: Processes each additional author, finding or creating profiles as needed]
[Suggests a meta description based on the post title]
[Suggests tags based on the post title by looking at similar blog posts]
[Asks remaining questions via AskUserQuestion, pre-populating detected values]
[Creates all needed author profiles, using auto-detected information where possible]
[Creates blog post structure with files: content/blog/my-new-post/index.md and content/blog/my-new-post/meta.png]
[Includes all author IDs in the frontmatter authors array]
[Provides next steps with summary of what was auto-populated]
```

## Error Handling

- If author ID already exists but user says it's a new author, warn them and ask if they want to use the existing profile
- If slug already exists in content/blog/, suggest an alternative slug or ask user to provide a different one
- If required fields are missing, prompt again
