
class StopListInteraction:
    def __init__(self):

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
            "ouro", "inibidor", "inibidores", "inibidora", "inibidoras", "inibitório", "inibitórios", "inibitória",
            "exame", "exames", "examinado", "examinada", "examinados", "examinadas", "o exame", "os exames", "fez",
            "seguinte", "pesquisa", "pesquisas", "pesquisado", "pesquisada", "pesquisados", "pesquisadas",

        ]

    def get_stoplist_interactions(self):
        return self.stoplist_interactions

