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
        self.nlp = spacy.load("pt_core_news_lg")
        self.leaflet1 = InteractionParser(calc_leaflet1)
        self.leaflet2 = InteractionParser(calc_leaflet2)
        self.weight_A = 0
        self.weight_B = 0

        result = get_similarity_lists(self.leaflet1, self.leaflet2)
        for __ in enumerate(result):
            self.drug_A_constraint = result[2]  # interactions of A
            self.drug_A_quality = result[3]  # Definition of A
            self.drug_B_constraint = result[6]  # interactions of B
            self.drug_B_quality = result[7]  # Definition of B

        # return (atc_code1, drug_name1, interactions_flags1, group_atc_code1,
        #         atc_code2, drug_name2, interactions_flags2, group_atc_code2)

        self.qty_A = len(self.drug_A_constraint)
        self.qty_B = len(self.drug_B_constraint)

        # Calculate the weight_A of each list of tuples
        weight_i = 0
        for w_A in self.drug_A_constraint:
            weight_i += w_A[1]
        if weight_i:
            self.weight_A = weight_i / len(self.drug_A_constraint)
        else:
            self.weight_A = 1
        print(f"Tamanho de A:{self.qty_A}, peso de A:{self.weight_A}")
        print(self.drug_A_constraint)

        # Calculate the weight_B of each list of tuples
        weight_j = 0
        for w_B in self.drug_B_constraint:
            weight_j += w_B[1]
        if weight_j:
            self.weight_B = weight_j / len(self.drug_B_constraint)
        else:
            self.weight_B = 1
        print(f"Tamanho de B:{self.qty_B}, peso de B:{self.weight_B}")
        print(self.drug_B_constraint)

        print("----------------------------------------------------------------------------------------------------")
        print("                                      PROCESSING SIMILARITY                                         ")
        print("----------------------------------------------------------------------------------------------------")

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
        global i
        measure_sim_chunk = []
        store_sim_chunk = []
        # mensura palavras e frase nominais iguais

        for j in self.drug_B_quality:
            # print(self.set_stemm(j.lower()))
            for i in self.drug_A_constraint:
                # print(self.set_stemm(i[0].lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    # print(self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_sim_chunk.append(f"{i[0].lower()} == {j.lower()}")
                    measure_sim_chunk.append(i[1] * self.weight_A)
                else:
                    measure_sim_chunk.append(0)

        for j in self.drug_A_quality:
            # print(self.set_stemm(j.lower()))
            for i in self.drug_B_constraint:
                # print(self.set_stemm(i[0].lower()))

                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    # print(self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_sim_chunk.append(f"{i[0].lower()} == {j.lower()}")
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

        print(f"Similarity for noun phrases between |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| is:\naverage: {statistics.mean(measure_sim_chunk)} "
              f" maximum: {max(measure_sim_chunk)}")

        measure_sim_chunk = sum(
            [(a / 100) * (100 / sum(measure_sim_chunk)) for a in measure_sim_chunk if sum(measure_sim_chunk) != 0])

        print(f"Prescrition with medications|{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| require your attention due to the presence of the "
              f"following terms: \n{store_sim_chunk}" if measure_sim_chunk > 0
              else f"Prescrition with medications |{self.leaflet1.get_atc_code()[0]}| e"
                   f" |{self.leaflet2.get_atc_code()[0]}| appears to have no drug interactions!")


        return measure_sim_chunk

    def measure_similarity_by_word(self):


        measure_sim_word = []
        store_similar_words = []
        local_drug_A_quality = []
        local_drug_B_quality = []
        local_drug_A_constraint = []
        local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            print(i[0])
            for j in self.clean_list((i[0].lower().split())):
                local_drug_A_quality.append((j, i[1]))
        print("     Lista Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_contraint2)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_B_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_quality:
            for j in self.clean_list((i.lower().split())):
                local_drug_A_constraint.append(j)
        # print("     Lista Local:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
            for j in self.clean_list((i.lower().split())):
                local_drug_B_constraint.append(j)
        # print("     Lista Local:", local_drug_B_constraint)

        # mensura palavras iguais

        for i in local_drug_A_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in local_drug_B_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    print(self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_similar_words.append(f"{i[0].lower()} == {j.lower()}")
                    measure_sim_word.append(i[1] * self.weight_A)
                else:
                    measure_sim_word.append(0)

        for i in local_drug_B_quality:
            # print(self.set_stemm(i[0].lower()))
            for j in local_drug_A_constraint:
                # print(self.set_stemm(j.lower()))
                if self.set_stemm(i[0].lower()) == self.set_stemm(j.lower()):
                    print(self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_similar_words.append(f"{i[0].lower()} == {j.lower()}")
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

        print(f"Similarity by words between |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| is {measure_sim_word} ")

        print(f"Prescription with medications |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| require your attention due to the presence of the "
              f"following terms: \n"
              f" {store_similar_words}" if measure_sim_word > 0
              else f"Prescrition with medications |{self.leaflet1.get_atc_code()[0]}| e"
                   f" |{self.leaflet2.get_atc_code()[0]}| appears to have no drug interactions!")

        return measure_sim_word

    def measure_similarity_by_bigstring(self):

        """A similaridade por bigstring é uma opção exemplificativa e provocativa de uso do medidor interno de spacy,
        uma sugestão de melhoria seria estabelecer um limite de avaliação baseadao no tamanho da menor lista
        """
        measure_spacy_values = []
        local_drug_A_quality = []
        local_drug_B_quality = []
        local_drug_A_constraint = []
        local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_A_quality.append((j, i[1]))
        # print("Lista Local:", local_drug_A_quality)
        # transforma a lista local em uma sentença
        doc_local_drug_A_quality = nlp(" ".join([i[0] for i in local_drug_A_quality]))
        # print("Sentença Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_contraint2)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i[0].lower().split())):
                local_drug_B_quality.append((j, i[1]))
        # print("Lista Local:", local_drug_B_quality)
        # transforma a lista local em uma sentença
        doc_local_drug_B_quality = nlp(" ".join([i[0] for i in local_drug_B_quality]))
        # print("Sentença Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_quality:
            for j in self.clean_list((i.lower().split())):
                local_drug_A_constraint.append(j)
        # print("Lista Local A_constraint:", local_drug_A_constraint)
        # transforma a lista local em uma sentença
        doc_local_drug_A_constraint = nlp(" ".join([i for i in local_drug_A_constraint]))
        # print("Sentença Local A_constraint:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
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

        print(f"Similaridade por (join) lista entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é média:{statistics.mean(measure_spacy_values)},"
              f" máximo:{max(measure_spacy_values)}")

        return statistics.mean(measure_spacy_values)

    def measure_similarity_by_chunk_jaro(self):
        global i
        measure_sim_chunk_jaro = [0]  # inicializa a lista com zero para evitar erro de média
        store_similar_chunks = []
        # mensura palavras e frase nominais iguais

        for j in self.drug_B_quality:
            # print(self.set_stemm(j.lower()))
            for i in self.drug_A_constraint:
                # print(self.set_stemm(i[0].lower()))
                measure_j = jellyfish.jaro_winkler_similarity(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                # measure_j = jellyfish.jaro_winkler_similarity(i[0].lower(), j.lower())
                # print(measure_j, i[0].lower(), " == ", j.lower())
                if measure_j > 0.99:
                    # print(measure_j, i[0].lower(), " == ", j.lower())
                    # print(measure_j, self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_similar_chunks.append(f"{i[0].lower()} == {j.lower()}")
                    measure_sim_chunk_jaro.append(measure_j)

        for j in self.drug_A_quality:
            # print(self.set_stemm(j.lower()))
            for i in self.drug_B_constraint:
                # print(self.set_stemm(i[0].lower()))
                measure_j = jellyfish.jaro_winkler_similarity(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                if measure_j > 0.99:
                    # print(measure_j, i[0].lower(), " == ", j.lower())
                    # print(measure_j, self.set_stemm(i[0].lower()), " == ", self.set_stemm(j.lower()))
                    store_similar_chunks.append(f"{i[0].lower()} == {j.lower()}")
                    measure_sim_chunk_jaro.append(measure_j)

        print(f"Similarity Jaro distance for noun phrases between |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| is:\naverage: {statistics.mean(measure_sim_chunk_jaro)} "
              f"maximum: {max(measure_sim_chunk_jaro)}")

        print(f"Prescription with medications |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| require your attention due to the presence of the "
              f"following terms: \n"
              f" {store_similar_chunks}" if max(measure_sim_chunk_jaro) == 1
              else f"Prescription with medications |{self.leaflet1.get_atc_code()[0]}| and"
                   f" |{self.leaflet2.get_atc_code()[0]}| appears to have no drug interactions!")

        return max(measure_sim_chunk_jaro)

    def measure_similarity_by_word_jaro(self):
        measure_jellyfish_values = []
        jellyfish_drug_A_quality = []
        jellyfish_drug_B_quality = []
        jellyfish_drug_A_constraint = []
        jellyfish_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i[0].lower().split())):
                jellyfish_drug_A_quality.append((j, i[1]))
        # print("Lista Local:", jellyfish_drug_A_quality)
        # transforma a lista local em uma sentença
        jellyfish_drug_A_quality = " ".join([i[0] for i in jellyfish_drug_A_quality])
        # print("Sentença Jellyfish:", jellyfish_drug_A_quality)

        # print("  Lista Original:", self.drug_B_contraint2)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i[0].lower().split())):
                jellyfish_drug_B_quality.append((j, i[1]))
        # print("Lista Local:", jellyfish_drug_B_quality)
        # transforma a lista local em uma sentença
        jellyfish_drug_B_quality = " ".join([i[0] for i in jellyfish_drug_B_quality])
        # print("Sentença Jellyfish:", jellyfish_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_quality:
            for j in self.clean_list((i.lower().split())):
                jellyfish_drug_A_constraint.append(j)
        # print("Lista Local A_constraint:", jellyfish_drug_A_constraint)
        # transforma a lista local em uma sentença
        jellyfish_drug_A_constraint = " ".join([i for i in jellyfish_drug_A_constraint])
        # print("Sentença Local A_constraint:", jellyfish_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
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

        print(f"Similaridade Distância de Jaro por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é média: {statistics.mean(measure_jellyfish_values)} "
              f"e máximo: {max(measure_jellyfish_values)}")

        return statistics.mean(measure_jellyfish_values)

    def measure_similarity_by_chunk_levenshtein(self):
        # inicializa a lista com um valor diferente de 0 para evitar erro de buscar o mínimo em uma lisat vazia
        lev_measure_chunk = [1]
        store_similar_lev_chunks = []
        # mensura palavras e frase nominais iguais

        for i in self.drug_A_constraint:

            for j in self.drug_B_quality:
                # print("(A)", self.set_stemm(j.lower()), "(B)", self.set_stemm(i[0].lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                if value_l == 0:
                    # print("adicionado ZERO")
                    store_similar_lev_chunks.append(f"{i[0].lower()} == {j.lower()}")
                lev_measure_chunk.append(value_l)

        for i in self.drug_B_constraint:

            for j in self.drug_A_quality:
                # print("(A)", self.set_stemm(j.lower()), "(B)", self.set_stemm(i[0].lower()))
                value_l = self.calc_levenshtein(self.set_stemm(i[0].lower()), self.set_stemm(j.lower()))
                if value_l == 0:
                    # print("adicionado ZERO")
                    store_similar_lev_chunks.append(f"{i[0].lower()} == {j.lower()}")
                lev_measure_chunk.append(value_l)

        print(f"Similarity Levenshtein distance for noun phrases between  |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| is:\naverage: {statistics.mean(lev_measure_chunk)}, "
              f"maximum: {max(lev_measure_chunk)} and minimum : {(min(lev_measure_chunk))}")

        print(f"Prescription with medications |{self.leaflet1.get_atc_code()[0]}| and"
              f" |{self.leaflet2.get_atc_code()[0]}| require your attention due to the presence of the "
              f"following terms: \n"
              f" {store_similar_lev_chunks}" if min(lev_measure_chunk) == 0
              else f"Prescription with medications |{self.leaflet1.get_atc_code()[0]}| and"
                   f" |{self.leaflet2.get_atc_code()[0]}| appears to have no drug interactions!")

        lev_measure_sim_chunk = sum(
            [(a / 100) * (100 / sum(lev_measure_chunk)) for a in lev_measure_chunk if sum(lev_measure_chunk) != 0])

        return (min(lev_measure_chunk)) if min(lev_measure_chunk) != 0 else lev_measure_sim_chunk

    def measure_similarity_by_word_levenshtein(self):
        """A similaridade por palavras é muito sensível a variações sutis de termos,
        capturando palavra simples sem valor de informação"""
        lev_local_drug_A_quality = []
        lev_local_drug_B_quality = []
        lev_local_drug_A_constraint = []
        lev_local_drug_B_constraint = []

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_constraint:
            for j in self.clean_list((i[0].lower().split())):
                lev_local_drug_A_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_A_quality)

        # print("  Lista Original:", self.drug_B_contraint2)
        for i in self.drug_B_constraint:
            for j in self.clean_list((i[0].lower().split())):
                lev_local_drug_B_quality.append((j, i[1]))
        # print("     Lista Local:", local_drug_B_quality)

        # print("  Lista Original:", self.drug_A_constraint)
        for i in self.drug_A_quality:
            for j in self.clean_list((i.lower().split())):
                lev_local_drug_A_constraint.append(j)
        # print("     Lista Local:", local_drug_A_constraint)

        # print("  Lista Original:", self.drug_B_quality)
        for i in self.drug_B_quality:
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
        max_lev_measure_sim_word = max([a for a in lev_measure_sim_word if sum(lev_measure_sim_word) != 0])
        min_lev_measure_sim_word = min([a for a in lev_measure_sim_word if sum(lev_measure_sim_word) != 0])
        mean_lev_measure_sim_word = sum(
            [(a / 100) * (100 / sum(lev_measure_sim_word)) for a in lev_measure_sim_word if
             sum(lev_measure_sim_word) != 0])


        print(f"Similaridade Distância de Levenshtein por palavras entre |{self.leaflet1.get_atc_code()[0]}| e"
              f" |{self.leaflet2.get_atc_code()[0]}| é  mín: {min_lev_measure_sim_word}, "
              f"méd: {mean_lev_measure_sim_word}, máx:{max_lev_measure_sim_word}")

        return min_lev_measure_sim_word, mean_lev_measure_sim_word, max_lev_measure_sim_word

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

    # calc1 = CalcSimilarity(leaflet1, leaflet2)
    # calc2 = CalcSimilarity(leaflet1, leaflet3)

    # calc3 = CalcSimilarity(leaflet12, leaflet14) # omeprazol e enalapril
    # calc3.measure_similarity_by_chunk()
    # calc3.measure_similarity_by_chunk_jaro()
    # calc3.measure_similarity_by_chunk_levenshtein()
    #
    # calc4 = CalcSimilarity(leaflet10, leaflet11) # omeprazol e dipirona
    # calc4.measure_similarity_by_chunk()
    # calc4.measure_similarity_by_chunk_jaro()
    # calc4.measure_similarity_by_chunk_levenshtein()

    # # diazepam - clopidogrel
    # calc5 = CalcSimilarity(leaflet4, leaflet13) # diazepam e clopidogrel
    # calc5.measure_similarity_by_chunk()
    # calc5.measure_similarity_by_chunk_jaro()
    # calc5.measure_similarity_by_chunk_levenshtein()

    # # fenobarbital - remdesivir Não possi=ui código ATC
    # calc6 = CalcSimilarity(leaflet3, leaflet8) # fenobarbital e remdesivir
    # calc6.measure_similarity_by_chunk()
    # calc6.measure_similarity_by_chunk_jaro()
    # calc6.measure_similarity_by_chunk_levenshtein()

    # omeprazol - amoxicilina
    # calc7 = CalcSimilarity(leaflet12, leaflet2) # omeprazol e amoxicilina
    # calc7.measure_similarity_by_chunk()
    # calc7.measure_similarity_by_chunk_jaro()
    # calc7.measure_similarity_by_chunk_levenshtein()
    #
    # #hidroclorotiazida - diazepam
    # calc8 = CalcSimilarity(leaflet5, leaflet4) # hidroclorotiazida e diazepam
    # calc8.measure_similarity_by_chunk()
    # calc8.measure_similarity_by_chunk_jaro()
    # calc8.measure_similarity_by_chunk_levenshtein()

    # # enalapril - loratadina
    # calc9 = CalcSimilarity(leaflet14, leaflet17) # enalapril e loratadina
    # calc9.measure_similarity_by_chunk()
    # calc9.measure_similarity_by_chunk_jaro()
    # calc9.measure_similarity_by_chunk_levenshtein()

    # # omeprazol - loratadina
    # calc10 = CalcSimilarity(leaflet12, leaflet17) # omeprazol e loratadina
    # calc10.measure_similarity_by_chunk()
    # calc10.measure_similarity_by_chunk_jaro()
    # calc10.measure_similarity_by_chunk_levenshtein()

    # # digoxina - diazepam
    # calc11 = CalcSimilarity(leaflet10, leaflet4) # digoxina e diazepam
    # calc11.measure_similarity_by_chunk()
    # calc11.measure_similarity_by_chunk_jaro()
    # calc11.measure_similarity_by_chunk_levenshtein()

    # # sulfametoxazol - budesonida
    # calc12 = CalcSimilarity(leaflet6, leaflet16) # sulfametoxazol e budesonida
    # calc12.measure_similarity_by_chunk()
    # calc12.measure_similarity_by_chunk_jaro()
    # calc12.measure_similarity_by_chunk_levenshtein()

    # # amoxicilina - loratadina
    # calc13 = CalcSimilarity(leaflet2, leaflet17) # amoxicilina e loratadina
    # calc13.measure_similarity_by_chunk()
    # calc13.measure_similarity_by_chunk_jaro()
    # calc13.measure_similarity_by_chunk_levenshtein()

    # # omeprazol - captopril

    # calc14 = CalcSimilarity(leaflet12, leaflet9) # omeprazol e captopril
    # calc14.measure_similarity_by_chunk()
    # calc14.measure_similarity_by_chunk_jaro()
    # calc14.measure_similarity_by_chunk_levenshtein()


    # # captopril - diazepam
    # calc15 = CalcSimilarity(leaflet9, leaflet4) # captopril e diazepam
    # calc15.measure_similarity_by_chunk()
    # calc15.measure_similarity_by_chunk_jaro()
    # calc15.measure_similarity_by_chunk_levenshtein()

    # # enalapril - sulfametoxazole
    # calc16 = CalcSimilarity(leaflet14, leaflet6) # enalapril e sulfametoxazole
    # calc16.measure_similarity_by_chunk()
    # calc16.measure_similarity_by_chunk_jaro()
    # calc16.measure_similarity_by_chunk_levenshtein()

    # # ácido acetilsalicílico - captopril
    # calc17 = CalcSimilarity(leaflet7, leaflet9) # ácido acetilsalicílico e captopril
    # calc17.measure_similarity_by_chunk()
    # calc17.measure_similarity_by_chunk_jaro()
    # calc17.measure_similarity_by_chunk_levenshtein()

    # # omeprazol - budesonida
    # calc18 = CalcSimilarity(leaflet12, leaflet16) # omeprazol e budesonida
    # calc18.measure_similarity_by_chunk()
    # calc18.measure_similarity_by_chunk_jaro()
    # calc18.measure_similarity_by_chunk_levenshtein()

    # # clopidogrel - budesonida
    # calc19 = CalcSimilarity(leaflet13, leaflet16) # clopidogrel e budesonida
    # calc19.measure_similarity_by_chunk()
    # calc19.measure_similarity_by_chunk_jaro()
    # calc19.measure_similarity_by_chunk_levenshtein()

    # # sulfametoxazol - fenobarbital
    # calc20 = CalcSimilarity(leaflet6, leaflet3) # sulfametoxazol e fenobarbital
    # calc20.measure_similarity_by_chunk()
    # calc20.measure_similarity_by_chunk_jaro()
    # calc20.measure_similarity_by_chunk_levenshtein()

    leaflet1 = r'datasources/leaflets_pdf/bula_1700662857659_ibuprofeno.pdf'
    leaflet2 = r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf'
    leaflet3 = r'datasources/leaflets_pdf/bula_1701267508373_Fenobarbital.pdf'
    leaflet4 = r'datasources/leaflets_pdf/bula_1701266245626_Diazepam.pdf'
    leaflet5 = r'datasources/leaflets_pdf/bula_1701224846500_Hidroclorotiazida.pdf'
    leaflet6 = (r'datasources/leaflets_pdf/bula_1701224202414_Sulfametoxazol.pdf')
    leaflet7 = (r'datasources/leaflets_pdf/bula_1701225057399_Acido_acetilsalicílico.pdf')
    leaflet8 = (r'datasources/leaflets_pdf/bula_1701267803044_Remdesivir.pdf')
    leaflet9 = r'datasources/leaflets_pdf/bula_1701260642978_captopril.pdf'
    leaflet10 = r'datasources/leaflets_pdf/bula_1701263093335_Digoxina.pdf' # digoxina
    leaflet11 = r'datasources/leaflets_pdf/bula_1701264125049_Albendazol.pdf' # albendazol
    leaflet12 = r'datasources/leaflets_pdf/bula_1700827705685_Omeprazol.pdf'
    leaflet13 = (r'datasources/leaflets_pdf/bula_1701267208681_Bissulfato de clopidogrel.pdf')
    leaflet14 = (r'datasources/leaflets_pdf/bula_1701258821940_enalapril.pdf')
    leaflet15 = (r'datasources/leaflets_pdf/bula_1701268132552_Dipirona.pdf')
    leaflet16 = (r'datasources/leaflets_pdf/bula_1701268966313_Budesonida.pdf')
    leaflet17 = (r'datasources/leaflets_pdf/bula_1701269088550_Loratadina.pdf')
    leaflet18 = (r'datasources/leaflets_pdf/bula_1701266792068_Paracetamol.pdf')
    leaflet19 = (r'datasources/leaflets_pdf/bula_1701266990892_Varfarina.pdf')
    leaflet20 = (r'datasources/leaflets_pdf/bula_1701224718747_Cefalexina.pdf')
    leaflet21 = (r'datasources/leaflets_pdf/bula_1701224448044_Trimetoprima.pdf')
    leaflet22 = (r'datasources/leaflets_pdf/bula_1701631169096_Dexametasona.pdf')


    # # ibuprofeno - enalapril
    # calc21 = CalcSimilarity(leaflet1, leaflet14) # ibuprofeno e enalapril
    # calc21.measure_similarity_by_chunk()
    # calc21.measure_similarity_by_chunk_jaro()
    # calc21.measure_similarity_by_chunk_levenshtein()
    #
    # # hidroclorotiazida - captopril
    # calc22 = CalcSimilarity(leaflet5, leaflet9) # hidroclorotiazida e captopril
    # calc22.measure_similarity_by_chunk()
    # calc22.measure_similarity_by_chunk_jaro()
    # calc22.measure_similarity_by_chunk_levenshtein()

    # # captopril - fenobarbital
    # calc23 = CalcSimilarity(leaflet9, leaflet3) # captopril e fenobarbital
    # calc23.measure_similarity_by_chunk()
    # calc23.measure_similarity_by_chunk_jaro()
    # calc23.measure_similarity_by_chunk_levenshtein()

    # # hidroclorotiazida - budesonida
    # calc24 = CalcSimilarity(leaflet5, leaflet16) # hidroclorotiazida e budesonida
    # calc24.measure_similarity_by_chunk()
    # calc24.measure_similarity_by_chunk_jaro()
    # calc24.measure_similarity_by_chunk_levenshtein()

    # # dexametasona - albendazole
    # calc25 = CalcSimilarity(leaflet22, leaflet11) # dexametasona e albendazole
    # calc25.measure_similarity_by_chunk()
    # calc25.measure_similarity_by_chunk_jaro()
    # calc25.measure_similarity_by_chunk_levenshtein()

    # # # dexametasona - omepazol
    # calc26 = CalcSimilarity(leaflet22, leaflet12) # dexametasona e omepazol
    # calc26.measure_similarity_by_chunk()
    # calc26.measure_similarity_by_chunk_jaro()
    # calc26.measure_similarity_by_chunk_levenshtein()

    # # # dexametasona - ibuprofeno
    calc27 = CalcSimilarity(leaflet22, leaflet1) # dexametasona e ibuprofeno
    calc27.measure_similarity_by_chunk()
    calc27.measure_similarity_by_chunk_jaro()
    calc27.measure_similarity_by_chunk_levenshtein()

