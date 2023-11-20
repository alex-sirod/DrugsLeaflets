from collections import Counter

from drug_leaflet import Leaflet


class InteractionParser:
    """Class to parse interaction data from a file."""

    def __init__(self, leaflet_path):

        self.leaflet = Leaflet(leaflet_path)

        self.doc = self.leaflet.get_doc()

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
        ]

    def get_interactions_flags(self):
        """Get interactions from a leaflet."""

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
                            print(token.text, token.lemma_, "está na lista?",
                                  token.lemma_.lower() in self.stoplist_interactions)
                            triggers_words_init.append(token.lemma_.lower())

                for nc in s.noun_chunks:
                    print("Noun Chunk ------------> ", nc.root.text, nc.root.dep_, nc.root.head.text)
                    if not any(value in nc.lemma_ for value in self.stoplist_interactions):

                        print("Noun Chunk na lista ---> ", nc)
                        print("Text:", nc.text)
                        print("Root Text:", nc.root.text)
                        print("Root Dependency Relation:", nc.root.dep_)
                        print("Start Index:", nc.start)
                        print("End Index:", nc.end)
                        print("Sentence:", nc.sent.text)

                        print("span", [a for a in self.doc[nc.start:nc.end].as_doc() if not a.is_stop])
                        print("---")
                        x = [a.text for a in self.doc[nc.start:nc.end].as_doc() if a.is_stop]
                        Y = [a.text for a in self.doc[nc.start:nc.end].as_doc() if a.text == 'eles']
                        print("X ---> ", x), print("Y ---> ", Y)
                        if x:
                            triggers_words_temp.append(x[0])

                        triggers_words_init.append(nc.lemma_.lower())

        print("TRIGGERS WORDS INIT---> ", triggers_words_init)
        print("TRIGGERS WORDS TEMP ---> ", triggers_words_temp)

        triggers_words_final = [item for item in triggers_words_init if item not in set(triggers_words_temp)]
        triggers_words_final.remove("eles")  # ??? o termo "eles" não deveria estar na lista
        print("T1 sem T2 ---> ", triggers_words_final)
        word_freq = Counter(triggers_words_final)
        common_words = word_freq.most_common()
        print("TRIGGERS WORDS FINAL ---> ", common_words)
        return common_words

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
