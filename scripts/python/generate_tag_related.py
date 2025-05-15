#!/usr/bin/env python3

import os
import yaml
import click
import frontmatter
from pathlib import Path
from datetime import date, datetime
from collections import defaultdict
from typing import Dict, List, Union

# Constants
BLOG_DIR = Path(__file__).parent.parent.parent / "content" / "blog"
RELATED_YAML = Path(__file__).parent.parent.parent / "data" / "related.yaml"
POSTS_PER_TAG = 4  # Generate 4 posts per tag to allow for self-exclusion

# Custom YAML dumper to add blank lines between entries
class CustomDumper(yaml.Dumper):
    def increase_indent(self, flow=False, indentless=False):
        return super().increase_indent(flow, False)
        
    def write_line_break(self, data=None):
        super().write_line_break(data)
        if len(self.indents) == 1:
            super().write_line_break()
        elif len(self.indents) == 3 and isinstance(self.event, yaml.events.SequenceEndEvent):
            super().write_line_break()

def normalize_date(d: Union[date, datetime, None]) -> datetime:
    """Convert a date or datetime to a naive datetime"""
    if d is None:
        return datetime.min
        
    if isinstance(d, str):
        try:
            # Try parsing ISO format first
            d = datetime.fromisoformat(d.replace('Z', '+00:00'))
        except ValueError:
            try:
                # Try common date formats
                d = datetime.strptime(d, '%Y-%m-%d')
            except ValueError:
                print(f"Warning: Could not parse date string: {d}")
                return datetime.min  # Return minimum date for unparseable dates
    
    if isinstance(d, date) and not isinstance(d, datetime):
        return datetime.combine(d, datetime.min.time())
    
    if hasattr(d, 'tzinfo') and d.tzinfo is not None:
        return d.astimezone().replace(tzinfo=None)
    
    return d

def normalize_tag(tag: str) -> str:
    """Convert a tag to a normalized format"""
    tag = str(tag)
    return tag.strip().lower().replace(' ', '-')

def get_blog_posts() -> List[dict]:
    """Get all blog posts with their metadata"""
    posts = []
    
    # Walk through all directories in the blog directory
    for root, _, files in os.walk(BLOG_DIR):
        for file in files:
            if file == "index.md":
                post_path = os.path.join(root, file)
                try:
                    post = frontmatter.load(post_path)
                    post_dict = {
                        'title': post.get('title', ''),
                        'date': normalize_date(post.get('date')),
                        'draft': post.get('draft', False),
                        'tags': [normalize_tag(tag) for tag in post.get('tags', [])],
                        'slug': os.path.basename(os.path.dirname(post_path))
                    }
                    posts.append(post_dict)
                except Exception as e:
                    print(f"Error processing {post_path}: {e}")
                    
    return posts

def get_posts_by_tag(posts: List[dict]) -> Dict[str, List[dict]]:
    """Group posts by tag"""
    posts_by_tag = defaultdict(list)
    
    for post in posts:
        if post.get('draft', False):  # Skip draft posts
            continue
            
        for tag in post.get('tags', []):
            tag = normalize_tag(tag)
            posts_by_tag[tag].append(post)
            
    return dict(posts_by_tag)

def select_related_posts(posts: List[dict]) -> List[str]:
    """Select the most recent posts for a tag"""
    sorted_posts = sorted(posts, key=lambda x: x['date'], reverse=True)
    return [post['slug'] for post in sorted_posts[:POSTS_PER_TAG]]

def load_existing_yaml() -> dict:
    """Load the existing YAML file"""
    try:
        with open(RELATED_YAML) as f:
            return yaml.safe_load(f) or {}
    except FileNotFoundError:
        return {}

def generate_yaml(posts_by_tag: Dict[str, List[dict]], preserve_existing: bool = True) -> str:
    """Generate YAML for the tags section while preserving existing content"""
    existing_content = load_existing_yaml()
    existing_tags = existing_content.get('tags', {})
    
    # Generate new tags
    new_tags = {
        tag: select_related_posts(posts)
        for tag, posts in posts_by_tag.items()
        if not preserve_existing or tag not in existing_tags
    }
    
    # Combine existing and new tags if preserving
    tags_section = existing_tags if preserve_existing else {}
    tags_section.update(new_tags)
    
    # Generate YAML with custom dumper
    yaml_str = yaml.dump({
        'default': existing_content.get('default', []),
        'tags': tags_section,
    }, Dumper=CustomDumper, sort_keys=False, allow_unicode=True, indent=2)
    
    # Add comments and format
    lines = yaml_str.split('\n')
    result = []
    in_tags = False
    last_indent = 0
    
    # Add default section comment
    result.append('# Default related posts shown as last resort when no specific entry or tag matches are found')
    result.append('')
    
    # Process the YAML content
    for line in lines:
        indent = len(line) - len(line.lstrip())
        
        # Add tags section comment before tags
        if line.startswith('tags:'):
            result.append('')
            result.append('# Tag-based related posts - Run make generate-related-tags to add entries for new tags')
            result.append('# These entries can be manually edited after generation')
            result.append('')
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
    
    # Add specific entries
    result.append('')
    result.append('# Specific related posts for individual blog posts - manually curated')
    result.append('# These take precedence over tag-based entries')
    result.append('')
    
    # Add specific post entries
    specific_entries = {
        key: value 
        for key, value in existing_content.items() 
        if key not in ['default', 'tags'] and not key.startswith('#')  # Skip comment keys
    }
    specific_yaml = yaml.dump(dict(sorted(specific_entries.items())), 
                            Dumper=CustomDumper, 
                            sort_keys=False, 
                            allow_unicode=True, 
                            indent=2)
    result.extend(specific_yaml.split('\n'))
    
    return '\n'.join(result)

@click.command()
@click.option('--preserve-existing/--no-preserve-existing', default=True,
              help='Preserve existing tag entries (default: True)')
def main(preserve_existing: bool):
    """Generate YAML for tag-based related posts"""
    posts = get_blog_posts()
    posts_by_tag = get_posts_by_tag(posts)
    yaml_output = generate_yaml(posts_by_tag, preserve_existing)
    
    # Write directly to related.yaml
    with open(RELATED_YAML, 'w') as f:
        f.write(yaml_output)
        f.write('\n')  # Add final newline

if __name__ == '__main__':
    main()
