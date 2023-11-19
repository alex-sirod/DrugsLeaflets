from drug_leaflet import Leaflet
from collections import Counter


class InteractionParser:
    """Class to parse interaction data from a file."""

    def __init__(self, leaflet_path):
        self.leaflet = Leaflet(leaflet_path)
        self.stoplist_interactions = [
            "Não há interações medicamentosas descritas para este medicamento",
            "Informe ao seu médico ou cirurgião-dentista se você está fazendo uso de algum outro medicamento.",
            "Não use medicamento sem o conhecimento do seu médico.",
            "Pode ser perigoso para a sua saúde. ", "Pode ser perigoso para a sua saúde.  5.",
            "precaução", "necessário", "adicionais", "efeito", "tratamento", "medicamento",
            "adicional", "refeição", "médico", "cirurgião-dentista", "conhecimento", "Interações medicamentosas",
            "ação", "o gravidez", "gravidez", "amamentação", "criança", "idoso", "uso", "os", "caso", "saúde", "pílulas"
            "indesejável",
        ]

    def get_interactions_flags(self):
        """Get interactions from a leaflet."""

        global word_freq
        triggers_words = []
        triggers_words2 = []

        for s in self.leaflet.get_interactions_section():
            text = s.text
            if text not in self.stoplist_interactions:
                triggers_words.append(s.text)
                lista_sem_n = [s.replace('\n', '').strip() for s in triggers_words]

        # for i, v in enumerate(lista_sem_n):
        #     print(i, "|" + v + "|")
        print(triggers_words)
        #print(lista_sem_n)|
            # print("FRASE ---> ", s, s.root.text, s.root.dep_, s.root.head.text)
            # for c in s.noun_chunks:
            #     print("Noun Chunk ---> ", c, "[ROOT]->", c.root.text, "[DEPEND]->", c.root.dep_, "[HEAD]->",
            #           c.root.head.text)

            # print("---------- início da sentença -----------")
            # print("VERBOS ---> ", [token for token in s if token.pos_ == 'VERB'])
            # print("VERBOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'VERB'])
            # print("SUBSTANTIVOS ---> ", [token for token in s if token.pos_ == 'NOUN'
            #                              and token.lemma_ not in self.stoplist_interactions])
            # print("SUBSTANTIVOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'NOUN'])
            # print("ADJETIVOS ---> ", [token for token in s if token.pos_ == 'ADJ'])
            # print("ADJETIVOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'ADJ'])
            # print("PREPOSIÇÕES ---> ", [token for token in s if token.pos_ == 'ADP'])
            # print("ADVÉRBIOS ---> ", [token for token in s if token.pos_ == 'ADV'])
            # print("PRONOMES ---> ", [token for token in s if token.pos_ == 'PRON'])
            # print("CONJUNÇÕES ---> ", [token for token in s if token.pos_ == 'CONJ'])
            # print("PARTÍCULAS ---> ", [token for token in s if token.pos_ == 'PART'])
            # print("INTERJEIÇÕES ---> ", [token for token in s if token.pos_ == 'INTJ'])
            # print("NUMERAIS ---> ", [token for token in s if token.pos_ == 'NUM'])
            # print("PONTUAÇÕES ---> ", [token for token in s if token.pos_ == 'PUNCT'])
            # print("OUTROS ---> ", [token for token in s if token.pos_ == 'X'])
            # print("ENTIDADES ---> ", [ent for ent in s.ents])
            # print("ENTIDADES ---> ", [ent for ent in s.ents if ent.label_ == 'DRUG'])
            # print("---------- fim da sentença -----------")
            # for token in s:
            #     # if token.pos_ == 'NOUN': # and token.lemma_ not in self.stoplist_interactions:
            #     print(token.lemma_)
                    # if token.lemma_.lower() not in self.stoplist_interactions:
                    #
                    #     triggers_words.append(token.lemma_.lower())
            # set(triggers_words)

            # for c in s.noun_chunks:
            #     print("Noun Chunk ------------> ", c)
            #     if not any(value in c.lemma_ for value in self.stoplist_interactions):
            #         print("Noun Chunk na lista ---> ", c)
            #
            #         triggers_words.append(c.lemma_)
            # word_freq = Counter(triggers_words)
            # common_words = word_freq.most_common(15)
        # chunks_limpos = [c for c in s.noun_chunks if not any(value in c.text for value in self.stoplist_interactions)]
        # print("KEY FLAGS -------> ", len(triggers_words),triggers_words)
        # print("CHUNKS LIMPOS ---> ", word_freq.most_common())



        # for token in s:
        #     if token.pos_ == 'NOUN':
        #         print("{:>20}{:>20}{:>10}{:>15}{:>10}{:>5}{:>5}{:>5}{:>5}".format(
        #         token.text, " lemma: " + token.lemma_, token.pos_, token.tag_, token.dep_,
        #         token.shape_ + " is: ", token.is_sent_start, token.orth_,
        #         token.is_stop, token.is_title, token.is_ancestor(s.root)))
        #         print('---------------------')


if __name__ == '__main__':
    leaflet3 = InteractionParser(r'leaflets_pdf/bula_1689362421673 - Amoxicilina.pdf')
    leaflet3.get_interactions_flags()
