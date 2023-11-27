from collections import Counter

from drug_leaflet import Leaflet
import spacy
from spacy.matcher import DependencyMatcher
import spacy
import pandas as pd
from spacy.matcher import DependencyMatcher


class InteractionParser:
    """Class to parse interaction data from a file."""

    def __init__(self, leaflet_path):

        self.cod_atc = pd.read_csv("datasources/ATC_small.csv")

        self.leaflet = Leaflet(leaflet_path)

        self.doc = self.leaflet.get_doc()
        self.drug_name = self.leaflet.get_drug_name()

        self.stoplist_interactions = [
            # FRASES sem relevância para a RECUPERAÇÃO
            "Interações medicamentosas", "Interações Medicamentosas",
            "Não há interações medicamentosas descritas para este medicamento",
            "Informe ao seu médico ou cirurgião-dentista se você está fazendo uso de algum outro medicamento.",
            "Não use medicamento sem o conhecimento do seu médico.",
            "Pode ser perigoso para a sua saúde. ",
            # PALAVRAS sem relevância para a RECUPERAÇÃO
            "precaução", "necessário", "adicionais", "efeito", "tratamento", "medicamento",
            "adicional", "refeição", "médico", "cirurgião-dentista", "conhecimento", "Interações medicamentosas",
            "ação", "o gravidez", "gravidez", "amamentação", "criança", "idoso", "uso", "os", "caso", "saúde",
            "pílulas", "indesejável", "indesejáveis", "Pílulas", "interação", "interações", "medicamentoso",
            "ouro","inibidor", "inibidores", "inibidora", "inibidoras", "inibitório", "inibitórios", "inibitória",
            "exame", "exames",  "examinado", "examinada", "examinados", "examinadas", "o exame", "os exames", "fez",
            "seguinte"

        ]

    def get_interactions_flags(self):
        """ Return a bag of words with the most common triggers of interactions.
        a list of tuple words and their frequency.
        """

        global word_freq
        triggers_words_init = []
        triggers_words_temp = []
        clean_sents = []

        for s in self.leaflet.get_interactions_section_sents():
            # print("SENTENÇA ---> ", s.text)
            text = s.text
            if text not in self.stoplist_interactions:
                clean_sents.append(s)
                for token in s:
                    if (token.pos_ == 'NOUN' or token.pos_ == 'ADJ'):
                        if token.lemma_.lower() not in self.stoplist_interactions:
                            # print(token.text, token.lemma_, "está na lista?",
                            #       token.lemma_.lower() in self.stoplist_interactions)
                            triggers_words_init.append(token.lemma_.lower())

                for nc in s.noun_chunks:
                    # print("Noun Chunk ------------> ", nc.root.text, nc.root.dep_, nc.root.head.text)
                    if not any(value in nc.lemma_ for value in self.stoplist_interactions):

                        # print("Noun Chunk na lista ---> ", nc)
                        # print("Text:", nc.text)
                        # print("Root Text:", nc.root.text)
                        # print("Root Dependency Relation:", nc.root.dep_)
                        # print("Start Index:", nc.start)
                        # print("End Index:", nc.end)
                        # print("Sentence:", nc.sent.text)
                        #
                        # print("span", [a for a in self.doc[nc.start:nc.end].as_doc() if not a.is_stop])
                        # print("---")

                        #Y = [a.text for a in self.doc[nc.start:nc.end].as_doc() if a.text == 'eles']
                        # print("X ---> ", x), print("Y ---> ", Y)

                        x = [a.text for a in self.doc[nc.start:nc.end].as_doc() if a.is_stop]
                        if x:
                            triggers_words_temp.append(x[0])
                        triggers_words_init.append(nc.lemma_.lower())

        # print("TRIGGERS WORDS INIT---> ", triggers_words_init)
        # print("TRIGGERS WORDS TEMP ---> ", triggers_words_temp)

        triggers_words_final = [item for item in triggers_words_init if item not in set(triggers_words_temp)]
        if "eles" in triggers_words_final:
            triggers_words_final.remove("eles")  # ??? o termo "eles" não deveria estar na lista
        # print("T1 sem T2 ---> ", triggers_words_final)
        word_freq = Counter(triggers_words_final)
        common_words = word_freq.most_common()
        # print("TRIGGERS WORDS FINAL ---> ", common_words)
        return common_words

    def get_whats_is(self):
        """ Return a list of root words of the noun chunks in the document. self.doc.noun_chunks
        """
        list_whats_is = ["este medicamento", "este remédio",
                         "este produto", "Este medicamento contém",
                         ]
        section_def = self.leaflet.get_definition_drug_section()

    def dependency_drug(self):

        nlp = spacy.load("pt_core_news_sm")
        doc = nlp("A amoxicilina, um antibiótico eficaz contra grande variedade de bactérias.")

        # Encontrar o sujeito (nsubj) e o objeto (obj)
        subject = None
        obj = None
        for s in doc.sents:
            print("SENTENÇA ---> ", s.text)

            for token in s:
                if token.text == self.drug_name:
                    print("SUJEITO:", token.text, token.dep_)
                    print("HEAD:", token.head.text, token.head.pos_, [t for t in token.subtree])


        if "nsubj" in token.dep_:
            subject = " ".join([child.text for child in token.subtree])
        elif "amod" in token.dep_:
            obj = " ".join([child.text for child in token.subtree])

            # Imprimir os resultados
            print(f"Sujeito: {subject}")
            print(f"Objeto: {obj}")


    def get_atc_code(self):
        """ Return the ATC code of the drug. """

        for i in range(len(self.cod_atc)):
            if self.cod_atc.iloc[i, 0].lower() == self.drug_name:
                return self.cod_atc.iloc[i, 0].lower(), self.cod_atc.iloc[i, 1]
    def get_group_atc_code(self):
        """ Return the ATC code of the drug. """

        for i in range(len(self.cod_atc)):
            if self.cod_atc.iloc[i, 0].lower() == self.drug_name:
                return self.cod_atc.iloc[i, 0].lower(), self.cod_atc.iloc[i, 2]


def get_similarity_index(leaflet1, leaflet2):
    """ Return the similarity index between two leaflets. """
    # Get the interactions flags of each leaflet
    interactions_flags1 = leaflet1.get_interactions_flags()
    interactions_flags2 = leaflet2.get_interactions_flags()
    print("interactions_flags1", interactions_flags1)
    print("interactions_flags2", interactions_flags2)
    # Get the ATC code of each leaflet
    atc_code1 = leaflet1.get_atc_code()[1]
    atc_code2 = leaflet2.get_atc_code()[1]
    # Get the definition of each ATC code
    definition1 = leaflet1.leaflet.get_definition_drug_section()
    definition2 = leaflet2.leaflet.get_definition_drug_section()


    # Get the similarity index
    similarity_index = 0
    if atc_code1 != atc_code2:
        similarity_index += 1
    if definition1 == definition2:
        similarity_index += 1
    if interactions_flags1 == interactions_flags2:
        similarity_index += 1

    return similarity_index

if __name__ == '__main__':
    leaflet1 = InteractionParser(r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf')
    leaflet2 = InteractionParser(r'datasources/leaflets_pdf/bula_1700662857659_Ibuprofeno.pdf')
    # leaflet.get_interactions_flags()
    # leaflet3.get_whats_is()
    # leaflet3.dependency_drug()
    print(f"Nome na Bula : {leaflet1.drug_name}")
    print(f"Código ATC {leaflet1.get_atc_code()[0]}: {leaflet1.get_atc_code()[1]}")
    print(f"Nome na Bula : {leaflet2.drug_name}")
    print(f"Código ATC {leaflet2.get_atc_code()[0]}: {leaflet2.get_atc_code()[1]}")
    print(get_similarity_index(leaflet1, leaflet2))
