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
from sklearn.feature_extraction.text import TfidfVectorizer
import numpy as np

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

def extract_document_content(file_path: str, title_weight: float = 0.5, meta_desc_weight: float = 0.3, content_weight: float = 0.2) -> Dict[str, Any]:
    """
    Extract content and frontmatter from a markdown file and somewhat hacky
    way to generate weighted text.
    
    Params:
    - file_path: path to the md file
    - title_weight: relative importance of the title
    - meta_desc_weight: relative importance of the meta description 
    - content_weight: relative importance of the main content
    """
    with open(file_path, "r") as f:
        content = f.read()
    
    # Parse frontmatter and content
    page = frontmatter.loads(content)
    
    # Extract title and meta description
    title = page.metadata.get("title", "")
    meta_desc = page.metadata.get("meta_desc", "")
    
    # Check if meta_desc is missing and rebalance weights if needed
    if not meta_desc:
        # Redistribute meta_desc weight relative to title and content
        total_remaining = title_weight + content_weight
        if total_remaining > 0:  # Avoid division by zero
            # Distribute meta_desc_weight proportionally
            title_weight += meta_desc_weight * (title_weight / total_remaining)
            content_weight += meta_desc_weight * (content_weight / total_remaining)
        meta_desc_weight = 0
    
    # Normalize weights to ensure they sum to 1.0. 
    # If they do not, then rebalance the weights based on the total sum.
    total_weight = title_weight + meta_desc_weight + content_weight
    if total_weight != 1.0:
        title_weight = title_weight / total_weight
        meta_desc_weight = meta_desc_weight / total_weight
        content_weight = content_weight / total_weight
    
    # add 1 to avoid divide by zero
    title_len = len(title.split()) + 1
    meta_desc_len = len(meta_desc.split()) + 1 if meta_desc else 1
    content_len = len(page.content.split()) + 1
    
    # calculate repetition values as a way to ensure each segment is weighted relative to the sizes of the text.
    content_repeat = 1
    title_repeat = int((title_weight * content_len * content_repeat) / (content_weight * title_len)) + 1 if content_weight > 0 else 1
    
    # Only calculate meta_desc_repeat if we have a meta_desc and its weight is > 0. Sometimes a meta_desc is not present
    # in the hugo frontmatter.
    if meta_desc and meta_desc_weight > 0:
        meta_desc_repeat = int((meta_desc_weight * content_len * content_repeat) / (content_weight * meta_desc_len)) + 1 if content_weight > 0 else 1
        weighted_text = f"{' '.join([title] * title_repeat)} {' '.join([meta_desc] * meta_desc_repeat)} {page.content}"
    else:
        # Skip meta_desc in the weighted text if it's missing
        weighted_text = f"{' '.join([title] * title_repeat)} {page.content}"
    
    return {
        "file_path": file_path,
        "weighted_text": weighted_text,
        "title": title,
        "content": content,
        "page": page
    }

def keybert_tfidf_keyword_extraction(documents: List[Dict[str, Any]], num_keywords=5, disallow=None) -> Dict[str, List[str]]:
    """
    Extract keywords using both corpus-level TF-IDF and KeyBERT.
    Opting for a combined approach here which leverages distinctiveness
    from TF-IDF and while also deriving semantic meaning from KeyBERT.

    TF-IDF is a way to find the most important words in a page by comparing how often
    they appear in a specific page relative to all the other pages. This helps us identify
    the unique keywords that make each page more distinct, helping to reject noise and common
    words that are of less meaning.
    
    Term Frequency: how often a word appears in the page
    Inverse Document Frequency: how rare a word is across all the pages
    
    KeyBERT is a way to find the most important words in a document by looking at the semantic
    meaning of the words. This helps us identify the keywords that are most important to the
    meaning of the page.
    
    Parameters:
    - documents: List of document dictionaries
    - num_keywords: Number of keywords to extract per document
    - disallow: List of terms to exclude from keywords
    """
    print(f"Performing hybrid keyword extraction on {len(documents)} documents")
    
    # Initialize disallow list if not provided
    if disallow is None:
        disallow = []
    else:
        print(f"Using disallow list with {len(disallow)} terms")
    
    # Create corpus from all documents
    corpus = [doc["weighted_text"] for doc in documents]
    file_paths = [doc["file_path"] for doc in documents]
    
    # Vectorizer that will be used to convert the enitre corpus into a TF-IDF matrix.
    print("Building corpus-level TF-IDF vectorizer...")
    vectorizer = TfidfVectorizer(
        ngram_range=(1, 1),
        stop_words='english',
        lowercase=True,
        max_features=10000,
        min_df=1,
        max_df=1.0
    )
    
    # fit_transform combines fit and transform.
    # fit calculates the IDF values for each term
    # transform performs dot product between the term frequency
    # vectors and the inverse document frequency values.
    tfidf_matrix = vectorizer.fit_transform(corpus)
    feature_names = vectorizer.get_feature_names_out()
    print(f"terms: {len(feature_names)} terms")
    
    # Extract 10 TF-IDF keywords
    tfidf_keywords = extract_tfidf_keywords(tfidf_matrix, feature_names, file_paths, 10, disallow)
    
    # Extract 10 KeyBERT keywords
    keybert_keywords = extract_keybert_keywords(documents, vectorizer, 10, disallow)
    
    # Combine the results with a preference for keywords that appear in both methods
    combined_keywords = {}
    
    # Iterate over each file and combine the keywords from both methods
    for file_path in tfidf_keywords:
        # Get keywords from both methods
        tfidf_kw = tfidf_keywords[file_path]
        keybert_kw = keybert_keywords[file_path]

        print(f"TF-IDF keywords for {file_path}:\n\t {tfidf_kw}")
        print(f"KeyBERT keywords for {file_path}:\n\t {keybert_kw}")
        
        # First prioritize common keywords that appear in both methods
        common_kw = []
        for kw in tfidf_kw:
            if any(kw.lower() == kb.lower() for kb in keybert_kw):
                common_kw.append(kw)
        
        print(f"Common keywords for {file_path}:\n\t {common_kw}")

        # Then add unique keywords from each method until we reach the desired count
        unique_kw = []
        # First add remaining TF-IDF keywords that aren't in common_kw
        for kw in tfidf_kw:
            if kw not in common_kw and not any(kw.lower() == unique.lower() for unique in unique_kw):
                unique_kw.append(kw)
                
        # Then add KeyBERT keywords that aren't in common_kw or already in unique_kw
        for kw in keybert_kw:
            if not any(kw.lower() == common.lower() for common in common_kw) and \
               not any(kw.lower() == unique.lower() for unique in unique_kw):
                unique_kw.append(kw)

        print(f"Unique keywords for {file_path}:\n\t {unique_kw}")
        
        # Combine results and prioritize common keywords
        result = common_kw + unique_kw
        combined_keywords[file_path] = result[:num_keywords]

        print(f"Combined keywords for {file_path}:\n\t {combined_keywords[file_path]}")
    
    return combined_keywords

def extract_tfidf_keywords(tfidf_matrix, feature_names, file_paths, num_keywords=5, disallow=None) -> Dict[str, List[str]]:
    """
    Extract keywords from a pre-computed TF-IDF matrix.
    """
    print("Extracting corpus-level TF-IDF keywords...")
    
    # Initialize disallow list if not provided
    if disallow is None:
        disallow = []
    
    # Extract top keywords for each document
    document_keywords = {}
    
    for i, file_path in enumerate(file_paths):
        # Get document's TF-IDF scores
        tfidf_scores = tfidf_matrix[i].toarray()[0]
        
        # Get indices of highest TF-IDF scores
        sorted_indices = tfidf_scores.argsort()[::-1]
        
        # Get top keywords filtering out low scores and disallowed terms
        top_keywords = []
        for idx in sorted_indices:
            term = feature_names[idx]
            if tfidf_scores[idx] > 0.02 and len(top_keywords) < num_keywords:
                # Check if the term is in the disallow list
                if not any(disallowed_term.lower() in term.lower() for disallowed_term in disallow):
                    top_keywords.append(term)
        
        document_keywords[file_path] = top_keywords
    
    return document_keywords

def extract_keybert_keywords(documents: List[Dict[str, Any]], vectorizer, num_keywords=5, disallow=None) -> Dict[str, List[str]]:
    """
    Extract keywords using KeyBERT
    """
    print("Extracting KeyBERT keywords...")
    
    # Initialize KeyBERT model
    kw_model = KeyBERT()
    
    # Extract keywords for each document
    document_keywords = {}
    
    for doc in documents:
        file_path = doc["file_path"]
        weighted_text = doc["weighted_text"]
        
        # Extract keywords using KeyBERT with the provided vectorizer
        keywords = kw_model.extract_keywords(
            weighted_text,
            keyphrase_ngram_range=(1, 1),
            stop_words='english',
            use_mmr=True,
            diversity=0.7,
            top_n=num_keywords
        )
        
        # Filter out disallowed terms
        filtered_keywords = []
        for kw, score in keywords:
            if not any(disallowed_term.lower() in kw.lower() for disallowed_term in disallow):
                filtered_keywords.append((kw, score))
        
        # Store just the keywords without scores (limited to requested number)
        document_keywords[file_path] = [kw for kw, _ in filtered_keywords[:num_keywords]]
    
    return document_keywords

def process_markdown_file(file_path: str, keywords: List[str]) -> Dict[str, Any]:
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
    # best guess at indentation for most of our files to retain original integrity as 
    # much as possible :shrug:
    yaml = YAML()
    yaml.preserve_quotes = True
    yaml.indent(mapping=2, sequence=4, offset=2)
    ordered_frontmatter = yaml.load(frontmatter_content)
    
    # Get existing title for logging
    title = ordered_frontmatter.get("title", "")
    
    # Initialize search in frontmatter if it doesn't exist
    if "search" not in ordered_frontmatter:
        ordered_frontmatter["search"] = {}
        
    # Combine existing and new keywords and also dedupe.
    if "keywords" in ordered_frontmatter["search"]:
        existing_keywords = ordered_frontmatter["search"]["keywords"]
        combined_keywords = list(existing_keywords)
        for keyword in keywords:
            if keyword not in combined_keywords:
                combined_keywords.append(keyword)
        ordered_frontmatter["search"]["keywords"] = combined_keywords
    else:
        ordered_frontmatter["search"]["keywords"] = keywords
    
    # Write updated frontmatter back to file
    with open(file_path, "w") as f:
        f.write("---\n")
        yaml.dump(ordered_frontmatter, f)
        f.write("---\n\n")
        f.write(page.content + "\n")

    # Return info for logging
    return {
        "file": file_path,
        "title": title,
        "keywords": ordered_frontmatter["search"]["keywords"]
    }

def write_keywords_to_files(files: List[str], file_keyword_map: Dict[str, List[str]]) -> List[Dict[str, Any]]:
    """
    Write generated keywords to markdown files.
    """
    print(f"Starting to write keywords to {len(files)} files")
    
    start_time = time.time()
    results = []
    
    for file_path in files:
        keywords = file_keyword_map[file_path]
        result = process_markdown_file(file_path, keywords)
        results.append(result)
    
    end_time = time.time()
    print(f"Finished writing keywords")
    return results

def main():
    # Root directory to start processing markdown files. Will recurse through subdirs.
    docs_dir = "content/docs/esc/"
    
    # list of terms to exclude from generated keywords
    disallow = [
        "example",
        "click",
        "documentation",
        "note",
        "pulumi",
        "href", 
        "src", 
        "div", 
        "shortcode", 
        "notes",
        "chooser", 
        "choosable"
    ]
    
    # Configure normalized weights - must sum to 1.0
    title_weight = 0.25     # title 25%
    meta_desc_weight = 0.25 # meta_desc 25% 
    content_weight = 0.5    # content 50%
    
    # Number of keywords to extract per document
    num_keywords = 7
    
    # Find all markdown files
    markdown_files = find_markdown_files(docs_dir)
    print(f"Found {len(markdown_files)} markdown files total")
    
    # TODO: Remove this... only processing a subset of files for testing purposes.
    # markdown_files = markdown_files[:32]
    print(f"Processing {len(markdown_files)} files")
    
    # Extract document content for corpus building with normalized weights
    print("Extracting document content...")
    documents = []
    for file_path in markdown_files:
        documents.append(extract_document_content(file_path, title_weight, meta_desc_weight, content_weight))
    
    # Extract keywords using hybrid approach with TF-IDF and KeyBERT
    file_keyword_map = keybert_tfidf_keyword_extraction(documents, num_keywords=num_keywords, disallow=disallow)
    
    # Update documents with new keywords
    results = write_keywords_to_files(markdown_files, file_keyword_map)
    
    # Print summary
    print("\nProcessing complete!")
    print(f"Processed {len(results)} files")
    for result in results:
        print(f"\nFile: {result['file']}")
        print(f"Title: {result['title']}")
        print(f"Generated keywords: {', '.join(result['keywords'])}")

if __name__ == "__main__":
    main()