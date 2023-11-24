

class LeafletSection:
    """
    This class is a container for the sections of the leaflet.
    """
    def __init__(self):
        self.main_section = [
            'IDENTIFICAÇÃO DO MEDICAMENTO',
            'INFORMAÇÕES AO PACIENTE',
            'DIZERES LEGAIS',
        ]
        # INFORMAÇÕES AO PACIENTE
        self.secondary_section = [
            "APRESENTAÇÃO", "APRESENTAÇÕES", "APRESENTAÇÕES COMERCIALIZADAS",
            # nesse intervalo são exibidas administração
            'COMPOSIÇÃO',
            "PARA QUE ESTE MEDICAMENTO É INDICADO?",
            "COMO ESTE MEDICAMENTO FUNCIONA?",
            "QUANDO NÃO DEVO USAR ESTE MEDICAMENTO?",
            "O QUE DEVO SABER ANTES DE USAR ESTE MEDICAMENTO?",# aqui encontra-se a secção de interações medicamentosas
            "ONDE, COMO E POR QUANTO TEMPO POSSO GUARDAR ESTE MEDICAMENTO?",
            "COMO DEVO USAR ESTE MEDICAMENTO?", #POSOLOGIA
            "O QUE DEVO FAZER QUANDO EU ME ESQUECER DE USAR ESTE MEDICAMENTO?",
            "QUAIS OS MALES QUE ESTE MEDICAMENTO PODE ME CAUSAR?",
            "O QUE FAZER SE ALGUÉM USAR UMA QUANTIDADE MAIOR DO QUE A INDICADA DESTE MEDICAMENTO?",
        ]
        self.administration = [
            "VIA DE ADMINISTRAÇÃO:"
            "USO ADULTO E PEDIÁTRICO",
            "USO ADULTO",
            "USO PEDIÁTRICO",
            "PEDIÁTRICO ACIMA DE 3 MESES.",
            "USO EM IDOSOS",
        ]

        self.infos_general = [
            "Após preparo",
            "modo de usar",

        ]

        self.alerts_general = [
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
            "Ligue para 0800 722 6001, se você precisar de mais orientações.", # TODO verificar se esse número é o mesmo para todos os medicamentos
            "Siga corretamente o modo de usar, não desaparecendo os sintomas procure orientação médica.",
            "contraindicado para"


        ],

        self.interactions_types = [
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

        self.what_i_should_know = [
            "Efeitos sobre a capacidade de dirigir veículos e de operar máquinas",
            "Gravidez e amamentação",
            "Uso em idosos, crianças e outros grupos de risco",
            "Interações medicamentosas",
            "Alterações na capacidade de dirigir veículos e operar máquinas",

            ]
        self.measures_units = ['mg', 'ml', 'g', 'mcg', 'ui', 'mg/ml', 'g/ml', 'mg/g', 'mg/ml,', 'q.s.p']
