#!/usr/bin/env python3
import os
from datetime import datetime
import re
from pathlib import Path

def extract_frontmatter(file_path):
    """Extract key-value pairs from YAML frontmatter manually."""
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Look for frontmatter between --- delimiters
        match = re.match(r'^---\s*\n(.*?)\n---\s*\n', content, re.DOTALL)
        if not match:
            return None
        
        frontmatter_text = match.group(1)
        
        # Simple parsing for the fields we need
        data = {}
        
        # Extract series
        series_match = re.search(r'^series:\s*(.+)$', frontmatter_text, re.MULTILINE)
        if series_match:
            data['series'] = series_match.group(1).strip().strip('"').strip("'")
        
        # Extract date
        date_match = re.search(r'^date:\s*(.+)$', frontmatter_text, re.MULTILINE)
        if date_match:
            data['date'] = date_match.group(1).strip().strip('"').strip("'")
        
        # Extract meta_image
        meta_image_match = re.search(r'^meta_image:\s*(.+)$', frontmatter_text, re.MULTILINE)
        if meta_image_match:
            data['meta_image'] = meta_image_match.group(1).strip().strip('"').strip("'")
            
        return data
    except Exception as e:
        print(f"Error processing {file_path}: {e}")
        return None

def find_blog_posts():
    """Find all blog post markdown files."""
    blog_dir = Path("content/blog")
    markdown_files = []
    
    for item in blog_dir.iterdir():
        if item.is_dir():
            index_file = item / "index.md"
            if index_file.exists():
                markdown_files.append(index_file)
    
    return markdown_files

def main():
    series_data = {}
    
    blog_posts = find_blog_posts()
    print(f"Found {len(blog_posts)} blog posts")
    
    for post_path in blog_posts:
        frontmatter = extract_frontmatter(post_path)
        if not frontmatter:
            continue
            
        # Check if post has a series tag
        series = frontmatter.get('series')
        if not series:
            continue
            
        # Get the date
        date = frontmatter.get('date')
        if not date:
            continue
            
        # Convert date to datetime object for comparison
        if isinstance(date, str):
            try:
                # Try different date formats
                for date_format in ['%Y-%m-%d', '%Y-%m-%dT%H:%M:%S%z', '%Y-%m-%dT%H:%M:%S-%H:%M', '%Y-%m-%dT%H:%M:%SZ']:
                    try:
                        date_obj = datetime.strptime(date, date_format)
                        break
                    except ValueError:
                        continue
                else:
                    # If none of the formats work, try to extract just the date part
                    date_part = date.split('T')[0]
                    date_obj = datetime.strptime(date_part, '%Y-%m-%d')
                
                # Convert to naive datetime if it has timezone info
                if date_obj.tzinfo is not None:
                    date_obj = date_obj.replace(tzinfo=None)
                    
            except ValueError:
                print(f"Could not parse date '{date}' in {post_path}")
                continue
        else:
            date_obj = date
            
        # Track the earliest date for each series (first article)
        if series not in series_data:
            series_data[series] = {
                'earliest_date': date_obj,
                'first_post': post_path,
                'meta_image': frontmatter.get('meta_image'),
                'post_count': 1
            }
        else:
            series_data[series]['post_count'] += 1
            if date_obj < series_data[series]['earliest_date']:
                series_data[series]['earliest_date'] = date_obj
                series_data[series]['first_post'] = post_path
                series_data[series]['meta_image'] = frontmatter.get('meta_image')
    
    # Sort series by earliest date (oldest first to see first articles)
    sorted_series = sorted(series_data.items(), 
                          key=lambda x: x[1]['earliest_date'])
    
    print("\nFirst article meta_image for each series:")
    print("=" * 60)
    for series_slug, data in sorted_series:
        earliest_date = data['earliest_date'].strftime('%Y-%m-%d')
        post_count = data['post_count']
        meta_image = data['meta_image'] or 'None'
        
        # Get the relative path from the blog post directory
        first_post_dir = data['first_post'].parent.name
        if meta_image and meta_image != 'None':
            # Build the full path relative to the blog post
            full_meta_image_path = f"/blog/{first_post_dir}/{meta_image}"
        else:
            full_meta_image_path = 'None'
            
        print(f"{series_slug}:")
        print(f"  First post: {earliest_date} - {first_post_dir}")
        print(f"  Meta image: {full_meta_image_path}")
        print(f"  Total posts: {post_count}")
        print()

if __name__ == "__main__":
    main()
