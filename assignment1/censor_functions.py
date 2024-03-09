import spacy
import re
from pathlib import Path
# import en_core_web_md
# from warning import filterwarnings
# filterwarnings('ignore')

# nlp = en_core_web_md.load()
# Load the spaCy language model
# nlp = spacy.load("en_core_web_sm")

try:
    nlp = spacy.load("en_core_web_md")
except OSError:
    print("Downloading the 'en_core_web_md' model...")
    from spacy.cli import download
    download("en_core_web_md")
    nlp = spacy.load("en_core_web_md")

def censor_names(text):
    """Censors names found in the given text."""
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "PERSON":
            text = text.replace(ent.text, "█" * len(ent.text))
    return text

def censor_dates(text):
    """Censors dates found in the given text using spaCy and enhanced regex."""
    # First, censor dates recognized by spaCy
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ == "DATE":
            text = text.replace(ent.text, "█" * len(ent.text))

    # Enhanced regex patterns for broader date format coverage
    date_patterns = [
        r'\b\d{1,2}[/-]\d{1,2}[/-]\d{2,4}\b',  # Matches MM/DD/YYYY, DD/MM/YYYY
        r'\b\d{1,2}\s+(Jan|Feb|Mar|Apr|May|Jun|Jul|Aug|Sep|Oct|Nov|Dec)[a-z]*\s+\d{2,4}\b',  # Matches "1 Jan 2020"
        r'\b\d{2,4}[/-]\d{1,2}[/-]\d{1,2}\b',  # Matches YYYY-MM-DD, YYYY/DD/MM
        r'\b(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},\s+\d{4}\b',  # Full month names
        # Add more patterns as needed for additional formats
    ]
    for pattern in date_patterns:
        text = re.sub(pattern, lambda x: "█" * len(x.group()), text)
    return text


def censor_phones(text):
    """Censors phone numbers found in the given text using enhanced regex."""
    phone_patterns = [
        # Matches various formats including international prefixes and extensions
        r'\+?\d[\d\s.-]{8,}\d',  # Broad pattern for international and varied formats
        r'\(\d{3}\)\s*\d{3}[-.]\d{4}',  # Matches (123) 456-7890
        r'\b\d{3}[-.]\d{3}[-.]\d{4}\b',  # Matches 123-456-7890
        r'\b\d{10}\b',  # Matches 1234567890
        # Add more patterns here as needed
    ]
    for pattern in phone_patterns:
        text = re.sub(pattern, lambda x: "█" * len(x.group()), text)
    return text


def censor_addresses(text):
    """Censors addresses found in the given text by combining regex and spaCy NER."""
    # Enhanced regex to match broader address patterns (numbers, street keywords, potentially building names, etc.)
    enhanced_address_regex = r'\b\d{1,4}\s([A-Za-z0-9\-]+\s){0,3}(Street|St|Avenue|Ave|Road|Rd|Boulevard|Blvd|Drive|Dr|Lane|Ln|Court|Ct)\b'

    # Use spaCy to find entities that could be part of addresses
    doc = nlp(text)
    for ent in doc.ents:
        if ent.label_ in ["ORG", "GPE", "LOC"]:
            text = re.sub(re.escape(ent.text), "█" * len(ent.text), text)
    
    # Apply the enhanced regex for address patterns
    text = re.sub(enhanced_address_regex, lambda x: "█" * len(x.group()), text, flags=re.IGNORECASE)
    
    return text


