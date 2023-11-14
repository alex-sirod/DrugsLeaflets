from drug_leaflet import Leaflet


class InteractionParser:
    """Class to parse interaction data from a file."""

    def __init__(self, leaflet_path):
        self.leaflet = Leaflet(leaflet_path)
        self.stopwords_interactions = [
            "Não há interações medicamentosas descritas para este medicamento",
            "precaução", "necessário", "adicionais", "efeito", "tratamento", "medicamento",
            "adicional", "refeição", "médico", "cirurgião-dentista", "conhecimento", "Interações medicamentosas",
            "ação", "o gravidez", "amamentação", "criança", "idoso", "uso", "os"
        ]

    def get_interactions_flags(self):
        """Get interactions from a leaflet."""

        triggers_words = set()
        triggers_words2 = set()

        for s in self.leaflet.get_interactions_section():
            # print("FRASE ---> ", s, s.root.text, s.root.dep_, s.root.head.text)
            # for c in s.noun_chunks:
            #     print("Noun Chunk ---> ", c, "[ROOT]->", c.root.text, "[DEPEND]->", c.root.dep_, "[HEAD]->",
            #           c.root.head.text)

            print("---------- início da sentença -----------")
            print("VERBOS ---> ", [token for token in s if token.pos_ == 'VERB'])
            print("VERBOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'VERB'])
            print("SUBSTANTIVOS ---> ", [token for token in s if token.pos_ == 'NOUN'
                                         and token.lemma_ not in self.stopwords_interactions])
            print("SUBSTANTIVOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'NOUN'])
            print("ADJETIVOS ---> ", [token for token in s if token.pos_ == 'ADJ'])
            print("ADJETIVOS LEMMA ---> ", [token.lemma_ for token in s if token.pos_ == 'ADJ'])
            print("PREPOSIÇÕES ---> ", [token for token in s if token.pos_ == 'ADP'])
            print("ADVÉRBIOS ---> ", [token for token in s if token.pos_ == 'ADV'])
            print("PRONOMES ---> ", [token for token in s if token.pos_ == 'PRON'])
            print("CONJUNÇÕES ---> ", [token for token in s if token.pos_ == 'CONJ'])
            print("PARTÍCULAS ---> ", [token for token in s if token.pos_ == 'PART'])
            print("INTERJEIÇÕES ---> ", [token for token in s if token.pos_ == 'INTJ'])
            print("NUMERAIS ---> ", [token for token in s if token.pos_ == 'NUM'])
            print("PONTUAÇÕES ---> ", [token for token in s if token.pos_ == 'PUNCT'])
            print("OUTROS ---> ", [token for token in s if token.pos_ == 'X'])
            print("ENTIDADES ---> ", [ent for ent in s.ents])
            print("ENTIDADES ---> ", [ent for ent in s.ents if ent.label_ == 'DRUG'])
            print("---------- fim da sentença -----------")
            for token in s:
                if token.pos_ == 'NOUN' and token.lemma_ not in self.stopwords_interactions:
                    triggers_words.add(token.lemma_)
            set(triggers_words)

            for c in s.noun_chunks:
                print("Noun Chunk ------------> ", c)
                if not any(value in c.lemma_ for value in self.stopwords_interactions):
                    print("Noun Chunk na lista ---> ", c)
                    triggers_words.add(c.lemma_)

        # chunks_limpos = [c for c in s.noun_chunks if not any(value in c.text for value in self.stopwords_interactions)]
        print("KEY FLAGS -------> ", set(triggers_words))
        print("CHUNKS LIMPOS ---> ", set(triggers_words2))
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
