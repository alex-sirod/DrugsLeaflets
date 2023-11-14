import spacy




nlp = spacy.load('pt_core_news_lg')


custom_rules = [
    ("contém", "VERB", "conter"),
    ("foi", "VERB", "ser"),
    # Adicione outras regras personalizadas conforme necessário
]


doc = nlp("A frase contém várias palavras.")

lemmatizer = nlp.add_pipe("lemmatizer")
# This usually happens under the hood
processed = lemmatizer(doc)
print(processed.text)