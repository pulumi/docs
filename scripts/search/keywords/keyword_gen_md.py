import os
import time
import threading
from collections import OrderedDict
from functools import partial
from keybert import KeyBERT
from ruamel.yaml import YAML
from typing import List, Dict, Any
import concurrent.futures
import frontmatter

def find_markdown_files(directory: str) -> List[str]:
    """
    Find all markdown files in the given directory and their subdirectories.
    """
    # get all markdown files in the given directory and their subdirectories.
    markdown_files = []
    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                markdown_files.append(os.path.join(root, file))
    return markdown_files

def process_markdown_file(file_path: str) -> Dict[str, Any]:
    """
    Process markdown file and generate keywords for it.
    """
    print(f"Processing file: {file_path}")
    
    # Read the markdown file.
    with open(file_path, "r") as f:
        content = f.read()

    # break apart the frontmatter and the content
    page = frontmatter.loads(content)
    frontmatter_content = content.split("---", 2)[1]

    # Use ruamel.yaml for this so that we can preserve the comments that are in
    # the frontmatter. This also allows us to preserve the ordering of the keys
    # that were originally on the page to cut down on file diffs.
    yaml = YAML()
    yaml.preserve_quotes = True
    # best guess at indentation for most of our files to retain original integrity as 
    # much as possible :shrug:
    yaml.indent(mapping=2, sequence=4, offset=2)
    ordered_frontmatter = yaml.load(frontmatter_content)

    # Extract title and meta description properties so we can use them
    # as part of the keyword generation process.
    title = ordered_frontmatter.get("title", "")
    meta_desc = ordered_frontmatter.get("meta_desc", "")
    
    # Combine title, meta_desc, and content for keyword generation. We may want to weight these
    # differently in the future, but can make optimizations later.
    combined_text = f"{title} {meta_desc} {page.content}"
    
    # Generate keywords. Up to 5 keywords and 1-gram (single word) range.
    new_keywords = generate_keywords(combined_text, 5, (1, 1))
    
    # Update the frontmatter with new keywords under search and initialize search key if
    # it doesn't exist.
    if "search" not in ordered_frontmatter:
        ordered_frontmatter["search"] = {}

    # Handle existing search.keywords if there happen to be any.
    if "keywords" in ordered_frontmatter["search"]:
        # Get existing keywords
        existing_keywords = ordered_frontmatter["search"]["keywords"]
        
        # Combine existing and new keywords and also dedupe.
        combined_keywords = list(existing_keywords)
        for keyword in new_keywords:
            if keyword not in combined_keywords:
                combined_keywords.append(keyword)
        
        # Update keywords
        ordered_frontmatter["search"]["keywords"] = combined_keywords
    else:
        # if no existing keywords, just set them with the new ones.
        ordered_frontmatter["search"]["keywords"] = new_keywords
    
    # Write the updated frontmatter back to the file
    with open(file_path, "w") as f:
        f.write("---\n")
        yaml.dump(ordered_frontmatter, f)
        f.write("---\n\n")
        f.write(page.content)
    
    # return back the list of keywords for logging purposes.
    final_keywords = ordered_frontmatter["search"]["keywords"]
    
    return {
        "file": file_path,
        "title": title,
        "keywords": final_keywords
    }

def process_batch(files: List[str], batch_size) -> List[Dict[str, Any]]:
    """
    Process markdown files in parallel.
    """
    print(f"Starting batch processing with {len(files)} files using {batch_size} workers")
    start_time = time.time()
    
    with concurrent.futures.ThreadPoolExecutor(max_workers=batch_size) as executor:
        results = list(executor.map(process_markdown_file, files))
    
    end_time = time.time()
    print(f"Batch processing completed in {end_time - start_time:.2f} seconds")
    return results

def generate_keywords(text, num_keywords, ngram_range=(1, 1)):
    """
    Generate keywords for input text using KeyBERT. Using very generic settings for now.
    We can fine tune this later after we prove concept.
    """
    # Initialize KeyBERT model
    kw_model = KeyBERT()
    
    # Extract keywords
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=ngram_range,
        stop_words="english",
        top_n=num_keywords
    )
    
    # Return just the keywords without the scoring
    return [kw for kw, _ in keywords]


def main():
    # Root directory to start processing markdown files. Will recurse through subdirs.
    docs_dir = "content/docs/esc/"
    
    # Find all markdown files
    markdown_files = find_markdown_files(docs_dir)
    print(f"Found {len(markdown_files)} markdown files total")
    
    # TODO: Remove this... only processing a subset of files for testing purposes.
    markdown_files = markdown_files[:32]
    print(f"Processing {len(markdown_files)} files")
    
    # Process files in batches
    batch_size = 8
    results = process_batch(markdown_files, batch_size)
    
    # Print summary
    print("\nProcessing complete!")
    print(f"Processed {len(results)} files")
    for result in results:
        print(f"\nFile: {result['file']}")
        print(f"Title: {result['title']}")
        print(f"Generated keywords: {', '.join(result['keywords'])}")

if __name__ == "__main__":
    main()