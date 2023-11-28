import spacy

# Carregar o modelo em português
nlp = spacy.load("pt_core_news_sm")

# Exemplo de lista de tokens
tokens = ["O", "outro", "cachorro", "marrom", "pula", "alto", "."]

# Processar a lista de tokens com spaCy
doc = nlp(" ".join(tokens))

# Criar uma nova lista sem os adjetivos
tokens_sem_adjetivos = [token.text for token in doc if token.pos_ == "DET"]

# Imprimir a nova lista
print("Tokens sem adjetivos:", tokens_sem_adjetivos)
