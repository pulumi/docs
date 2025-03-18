from keybert import KeyBERT
import torch
from sentence_transformers import SentenceTransformer
import sys
import json

def generate_keywords_mini(text, num_keywords=5, ngram_range=(1, 1)):
    # Use a smaller model optimized for apple silicon when running locally.
    model = SentenceTransformer('all-MiniLM-L6-v2', device='mps' if torch.backends.mps.is_available() else 'cpu')
    
    kw_model = KeyBERT(model=model)
    
    # Extract keywords
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=ngram_range,
        stop_words='english',
        top_n=num_keywords
    )
    
    # Return just the keywords without scores
    return [kw for kw, _ in keywords]

def generate_keywords(text, num_keywords=5, ngram_range=(1, 1)):
    # Initialize KeyBERT model
    kw_model = KeyBERT()
    
    # Extract keywords
    keywords = kw_model.extract_keywords(
        text,
        keyphrase_ngram_range=ngram_range,
        stop_words='english',
        top_n=num_keywords
    )
    
    # Return just the keywords without scores
    return [kw for kw, _ in keywords]

if __name__ == "__main__":
    # Read input from command line
    if len(sys.argv) < 2:
        print(json.dumps({"error": "No input text provided"}))
        sys.exit(1)
    
    input_text = sys.argv[1]
    try:
        keywords = generate_keywords(input_text)
        print(json.dumps(keywords))
    except Exception as e:
        print(json.dumps({"error": str(e)}))
