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
doc = nlp('''
































Microsoft Word - Ibuprofeno_Bula_Paciente.doc


 

Ibuprofeno_bula_paciente 
 
 
 
 

 
 
 

 

Ibuprofeno 
Prati-Donaduzzi 
Suspensão oral 

50 mg/mL 
 
 
 
 
 
 
 
 



 
 

 

Ibuprofeno_bula_paciente 
1 

 

INFORMAÇÕES AO PACIENTE 
ibuprofeno 
Medicamento genérico Lei n° 9.787, de 1999 
 
APRESENTAÇÃO 
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
 
1. PARA QUE ESTE MEDICAMENTO É INDICADO? 
Ibuprofeno é um medicamento indicado para redução da febre e para o alívio de dores, tais como: dores 
decorrentes de gripes e resfriados, dor de garganta, dor de cabeça, dor de dente, dor nas costas, cólicas 
menstruais e dores musculares. 
 
2. COMO ESTE MEDICAMENTO FUNCIONA? 
Este medicamento exerce atividades contra a dor e contra a febre. O início de ação ocorre de 15 a 30 minutos 
após sua administração oral e permanece por 4 a 6 horas. 
 
3. QUANDO NÃO DEVO USAR ESTE MEDICAMENTO? 
Não utilize este medicamento se você já teve qualquer alergia ou alguma reação incomum a qualquer um dos 
componentes da fórmula do produto. 
Este produto contém ibuprofeno que pode causar reações de natureza alérgica, entre as quais a asma brônquica, 
especialmente em pessoas alérgicas ao ácido acetilsalicílico. 
Não utilize este medicamento caso tenha apresentado alguma reação alérgica ao ácido acetilsalicílico e a outros 
anti-inflamatórios, medicamentos para dor ou febre. Não utilize este produto contra a dor por mais de 10 dias ou 
contra a febre por mais de 3 dias, a menos que seja prescrito pelo médico. Não ultrapasse a dose recomendada. 
Não tome este produto com outros medicamentos contendo ibuprofeno ou outros medicamentos para dor, exceto 
sob orientação médica. 
Não utilize este medicamento em casos em que o ácido acetilsalicílico, iodeto e outros anti-inflamatórios não 
esteroides tenham induzido asma, rinite, urticária, pólipo nasal, angioedema, broncoespasmo e outros sintomas 
de reação alérgica ou anafilática. 
Não utilizar este medicamento junto com bebidas alcoólicas. 
Este medicamento é contraindicado a pacientes com úlcera gastroduodenal ou sangramento 
gastrintestinal. 
Este medicamento é contraindicado para menores de 6 meses de idade. 
 
4. O QUE DEVO SABER ANTES DE USAR ESTE MEDICAMENTO? 
Advertências 
O uso de ibuprofeno em crianças com menos de 2 anos de idade e idosos deve ser feito sob orientação 
médica. 
Informe sempre o médico sobre possíveis doenças do coração, nos rins, no fígado ou outras que você tenha, para 
receber uma orientação cuidadosa. Em pacientes com asma ou outras doenças alérgicas, especialmente quando 
há história de broncoespasmo, o ibuprofeno deve ser usado com cautela. 
Consulte um médico caso: Não esteja ingerindo líquidos; tenha perda contínua de líquidos por diarreia ou 
vômito; tenha dor de estômago; apresente dor de garganta grave ou persistente ou dor de garganta acompanhada 



 
 

 

Ibuprofeno_bula_paciente 
2 

 

de febre elevada, dor de cabeça, enjoos e vômitos; e tenha ou teve problemas ou efeitos colaterais com este ou 
qualquer outro medicamento para dor e febre. 
Consulte um médico antes de utilizar este medicamento se: estiver sob tratamento de alguma doença grave; 
estiver tomando outro(s) medicamento(s); e estiver tomando outro produto que contenha ibuprofeno ou outro 
analgésico e antipirético. 
Pare de utilizar este medicamento e consulte um médico caso: ocorra uma reação alérgica; a dor ou a febre piorar 
ou durar mais de 3 dias; não obtenha melhora após 24 horas de tratamento; ocorra vermelhidão ou inchaço na 
área dolorosa; e surjam novos sintomas. 
Gravidez e amamentação 
Não utilizar este medicamento durante a gestação ou a amamentação, exceto sob recomendação médica. 
Informe ao seu médico a ocorrência de gravidez durante o tratamento ou após o seu término. Informe ao seu 
médico se você estiver amamentando. 
Este medicamento não deve ser utilizado por mulheres grávidas sem orientação médica. 
Informe imediatamente seu médico em caso de suspeita de gravidez. 
Durante o período de aleitamento materno ou doação de leite humano, só utilize medicamentos com o 
conhecimento do seu médico ou cirurgião-dentista, pois alguns medicamentos podem ser excretados no leite 
humano, causando reações indesejáveis no bebê. 
Interações medicamentosas 
Interações medicamento-medicamento 
O uso de ibuprofeno e de outros analgésicos e antipiréticos junto com os seguintes fármacos deve ser evitado, 
especialmente nos casos de administração continua: ácido acetilsalicílico, paracetamol, colchicina, iodetos, 
medicamentos fotossensibilizantes, outros anti-inflamatórios não esteroides, corticosteroides, corticotrofina, 
uroquinase, antidiabéticos orais ou insulina, anti-hipertensivos e diuréticos, ácido valproico, plicamicina, sais de 
ouro, ciclosporina, lítio, probenecida, inibidores da ECA (enzima conversora da angiotensina), agentes 
anticoagulantes ou trombolíticos, inibidores de agregação plaquetária, cardiotônicos digitálicos, digoxina, 
metotrexato e hormônios tireoidianos. 
Interações medicamento-exame laboratorial 
Durante o uso de ibuprofeno, os exames de sangue poderão indicar anemia. Se houver sangramento no aparelho 
digestivo devido ao uso do ibuprofeno, o exame de fezes para pesquisa de sangue oculto poderá ter resultado 
positivo. O valor da taxa de açúcar no sangue (glicemia) poderá ser mais baixo durante o uso de ibuprofeno. Não 
existe interferência conhecida com outros exames. 
Informe ao seu médico ou cirurgião-dentista se você está fazendo uso de algum outro medicamento. 
 
5. ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO? 
Você deve manter este medicamento em temperatura ambiente (entre 15 e 30 °C), em lugar seco, fresco e ao 
abrigo da luz. Nestas condições o prazo de validade é de 24 meses a contar da data de fabricação. 
Número de lote e datas de fabricação e validade: vide embalagem. 
Não use medicamento com o prazo de validade vencido. Guarde-o em sua embalagem original. 
Este medicamento apresenta-se na forma de uma suspensão oral, de cor branca, com aroma característico. 
Antes de usar, observe o aspecto do medicamento. Caso ele esteja no prazo de validade e você observe 
alguma mudança no aspecto, consulte o farmacêutico para saber se poderá utilizá-lo. 
Todo medicamento deve ser mantido fora do alcance das crianças. 
 
6. COMO DEVO USAR ESTE MEDICAMENTO? 
Modo de usar  
Para usar, rompa o lacre da tampa, pressione levemente o frasco e goteje a quantidade necessária de acordo com 
a posologia. Fechar o frasco após o uso.  
Agite antes de usar. 
Posologia 
Crianças 
A dose recomendada para crianças a partir de 6 meses de idade pode variar de 1 a 2 gotas/Kg de peso, em 
intervalos de 8 a 6 horas, ou seja, de 3 a 4 vezes ao dia. 
A dose máxima por dose em crianças menores de 12 anos de idade é de 40 gotas (200 mg) e a dose máxima 
permitida por dia é de 160 gotas (800 mg). 
Adultos 
Em adultos, a dose habitual deste medicamento, para febre é de 40 gotas (200 mg) a 160 gotas (800 mg), 



 
 

 

Ibuprofeno_bula_paciente 
3 

 

podendo ser repetida por, no máximo, 4 vezes por dia. 
A dose máxima permitida por dia em adultos é de 640 gotas (3200 mg). 
Dose recomendada por no máximo, 4 vezes ao dia: 
 

Peso (Kg) 
Febre baixa 
(< 39°C) 

Febre alta 
(≥ 39°C) 

5 Kg 5 gotas 10 gotas 
6 Kg 6 gotas 12 gotas 
7 Kg 7 gotas 14 gotas 
8 Kg 8 gotas 16 gotas 
9 Kg 9 gotas 18 gotas 
10 Kg 10 gotas 20 gotas 
11 Kg 11 gotas 22 gotas 
12 Kg 12 gotas 24 gotas 
13 Kg 13 gotas 26 gotas 
14 Kg 14 gotas 28 gotas 
15 Kg 15 gotas 30 gotas 
16 Kg 16 gotas 32 gotas 
17 Kg 17 gotas 34 gotas 
18 Kg 18 gotas 36 gotas 
19 Kg 19 gotas 38 gotas 
20 Kg 20 gotas 40 gotas 
21 Kg 21 gotas 40 gotas 
22 Kg 22 gotas 40 gotas 

Peso (Kg) 
Febre baixa 
(< 39°C) 

Febre alta 
(≥ 39°C) 

23 Kg 23 gotas 40 gotas 
24 Kg 24 gotas 40 gotas 
25 Kg 25 gotas 40 gotas 
26 Kg 26 gotas 40 gotas 
27 Kg 27 gotas 40 gotas 
28 Kg 28 gotas 40 gotas 
29 Kg 29 gotas 40 gotas 
30 Kg 30 gotas 40 gotas 
31 Kg 31 gotas 40 gotas 
32 Kg 32 gotas 40 gotas 
33 Kg 33 gotas 40 gotas 
34 Kg 34 gotas 40 gotas 
35 Kg 35 gotas 40 gotas 
36 Kg 36 gotas 40 gotas 
37 Kg 37 gotas 40 gotas 
38 Kg 38 gotas 40 gotas 
39 Kg 39 gotas 40 gotas 
40 Kg 40 gotas 40 gotas 

 
Siga corretamente o modo de usar. Em caso de dúvidas sobre este medicamento, procure orientação do 
farmacêutico. Não desaparecendo os sintomas, procure orientação de seu médico ou cirurgião-dentista.  
 
7. O QUE DEVO FAZER QUANDO EU ME ESQUECER DE USAR ESTE MEDICAMENTO? 
Use a medicação assim que se lembrar. Se o horário estiver próximo ao que seria a dose seguinte, pule a dose 
perdida e siga o horário das outras doses programadas normalmente. Não dobre a dose para compensar a dose 
perdida. 
Em caso de dúvidas, procure orientação do farmacêutico ou de seu médico, ou cirurgião-dentista. 
 
8. QUAIS OS MALES QUE ESTE MEDICAMENTO PODE ME CAUSAR? 
Junto com os efeitos necessários para seu tratamento, este medicamento pode causar efeitos não desejados. 
Apesar de nem todos estes efeitos colaterais ocorrerem, você deve procurar atendimento médico caso algum 
deles ocorra. Ao classificar a frequência das reações, utilizamos os seguintes parâmetros: 
Reações comuns (ocorre entre 1% e 10% dos pacientes que utilizam este medicamento) 
- Sistema nervoso central: tontura; 
- Pele: rash cutâneo (aparecimento de lesões na pele, como bolhas consistentes ou manchas); 
- Sistema gastrintestinal: dor de estômago; náuseas. 
Reações incomuns (ocorre entre 0,1% e 1% dos pacientes que utilizam este medicamento) 
- Sistema gastrintestinal: indigestão; prisão de ventre; perda de apetite; vômitos; diarreia; gases. 
- Sistema geniturinário: retenção de sódio e água. 
- Sistema Nervoso Central: dor de cabeça; irritabilidade; zumbido. 
Reações raras (ocorre entre 0,01% e 0,1% dos pacientes que utilizam este medicamento) 
- Pele: alergia; eritema multiforme (reação do sistema de defesa das mucosas e da pele); necrólise epidérmica 
tóxica (lesão dermatológica rara); Síndrome de Stevens-Johnson (forma grave do eritema multiforme); urticária; 
Síndrome lupus-like; manchas roxas e avermelhadas; sensibilidade da luz. 
- Sistema Nervoso Central: depressão; ansiedade; meningite asséptica (inflamação da camada que reveste o 
cérebro); confusão mental; alucinações; alterações de humor; insônia. 
- Sistema nervoso periférico: formigamento. 



 
 

 

4 
 

- Sistema gastrintestinal: icterícia (cor amarelada na pele causada por problemas com a bile); feridas no esôfago; 
feridas no estômago; feridas no duodeno; hepatite medicamentosa; inflamação no pâncreas; sangramento 
digestivo. 
- Sistema geniturinário: insuficiência dos rins; morte do tecido dos rins; infecção na bexiga; sangue na urina; 
aumento da frequência e quantidade de urina. 
- Sangue: anemia, anemia hemolítica (anemia causada pela quebra das células vermelhas); pancitopenia 
diminuição das células do sangue); hipoplasia medular (diminuição da atividade formadora dos tecidos orgânicos 
pele, músculos); trombocitopenia (diminuição das plaquetas no sangue); leucopenia (diminuição das células de 
defesa); agranulocitose (diminuição de tipos especiais de células de defesa); eosinofilia (aumento de um tipo 
especial de célula de defesa). 
- Visão: visão dupla; redução da capacidade visual; vermelhidão ocular; olho seco. 
- Ouvido, nariz e garganta: diminuição da capacidade de ouvir; inflamação da mucosa nasal; sangramento pelo 
nariz; edema de glote (reação alérgica, conhecida como “garganta fechada”); boca seca. 
- Sistema cardiovascular: aumento de pressão arterial; infarto do miocárdio; arritmia cardíaca; taquicardia; 
palpitações; insuficiência cardíaca congestiva; acidente vascular cerebral; vasculite. 
- Sistema respiratório: broncoespasmo; chiado no peito; falta de ar; dor torácica. 
Informe ao seu médico, cirurgião-dentista ou farmacêutico o aparecimento de reações indesejáveis pelo 
uso do medicamento. Informe também à empresa através do seu serviço de atendimento. 
 
9. O QUE FAZER SE ALGUÉM USAR UMA QUANTIDADE MAIOR DO QUE A INDICADA DESTE 
MEDICAMENTO? 
O tratamento da superdose pelo ibuprofeno é de suporte, uma vez que não existem antídotos a este fármaco. Os 
sintomas podem incluir vertigem, movimento ocular involuntário, parada transitória da respiração, inconsciência, 
queda da pressão arterial e insuficiência respiratória. 
Deve-se evitar a provocação de vômitos e a ingestão de alimentos ou bebidas. Procure um serviço médico. 
Em caso de uso de grande quantidade deste medicamento, procure rapidamente socorro médico e leve a 
embalagem ou bula do medicamento, se possível. Ligue para 0800 722 6001, se você precisar de mais 
orientações. 
 
DIZERES LEGAIS 
MS - 1.2568.0219 
Farmacêutico Responsável: Dr. Luiz Donaduzzi  
CRF-PR 5842 
 
Registrado e fabricado por:  
PRATI, DONADUZZI & CIA LTDA 
Rua Mitsugoro Tanaka, 145 
Centro Industrial Nilton Arruda - Toledo - PR 
CNPJ 73.856.593/0001-66 
Indústria Brasileira 
 
CAC - Centro de Atendimento ao Consumidor  
0800-709-9333 
cac@pratidonaduzzi.com.br 
www.pratidonaduzzi.com.br 
 
Siga corretamente o modo de usar; não desaparecendo os sintomas, procure orientação médica. 
 
 

                         



 
 

 

5 
 

 
 Anexo B 

 
Histórico de alteração para a bula 

 
 

Dados da submissão eletrônica Dados da petição/notificação que altera bula Dados das alterações de bulas 

Data do  

expediente 
No. expediente Assunto 

Data do  

expediente 
N° do expediente Assunto 

Data de  

aprovação 
Itens de bula 

Versões 

(VP/VPS) 

Apresentações  

relacionadas 

- - 
10452 – GENÉRICO – 

Notificação de Alteração de 

Texto de Bula – RDC 60/12 

- - - - 

3. QUANDO NÃO DEVO USAR 
ESTE MEDICAMENTO? 

 

VP Suspensão oral de 50 
mg/mL 

19/12/2014 1140828/14-6 
10459 – GENÉRICO 

Inclusão Inicial de Texto de 

Bula 

- - - - - - - 

 
 
 
 
 
 
 

 


''')


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
    matcher2.add("excipiente", [pattern2])

    for match_id, start, end in matcher(doc):
        match_text = doc[start:end].text
        print(f"Encontrado padrão 1: '{match_text}'. Início: {start}. Fim: {end}")
        print(matcher(doc)[-1][2], "próximo token após o padrão:", doc[matcher(doc)[-1][2] + 1].text)

    for match_id, start, end in matcher2(doc):
        match_text2 = doc[start:end].text
        print(f"Encontrado padrão 2: '{match_text2}'. Início: {start}. Fim: {end}")

        indice_token_anterior = matcher2(doc)[-1][2] - 1

        if indice_token_anterior >= 0:
            token_anterior = doc[indice_token_anterior]
            print(f"Token anterior: {token_anterior.text}")
        else:
            print("Não há token anterior, pois o último token é o primeiro token do documento.")


    indice_fim_primeiro_padrao = matcher(doc)[-1][2]
    indice_inicio_segundo_padrao = matcher2(doc)[0][1]
    span_entre_padroes = doc[indice_fim_primeiro_padrao:indice_inicio_segundo_padrao]  # .text.split('\n')
    # print('Span entre padrões:', span_entre_padroes)

    list_final = []
    for t in span_entre_padroes:
        if (not t.is_punct
            and not t.is_digit
            and not t.is_currency
            and not t.text.__contains__('\n')
            and not t.is_stop
            and not t.is_space
            and t.text.lower() not in LeafletSection().measures_units
        ):


            list_final.append(t.text)


        # if s.root.text != 'contém' and not s.root.is_ancestor(s[0]):
        #     print('Toda sentença:', [c for c in s.noun_chunks])

        # if s.root.text == 'contém' and s.root.is_ancestor(s[0]):  # or s.root.lemma_ == 'conter':
        #     print('NOMES', [i for i in s.noun_chunks])
        #     print(next(s.root.children))
        #
        # print(i+1,s)
        # for c in s.noun_chunks:
        #     if not any(value in c.text for value in LeafletSection().measures_units):
        #         print(c.text)
    print(list_final)
    print("Span entre padrões:", span_entre_padroes)


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




