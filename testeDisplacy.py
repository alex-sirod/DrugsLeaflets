import spacy
from spacy import displacy

nlp = spacy.load("pt_core_news_sm")
doc = nlp("displaCy uses JavaScript, SVG and CSS.")
spacy.displacy.serve(doc, style="dep", page=True)

