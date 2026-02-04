# Event Page Template System

This document describes the modular event page template system that allows you to create event pages using reusable widgets.

## Overview

The event page template system consists of:

1. **Template Partials** - Reusable UI components (widgets) in `layouts/partials/template-partials/`
2. **Content Partial** - Orchestrates all widgets in `layouts/partials/event-page-content.html`
3. **Content Files** - Markdown files with YAML frontmatter defining widget data

## How It Works

1. Create a markdown file with frontmatter containing widget parameters
2. Set `layout: event-page` in the frontmatter
3. The template reads `.Params` and passes data to widgets
4. All widgets render in the order defined in `event-page-content.html`

## Available Widgets

### 1. Hero

Displays a prominent hero section with title, description, CTA button(s), and hero image.

**Frontmatter:**
```yaml
hero:
  title: "Your Event Title"
  description: "Event description text"
  cta_text: "Button Text"
  cta_link: "/link"
  cta_secondary_text: "Secondary Button Text"  # optional, displays inline with primary CTA
  cta_secondary_link: "/link"  # optional, can be anchor link like #section-id
  image: "/images/hero-image.png"
  image_alt: "Hero image description"  # optional, defaults to title
  tag_line: "Tag line text"  # optional, displays in violet above title
  booth_number: "Booth S450"  # optional, displays in black above title
```

### 2. Logo Banner

Displays a horizontal banner of company/partner logos with optional text above.

**Frontmatter:**
```yaml
logos_text: "Trusted by over 3,700 innovative companies."  # optional
logos:
  - src: "/logos/customers/company1.svg"
    alt: "Company 1"
  - src: "/logos/customers/company2.svg"
    alt: "Company 2"
```

### 3. Features List

Displays a section with icon-based feature items in a two-column layout with an optional image.

**Frontmatter:**
```yaml
features:
  tag_line: "Why Pulumi"  # optional, displays in violet above title
  title: "What you'll see from Pulumi"
  subtitle: "Discover how Pulumi transforms cloud infrastructure management"  # optional description paragraph
  image: "/images/feature-image.png"  # optional, displays in right column
  image_alt: "Feature image description"  # optional, defaults to title
  features:
    - icon: "fa-rocket"  # Font Awesome icon class
      title: "Feature Title"
      description: "Feature description"
    - icon: "fa-code"  # Font Awesome icon class
      title: "Another Feature"
      description: "Another description"
```

### 4. Two Column Layout

Displays content in two equal columns.

**Frontmatter:**
```yaml
two_column:
  - label: "Get started now"
    title: "Column Title"
    description: "Column content"
    cta_text: "Button Text"
    cta_link: "/link"
  - label: "Technical workshop"
    title: "Another Column"
    description: "More content"
    cta_text: "Register"
    cta_link: "/link"
```

### 5. Workshop Banner

Displays a prominent workshop or guide promotion with bullet points.

**Frontmatter:**
```yaml
workshop_banner:
  label: "Workshop Available"
  title: "From Zero to Production in Kubernetes"
  description: "Register for workshop"
  items:
    - "Step 1"
    - "Step 2"
    - "Step 3"
  cta_text: "Register Now"
  cta_link: "/workshop"
```

### 6. Promo Banner

Displays a promotional banner with background image or fallback violet color.

**Frontmatter:**
```yaml
promo_banner:
  title: "Get $500 in AWS Credits"
  description: "All students get access..."
  cta_text: "Claim Your Credits"
  cta_link: "/aws-credits"
  bg_image: "/images/promo-background.png"  # optional, falls back to violet-600 if not provided
```

### 7. Three Column Layout

Displays content in three equal columns with Font Awesome icons.

**Frontmatter:**
```yaml
three_column:
  tag_line: "Why Choose Us"  # optional, displays in violet above title
  title: "Infrastructure that reduces complexity"
  subtitle: "Optional description paragraph"  # optional
  columns:
    - icon: "fa-shield"  # Font Awesome icon class
      title: "Feature Title"
      description: "Feature description"
    - icon: "fa-rocket"  # Font Awesome icon class
      title: "Another Feature"
      description: "Another description"
    - icon: "fa-code"  # Font Awesome icon class
      title: "Third Feature"
      description: "Third description"
```

### 8. Testimonial

Displays a customer testimonial with background image or fallback violet color.

**Frontmatter:**
```yaml
testimonial:
  quote: "We manage over 20,000 resources..."
  author: "John Doe"
  title: "CTO"
  company: "Acme Inc"
  logo: "/images/logos/acme.svg"
  bg_image: "/images/testimonial-background.png"  # optional, falls back to violet-700 if not provided
```

### 9. Location

Displays booth location information with optional map.

**Frontmatter:**
```yaml
location:
  tag_line: "Find Us"  # optional, displays in violet above title
  title: "Where to find us"
  subtitle: "Visit us at the conference"  # optional description paragraph
  location: |
    Booth [TBD]
    Amsterdam RAI March 23-26, 2026
  description: "Additional details about the location"  # optional
  map_embed: '<iframe src="..."></iframe>'  # optional, use either map_embed or map_image
  map_image: "/images/kubecon/kubecon-map-25.png"  # optional
  cta_text: "Get directions"
  cta_link: "https://maps.google.com"
```

**Notes:**
- The `location` field accepts markdown and is displayed prominently in the left column
- The `description` field accepts markdown for additional context
- Use `map_embed` for interactive Google Maps iframes or `map_image` for static map images

### 10. Footer CTA

Displays a final call-to-action section before the footer.

**Frontmatter:**
```yaml
footer_cta:
  title: "The Infrastructure As Code platform for any cloud."
  cta_primary_text: "Get Started for Free"
  cta_primary_link: "/signup"
  cta_secondary_text: "Contact Sales"
  cta_secondary_link: "/contact"
```

## Creating a New Event Page

1. Create a new markdown file in the appropriate content directory (e.g., `content/my-event/`).

1. Add frontmatter with the `event-page` layout and define your widgets:

```yaml
---
title: Your Event Title
meta_desc: Event description for SEO
meta_image: /images/event/event-meta.png
type: page
layout: event-page

hero:
  title: "Event Title"
  description: "Event description"
  cta_text: "Register Now"
  cta_link: "/register"
  image: "/images/event-hero.png"
  image_alt: "Event Hero"
  tag_line: "Event 2025"
  booth_number: "Booth S450"

logos_text: "Trusted by innovative companies."
logos:
  - src: "/logos/customers/company1.svg"
    alt: "Company 1"
  - src: "/logos/customers/company2.svg"
    alt: "Company 2"

# Add more widgets as needed...
---
```

1. The template will automatically render all defined widgets in order.

1. See [content/kubecon/_index.md](content/kubecon/_index.md) for a complete example.

## Icon Colors

Available icon colors for widgets:
- `violet`
- `blue`
- `salmon`
- `yellow`
- `fuchsia`

## File Locations

- **Template Partials**: [layouts/partials/template-partials/](layouts/partials/template-partials/) - Individual widget implementations
- **Content Partial**: [layouts/partials/event-page-content.html](layouts/partials/event-page-content.html) - Orchestrates all widgets
- **Event Layout**: [layouts/page/kubecon.html](layouts/page/kubecon.html) - Main event page layout
- **Example**: [content/kubecon/_index.md](content/kubecon/_index.md) - Live example using frontmatter

## Architecture

The system uses a **layered partial architecture**:

1. **Template Partials** (`layouts/partials/template-partials/*.html`) - Individual widget implementations (reusable beyond events)
2. **Content Partial** (`layouts/partials/event-page-content.html`) - Orchestrates widgets in order (event-specific)
3. **Layout Template** (`layouts/page/kubecon.html`) - Calls the content partial

### Hierarchy

```
layouts/page/kubecon.html ──> layouts/partials/event-page-content.html ──> layouts/partials/template-partials/*.html
```

### Benefits of This Architecture

- **Single source of truth**: Widget order defined once in `event-page-content.html`
- **Generic widgets**: Template partials can be reused for any purpose beyond events
- **Easy updates**: Update individual widget partials or change widget order in one place
- **Clean separation**: Event-specific logic in `event-page-content.html`, generic widgets in `template-partials/`
- **Content-focused**: Content editors work with simple YAML frontmatter
- **Maximum DRY**: Zero duplication across pages

## Benefits

- **Consistent styling** - All widgets follow the same design system
- **Easy to maintain** - Update widget partials once, affects all pages
- **Flexible composition** - Pick and choose which widgets to use per page
- **Content-focused** - Content editors work with YAML, never touch HTML/CSS
- **Type-safe** - Clear parameter structure for each widget
- **Reusable** - Template partials can be used for other page types beyond events
