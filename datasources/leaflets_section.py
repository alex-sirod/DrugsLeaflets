
class LeafletSection:
    """
    This class is a container for the sections of the leaflet.
    """
    def __init__(self):
        self.MAIN_SECTION = [
            "IDENTIFICAÇÃO DO MEDICAMENTO",
            "INFORMAÇÕES AO PACIENTE",
            "DIZERES LEGAIS",
        ]
        # INFORMAÇÕES AO PACIENTE
        self.SECONDARY_SECTION = [
            "APRESENTAÇÃO", "APRESENTAÇÕES", "APRESENTAÇÕES COMERCIALIZADAS",
            # nesse intervalo são exibidas administração
            'COMPOSIÇÃO',
            "PARA QUE ESTE MEDICAMENTO É INDICADO?",
            "COMO ESTE MEDICAMENTO FUNCIONA?",
            "QUANDO NÃO DEVO USAR ESTE MEDICAMENTO?",
            "O QUE DEVO SABER ANTES DE USAR ESTE MEDICAMENTO?",
            # aqui encontra-se a secção de interações medicamentosas
            "ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO?",
            "COMO DEVO USAR ESTE MEDICAMENTO?",  # POSOLOGIA
            "O QUE DEVO FAZER QUANDO EU ME ESQUECER DE USAR ESTE MEDICAMENTO?",
            "QUAIS OS MALES QUE ESTE MEDICAMENTO PODE ME CAUSAR?",
            "O QUE FAZER SE ALGUÉM USAR UMA QUANTIDADE MAIOR DO QUE A INDICADA DESTE MEDICAMENTO?",
        ]

        self.GENERAL_WARNINGS = [
            "Este medicamento não deve ser usado por mulheres grávidas sem orientação médica ou do cirurgião-dentista.",
            "Informe ao seu médico ou cirurgião-dentista se você está fazendo uso de algum outro medicamento."
            "Não use medicamento sem o conhecimento do seu médico. Pode ser perigoso para a sua saúde.",
            "atenção",
            "Número de lote e datas de fabricação e validade: vide embalagem.",
            "Não use medicamento com o prazo de validade vencido. Guarde-o em sua embalagem original.",
            "Antes de usar, observe o aspecto do medicamento.",
            "TODO MEDICAMENTO DEVE SER MANTIDO FORA DO ALCANCE DAS CRIANÇAS.",
            "Em caso de dúvidas, procure orientação do farmacêutico ou de seu médico, ou cirurgião-dentista.",
            "Informe ao seu médico, cirurgião - dentista ou farmacêutico o aparecimento de reações indesejáveis pelo uso do medicamento.",
            "Informe também à empresa através do seu serviço de atendimento.",
            "Em caso de uso de grande quantidade deste medicamento, procure rapidamente socorro médico e leve a embalagem ou bula do medicamento, se possível.",
            "Ligue para 0800 722 6001, se você precisar de mais orientações.",
            # TODO verificar se esse número é o mesmo para todos os medicamentos
            "Siga corretamente o modo de usar, não desaparecendo os sintomas procure orientação médica.",
            "contraindicado para"
        ],

        self.INTERACTION_TYPES = [
            "Interações medicamentosas",
            "Interação com alimentos",
            "Interação com álcool",
            "Interação com testes laboratoriais",
            "Interação medicamento-substância química",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-alimento",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
            "Interação medicamento-bebida alcoólica",
            "Interação medicamento-álcool",
            "Interação medicamento-tabaco",
            "Interação medicamento-plantas medicinais",
            "Interação medicamento-exame laboratorial",
            "Interação medicamento-substância química",
        ]

        self.MEASURE_UNITS = ["mg", "ml", "g", "mcg", "ui", "mg/ml", "g/ml", "mg/g", "mg/ml", "q.s.p", "qsp"]

        self.PRESENTATION = ["cápsula", "comprimido", "cápsulas", "comprimidos", "drágea", "drágeas",
                             "solução", "solução oral", "solução injetável",
                             "solução nasal", "solução oftálmica", "solução otológica", "suspensão", "suspensão oral",
                             "suspensão injetável", "suspensão nasal", "suspensão oftálmica", "suspensão otológica",
                             "pó", "pó para solução", "pó para solução injetável", "pó para solução oral", "pó oral",
                             "pó para solução nasal", "pó para solução oftálmica", "pó para solução otológica",
                             "pó para suspensão oral", "pó para suspensão injetável", "pó para suspensão nasal",
                             "pó para suspensão oftálmica", "pó para suspensão otológica", "pó para solução oral",
                             "pó para solução injetável", "pó para solução nasal", "pó para solução oftálmica",
                             "pó para solução otológica", "pó para suspensão oral", "pó para suspensão injetável",
                             "pó para suspensão nasal", "pó para suspensão oftálmica", "pó para suspensão otológica",
                             "pó para solução oral", "pó para solução injetável", "pó para solução nasal",
                             "pó para solução oftálmica", "pó para solução otológica", "pó para suspensão oral",
                             "pó para suspensão injetável", "pó para suspensão nasal", "pó para suspensão oftálmica",
                             "pó para suspensão otológica", "pó para solução oral", "pó para solução injetável",
                             "pó para solução nasal", "pó para solução oftálmica", "pó para solução otológica",
                             "pó para suspensão oral", "pó para suspensão injetável", "pó para suspensão nasal",
                             "pó para suspensão oftálmica", "pó para suspensão otológica"]
