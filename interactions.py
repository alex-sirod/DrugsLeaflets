from collections import Counter
from datasources import atc_reference
from datasources.leaflets_section import LeafletMetadata
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
        self.excipients = self.leaflet.get_excipients()[1]
        self.composition = self.leaflet.get_composition()
        self.stoplist_interactions = LeafletMetadata().stoplist_interactions

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

                        # Y = [a.text for a in self.doc[nc.start:nc.end].as_doc() if a.text == 'eles']
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


###### ESTAS FUNÇÕES NÃO PERTENCEM A CLASSE INTERACTIONPARSER, MAS ESTÃO AQUI POR ENQUANTO ########
def get_group_atc_code(code_atc):
    """ Return the ATC code of the drug. """
    # print(code_atc)
    if len(code_atc) < 4:
        return f"Código ATC {code_atc} inválido! Deve ter ao menos 4 caracteres."
    else:

        first_level = code_atc[0]
        second_level = code_atc[1:3]
        third_level = code_atc[3]
        # print(first_level, second_level, third_level)
        result0 = atc_reference.ATC[first_level][0][second_level][0]
        result1 = result0 + ", " + "".join(atc_reference.ATC[first_level][0][second_level][1][third_level])
        # print(result0)
        # print(result1)
        return [r for r in result1.split(", ") if r != ""]


def get_similarity_lists(sim_leaflet1, sim_leaflet2):
    """ Return the similarity index between two leaflets. """
    # Get the interactions flags of each leaflet
    interactions_flags1 = sim_leaflet1.get_interactions_flags()
    interactions_flags2 = sim_leaflet2.get_interactions_flags()
    # print("interactions_flags1", interactions_flags1)
    # print("interactions_flags2", interactions_flags2)
    # Get the ATC code of each leaflet
    atc_code1 = sim_leaflet1.get_atc_code()[1]
    atc_code2 = sim_leaflet2.get_atc_code()[1]
    # Get drug name
    drug_name1 = sim_leaflet1.get_atc_code()[0]
    drug_name2 = sim_leaflet2.get_atc_code()[0]

    # Get excipients
    excipients1 = sim_leaflet1.excipients
    excipients2 = sim_leaflet2.excipients
    print("excipients1", excipients1)
    print("excipients2", excipients2)

    #Get composition
    composition1 = sim_leaflet1.composition
    composition2 = sim_leaflet2.composition
    print("composition1", composition1)
    print("composition2", composition2)

    # Get group ATC code
    group_atc_code1 = get_group_atc_code(atc_code1)
    group_atc_code1.extend(excipients1)
    group_atc_code1.extend(composition1)

    group_atc_code2 = get_group_atc_code(atc_code2)
    group_atc_code2.extend(excipients2)
    group_atc_code2.extend(composition2)
    # print("group_atc_code1", group_atc_code1)
    # print("group_atc_code2", group_atc_code2)





    return (atc_code1, drug_name1, interactions_flags1, group_atc_code1,
            drug_name2, atc_code2, interactions_flags2, group_atc_code2)


if __name__ == '__main__':
    leaflet1 = InteractionParser(r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf')
    leaflet2 = InteractionParser(r'datasources/leaflets_pdf/bula_1700662857659_Ibuprofeno.pdf')
    # leaflet.get_interactions_flags()
    # leaflet2.get_whats_is()
    # leaflet2.dependency_drug()
    # print(f"Nome na Bula : {leaflet1.drug_name}")
    # print(f"Código ATC {leaflet1.get_atc_code()[0]}: {leaflet1.get_atc_code()[1]}")
    # print(f"Nome na Bula : {leaflet2.drug_name}")
    print(f"Código ATC {leaflet2.get_atc_code()[0]}: {leaflet2.get_atc_code()[1]}")
    # print(get_similarity_index(leaflet1, leaflet2))
    # print(get_group_atc_code("A0"))
    # print(get_group_atc_code(leaflet2.get_atc_code()[1]))

    for i in get_similarity_lists(leaflet1, leaflet2):
        print(i)
