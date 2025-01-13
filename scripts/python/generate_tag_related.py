#!/usr/bin/env python3

import click
from pathlib import Path
import frontmatter
from datetime import datetime, date
import sys
import yaml
from collections import defaultdict
from typing import Dict, List, Set

BLOG_DIR = Path(__file__).parent.parent.parent / "content" / "blog"
RELATED_YAML = Path(__file__).parent.parent.parent / "data" / "related.yaml"
POSTS_PER_TAG = 3

# Custom YAML dumper to add blank lines between entries
class CustomDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)
        
    def write_line_break(self, data=None):
        super().write_line_break(data)
        # Add extra line break for top-level entries
        if len(self.indents) == 1:
            super().write_line_break()
        # Add extra line break between tag entries
        elif len(self.indents) == 3 and isinstance(self.event, yaml.events.SequenceEndEvent):
            super().write_line_break()

def normalize_date(d):
    """Convert various date formats to naive datetime objects"""
    if isinstance(d, str):
        try:
            # Try parsing ISO format first
            d = datetime.fromisoformat(d.replace('Z', '+00:00'))
        except ValueError:
            try:
                # Try common date formats
                d = datetime.strptime(d, '%Y-%m-%d')
            except ValueError:
                print(f"Warning: Could not parse date string: {d}", file=sys.stderr)
                return datetime.min  # Return minimum date for unparseable dates
    
    if isinstance(d, date) and not isinstance(d, datetime):
        return datetime.combine(d, datetime.min.time())
    
    # If it's a datetime, ensure it's naive by converting to naive UTC
    if hasattr(d, 'tzinfo') and d.tzinfo is not None:
        return d.astimezone().replace(tzinfo=None)
    
    return d

def normalize_tag(tag: str) -> str:
    """Convert a tag to a normalized format"""
    # Handle non-string tags
    tag = str(tag)
    # Remove whitespace and convert to lowercase
    return tag.strip().lower().replace(' ', '-')

def get_blog_posts():
    """Get all blog posts with their metadata"""
    posts = []
    for post_dir in BLOG_DIR.iterdir():
        if not post_dir.is_dir():
            continue
            
        index_file = post_dir / "index.md"
        if not index_file.exists():
            continue
            
        try:
            post = frontmatter.load(index_file)
            if post.get('draft', False):
                continue
                
            date = post.get('date')
            if not date:
                continue
            
            # Split tags on commas and normalize each tag
            raw_tags = post.get('tags', [])
            if isinstance(raw_tags, str):
                tags = [normalize_tag(t) for t in raw_tags.split(',')]
            else:
                tags = [normalize_tag(t) for t in raw_tags]
                
            posts.append({
                'date': normalize_date(date),
                'title': post.get('title', ''),
                'slug': post_dir.name,
                'tags': tags,
            })
        except Exception as e:
            print(f"Error processing {index_file}: {e}", file=sys.stderr)
            continue
    
    return sorted(posts, key=lambda x: x['date'], reverse=True)

def get_posts_by_tag(posts: List[dict]) -> Dict[str, List[dict]]:
    """Group posts by tag"""
    posts_by_tag = defaultdict(list)
    for post in posts:
        for tag in post.get('tags', []):
            posts_by_tag[tag].append(post)
    return posts_by_tag

def select_related_posts(posts: List[dict]) -> List[str]:
    """Select the most recent posts for a tag"""
    # Sort by date and take the most recent ones
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    return [post['slug'] for post in sorted_posts[:POSTS_PER_TAG]]

def load_existing_yaml() -> dict:
    """Load the existing related.yaml file"""
    try:
        with open(RELATED_YAML, 'r') as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

def generate_yaml(posts_by_tag: Dict[str, List[dict]]) -> str:
    """Generate YAML for the tags section while preserving existing content"""
    existing_content = load_existing_yaml()
    existing_tags = existing_content.get('tags', {})
    
    # Generate new tags section for tags that don't exist yet
    new_tags = {
        tag: select_related_posts(posts)
        for tag, posts in posts_by_tag.items()
        if len(posts) >= POSTS_PER_TAG and tag not in existing_tags
    }
    
    # Combine existing and new tags
    tags_section = {**existing_tags, **new_tags}
    
    # Update existing content
    content = {
        'default': existing_content.get('default', []),
    }
    
    # Add specific post entries
    for key, value in existing_content.items():
        if key not in ['default', 'tags']:
            content[key] = value
            
    # Add tags section last
    content['tags'] = tags_section
    
    # Generate YAML with custom dumper
    yaml_str = yaml.dump(content, Dumper=CustomDumper, sort_keys=True, allow_unicode=True, indent=2)
    
    # Add blank lines between tag entries
    lines = yaml_str.split('\n')
    result = []
    in_tags = False
    last_indent = 0
    
    for line in lines:
        indent = len(line) - len(line.lstrip())
        
        # Track when we enter/exit the tags section
        if line.startswith('tags:'):
            in_tags = True
            result.append(line)
            continue
        elif in_tags and (not line.strip() or indent < 2):
            in_tags = False
            
        # Add blank line between tag entries
        if in_tags and indent == 2 and last_indent > 2:
            result.append('')
            
        result.append(line)
        if line.strip():
            last_indent = indent
    
    return '\n'.join(result)

def main():
    """Generate YAML for tag-based related posts"""
    posts = get_blog_posts()
    posts_by_tag = get_posts_by_tag(posts)
    yaml_output = generate_yaml(posts_by_tag)
    print(yaml_output)

if __name__ == '__main__':
    main()
