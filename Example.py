from spacy.matcher import Matcher
from datasources.leaflets_section import LeafletSection
from drug_leaflet import Leaflet
import spacy
from time import sleep
from spacy import displacy
import re
from IPython.display import display, HTML
from nltk.stem import PorterStemmer
stemmer = PorterStemmer()

nlp = spacy.load('pt_core_news_lg')
doc = nlp('''APRESENTAÇÃO 
Suspensão oral de 50 mg/mL em embalagem com 1 frasco de 30 mL. 
 
USO ORAL 
USO ADULTO E PEDIÁTRICO ACIMA DE 6 MESES 
 
COMPOSIÇÃO 
Cada mL (10 gotas) da suspensão oral contém:  
ibuprofeno............................................. 50 mg 
veículo q.s.p.......................................... 1 mL 
Excipientes: sacarina sódica, benzoato de sódio, celulose microcristalina, carmelose sódica, laurilsulfato de 
sódio, sorbitol, propilenoglicol, glicerol, goma xantana, manitol, acessulfame potássico, simeticona, sucralose, 
aroma de morango, aroma de bala, aroma de açúcar, dióxido de titânio, ácido cítrico e água purificada. 
Cada gota deste medicamento contém 5 mg de ibuprofeno. 
 
1. PARA QUE ESTE MEDICAMENTO É INDICADO? ''')


def ingredientes():
    # for s in doc.sents:

    # if s[0].is_title and s[0].lemma_ == 'excipiente':
    #     print('Toda sentença:', s)
    #     print('Lema do primeiro token:', s[0].lemma_)
    #     print('root', s.root)
    #     print('conjuncts', s.conjuncts)
    #     print('conjuncts', [sb for sb in s.root.subtree])
    #
    #     ingredientes = re.sub(r'\s*,\s*|\n', ',', s.text.split('Excipientes: ', 1)[1])
    #     # ingredientes_divididos = re.split(r',\s*|:\s*', s.text)
    #     list_empty = ["", " "]
    #     print('Toda sentença:', s.text_with_ws)
    #     composition = [i for i in ingredientes.split(',') if i not in list_empty]
    #
    #     print('---------------------')

    for i, s in enumerate(doc.sents):

        if s.root.text == 'contém' and s.root.is_ancestor(s[0]):  # or s.root.lemma_ == 'conter':
            print('NOMES', [i for i in s.noun_chunks])
            print('is ancestor de ', s[0], s.root.is_ancestor(s[0]))

            print('Toda sentença:', s)
            # print('Subtree:', [i for i in s.subtree])
            # print('Lema do primeiro token:', s[0].lemma_)
            # print('root', s.root.lemma_)
            # print('orth', s.root.orth_)
            #
            # print('---------------------')
            # print('end', s[0::] )
            # print('------ Pegar a próxima sentença ------')
            # if i +1 < len(list(doc.sents)):
            #     proxima_sentenca = list(doc.sents)[i+1]
            #     print('próxima sentença:', type(proxima_sentenca), proxima_sentenca)
            #     proxima_sentenca = proxima_sentenca.noun_chunks
            #     print('próxima sentença(noun):', type(proxima_sentenca), proxima_sentenca)
            #     l=[c.text for c in proxima_sentenca]
            #     print('lista da próxima sentença:', l)
            #     print('tamanho', len(l))
            #
            #
            #     # txt = nlp(" ".join(l))
            #     # print('txt', txt)
            #     # filtered_tokens = [token for token in txt if not (
            #     #             token.is_punct or token.is_digit or token.is_currency or token.pos_ == 'NUM')]
            #     # print('filtered_tokens', filtered_tokens)
            #     # for token in txt:
            #     #     if not token.is_punct and not token.is_digit and not token.is_currency\
            #     #             and not token.pos_ == 'NUM':
            #     #         print('token', token)
            #     #
            #     #         print("{:>20}{:>20}{:>10}{:>15}{:>10}{:>5}{:>5}{:>5}{:>5}".format(
            #     #             token.text, "lemma:" + token.lemma_, token.pos_, token.tag_,
            #     #             token.dep_, token.shape, token.is_alpha,
            #     #             token.is_stop, token.is_title, token.is_ancestor(doc[0])))
            # else:
            #     print('Não há mais sentenças')


def ingredientes_matcher():
    matcher = Matcher(nlp.vocab)
    pattern = [{'LOWER': 'contém'},
               {'IS_PUNCT': True}]
    matcher.add("composicao_medicamento", [pattern])

    matcher2 = Matcher(nlp.vocab)
    pattern2 = [{"lower": {"in": ["excipientes"]}},
               ]
    matcher2.add("informacao_paciente", [pattern2])

    for match_id, start, end in matcher(doc):
        match_text = doc[start:end].text
        print(f"Encontrado padrão 1: '{match_text}'. Início: {start}. Fim: {end}")
        print(matcher(doc)[-1][2], "próximo token após o padrão:", doc[matcher(doc)[-1][2] + 1].text)

    for match_id, start, end in matcher2(doc):
        match_text2 = doc[start:end].text
        print(f"Encontrado padrão 2: '{match_text2}'. Início: {start}. Fim: {end}")

        indice_token_anterior = matcher2(doc)[-1][2] - 1
    #
    #     if indice_token_anterior >= 0:
    #         token_anterior = doc[indice_token_anterior]
    #         print(f"Token anterior: {token_anterior.text}")
    #     else:
    #         print("Não há token anterior, pois o último token é o primeiro token do documento.")

    # find the span between the patterns
    # indice_fim_primeiro_padrao = matcher(doc)[-1][2]
    # indice_inicio_segundo_padrao = matcher2(doc)[0][1]
    # span_entre_padroes = doc[indice_fim_primeiro_padrao:indice_inicio_segundo_padrao]  # .text.split('\n')
    # print('Span entre padrões:', span_entre_padroes)
    #
    # for i, s in enumerate(span_entre_padroes.sents):
    #     if s.root.text != 'contém' and not s.root.is_ancestor(s[0]):
    #         print('Toda sentença:', [c for c in s.noun_chunks])

        # if s.root.text == 'contém' and s.root.is_ancestor(s[0]):  # or s.root.lemma_ == 'conter':
        #     print('NOMES', [i for i in s.noun_chunks])
        #     print(next(s.root.children))

        # print(i+1,s)
        # for c in s.noun_chunks:
        #     if not any(value in c.text for value in LeafletSection().measures_units):
        #         print(c.text)

    # print("Span entre padrões:", span_entre_padroes)


def example():
    pattern = [
        {"LEMMA": "love", "POS": "VERB"},
        {"POS": "NOUN"}
    ]

    pattern = [
        {"LEMMA": "buy"},
        {"POS": "DET", "OP": "?"},  # optional: match 0 or 1 times
        {"POS": "NOUN"}
    ]

    pattern = [{"TEXT": "iOS"}, {"IS_DIGIT": True}]

    pattern = [{"LEMMA": "download"}, {"POS": "PROPN"}]

    # Write a pattern for adjective plus one or two nouns
    pattern = [{"POS": "ADJ"}, {"POS": "NOUN"}, {"POS": "NOUN", "OP": "?"}]


def example2():
    import json
    import spacy

    with open("exercises/en/countries.json", encoding="utf8") as f:
        COUNTRIES = json.loads(f.read())

    nlp = spacy.blank("en")
    doc = nlp("Czech Republic may help Slovakia protect its airspace")

    # Import the PhraseMatcher and initialize it
    from spacy.matcher import PhraseMatcher

    matcher = PhraseMatcher(nlp.vocab)

    # Create pattern Doc objects and add them to the matcher
    # This is the faster version of: [nlp(country) for country in COUNTRIES]
    patterns = list(nlp.pipe(COUNTRIES))
    matcher.add("COUNTRY", patterns)

    # Call the matcher on the test document and print the result
    matches = matcher(doc)
    print([doc[start:end] for match_id, start, end in matches])



if __name__ == '__main__':
    # ingredientes()
    ingredientes_matcher()




