from interactions import get_similarity_lists, InteractionParser
import statistics
import copy
import nltk
from nltk.stem import RSLPStemmer
from nltk.tokenize import word_tokenize

import spacy  # used in clean list


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

        # Calculate the weight_A of each list of tuples
        weight_i = 0
        for w_A in self.drug_A_quality:
            weight_i += w_A[1]
        self.weight_A = weight_i / len(self.drug_A_quality)
        print("Peso de A", self.weight_A)
        print(self.drug_A_quality)
        # Calculate the weight_B of each list of tuples
        weight_j = 0
        for w_B in self.drug_B_quality:
            weight_j += w_B[1]
        self.weight_B = weight_j / len(self.drug_B_quality)
        print("Peso de B", self.weight_B)
        print(self.drug_B_quality)

        self.qty_A = len(self.drug_A_quality)
        self.qty_B = len(self.drug_B_quality)
        # print(i, type(s), result[i])
        print("Tamanho de a e B", self.qty_A, self.qty_B)

    def set_stemm(self, text):
        words = word_tokenize(text, language='portuguese')
        lemmatizer = RSLPStemmer()
        lemmatized_words = [lemmatizer.stem(word) for word in words]
        lemmatized_text = ' '.join(lemmatized_words)
        return lemmatized_text

    def clean_list(self, list_text):
        doc = self.nlp(" ".join(list_text))
        det_removed = [token.text for token in doc if token.pos_ != "DET"]
        # print("Tokens sem determinantes:", det_removed)
        return det_removed

    def measure_similarity_by_chunk(self):
        measure_chunk = []
        # mensura palavras e frase nominais iguais
        for i in self.drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_chunk.append(i[1] * self.weight_A)
                else:
                    measure_chunk.append(0)

        for i in self.drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure_chunk.append(i[1] * self.weight_B)
                else:
                    measure_chunk.append(0)

        print("SOMA:", sum(measure_chunk))
        print("Média:", statistics.mean(measure_chunk))
        print("Valores:", measure_chunk)
        print("% Total:",
              sum([(a / 100) * (100 / sum(measure_chunk)) for a in measure_chunk if sum(measure_chunk) != 0]))
        print("% Item:", ([(a / 100) * (100 / sum(measure_chunk)) for a in measure_chunk if sum(measure_chunk) != 0]))
        print("Quantidade:", len(measure_chunk))

        print(f"********* Similaridade por frases nominais entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(measure_chunk)} *******")

        measure_sim_chunk = sum(
            [(a / 100) * (100 / sum(measure_chunk)) for a in measure_chunk if sum(measure_chunk) != 0])
        return measure_sim_chunk

    def measure_similarity_by_word(self):
        measure = []
        # mensura palavras iguais
        for i in self.drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure.append(i[1] * self.weight_A)
                else:
                    measure.append(0)

        for i in self.drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in self.drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    measure.append(i[1] * self.weight_B)
                else:
                    measure.append(0)

        # print("SOMA:", sum(measure))
        # print("Média:", statistics.mean(measure))
        # print("Valores:", measure)
        # print("% Total:", sum([(a / 100) * (100 / sum(measure)) for a in measure if sum(measure) != 0]))
        # print("% Item:", ([(a / 100) * (100 / sum(measure)) for a in measure if sum(measure) != 0]))
        # print("Quantidade:", len(measure))
        #
        # print(f"********* Similaridade por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
        #       f" |{self.leaflet2.get_atc_code()[0]}| é {statistics.mean(measure)} *******")
        print("  Lista Original:", self.drug_A_quality)
        drug_A_quality_temp = []
        for i in self.drug_A_quality:
            for j in self.clean_list((i[0].lower().split())):
                drug_A_quality_temp.append((j, i[1]))

        print("Lista Temporária:", drug_A_quality_temp)
        self.drug_A_quality = copy.deepcopy(drug_A_quality_temp)
        print("       Deep Copy:", self.drug_A_quality)

        # print(self.drug_B_constraint)
        # print(self.drug_B_quality)
        # print(self.drug_A_constraint)


if __name__ == '__main__':
    leaflet1 = r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf'
    leaflet2 = r'datasources/leaflets_pdf/bula_1700662857659_Ibuprofeno.pdf'
    calc = CalcSimilarity(leaflet1, leaflet2)
    # calc.measure_similarity_by_chunk()
    calc.measure_similarity_by_word()
    # calc.clean_list(["O outro cachorro marrom pula alto ."])
