

from interactions import InteractionParser
class SimilatyIndex:
        def __init__(self, leaflet1, leaflet2):
            self.leaflet1 = InteractionParser(leaflet1)
            self.leaflet2 = InteractionParser(leaflet2)
            print(self.leaflet1.get_interactions_flags())
        def get_similarity_index(self):
            """ Return the similarity index between two leaflets. """

            # Get the interactions flags of each leaflet
            interactions_flags1 = self.leaflet1.get_interactions_flags()
            interactions_flags2 = self.leaflet2.get_interactions_flags()

            # # Get the ATC code of each leaflet
            # atc_code1 = self.leaflet1.get_atc_code()[1]
            # atc_code2 = self.leaflet2.get_atc_code()[1]
            #
            # # Get the definition of each ATC code
            # definition1 = self.leaflet1.leaflet.get_definition_drug_section()
            # definition2 = self.leaflet2.leaflet.get_definition_drug_section()
            #
            # # Get the similarity index
            # similarity_index = 0
            # if atc_code1 == atc_code2:
            #     similarity_index += 1
            # if definition1 == definition2:
            #     similarity_index += 1
            # if interactions_flags1 == interactions_flags2:
            #     similarity_index += 1

            # return similarity_index
            # return interactions_flags1, interactions_flags2


if __name__ == '__main__':
    leaflet1 = InteractionParser(r'datasources/leaflets_pdf/bula_1689362421673_Amoxicilina.pdf')
    leaflet2 = InteractionParser(r'datasources/leaflets_pdf/bula_1700662857659_Ibuprofeno.pdf')
    similaty_index = SimilatyIndex(leaflet1, leaflet2)
