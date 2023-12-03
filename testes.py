import spacy

# Carregar o modelo do spaCy para o idioma desejado
nlp = spacy.load("pt_core_news_sm")

# Sentença com pontuações
sentenca = "- corticosteróides  (glicocorticóides e mineralocorticóides sistêmicos);"

# Processar a sentença com spaCy
doc = nlp(sentenca)

# Lista para armazenar os tokens sem pontuações
tokens_sem_pontuacao = []

# Iterar pelos tokens da sentença
for token in doc:
    # Verificar se o token não é uma pontuação
    if not token.is_punct:
        # Adicionar o texto do token à lista
        tokens_sem_pontuacao.append(token.text)

# Juntar os tokens para obter a sentença sem pontuações
sentenca_sem_pontuacao = " ".join(tokens_sem_pontuacao)

# Imprimir a sentença resultante
print(sentenca_sem_pontuacao)
