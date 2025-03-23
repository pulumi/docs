#!/bin/bash

read -p "Slug (e.g., 'my-new-post'): " slug

hugo new --kind blog-post --contentDir content "blog/$slug"

# Calculate next Wednesday's date
next_wednesday=$(date -v+7d -v wed +%Y-%m-%d)

# Update the date in the post
sed -i '' "s/date: .*$/date: $next_wednesday/" "content/blog/$slug/index.md"

echo "Created new blog post for next Wednesday ($next_wednesday)"
