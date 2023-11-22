import re
from collections import Counter

import PyPDF2
import spacy
from spacy.matcher import Matcher
from spacy.matcher import PhraseMatcher
from tika import parser

from datasources.leaflets_section import LeafletSection

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
        self.manufacturer = self.get_manufacturer()
        self.file_name_txt = 'sample.txt'
        self.doc_test = nlp(u'''APRESENTAÇÃO
Pó para suspensão oral de 250 mg/5 mL: embalagem com frasco contendo pó para reconstituição de 150 mL de suspensão acompanhado de uma seringa dosadora de 10 mL.
USO ORAL
USO ADULTO E PEDIÁTRICO
COMPOSIÇÃO 
Cada 5 mL de suspensão oral contém:
amoxicilina tri-hidratada (equivalente a 250 mg de amoxicilina) ............................................................. 287,0 mg
Excipientes: sorbitol, dióxido de silício, celulose microcristalina, crospovidona, goma xantana, aspartamo, ciclamato de sódio, sacarina sódica di-hidratada, ácido cítrico, citrato de sódio, propilparabeno, metilparabeno, benzoato de sódio, aroma de laranja e estearato de magnésio.
II – INFORMAÇÕES AO PACIENTE
1. PARA QUE ESTE MEDICAMENTO É INDICADO?''')

    def get_text_1(self):

        pattern_end_of_text = r"(?i)\bhist[oó]rico de altera[çc][õo]es da bula\b"
        pattern_end_of_text2 = r"(?i)\Hist[oó]rico de altera[çc][õo]es do texto de bula\b"

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
        the_end = ['Histórico de Alterações da Bula',
                   'Histórico de Alterações do Texto de Bula'
                   ]
        try:
            parsed_pdf = parser.from_file(self.file_name_leaflet)
            data_prev = parsed_pdf['content']
            data_next = ""

            for i in the_end:
                if i in data_prev:
                    data_prev = data_prev.split(i, 1)[0]
                    break
            # print(data_prev)
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
        aux_list = ["registrado por", "fabricado por", "importado por", "distribuído por", "embalado por",]
        manufacturers = []
        for entity in self.doc.ents:
            if entity.label_ == 'ORG' and entity.start != 0:
                e = entity.text.split('\n')[0]
                manufacturers.append(e.strip())
            if entity.label_ == 'ORG' and entity.start != 0:
                prev_token = self.doc[entity.start - 4:entity.start - 2].text.lower()
                if prev_token in aux_list:
                    e = entity.text.split('\n')[0]
                    manufacturers.append(e.strip())
                # print(prev_token, entity.text)

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

                print(f'File {self.file_name_leaflet} The page {number_page} has been extracted to text object')
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
        #print(span_entre_padroes)
        for i in span_entre_padroes:
            if i.islower():
                # print("NOME DO MEDICAMENTO:", i)

                # print("Span entre padrões:", span_entre_padroes)
                return i.strip()

    def get_entity(self):
        for entity in self.doc.ents:
            print(entity.text, entity.label_)

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
                    ]
        pattern2 = nlp("5. ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO?")


        for pattern in pattern1:
            matcher.add("interaction", [pattern])

        matcher2.add("end_interaction", [pattern2])

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

        # print("------------------INICIO DE INTERAÇÕES---------------\n", self.doc[span.start:span2.start].text,
        #       "\n----------------FIM DE INTERAÇÕES-----------------")
        return [s for s in self.doc[span.start:span2.start].sents][:-2]
        # [:-2] para retirar os tokens "5" e ".", que  é o início da próxima frase após o padrão "Interações medicamentosas"

    def get_definition_drug_section(self):
        global span, span2
        span = None
        span2 = None

        matcher = PhraseMatcher(nlp.vocab)
        matcher2 = PhraseMatcher(nlp.vocab)

        pattern1 = [nlp("PARA QUE ESTE MEDICAMENTO É INDICADO?"),]
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
                # s2 = re.sub(r'\n', '', s.lemma_).replace("\n", "")
                excipients = re.sub(r'\s*,\s*|\s* e \s*|\n', ',', s.text.split('Excipientes: ', 1)[1])
                excipients = excipients.split('.', 1)[0]
                excipients_list = [i for i in excipients.split(',') if i not in list_empty]
                break

        return excipients_list, len(excipients_list)

    def get_composition(self):
        matcher = Matcher(nlp.vocab)
        pattern = [{"lower": "contém"}, {'lower': ':'}]
        matcher.add("composicao_medicamento", [pattern])

        matcher2 = Matcher(nlp.vocab)
        pattern2 = [{"lower": {"in": ["excipientes"]}}]
        matcher2.add("excipiente", [pattern2])

        ind_end_first_pattern = matcher(self.doc)[-1][2]
        ind_start_second_pattern = matcher2(self.doc)[0][1]
        span_between_patterns = self.doc[ind_end_first_pattern:ind_start_second_pattern]  # .text.split('\n')

        for i, s in enumerate(span_between_patterns.sents):
            if s.root.text != 'contém' and not s.root.is_ancestor(s[0]):
                ingredients = [c for c in s.noun_chunks if not any(
                    value in c.text for value in LeafletSection().measures_units)]
                return dict(ingredients=ingredients)



if __name__ == '__main__':
    # leaflet = Leaflet('leaflets_pdf/bula_1689362421673.pdf') # amoxicilina
    leaflet2 = Leaflet('leaflets_pdf/bula_1697765645208 - Heparina Sódica Bovina.pdf')

    leaflet3 = Leaflet(r'leaflets_pdf/bula_1689362421673 - Amoxicilina.pdf')
    leaflet4 = Leaflet(r'leaflets_pdf/bula_1699032061377 - tigeciclina.pdf')
    # leaflet3.save_text()
    #print(leaflet3.get_drug_name())
    # print(leaflet3.get_text_from_page(2))
    # leaflet4.most_common_words()
    # leaflet3.get_interactions_flags()
    # print(leaflet3.get_composition())
    # print(leaflet3.get_attributes())
    # leaflet3.get_interactions_section()
    # leaflet3.get_definition_drug_section()
    # print(leaflet3.get_manufacturer())
    print(leaflet3.get_excipients())
    # print(leaflet3.get_composition())
    # print(leaflet3.get_drug_name())
    # print(leaflet3.get_manufacturer())
    # print(leaflet4.get_drug_name())
    # print(leaflet4.get_manufacturer())
    print(leaflet4.get_excipients())
    print(leaflet2.get_excipients())
    #print(leaflet4.get_composition())
