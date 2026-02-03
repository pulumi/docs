---
user-invocable: false
---

# AskUserQuestion Patterns - Index Pages

Complete patterns for gathering metadata and building sections for index documentation pages.

## Table of Contents

- [Part 1: Basic Metadata (8 Fields)](#part-1-basic-metadata-8-fields)
  - [Field 1: Title](#field-1-title)
  - [Field 2: Link Title](#field-2-link-title)
  - [Field 3: H1 Heading](#field-3-h1-heading)
  - [Field 4: Meta Description](#field-4-meta-description)
  - [Field 5: Description HTML](#field-5-description-html)
  - [Field 6: Primary Button Label](#field-6-primary-button-label)
  - [Field 7: Primary Button Link](#field-7-primary-button-link)
  - [Field 8: Secondary Button](#field-8-secondary-button)
- [Part 2: Sections Array Builder](#part-2-sections-array-builder)
  - [Section Type Selection](#section-type-selection)
  - [Section Heading](#section-heading)
  - [Card Count](#card-count)
  - [Button Cards Fields](#button-cards-fields)
  - [Logo Label Cards Fields](#logo-label-cards-fields)
  - [Flat Section Fields](#flat-section-fields)
  - [Continue Loop](#continue-loop)

---

## Part 1: Basic Metadata (8 Fields)

Ask for these fields in order using AskUserQuestion with smart suggestions.

### Field 1: Title

Generate from user's description.

```text
Question: "What should the page title be?"
Options:
- "{Suggested Title} (Recommended)"
- "Enter a different title"
```

**Logic:**

- Generate appropriate title from user's description
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Store result as `{title}`

### Field 2: Link Title

Offer to use page title or customize for navigation.

```text
Question: "Should this page have a different link title in navigation?"
Options:
- "Use the page title (Recommended)"
- "Specify a different link title"
```

**Logic:**

- Default to using page title for consistency
- If user selects "Specify different", prompt for text input
- Store result as `{linktitle}` (empty string if using page title)

### Field 3: H1 Heading

Suggest same as title or allow variant.

```text
Question: "What should the H1 heading be?"
Options:
- "{title} (Recommended)"
- "Enter a different H1"
```

**Logic:**

- Default to page title for consistency
- Allow customization if user needs different H1
- Store result as `{h1}`

### Field 4: Meta Description

Generate based on context and validate length.

```text
Question: "Choose or provide a meta description (50-160 characters):"
Options:
- "{Suggested meta description} (Recommended)"
- "Enter a different meta description"
```

**Logic:**

- Generate concise SEO-friendly description
- Present as recommended option
- If user selects "Enter different", prompt for text input
- Validate length is 50-160 characters
- Warn and request adjustment if out of range
- Store result as `{meta_desc}`

### Field 5: Description HTML

Generate paragraph for below H1 heading.

```text
Question: "Choose or provide the description paragraph (appears below H1):"
Options:
- "{Suggested description paragraph} (Recommended)"
- "Enter different description (HTML allowed)"
```

**Logic:**

- Generate contextual description paragraph
- Allow HTML tags (especially `<a>` for links)
- Store result as `{description_html}`

### Field 6: Primary Button Label

Suggest common action labels.

```text
Question: "What should the primary button say?"
Options:
- "Get Started (Recommended)"
- "Learn More"
- "View Documentation"
- "Enter different label"
```

**Logic:**

- Provide common, action-oriented labels
- "Get Started" is typically best for index pages
- Allow custom label if none fit
- Store result as `{primary_label}`

### Field 7: Primary Button Link

Suggest relevant documentation path.

```text
Question: "Where should the primary button link to?"
Options:
- "{Suggested path based on context} (Recommended)"
- "Enter different link"
```

**Logic:**

- Analyze context to suggest most relevant starting point
- Should typically be a `/docs/` path
- Allow custom link (internal or external)
- Store result as `{primary_link}`

### Field 8: Secondary Button

Determine if secondary button is needed.

```text
Question: "Does this page need a secondary button?"
Options:
- "No, just primary button (Recommended)"
- "Yes, add secondary button"
```

**Logic:**

- Most index pages only need primary button
- If user selects "Yes", repeat Field 6 and Field 7 patterns for secondary button
- Store results as `{secondary_label}` and `{secondary_link}`
- If "No", omit secondary button from frontmatter

---

## Part 2: Sections Array Builder

Index pages require at least one section. Build the sections array iteratively using AskUserQuestion for all inputs.

### Section Type Selection

Determine section layout type.

```text
Question: "What type of section is this?"
Options:
- "Button cards (cards with emoji, heading, description, link) (Recommended)"
- "Logo label cards (cards with icon, label, description, link)"
- "Flat text (simple paragraph with description)"
```

**Logic:**

- Button cards are most common for index pages
- Logo label cards work well for provider/platform listings
- Flat text for simple descriptive sections
- Store as `{section_type}`: `button-cards` or `cards-logo-label-link` or `flat`

### Section Heading

Suggest contextual heading.

```text
Question: "What should this section's heading be?"
Options:
- "{Suggested heading based on context} (Recommended)"
- "Enter a different heading"
```

**Logic:**

- Generate descriptive heading for this section
- Use Sentence case (not Title Case) for H2
- Store result as `{section_heading}`

### Card Count

Determine number of cards (if button-cards or cards-logo-label-link).

```text
Question: "How many cards should this section have?"
Options:
- "3 (Recommended)"
- "2"
- "4"
- "Enter a different number"
```

**Logic:**

- 3 cards is typical for balanced layout
- 2 or 4 cards also work well
- Store result as `{card_count}`
- Proceed to gather data for each card

### Button Cards Fields

For each card in button-cards sections, gather:

**Emoji Selection:**

```text
Question: "Card {n} - Choose an emoji:"
Options:
- "🚀 (Recommended for getting started)"
- "📦 (for packages/resources)"
- "🔧 (for configuration)"
- "⚡ (for performance)"
- "🔒 (for security)"
- "Enter a different emoji"
```

Store as `{card_emoji}`.

**Heading:**

```text
Question: "Card {n} - What should the heading be?"
Options:
- "{Suggested heading} (Recommended)"
- "Enter a different heading"
```

Store as `{card_heading}`.

**Description:**

```text
Question: "Card {n} - Choose or enter the description:"
Options:
- "{Suggested description} (Recommended)"
- "Enter a different description"
```

Store as `{card_description}`.

**Link:**

```text
Question: "Card {n} - Where should this card link to?"
Options:
- "{Suggested /docs/ path} (Recommended)"
- "Enter a different link"
```

Validate: must start with `/docs/` or be external URL. Store as `{card_link}`.

### Logo Label Cards Fields

For each card in cards-logo-label-link sections, gather:

**Icon Selection:**

```text
Question: "Card {n} - Choose a logo/icon:"
Options:
- "aws (Recommended for AWS content)"
- "azure (for Azure content)"
- "gcp (for Google Cloud)"
- "kubernetes (for Kubernetes)"
- "Enter a different icon name"
```

Store as `{card_icon}`.

**Label, Description, Link:**
Use similar patterns as button-cards above for label, description, and link fields.

### Flat Section Fields

For flat text sections, gather:

```text
Question: "Provide the description paragraph for this section:"
Options:
- "{Suggested paragraph based on context} (Recommended)"
- "Enter a different paragraph (HTML allowed)"
```

Store as `{section_description}`.

### Continue Loop

Determine if more sections are needed.

```text
Question: "Add another section to this index page?"
Options:
- "No, done with sections (Recommended)"
- "Yes, add another section"
```

**Logic:**

- If "Yes": Loop back to Section Type Selection for next section
- If "No": Validate at least one section exists, then proceed to Step 5 (weight calculation)
- Most index pages have 1-3 sections

## Implementation Notes

- Always provide smart suggestions based on context
- Use Sentence case for section headings (H2+)
- Ensure at least one section before proceeding
- Validate all links start with `/docs/` or are external URLs
- Build sections array iteratively to avoid overwhelming user
- Store all section data in structured format for YAML generation
