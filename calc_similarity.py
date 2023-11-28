from interactions import get_similarity_lists, InteractionParser
import statistics
import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize
import jellyfish._jellyfish as pyjellyfish
import jellyfish  # used in measure similarity by word

import spacy  # used in clean list and measure similarity by spacy

nlp = spacy.load("pt_core_news_lg")


# # Baixe o stemmer RSLP
# try:
#     nltk.data.find('tokenizers/rslp')
# except LookupError:
#     nltk.download('rslp')
class CalcSimilarity:
    def __init__(self, calc_leaflet1, calc_leaflet2):
        self.nlp = spacy.load("pt_core_news_sm")
        self.leaflet1 = InteractionParser(calc_leaflet1)
        self.leaflet2 = InteractionParser(calc_leaflet2)
        self.weight_A = 0
        self.weight_B = 0

        result = get_similarity_lists(self.leaflet1, self.leaflet2)
        for __ in enumerate(result):
            self.drug_A_quality = result[2]  # list contains tuples
            self.drug_A_constraint = result[3]  # list simple
            self.drug_B_quality = result[6]  # list contains tuples
            self.drug_B_constraint = result[7]  # list simple

        self.qty_A = len(self.drug_A_quality)
        self.qty_B = len(self.drug_B_quality)

        # Calculate the weight_A of each list of tuples
        weight_i = 0
        for w_A in self.drug_A_quality:
            weight_i += w_A[1]
        self.weight_A = weight_i / len(self.drug_A_quality)
        print(f"Tamanho de A:{self.qty_A}, peso de A:{self.weight_A}")
        print(self.drug_A_quality)

        # Calculate the weight_B of each list of tuples
        weight_j = 0
        for w_B in self.drug_B_quality:
            weight_j += w_B[1]
        self.weight_B = weight_j / len(self.drug_B_quality)
        print(f"Tamanho de B:{self.qty_B}, peso de B:{self.weight_B}")
        print(self.drug_B_quality)
        print("--------------------------------------------------")
        print("                     RESULTADOS                   ")
        print("--------------------------------------------------")
    def set_stemm(self, text):
        words = word_tokenize(text, language='portuguese')
        lemmatizer = RSLPStemmer()
        lemmatized_words = [lemmatizer.stem(word) for word in words]
        lemmatized_text = ' '.join(lemmatized_words)
        return lemmatized_text

    def clean_list(self, list_text):
        doc = self.nlp(" ".join(list_text))
        det_removed = [token.text for token in doc if token.pos_ != "DET"
                       and token.is_punct is False
                       and token.is_stop is False
                       and token.is_space is False
                       ]

        # print("Tokens sem determinantes:", det_removed)

        return det_removed

    def measure_similarity_by_chunk(self):
        measure_sim_chunk = []
        # mensura palavras e frase nominais iguais
        for i in self.drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_sim_chunk.append(i[1] * self.weight_A)
                else:
                    measure_sim_chunk.append(0)

        for i in self.drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_sim_chunk.append(i[1] * self.weight_B)
                else:
                    measure_sim_chunk.append(0)

        # print("SOMA:", sum(measure_sim_chunk))
        # print("Média:", statistics.mean(measure_sim_chunk))
        # print("Valores:", measure_sim_chunk)
        # print("% Total:",
        #       sum([(a / 100) * (100 / sum(measure_sim_chunk)) for a in measure_sim_chunk if sum(measure_sim_chunk) != 0]))
        # print("% Item:", ([(a / 100) * (100 / sum(measure_sim_chunk)) for a in measure_sim_chunk if sum(measure_sim_chunk) != 0]))
        # print("Quantidade:", len(measure_sim_chunk))

        print(f"Similaridade por frases nominais entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(measure_sim_chunk)}")

        measure_sim_chunk = sum(
            [(a / 100) * (100 / sum(measure_sim_chunk)) for a in measure_sim_chunk if sum(measure_sim_chunk) != 0])
        return measure_sim_chunk

    def measure_similarity_by_word(self):
        measure_sim_word = []
        local_drug_A_quality = []
        local_drug_B_quality = []
        local_drug_A_constraint = []
        local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_quality)
        for i in self.drug_A_quality:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_A_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_B_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i.lower().split())):
                local_drug_A_constraint.append(j)
        # print("     Lista Local:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_constraint)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i.lower().split())):
                local_drug_B_constraint.append(j)
        # print("     Lista Local:", local_drug_B_constraint)

        # mensura palavras iguais


        for i in local_drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in local_drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_sim_word.append(i[1] * self.weight_A)
                else:
                    measure_sim_word.append(0)

        for i in local_drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in local_drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_sim_word.append(i[1] * self.weight_B)
                else:
                    measure_sim_word.append(0)

        # print("SOMA:", sum(measure_sim_word))
        # print("Média:", statistics.mean(measure_sim_word))
        # print("Valores:", measure_sim_word)
        # print("% Total:", sum([(a / 100) * (100 / sum(measure_sim_word)) for a in measure_sim_word if sum(measure_sim_word) != 0]))
        # print("% Item:", ([(a / 100) * (100 / sum(measure_sim_word)) for a in measure_sim_word if sum(measure_sim_word) != 0]))
        # print("Quantidade:", len(measure_sim_word))
        measure_sim_word = sum(
            [(a / 100) * (100 / sum(measure_sim_word)) for a in measure_sim_word if sum(measure_sim_word) != 0])

        print(f"Similaridade por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {measure_sim_word}")

        return measure_sim_word

    def measure_similarity_by_bigstring(self):
        measure_spacy_values = []
        local_drug_A_quality = []
        local_drug_B_quality = []
        local_drug_A_constraint = []
        local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_quality)
        for i in self.drug_A_quality:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_A_quality.append((j, i[1]))
        # print("Lista Local:", local_drug_A_quality)
        # transforma a lista local em uma sentença
        doc_local_drug_A_quality = nlp(" ".join([i[0] for i in local_drug_A_quality]))
        # print("Sentença Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_B_quality.append((j, i[1]))
        # print("Lista Local:", local_drug_B_quality)
        # transforma a lista local em uma sentença
        doc_local_drug_B_quality = nlp(" ".join([i[0] for i in local_drug_B_quality]))
        # print("Sentença Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i.lower().split())):
                local_drug_A_constraint.append(j)
        # print("Lista Local A_constraint:", local_drug_A_constraint)
        # transforma a lista local em uma sentença
        doc_local_drug_A_constraint = nlp(" ".join([i for i in local_drug_A_constraint]))
        # print("Sentença Local A_constraint:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_constraint)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i.lower().split())):
                local_drug_B_constraint.append(j)
        # print("Lista Local B_constraint:", local_drug_B_constraint)
        # transforma a lista local em uma sentença
        doc_local_drug_B_constraint = nlp(" ".join([i for i in local_drug_B_constraint]))
        # print("Doc B_constraint:", doc_local_drug_B_constraint)

        # Preenche a lista de medidas com os valores de similaridade
        measure_spacy_values.append(doc_local_drug_A_quality.similarity(doc_local_drug_B_constraint))
        measure_spacy_values.append(doc_local_drug_B_constraint.similarity(doc_local_drug_A_quality))
        measure_spacy_values.append(doc_local_drug_A_constraint.similarity(doc_local_drug_B_quality))
        measure_spacy_values.append(doc_local_drug_B_quality.similarity(doc_local_drug_A_constraint))

        # print("Measure Spacy Values:", statistics.mean(measure_spacy_values))
        #
        # print("-------Calibrando ------------")
        # print("Similaridade por spacy:       A_quality / A_quality",
        #       doc_local_drug_A_quality.similarity(doc_local_drug_A_quality))
        # print("Similaridade por spacy:       B_quality / B_quality",
        #       doc_local_drug_B_quality.similarity(doc_local_drug_B_quality))
        # print("----------Testando---------")
        # print("Similaridade por spacy:    A_quality / B_constraint",
        #       doc_local_drug_A_quality.similarity(doc_local_drug_B_constraint))
        # print("Similaridade por spacy:    B_constraint / A_quality",
        #       doc_local_drug_B_constraint.similarity(doc_local_drug_A_quality))
        # print("Similaridade por spacy:    A_constraint / B_quality",
        #       doc_local_drug_A_constraint.similarity(doc_local_drug_B_quality))
        # print("Similaridade por spacy:    B_quality / A_constraint",
        #       doc_local_drug_B_quality.similarity(doc_local_drug_A_constraint))
        # print("-------------------")

        print(f"Similaridade por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(measure_spacy_values)}")

        return statistics.mean(measure_spacy_values)

    def measure_similarity_by_word_jaro(self):
        measure_jellyfish_values = []
        jellyfish_drug_A_quality = []
        jellyfish_drug_B_quality = []
        jellyfish_drug_A_constraint = []
        jellyfish_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_quality)
        for i in self.drug_A_quality:
            for j in self.clean_list((i[0].lower().split())):
                jellyfish_drug_A_quality.append((j, i[1]))
        # print("Lista Local:", jellyfish_drug_A_quality)
        # transforma a lista local em uma sentença
        jellyfish_drug_A_quality = " ".join([i[0] for i in jellyfish_drug_A_quality])
        # print("Sentença Jellyfish:", jellyfish_drug_A_quality)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
            for j in self.clean_list((i[0].lower().split())):
                jellyfish_drug_B_quality.append((j, i[1]))
        # print("Lista Local:", jellyfish_drug_B_quality)
        # transforma a lista local em uma sentença
        jellyfish_drug_B_quality = " ".join([i[0] for i in jellyfish_drug_B_quality])
        # print("Sentença Jellyfish:", jellyfish_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i.lower().split())):
                jellyfish_drug_A_constraint.append(j)
        # print("Lista Local A_constraint:", jellyfish_drug_A_constraint)
        # transforma a lista local em uma sentença
        jellyfish_drug_A_constraint = " ".join([i for i in jellyfish_drug_A_constraint])
        # print("Sentença Local A_constraint:", jellyfish_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_constraint)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i.lower().split())):
                jellyfish_drug_B_constraint.append(j)
        # print("Lista Local B_constraint:", jellyfish_drug_B_constraint)
        # transforma a lista local em uma sentença
        jellyfish_drug_B_constraint = " ".join([i for i in jellyfish_drug_B_constraint])
        # print("Sentença Local B_constraint:", jellyfish_drug_B_constraint)

        # Preenche a lista de medidas com os valores de similaridade
        measure_jellyfish_values.append(
            jellyfish.jaro_winkler_similarity(jellyfish_drug_A_quality, jellyfish_drug_B_constraint))
        measure_jellyfish_values.append(
            jellyfish.jaro_winkler_similarity(jellyfish_drug_B_constraint, jellyfish_drug_A_quality))
        measure_jellyfish_values.append(
            jellyfish.jaro_winkler_similarity(jellyfish_drug_A_constraint, jellyfish_drug_B_quality))
        measure_jellyfish_values.append(
            jellyfish.jaro_winkler_similarity(jellyfish_drug_B_quality, jellyfish_drug_A_constraint))

        # print("Measure Jellyfish Jaro-Winkler Values:", statistics.mean(measure_jellyfish_values))
        #
        # print("-------Calibrando ------------")
        # print("Similaridade por jellyfish:       A_quality / A_quality",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_A_quality, jellyfish_drug_A_quality))
        # print("Similaridade por jellyfish:       B_quality / B_quality",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_B_quality, jellyfish_drug_B_quality))
        # print("----------Testando---------")
        # print("Similaridade por jellyfish:    A_quality / B_constraint",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_A_quality, jellyfish_drug_B_constraint))
        # print("Similaridade por jellyfish:    B_constraint / A_quality",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_B_constraint, jellyfish_drug_A_quality))
        # print("Similaridade por jellyfish:    A_constraint / B_quality",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_A_constraint, jellyfish_drug_B_quality))
        # print("Similaridade por jellyfish:    B_quality / A_constraint",
        #       jellyfish.jaro_winkler_similarity(jellyfish_drug_B_quality, jellyfish_drug_A_constraint))
        # print("-------------------")

        print(f"Similaridade Distância de Jaro por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(measure_jellyfish_values)}")

        return statistics.mean(measure_jellyfish_values)

    def measure_similarity_by_chunk_levenshtein(self):

        lev_measure_chunk = []
        # mensura palavras e frase nominais iguais

        for i in self.drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_B_constraint:
                # print("(A)", self.set_stemm(j.lower()), "(B)", self.set_stemm(i[0].lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                lev_measure_chunk.append(value_l)

        for i in self.drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_A_constraint:
                # print("(A)", self.set_stemm(j.lower()), "(B)", self.set_stemm(i[0].lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                lev_measure_chunk.append(value_l)

        # print("SOMA:", sum(lev_measure_chunk))
        # print("Média:", statistics.mean(lev_measure_chunk))
        # print("Valores:", lev_measure_chunk)
        # print("% Total:",
        #       sum([(a / 100) * (100 / sum(lev_measure_chunk)) for a in lev_measure_chunk if
        #            sum(lev_measure_chunk) != 0]))
        # print("% Item:",
        #       ([(a / 100) * (100 / sum(lev_measure_chunk)) for a in lev_measure_chunk if sum(lev_measure_chunk) != 0]))
        # print("Quantidade:", len(lev_measure_chunk))

        print(f"Similaridade Distância de Levenshtein por frases nominais entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(lev_measure_chunk)}")

        lev_measure_sim_chunk = sum(
            [(a / 100) * (100 / sum(lev_measure_chunk)) for a in lev_measure_chunk if sum(lev_measure_chunk) != 0])
        return lev_measure_sim_chunk

    def measure_similarity_by_word_levenshtein(self):

        lev_local_drug_A_quality = []
        lev_local_drug_B_quality = []
        lev_local_drug_A_constraint = []
        lev_local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_quality)
        for i in self.drug_A_quality:
            for j in self.clean_list((i[0].lower().split())):
                lev_local_drug_A_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
            for j in self.clean_list((i[0].lower().split())):
                lev_local_drug_B_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i.lower().split())):
                lev_local_drug_A_constraint.append(j)
        # print("     Lista Local:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_constraint)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i.lower().split())):
                lev_local_drug_B_constraint.append(j)
        # print("     Lista Local:", local_drug_B_constraint)

        # mensura palavras iguais
        lev_measure_sim_word = []

        for i in lev_local_drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in lev_local_drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                lev_measure_sim_word.append(value_l)

        for i in lev_local_drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in lev_local_drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                lev_measure_sim_word.append(value_l)

        # print("SOMA:", sum(lev_measure_sim_word))
        # print("Média:", statistics.mean(lev_measure_sim_word))
        # print("Valores:", lev_measure_sim_word)
        # print("% Total:",
        #       sum([(a / 100) * (100 / sum(lev_measure_sim_word)) for a in lev_measure_sim_word if sum(lev_measure_sim_word) != 0]))
        # print("% Item:",
        #       ([(a / 100) * (100 / sum(lev_measure_sim_word)) for a in lev_measure_sim_word if sum(lev_measure_sim_word) != 0]))
        # print("Quantidade:", len(lev_measure_sim_word))
        lev_measure_sim_word = sum(
            [(a / 100) * (100 / sum(lev_measure_sim_word)) for a in lev_measure_sim_word if sum(lev_measure_sim_word) != 0])

        print(f"Similaridade Distância de Levenshtein por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {lev_measure_sim_word}")

        return lev_measure_sim_word

    def calc_levenshtein(self, s1, s2):
        if len(s1) > len(s2):
            v = len(s1)
        else:
            v = len(s2)
        lev = jellyfish.levenshtein_distance(s1, s2)
        # print(f"Maior Valor: {v}")
        # print(f"TAMANHO 1 \'{s1}\' ", len(s1))
        # print(f"TAMANHO 2 \'{s2}\' ", len(s2))
        # print("LEVENSHTEIN", jellyfish.levenshtein_distance(s1, s2))
        #
        # print(((100 / v) * l) / 100)
        return ((100 / v) * lev) / 100


if __name__ == '__main__':
    leaflet1 = r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf'
    leaflet2 = r'datasources/leaflets_pdf/bula_1700662857659_Ibuprofeno.pdf'
    # calc.clean_list(["O outro cachorro marrom pula alto ."])

    calc = CalcSimilarity(leaflet1, leaflet2)
    calc.measure_similarity_by_chunk()
    calc.measure_similarity_by_word()
    calc.measure_similarity_by_bigstring()
    calc.measure_similarity_by_word_jaro()
    calc.measure_similarity_by_chunk_levenshtein()
    calc.measure_similarity_by_word_levenshtein()
    print("--------------------------------------------------")