#!/usr/bin/env python3

import click
from pathlib import Path
import frontmatter
from datetime import datetime, date
import sys

BLOG_DIR = Path(__file__).parent.parent.parent / "content" / "blog"

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

def get_blog_posts(include_drafts=False):
    posts = []
    for post_dir in BLOG_DIR.iterdir():
        if not post_dir.is_dir():
            continue
            
        index_file = post_dir / "index.md"
        if not index_file.exists():
            continue
            
        try:
            post = frontmatter.load(index_file)
            if not include_drafts and post.get('draft', False):
                continue
                
            date = post.get('date')
            if not date:
                continue
                
            posts.append({
                'date': normalize_date(date),
                'title': post.get('title', ''),
                'path': str(index_file.absolute()),
            })
        except Exception as e:
            print(f"Error processing {index_file}: {e}", file=sys.stderr)
            continue
            
    return sorted(posts, key=lambda x: x['date'], reverse=True)

@click.command()
@click.option('--count', '-n', default=15, help='Number of posts to show')
@click.option('--include-drafts/--no-drafts', default=False, help='Include draft posts')
@click.option('--format', '-f', type=click.Choice(['path', 'full']), default='path',
              help='Output format (path or full details)')
def main(count, include_drafts, format):
    """List the most recent blog posts."""
    posts = get_blog_posts(include_drafts)[:count]
    
    if format == 'path':
        for post in posts:
            print(post['path'])
    else:
        for post in posts:
            print(f"{post['date'].strftime('%Y-%m-%d')} - {post['title']}")
            print(f"Path: {post['path']}")
            print("-" * 80)

if __name__ == '__main__':
    main()
