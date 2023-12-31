import re
from collections import Counter

import PyPDF2
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from tika import parser

from datasources import leaflets_section
from datasources.leaflets_section import LeafletMetadata

nlp = spacy.load('pt_core_news_lg')


class Leaflet:
    """
    Class to extract text from pdf leaflets.
    This class receive a pdf file and extract the text from it and save it in a txt file
    To initialize this class you need to pass the leaflet pdf file name how
    argument to the constructor in string format.

    """

    def __init__(self, file_name_leaflet):
        print(f'Initializing Leaflet class with file {file_name_leaflet}')

        self.file_name_leaflet = file_name_leaflet

        self.text = self.get_text()
        self.doc = self.get_doc()
        # self.manufacturer = self.get_manufacturer()
        self.file_name_txt = 'sample.txt'


    def get_text_full(self):

        pattern_end_of_text = r"(?i)\bhist[oó]rico de altera[çc][õo]es da bula\b"
        pattern_end_of_text2 = r"(?i)\Hist[oó]rico de altera[çc][õo]es do texto da bula\b"

        with open(self.file_name_leaflet, 'rb') as leaflet_file:
            reader = PyPDF2.PdfReader(leaflet_file)
            if len(reader.pages) > 0:
                text_readed = ''
                for page_number in range(len(reader.pages)):
                    page = reader.pages[page_number]
                    # Extract the text from current page
                    text_readed += page.extract_text()
                    # if end_of_text in text_readed.lower():

                    if re.search(pattern_end_of_text, text_readed):
                        break
                print(f'File {self.file_name_leaflet} has been extracted to text object')
                return text_readed
            else:
                return None

    def get_text(self):
        print("Start extraction...")
        list_the_end = ['histórico de alterações da bula', 'histórico de alteração da bula',
                        'histórico de alterações do texto de bula', "histórico de alteração do texto de bula",
                        'histórico de alterações para a bula', 'histórico de alteração para a bula'
                        ]
        try:
            parsed_pdf = parser.from_file(self.file_name_leaflet)
            data_prev = parsed_pdf['content']

            for line in data_prev.splitlines():
                if any(item in line.lower() for item in list_the_end):
                    data_prev = data_prev.split(line, 1)[0]
                    print("Extraction finished!")
                    break

            return data_prev
        except FileNotFoundError:
            print(f'File {self.file_name_leaflet} not found')
            return None

    def save_text(self):

        with open(self.file_name_txt, 'w', encoding='UTF-8') as txt_file:
            txt_file.write(self.get_text())
        print(f'File {self.file_name_leaflet} has been extracted to {self.file_name_txt}')

    def get_doc(self):

        # nlp = spacy.load('pt_core_news_lg')
        doc = nlp(self.text)
        return doc

    def get_manufacturer(self):
        """
        This method extract the manufacturer from the leaflet
        based on the patterns and selects the Entity Named by majority vote
        """

        page_one = self.get_text_from_page(1).text.lower()
        name_drug = self.get_drug_name().lower()
        aux_list = ["registrado por", "fabricado por", "importado por", "distribuído por", "embalado por",
                    "s/a", "s.a.", "indústria brasileira", "indústria nacional", "indústria estrangeira",
                    "ltda", "indústria"
                    ]
        manufacturers = []
        for entity in self.doc.ents:
            if entity.label_ == 'ORG':  # one vote for each entity
                e = entity.text.split('\n')[0]
                manufacturers.append(e.strip())
            if entity.label_ == 'ORG' and entity.start != 0:  # one vote for each entity
                prev_token = self.doc[entity.start - 4:entity.start - 2].text.lower()
                # print(prev_token, entity.text)
                if prev_token in aux_list:
                    e = entity.text.split('\n')[0]
                    manufacturers.append(e.strip())
                    # print(prev_token, entity.text)
                    # print("o termo é uma entidade:", entity.text.lower().split('\n')[0], "fim")

            if entity.label_ == 'ORG' and entity.start != 0:  # one vote for each entity
                prev_token = self.doc[entity.start - 3:entity.start - 1].text.lower()
                # print(prev_token, entity.text)
                if prev_token in aux_list:
                    e = entity.text.split('\n')[0]
                    manufacturers.append(e.strip())
                    # print(prev_token, entity.text)
                    # print("o termo é uma entidade:", entity.text.lower().split('\n')[0], "fim")

                # print(prev_token, entity.text)
            if entity.label_ == 'ORG':  # two votes for each entity
                # print("o termo é uma entidade", entity.text.lower().split('\n')[0])
                if entity.text.lower().split('\n')[0] in page_one and entity.text.lower() != name_drug:
                    # print("o termo está na página 1 ------------------>", entity.text)
                    for _ in range(2):
                        e = entity.text.split('\n')[0]
                        manufacturers.append(e.strip())
            #
            if entity.label_ == 'ORG' and entity.start != 0:  # one vote for each entity
                if any(subst in entity.lemma_.lower() for subst in aux_list):
                    # print("o termo contem S/A", entity.text)
                    manufacturers.append(e.strip())

        word_freq = Counter(manufacturers)
        common_words = word_freq.most_common(15)
        # print(common_words)

        if manufacturers:
            return common_words[0][0]
        else:
            return "Não encontrado"

    def get_text_from_page(self, number_page):
        with open(self.file_name_leaflet, 'rb') as leaflet_file:
            reader = PyPDF2.PdfReader(leaflet_file)
            if len(reader.pages) > 0:
                text_readed = ''
                for page_number in range(len(reader.pages)):
                    page = reader.pages[page_number]
                    # Extract the text from current page
                    if page_number == number_page - 1:
                        text_readed += page.extract_text()

                # print(f'File {self.file_name_leaflet} - page {number_page}')
                doc_pag = nlp(text_readed)

                return doc_pag
            else:
                return None

    def get_patterns_template(self):  # template para criar novos padrões
        matcher = Matcher(nlp.vocab)
        pattern = [{"text": "IDENTIFICAÇÃO"}, {"text": "DO"}, {"text": "MEDICAMENTO"}, ]
        matcher.add("identificacao_medicamento", [pattern])

        matcher2 = Matcher(nlp.vocab)
        pattern2 = [{"text": "APRESENTAÇ ÃO"}, ]
        matcher2.add("apresentacao", [pattern2])

        for match_id, start, end in matcher(self.doc):
            match_text = self.doc[start:end].text
            print(f"Encontrado padrão: '{match_text}'. Início: {start}. Fim: {end}")
            print(matcher(self.doc)[-1][2], "próximo token após o padrão", self.doc[matcher(self.doc)[-1][2] + 1].text)

        for match_id, start, end in matcher2(self.doc):
            match_text2 = self.doc[start:end].text
            print(f"Encontrado padrão: '{match_text2}'. Início: {start}. Fim: {end}")

            indice_token_anterior = matcher2(self.doc)[-1][2] - 1

            if indice_token_anterior >= 0:
                token_anterior = self.doc[indice_token_anterior]
                print(f"Token anterior: {token_anterior.text}")
            else:
                print("Não há token anterior, pois o último token é o primeiro token do documento.")

        # find the span between the patterns
        indice_fim_primeiro_padrao = matcher(self.doc)[-1][2]
        indice_inicio_segundo_padrao = matcher2(self.doc)[0][1]
        span_entre_padroes = self.doc[indice_fim_primeiro_padrao:indice_inicio_segundo_padrao].text.split('\n')
        for i in span_entre_padroes:
            if i.islower():
                print("NOME DO MEDICAMENTO:", i)

                print("Span entre padrões:", span_entre_padroes)

    def get_drug_name(self):

        doc = self.get_text_from_page(2)

        matcher = Matcher(nlp.vocab)
        pattern = [{"lemma": {"in": ["APRESENTAÇÕES", "APRESENTAÇÃO",
                                     "APRESENTAÇ"]}}, ]  # TODO criar dicionário com as variações de "apresentação"

        matcher.add("apresentacao", [pattern])

        for match_id, start, end in matcher(doc):
            match_text = doc[start:end].text
            # print(f"Encontrado padrão: '{match_text}'. Início: {start}. Fim: {end}")

        indice_token_anterior = matcher(doc)[-1][2] - 2

        span_entre_padroes = doc[0:indice_token_anterior].text.split('\n')
        # print(span_entre_padroes)
        for i in span_entre_padroes:
            if i.islower():
                # print("NOME DO MEDICAMENTO:", i)

                # print("Span entre padrões:", span_entre_padroes)
                return i.strip()

    def get_entity(self):
        for entity in self.doc.ents:
            if entity.label_ == "ORG":
                print(f"Entidade: {entity.text}, Rótulo: {entity.label_}")

    def most_common_words(self):
        char_list = [' \n', '\n\n', '\n \n', ' \n \n']
        # char_list = []
        words = [token.text for token in self.doc
                 if
                 not token.is_stop
                 and not token.is_punct
                 and token.text not in char_list
                 and not token.is_space
                 ]
        entity = [entity.text for entity in self.doc.ents if entity.label_ != 'ORG' and entity.label_ != 'PER']
        word_freq = Counter(words)
        common_words = word_freq.most_common(15)
        print(common_words)

    def table_tokens(self):
        for token in self.doc:
            print("{:>20}{:>20}{:>10}{:>15}{:>10}{:>5}{:>5}{:>5}".format(
                token.text, "lemma:" + token.lemma_, token.pos_, token.tag_, token.dep_, token.shape_, token.is_alpha,
                token.is_stop))

    def chunking(self):  # use this method to detection Noun Phrases
        counter = 0
        for chunk in self.doc.noun_chunks:

            print("chunk: {:30} head: {:20} root:{:20}".format(chunk.text,
                                                               chunk.root.text,
                                                               # chunk.root.dep_,
                                                               chunk.root.head.text
                                                               )
                  )
            counter += 1
            if counter > 50:
                break

    def phrase_pat(self):

        matcher = PhraseMatcher(nlp.vocab)

        pattern = nlp("Golden Retriever")
        matcher.add("DOG", [pattern])
        doc = nlp("I have a Golden Retriever")

        # Iterar nas correspondências
        for match_id, start, end in matcher(doc):
            # Obter a partição que houve correspondência
            span = doc[start:end]
            print("Matched span:", span.text)

    def get_sentence(self):
        l_sentences = []
        counter = 0
        for sent in self.doc.sents:
            counter += 1
            # print("{:5} ->>> {:20}".format(counter, sent.text))
            l_sentences.append(sent.text)
        return l_sentences

    def get_interactions_section_sents(self):
        global span, span2
        matcher = PhraseMatcher(nlp.vocab)
        matcher2 = PhraseMatcher(nlp.vocab)

        pattern1 = [nlp("Interações medicamentosas"),
                    nlp("INTERAÇÕES MEDICAMENTOSAS"),
                    nlp("Interações Medicamentosas"),
                    nlp("Interações com medicamentos"),
                    nlp("interações com medicamentos"),
                    nlp("interações com outros medicamentos"),
                    nlp("Interações com outros medicamentos"),
                    nlp("QUE DEVO SABER ANTES DE USAR ESTE MEDICAMENTO?")
                    ]
        pattern2 = [nlp("5. ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO?"),
                    nlp("ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO"),
                    nlp("ONDE, COMO E POR QUANTO"),
                    ]

        for p1 in pattern1:
            matcher.add("interaction", [p1])

        for p2 in pattern2:
            matcher2.add("end_interaction", [p2])


        # Iterar nas correspondências

        for phrase_id, start, end in matcher(self.doc):
            # Obter a partição que houve correspondência

            span = self.doc[start:end]



            # span = self.doc[start:end]
            # print("Matched span:", span.text)
            # print(f"Encontrado padrão: '{phrase_id}'. Início: {start}. Fim: {end}")
            # print(matcher(self.doc)[-1][2], "Início da próxima frase após o padrão: \"" +
            #       self.doc[matcher(self.doc)[-1][2] + 1].text, "...\"")
            # if span:  # TODO verificar se o span é um início de sentença ou título
            #     break

        for phrase_id2, start2, end2 in matcher2(self.doc):
            span2 = self.doc[start2:end2]
            # print("Matched span:", span2.text)
            # print(f"Encontrado padrão: '{phrase_id2}'. Início: {start2}. Fim: {end2}")

        # print("------------------INICIO DE INTERAÇÕES---------------\n", self.doc[span.start:span2.start].text,
        #       "\n----------------FIM DE INTERAÇÕES-----------------")
        print("Drug Interactions Section successfully extracted!")
        # print([s for s in self.doc[span.start:span2.start].sents][:-2])
        return [s for s in self.doc[span.start:span2.start].sents][:-2]
        # [:-2] para retirar os tokens "5" e ".", que  é o início da próxima frase após o padrão "Interações medicamentosas"

    def get_definitions_section_sents(self):
        global span, span2
        span = None
        span2 = None

        matcher = PhraseMatcher(nlp.vocab)
        matcher2 = PhraseMatcher(nlp.vocab)

        pattern1 = [nlp("PARA QUE ESTE MEDICAMENTO É INDICADO?"), ]
        pattern2 = nlp("QUANDO NÃO DEVO USAR ESTE MEDICAMENTO?")

        for pattern in pattern1:
            matcher.add("definition", [pattern])

        matcher2.add("end_definition", [pattern2])

        # Iterar nas correspondências
        for phrase_id, start, end in matcher(self.doc):
            # Obter a partição que houve correspondência
            span = self.doc[start:end]
            # print("Matched span:", span.text)
            # print(f"Encontrado padrão: '{phrase_id}'. Início: {start}. Fim: {end}")
            # print(matcher(self.doc)[-1][2], "Início da próxima frase após o padrão: \"" +
            #       self.doc[matcher(self.doc)[-1][2] + 1].text, "...\"")
            # if span:  # TODO verificar se o spn é um início de sentença ou título
            #     break
        for phrase_id, start, end in matcher2(self.doc):
            span2 = self.doc[start:end]
            # print("Matched span:", span2.text)
            # print(f"Encontrado padrão: '{phrase_id}'. Início: {start}. Fim: {end}")

        # print("------------------INICIO DE DEFINIÇÃO    ---------------\n", self.doc[span.start-2:span2.start -2 ].text,
        #       "\n----------------FIM DE DEFINIÇÃO -----------------")
        print("Medicine Characterization Section extracted successfully!")
        return [s for s in self.doc[span.start:span2.start].sents][:-2]
        # [:-2] para retirar os tokens "5" e ".", que  é o início da próxima frase após o padrão "Interações medicamentosas"

    def get_metadata(self):
        # tika.initVM()
        try:
            parsed_pdf = parser.from_file(self.file_name_leaflet)
            print(parsed_pdf.keys())
            metadata_doc = parsed_pdf['metadata']
            for md in metadata_doc:
                print(md, metadata_doc[md])
                print('-------------------')
            print(metadata_doc['xmpTPg:NPages'])
            print(metadata_doc['pdf:docinfo:creator'])
            print(metadata_doc[
                      'pdf:overallPercentageUnmappedUnicodeChars'])  # TODO verificar se esse valor é um bom indicador de qualidade do OCR
            print(metadata_doc['pdf:totalUnmappedUnicodeChars'])
            print(metadata_doc['pdf:charsPerPage'])
            print(metadata_doc['access_permission:extract_content'])
            return metadata_doc

        except FileNotFoundError:
            print(f'File {self.file_name_leaflet} not found')
            return None

    def get_excipients(self):
        global excipients_list
        excipients_list = []
        list_empty = ["", " "]
        for s in self.doc.sents:
            if s.lemma_.__contains__('Excipientes') or (s[0].is_title and s[0].lemma_ == 'excipiente'):
                excipients = re.sub(r'\s*,\s*|\s* e \s*|\n', ',', s.text.split('Excipientes: ', 1)[1])
                excipients = excipients.split('.', 1)[0]
                excipients_list = [i for i in excipients.split(',') if i not in list_empty]
                break
        return len(excipients_list), excipients_list

    def get_composition(self):
        try:
            matcher = Matcher(nlp.vocab)
            matcher2 = Matcher(nlp.vocab)

            pattern = [{"lower": "contém"}, {'IS_PUNCT': True}]
            pattern2 = [{"lower": {"in": ["excipientes"]}}, {'IS_PUNCT': True}]

            matcher.add("composicao_medicamento", [pattern])
            matcher2.add("excipiente", [pattern2])

            ind_end_first_pattern = matcher(self.doc)[-1][2]
            ind_start_second_pattern = matcher2(self.doc)[0][1]
            span_between_patterns = self.doc[ind_end_first_pattern:ind_start_second_pattern]  # .text.split('\n')
            for s in span_between_patterns.sents:
                if s.root.text != 'contém' and not s.root.is_ancestor(s[0]):
                    ingredients = [c.text for c in s.noun_chunks if not any(
                        value in c.text for value in LeafletMetadata().MEASURE_UNITS) and not any(
                        value in c.text for value in LeafletMetadata().PRESENTATION


                    )]
                    if ingredients:
                        return ingredients

                # A second way to get the ingredients whether the first way doesn't work and return an empty list

                ingredients = []
                for t in span_between_patterns:
                    if (not t.is_punct
                            and not t.is_digit
                            and not t.is_currency
                            and not t.text.__contains__('\n')
                            and not t.is_stop
                            and not t.is_space
                            and t.text.lower() not in LeafletMetadata().MEASURE_UNITS
                            and t.text.lower() not in LeafletMetadata().PRESENTATION
                            and t.lemma_ not in LeafletMetadata().MEASURE_UNITS
                            and t.lemma_ not in LeafletMetadata().PRESENTATION):
                        ingredients.append(t.text)
                return ingredients
        except IndexError:
            return ["Não possível extrair a composição do medicamento"]


    def aux_get_composition(self):
        matcher = Matcher(nlp.vocab)
        matcher2 = Matcher(nlp.vocab)

        pattern = [{'LOWER': 'contém'}, {'IS_PUNCT': True}]
        pattern2 = [{"lower": {"in": ["excipientes"]}}, {'IS_PUNCT': True}]

        matcher.add("composicao_medicamento", [pattern])
        matcher2.add("excipiente", [pattern2])
        for match_id, start, end in matcher(self.doc):
            match_text = self.doc[start:end].text
            # print(f"Encontrado padrão 1: '{match_text}'. Início: {start}. Fim: {end}")
            # print(matcher(self.doc)[-1][2], "próximo token após o padrão:", self.doc[matcher(self.doc)[-1][2] + 1].text)
        indice_fim_primeiro_padrao = matcher(self.doc)[-1][2]
        indice_inicio_segundo_padrao = matcher2(self.doc)[0][1]
        span_entre_padroes = self.doc[indice_fim_primeiro_padrao:indice_inicio_segundo_padrao]  # .text.split('\n')
        # print('Span entre padrões:', span_entre_padroes)

        list_final = []
        for t in span_entre_padroes:
            if (not t.is_punct
                    and not t.is_digit
                    and not t.is_currency
                    and not t.text.__contains__('\n')
                    and not t.is_stop
                    and not t.is_space
                    and t.text.lower() not in LeafletMetadata().MEASURE_UNITS
                    and t.text.lower() not in LeafletMetadata().PRESENTATION
                    and t.lemma_ not in LeafletMetadata().MEASURE_UNITS
                    and t.lemma_ not in LeafletMetadata().PRESENTATION):
                list_final.append(t.text)
        # print("Span entre padrões:", span_entre_padroes)
        # print(list_final)
        return list_final


if __name__ == '__main__':
    leaflet1 = Leaflet('datasources/leaflets_pdf/bula_1700662857659_ibuprofeno.pdf')  # ibuprofeno
    print("Drug name:", leaflet1.get_drug_name())
    print("Manufacturer:", leaflet1.get_manufacturer())
    print("Excipients:", leaflet1.get_excipients())
    print("Composition:", leaflet1.get_composition())
    leaflet1.get_interactions_section_sents()
    leaflet1.get_definitions_section_sents()



    # # leaflet1.get_definition_drug_section()
    # print("-------------------------------------------------------------------")
    #
    # leaflet2 = Leaflet(r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf')
    # print("Drug name:", leaflet2.get_drug_name())
    # print("Manufacturer:", leaflet2.get_manufacturer())
    # print("Excipients:", leaflet2.get_excipients())
    # print("Composition:", leaflet2.get_composition())
    # leaflet2.get_interactions_section_sents()
    # leaflet2.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    #
    # leaflet3 = Leaflet(r'datasources/leaflets_pdf/bula_1700827705685_Omeprazol.pdf')
    # print("Drug name:", leaflet3.get_drug_name())
    # print("Manufacturer:", leaflet3.get_manufacturer())
    # print("Excipients:", leaflet3.get_excipients())
    # print("Composition:", leaflet3.get_composition())
    # leaflet3.get_interactions_section_sents()
    # leaflet3.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet4 = Leaflet(r'datasources/leaflets_pdf/bula_1701258821940_enalapril.pdf')
    # print("Drug name:", leaflet4.get_drug_name())
    # print("Manufacturer:", leaflet4.get_manufacturer())
    # print("Excipients:", leaflet4.get_excipients())
    # print("Composition:", leaflet4.get_composition())
    # leaflet4.get_interactions_section_sents()
    # leaflet4.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet5 = Leaflet(r'datasources/leaflets_pdf/bula_1701224846500_Hidroclorotiazida.pdf')
    # print("Drug name:", leaflet5.get_drug_name())
    # print("Manufacturer:", leaflet5.get_manufacturer())
    # print("Excipients:", leaflet5.get_excipients())
    # print("Composition:", leaflet5.get_composition())
    # leaflet5.get_interactions_section_sents()
    # leaflet5.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet6 = Leaflet(r'datasources/leaflets_pdf/bula_1701224202414_Sulfametoxazol.pdf')
    # print("Drug name:", leaflet6.get_drug_name())
    # print("Manufacturer:", leaflet6.get_manufacturer())
    # print("Excipients:", leaflet6.get_excipients())
    # print("Composition:", leaflet6.get_composition())
    # leaflet6.get_interactions_section_sents()
    # leaflet6.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet7 = Leaflet(r'datasources/leaflets_pdf/bula_1701225057399_Acido_acetilsalicílico.pdf')
    # print("Drug name:", leaflet7.get_drug_name())
    # print("Manufacturer:", leaflet7.get_manufacturer())
    # print("Excipients:", leaflet7.get_excipients())
    # print("Composition:", leaflet7.get_composition())
    # leaflet7.get_interactions_section_sents()
    # leaflet7.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # # # OBS: REMDESIVIR NÃO ESTÁ NA RENAME 2022, inviabilizando a implementação do método get_atc()
    # leaflet8 = Leaflet(r'datasources/leaflets_pdf/bula_1701267803044_Remdesivir.pdf')
    # print("Drug name:", leaflet8.get_drug_name())
    # print("Manufacturer:", leaflet8.get_manufacturer())
    # print("Excipients:", leaflet8.get_excipients())
    # print("Composition:", leaflet8.get_composition())
    # leaflet8.get_interactions_section_sents()
    # leaflet8.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet9 = Leaflet(r'datasources/leaflets_pdf/bula_1701260642978_captopril.pdf')
    # print("Drug name:", leaflet9.get_drug_name())
    # print("Manufacturer:", leaflet9.get_manufacturer())
    # print("Excipients:", leaflet9.get_excipients())
    # print("Composition:", leaflet9.get_composition())
    # leaflet9.get_interactions_section_sents()
    # leaflet9.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet10 = Leaflet(r'datasources/leaflets_pdf/bula_1701263093335_Digoxina.pdf')
    # print("Drug name:", leaflet10.get_drug_name())
    # print("Manufacturer:", leaflet10.get_manufacturer())
    # print("Excipients:", leaflet10.get_excipients())
    # print("Composition:", leaflet10.get_composition())
    # leaflet10.get_interactions_section_sents()
    # leaflet10.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # #
    # leaflet11 = Leaflet(r'datasources/leaflets_pdf/bula_1701264125049_Albendazol.pdf')
    # print("Drug name:", leaflet11.get_drug_name())
    # print("Manufacturer:", leaflet11.get_manufacturer())
    # print("Excipients:", leaflet11.get_excipients())
    # print("Composition:", leaflet11.get_composition())
    # leaflet11.get_interactions_section_sents()
    # leaflet11.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    #
    # leaflet12 = Leaflet(r'datasources/leaflets_pdf/bula_1701266245626_Diazepam.pdf')
    # print("Drug name:", leaflet12.get_drug_name())
    # print("Manufacturer:", leaflet12.get_manufacturer())
    # print("Excipients:", leaflet12.get_excipients())
    # print("Composition:", leaflet12.get_composition())
    # leaflet12.get_interactions_section_sents()
    # leaflet12.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # # #
    # leaflet13 = Leaflet(r'datasources/leaflets_pdf/bula_1701267208681_Bissulfato de clopidogrel.pdf')
    # print("Drug name:", leaflet13.get_drug_name())
    # print("Manufacturer:", leaflet13.get_manufacturer())
    # print("Excipients:", leaflet13.get_excipients())
    # print("Composition:", leaflet13.get_composition())
    # leaflet13.get_interactions_section_sents()
    # leaflet13.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet14 = Leaflet(r'datasources/leaflets_pdf/bula_1701267508373_Fenobarbital.pdf')
    # print("Drug name:", leaflet14.get_drug_name())
    # print("Manufacturer:", leaflet14.get_manufacturer())
    # print("Excipients:", leaflet14.get_excipients())
    # print("Composition:", leaflet14.get_composition())
    # leaflet14.get_interactions_section_sents()
    # leaflet14.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet15 = Leaflet(r'datasources/leaflets_pdf/bula_1701268132552_Dipirona.pdf')
    # print("Drug name:", leaflet15.get_drug_name())
    # print("Manufacturer:", leaflet15.get_manufacturer())
    # print("Excipients:", leaflet15.get_excipients())
    # print("Composition:", leaflet15.get_composition())
    # leaflet15.get_interactions_section_sents()
    # leaflet15.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    #
    # leaflet16 = Leaflet(r'datasources/leaflets_pdf/bula_1701268966313_Budesonida.pdf')
    # print("Drug name:", leaflet16.get_drug_name())
    # print("Manufacturer:", leaflet16.get_manufacturer())
    # print("Excipients:", leaflet16.get_excipients())
    # print("Composition:", leaflet16.get_composition())
    # leaflet16.get_interactions_section_sents()
    # leaflet16.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet17 = Leaflet(r'datasources/leaflets_pdf/bula_1701269088550_Loratadina.pdf')
    # print("Drug name:", leaflet17.get_drug_name())
    # print("Manufacturer:", leaflet17.get_manufacturer())
    # print("Excipients:", leaflet17.get_excipients())
    # print("Composition:", leaflet17.get_composition())
    # leaflet17.get_interactions_section_sents()
    # leaflet17.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet18 = Leaflet(r'datasources/leaflets_pdf/bula_1701266792068_Paracetamol.pdf')
    # print("Drug name:", leaflet18.get_drug_name())
    # print("Manufacturer:", leaflet18.get_manufacturer())
    # print("Excipients:", leaflet18.get_excipients())
    # print("Composition:", leaflet18.get_composition())
    # leaflet18.get_interactions_section_sents()
    # leaflet18.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet19 = Leaflet(r'datasources/leaflets_pdf/bula_1701266990892_Varfarina.pdf')
    # print("Drug name:", leaflet19.get_drug_name())
    # print("Manufacturer:", leaflet19.get_manufacturer())
    # print("Excipients:", leaflet19.get_excipients())
    # print("Composition:", leaflet19.get_composition())
    # leaflet19.get_interactions_section_sents()
    # leaflet19.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet20 = Leaflet(r'datasources/leaflets_pdf/bula_1701224718747_Cefalexina.pdf')
    # print("Drug name:", leaflet20.get_drug_name())
    # print("Manufacturer:", leaflet20.get_manufacturer())
    # print("Excipients:", leaflet20.get_excipients())
    # print("Composition:", leaflet20.get_composition())
    # leaflet20.get_interactions_section_sents()
    # leaflet20.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")
    # #
    # leaflet21 = Leaflet(r'datasources/leaflets_pdf/bula_1701224448044_Trimetoprima.pdf')
    # print("Drug name:", leaflet21.get_drug_name())
    # print("Manufacturer:", leaflet21.get_manufacturer())
    # print("Excipients:", leaflet21.get_excipients())
    # print("Composition:", leaflet21.get_composition())
    # leaflet21.get_interactions_section_sents()
    # leaflet21.get_definitions_section_sents()
    # print("-------------------------------------------------------------------")# TODO verificar porque está retornando uma string vazia
