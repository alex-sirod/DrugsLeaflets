import re
import nltk
from nltk import ngrams
from nltk.probability import FreqDist
from nltk.text import Text

# nltk.download('punkt')

text1 = u'''APRESENTAÇÃO  
Pó para suspensão oral de 250 mg/5 mL: embalagem com frasco contendo pó para reconstituição de 150 mL de 
suspensão acompanhado de uma seringa dosadora de 10 mL. 
 
USO ORAL  
USO ADULTO E PEDIÁTRICO 
 
COMPOSIÇÃO 
Cada 5 mL de suspensão oral contém: 
amoxicilina tri-hidratada (equivalente a 250 mg de amoxicilina) ............................................................. 287,0 mg 
Excipientes: sorbitol, dióxido de silício, celulose microcristalina, crospovidona, goma xantana, aspartamo, 
ciclamato de sódio, sacarina sódica di-hidratada, ácido cítrico, citrato de sódio, propilparabeno, metilparabeno, 
benzoato de sódio, aroma de laranja e estearato de magnésio. 
 
II – INFORMAÇÕES AO PACIENTE 
 
1. PARA QUE ESTE MEDICAMENTO É InDICADO? '''


def find_ngrams(target_word, n=3):

    # Quebra o texto em palavras
    words = re.findall(r'\w+', text1)

    # Gera os n-gramas
    five_grams = list(ngrams(words, n))

    # Encontra os 5-gramas que contêm 'amoxicilina'
    relevant_grams = [gram for gram in five_grams if target_word in gram]

    # Imprime os 5-gramas encontrados
    for gram in relevant_grams:
        print(' '.join(gram))

def simplify_tag(t):
    if "contém" in t:
        return t[t.index("contém")+1:]
    else:
        return t
def freq_dist(text):
    target_word = 'aroma'
    sentence = text
    tokens = nltk.tokenize.word_tokenize(sentence)
    fdist = FreqDist(tokens)
    return fdist.most_common()

def concordance_in(word):
    a = Text(nltk.word_tokenize(text1))
    return a.concordance(word)

# find_ngrams("amoxicilina")
# print(simplify_tag(text1))

print(freq_dist(text1))
#concordance_in("de")


import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

# Baixe o lematizador RSLP
#nltk.download('rslp')

def stemming_portuguese_text(text):
    # Tokenize o texto em palavras
    words = word_tokenize(text, language='portuguese')

    # Inicialize o lematizador RSLP
    lemmatizer = RSLPStemmer()

    # Lematize cada palavra
    lemmatized_words = [lemmatizer.stem(word) for word in words]

    # Recrie o texto lematizado
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text

import nltk
from nltk.stem import WordNetLemmatizer
from nltk.tokenize import word_tokenize

# Baixe o lematizador WordNet
# nltk.download('wordnet')

def lemmatize_portuguese_text(text):
    # Tokenize o texto em palavras
    words = word_tokenize(text, language='portuguese')

    # Inicialize o lematizador WordNet
    lemmatizer = WordNetLemmatizer()

    # Lematize cada palavra
    lemmatized_words = [lemmatizer.lemmatize(word) for word in words]

    # Recrie o texto lematizado
    lemmatized_text = ' '.join(lemmatized_words)

    return lemmatized_text

# Exemplo de uso:
# texto_original = "não use medicamentos sem o conhecimento da sua médica."
texto_original = "não use medicamentos sem o conhecimento da sua profissional médica"
texto_lemmatizado = lemmatize_portuguese_text(texto_original)
texto_stemming = stemming_portuguese_text(texto_original)

print("Texto Original:")
for a in texto_original.split():
    print(a)
print("Texto Lematizado:")
for a in texto_lemmatizado.split():
    print(a)

print("Texto stemming:")
for a in texto_stemming.split():
    print(a)

