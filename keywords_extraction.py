from langdetect import detect
from rutermextract import TermExtractor
from rake_nltk import Rake
from textblob import TextBlob
from stemming.porter2 import stem


def keywords_extraction(text):
    text = text.replace('\n', ' ')
    text = text.replace('  ', ' ')
    text = text.replace('-', '')
    lang = detect(text)
    link = ''
    if lang == 'ru':
        term_extractor = TermExtractor()
        for term in term_extractor(text):
            if link:
                link = link + ', '+ term.normalized
            else:
                link = term.normalized
    elif lang == 'en':
        blob = TextBlob(text)
        for term in [stem(n) for n,t in blob.tags if t == 'NN' or t == 'NNS']:
            if link: 
                link = link + ', '+ term
            else:
                link = term
    return text, link
    
