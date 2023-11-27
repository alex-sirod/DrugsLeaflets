# https://www.paho.org/pt/oms-uma-organizacao-global-saude


ATC = {
    'A': [{
        "01": ["preparados estomatológicos (boca e dentes)",
               {"A": ["preparados estomatológicos",
                      {"A": "Agentes profiláticos contra cárie",
                       "B": "Antiinfecciosos e anti-sépticos para tratamento oral local",
                       "C": "Corticosteróides para tratamento oral local",
                       "D": "Outros agentes para tratamento oral local"}
                      ]}, ],

        "02": ["antiácidos, inibidores da secreção gástrica e tratamento das úlceras",
               {"A": "antiácidos",
                "B": "inibidores da secreção gástrica",
                "C": "tratamento das úlceras",
                }],

        "03": ["antiespasmódicos, anticolinérgicos e propulsivos",
               {"A": "Medicamentos para distúrbios gastrointestinais funcionais",
                "B": "BELADONA E DERIVADOS, SIMPLES",
                "C": "ANTISPASMÓDICOS EM COMBINAÇÃO COM PSICOLÉPTICOS",
                "D": "ANTISPASMÓDICOS EM COMBINAÇÃO COM ANALGÉSICOS",
                "E": "ANTISPASMÓDICOS E ANTICOLINÉRGICOS EM COMBINAÇÃO COM OUTRAS MEDICAMENTOS",
                "F": "PROPULSIVOS",
                }],

        "04": ["antieméticos e antinauseantes",
               {"A": ["ANTIEMÉTICOS E ANTINAUSEANTES",
                      {"A": "Antagonistas da serotonina (5HT3)",
                       "D": "Outros antieméticos",
                       }], }],

        "05": ["tratamento biliar e hepático",
               {"A": ["TERAPIA BILE"],
                "B": ["TERAPIA DO FÍGADO, LIPOTRÓPICOS"],
                "C": ["MEDICAMENTOS PARA TERAPIA BILE E LIPOTRÓPICOS EM COMBINAÇÃO"]
                }],

        "06": ["laxativos",
               {"A": ["Medicamentos para constipação"],
                }],

        "07": ["antidiarréicos, anti-inflamatórios e anti-infecciosos intestinais",
               {"A": ["ANTIINFECCIOSOS INTESTINAIS"],
                "B": ["ADSORVENTES INTESTINAIS"],
                "C": ["ELETRÓLITOS COM CARBOIDRATOS"],
                "D": ["ANTIPROPULSIVOS"],
                "E": ["AGENTES ANTIINFLAMATÓRIOS INTESTINAIS"],
                "F": ["MICRORGANISMOS ANTIDIARRÉICOS"],
                "X": ["OUTROS ANTIDIARRÉICOS"],
                }],

        "08": ["preparados antiobesidade",
               {"A": ["PREPARAÇÕES ANTIOBESIDADE"],  # (EXCLUINDO DIETAS)"],
                }],

        "09": ["digestivos e enzimas digestivas",
               {"A": ["digestivos e enzimas digestivas"],
                }],

        "10": ["medicamentos utilizados na diabetes",
               {"A": ["INSULINAS E ANÁLOGOS"],
                "B": ["MEDICAMENTOS PARA REDUÇÃO DA GLICOSE NO SANGUE, exceto INSULINAS"],
                "X": ["OUTROS MEDICAMENTOS USADOS NO DIABETES"],
                }],

        "11": ["vitaminas e associações",
               {"A": ["MULTIVITAMINAS, COMBINAÇÕES"],
                "B": ["MULTIVITAMINAS, SIMPLES"],
                "C": ["VITAMINAS A E D, inclusive. COMBINAÇÕES DOS DOIS"],
                "D": ["VITAMINA B1, SIMPLES E EM COMBINAÇÃO COM VITAMINA B6 E B12"],
                "E": ["COMPLEXO DE VITAMINA B, inclusive COMBINAÇÕES"],
                "G": ["ÁCIDO ASCÓRBICO (VITAMINA C), inclusive COMBINAÇÕES"],
                "H": ["OUTRAS PREPARAÇÕES DE VITAMINAS SIMPLES"],
                "J": ["OUTROS PRODUTOS VITAMINOSOS, COMBINAÇÕES"],
                }],

        "12": ["suplementos minerais e associações",
               {"A": ["CÁLCIO"],
                "B": ["POTÁSSIO"],
                "C": ["OUTROS SUPLEMENTOS MINERAIS"],
                }],

        "13": ["tônicos e repositores hidroeletrolíticos orais",
               {"A": ["Tônicos"],
                }],

        "14": ["anabolizantes para o uso sistêmico",
               {"A": ["ESTEROIDES anabolizantes"],
                "B": ["OUTROS AGENTES ANABÓLICOS"],
                }],

        "15": ["estimulantes do apetite"],

        "16": ["outros medicamentos para o sistema digestivo e o metabolismo",
               {"A": ["outros medicamentos para o sistema digestivo e o metabolismo"],
                }],
    }, ],  # Fim do grupo A

    'B': [
        {"01": ["anticoagulantes, antitrombóticos e trombolíticos",
                {"A": ["anticoagulantes e antitrombóticos"], }
                ],

         "02": ["anti-hemorrágicos, fatores de coagulação e correlatos",
                {"A": ["ANTIFIBRINOLÍTICOS"], }
                ],

         "03": ["preparados antianêmicos",
                {"A": ["PREPARAÇÕES DE FERRO"],
                 "B": ["VITAMINA B12 E ÁCIDO FÓLICO"],
                 "X": ["OUTRAS PREPARAÇÕES ANTIANÊMICAS"],
                 }],

         "05": ["hemodiálises, diálises e soluções para perfusão e irrigação",
                {"A": ["sangue e produtos relacionados"],
                 "B": ["soluções intravenosas"],
                 "C": ["soluções de irrigação"],
                 "D": ["diálise peritoneal"],
                 "X": ["aditivos de solução intravenosa"],
                 "Z": ["hemodiálise e hemofiltração"],

                 }],

         "05BA": ["nutrição parenteral"],

         "06": ["outros preparados hematológicos",
                {"A": ["outros preparados hematológicos"],
                 }],
         }, ],  # Fim do grupo B

    'C': [{
        "01": ["estimulantes cardíacos, cardiotônicos e glicosídeos",
               {"A": ["GLICOSÍDEOS CARDÍACOS"],
                "B": ["ANTIARRÍTMICOS CLASSE I E III"],
                "C": ["ESTIMULANTES CARDÍACOS exceto GLICOSÍDEOS CARDÍACOS"],
                "D": ["VASODILATADORES USADOS EM DOENÇAS CARDÍACAS"],
                "E": ["OUTRAS PREPARAÇÕES CARDÍACAS"],
                }],

        "02": ["anti-hipertensivos",
               {"A": ["AGENTES ANTIADRENERGICOS DE ATUAÇÃO CENTRAL"],
                "B": ["AGENTES ANTIADRENERGICOS, BLOQUEADORES DE GÂNGLIOS"],
                "C": ["AGENTES ANTIADRENERGICOS DE ATUAÇÃO PERIFÉRICA"],
                "D": ["MÚSCULO LISO ARTERIOLAR, AGENTES ATUANDO"],
                "K": ["OUTROS ANTI-HIPERTENSIVOS"],
                "L": ["ANTI-HIPERTENSIVOS E DIURÉTICOS EM COMBINAÇÃO"],
                "N": ["COMBINAÇÕES DE ANTI-HIPERTENSIVOS EM ATC-GR. C02"],

                }],

        "03": ["diuréticos",
               {"A": ["DIURÉTICOS DE BAIXO TETO, TIAZIDAS"],
                "B": ["DIURÉTICOS DE BAIXO TETO, exceto TIAZIDAS"],
                "C": ["DIURÉTICOS DE TETO ALTO"],
                "D": ["ANTAGONISTAS DA ALDOSTERONA E OUTROS AGENTES POUPADORES DE POTÁSSIO"],
                "E": ["DIURÉTICOS E AGENTES POUPADORES DE POTÁSSIO EM COMBINAÇÃO"],
                "X": ["OUTROS DIURÉTICOS"],
                }],

        "04": ["vasodilatadores periféricos", {
            "A": ["VASODILATADORES PERIFÉRICOS"],
        }],

        "05": ["vasoprotetores", {
            "A": ["Agentes para o tratamento de hemorróidas e fissuras anais para uso tópico"],
            "B": ["Terapia antivaricose"],
            "C": ["Agentes estabilizadores capilares"],
        }],

        "07": ["]beta-bloqueadores", {
            "A": ["AGENTES BLOQUEADORES BETA"],
            "B": ["AGENTES BLOQUEADORES BETA E TIAZIDAS"],
            "C": ["AGENTES BLOQUEADORES BETA E OUTROS DIURÉTICOS"],
            "D": ["AGENTES BLOQUEADORES BETA, TIAZIDAS E OUTROS DIURÉTICOS"],
            "E": ["AGENTES BLOQUEADORES BETA E VASODILATADORES"],
            "F": ["AGENTES BLOQUEADORES BETA, OUTRAS COMBINAÇÕES"],

        }],

        "08": ["bloqueadores de canal de cálcio", {
            "C": ["BLOQUEADORES DE CANAIS DE CÁLCIO COM EFEITOS PRINCIPALMENTE VASCULARES"],
            "D": ["BLOQUEADORES SELETIVOS DE CANAIS DE CÁLCIO COM EFEITOS CARDÍACOS DIRETOS"],
            "E": ["BLOQUEADORES DE CANAIS DE CÁLCIO NÃO SELETIVOS"],
            "G": ["BLOQUEADORES DE CANAIS DE CÁLCIO E DIURÉTICOS"],
        }],

        "09": ["sistema renina-angiotensina", {
            "A": ["INIBIDORES ECA, SIMPLES"],
            "B": ["INIBIDORES DA ECA, COMBINAÇÕES"],
            "C": ["BLOQUEADORES DO RECEPTOR DE ANGIOTENSINA II (BRA), SIMPLES"],
            "D": ["BLOQUEADORES DO RECEPTOR DE ANGIOTENSINA II (BRA), COMBINAÇÕES"],
            "X": ["OUTROS AGENTES QUE ATUAM NO SISTEMA RENINA-ANGIOTENSINA"],
        }],

        "10": ["hipolipemiantes", {
            "A": ["Agentes modificadores de lipídeos, simples"],
            "B": ["Agentes modificadores de lipídeos, combinações"],
        }],

    }, ],  # Fim do grupo C

    'D': [{
        "01": ["anti-infecciosos, antibióticos e anti-inflamatórios tópicos",
               {"A": ["ANTIFÚNGICOS TÓPICOS"],
                "B": ["ANTIFÚNGICOS PARA USO SISTÊMICO"],
                }],

        "02": ["emolientes, hidratantes, protetores e filtro solar",
               {"A": ["EMOLIENTES E HIDRATANTES"],
                "B": ["PROTETORES CONTRA RADIAÇÃO UV"],
                }],

        "03": ["tratamento de feridas e úlceras",
               {"A": ["CICATRIZANTES"],
                "B": ["enzimas"],
                }],

        "04": ["antipuriginosos",
               {"A": ["ANTIPRURÍTICOS, INCLUINDO ANTI-HISTAMÍNICOS, ANESTÉSICOS, ETC."],
                }],

        "05": ["antipsoriáticos",
               {"A": ["ANTIPSORIÁTICOS PARA USO TÓPICO"],
                "B": ["ANTIPSORIÁTICOS PARA USO SISTÊMICO"],
                }],
        "06": ["ANTIBIÓTICOS E QUIMIOTERAPÊUTICOS PARA USO DERMATOLÓGICO",
               {"A": ["ANTIBIÓTICOS PARA USO TÓPICO"],
                "B": ["QUIMIOTERAPÊUTICOS PARA USO TÓPICO"],
                "C": ["ANTIBIÓTICOS E QUIMIOTERAPÊUTICOS, COMBINAÇÕES"],
                }],

        "07": ["corticosteróides, dermatológicos",
               {"A": ["CORTICOSTEROIDES simples, MONOPREPARAÇÕES"],
                "B": ["CORTICOSTEROIDES, COMBINAÇÕES COM ANTISSÉPTICOS"],
                "C": ["CORTICOSTEROIDES, COMBINAÇÕES COM ANTIBIÓTICOS"],
                "X": ["CORTICOSTEROIDES, OUTRAS COMBINAÇÕES"],
                }],

        "08": ["antissépticos e desinfetantes",
               {"A": ["ANTISSÉPTICOS E DESINFETANTES"],
                }],

        "10": ["antiacneicos", {
            "A": ["PREPARAÇÕES ANTI-ACNE PARA USO TÓPICO"],
            "B": ["PREPARAÇÕES ANTI-ACNE PARA USO SISTÊMICO"],
        }],

        "11": ["outros preparados dermatológicos", {
            "A": ["OUTROS PREPARADOS DERMATOLÓGICOS"],
        }],
    }, ],  # Fim do grupo D

    'G': [{
        "01": ["anti-infecciosos e antissépticos ginecológicos", {
            "A": ["ANTIINFECTIVOS E ANTISSÉPTICOS, EXCL. COMBINAÇÕES COM CORTICOSTERÓIDES"],
            "B": ["ANTIINFECTIVOS/ANTISSÉPTICOS EM COMBINAÇÃO COM CORTICOSTERÓIDES"],
        }],

        "02": ["outros preparados ginecológicos", {
            "A": ["UTEROTÔNICOS"],
            "B": ["CONTRACEPTIVOS PARA USO TÓPICO"],
            "C": ["OUTROS GINECOLÓGICOS"],
        }],

        "03": ["anticoncepcionais, hormônios sexuais e moduladores do sistema genital", {
            "A": ["ANTICONCEPCIONAIS HORMONAIS PARA USO SISTÊMICO"],
            "B": ["ANDRÓGENOS"],
            "C": ["ESTRÓGENOS"],
            "D": ["PROGESTOGÊNIOS"],
            "E": ["ANDRÓGENOS E HORMÔNIOS SEXUAIS FEMININOS EM COMBINAÇÃO"],
            "F": ["PROGESTOGÊNIOS E ESTROGÊNIOS EM COMBINAÇÃO"],
            "G": ["GONADOTROFINAS E OUTROS ESTIMULANTES DE OVULAÇÃO"],
            "H": ["ANTIANDRÓGENOS"],
            "X": ["OUTROS HORMÔNIOS SEXUAIS E MODULADORES DO SISTEMA GENITAL"],
        }],

        "04": ["medicamentos urológicos", {
            "A": ["PREPARAÇÕES PARA O TRATAMENTO DA INCONTINÊNCIA URINÁRIA"],
            "B": ["UROLÓGICOS"],
            "C": ["DROGAS USADAS NA HIPERTROFIA PROSTÁTICA BENIGNA"],
        }],
    }, ],  # Fim do grupo G

    'H': [{
        "01": ["hormônios, hipofisários hipotalâmicos e análogos", {
            "A": ["HORMÔNIOS E ANÁLOGOS DO LOBO PITUITÁRIO ANTERIOR"],
            "B": ["HORMÔNIOS DO LOBO PITUITÁRIO POSTERIOR"],
            "C": ["HORMÔNIOS HIPOTALÂMICOS"],
        }],

        "02": ["corticoesteróides sistêmicos", {

            "A": ["CORTICOSTEROIDES PARA USO SISTÊMICO, SIMPLES"],
            "B": ["CORTICOSTEROIDES PARA USO SISTÊMICO, COMBINAÇÕES"],
            "C": ["PREPARAÇÕES ANTIADRENAIS"],
        }],

        "03": ["tratamento da tireoide", {
            "A": ["PREPARAÇÕES DA TIREÓIDE"],
            "B": ["PREPARAÇÕES ANTICIREÓIDES"],
            "C": ["TERAPIA COM IODO"],
        }],

        "04": ["hormônios pancreáticos", {
            "A": ["HORMÔNIOS GLICOGENOLÍTICOS"],
        }],

        "05": ["medicamentos relacionados à homeostasia do cálcio", {
            "A": ["HORMÔNIOS PARATIREÓIDEOS E ANÁLOGOS"],
            "B": ["AGENTES ANTI-PARATIREÓIDES"],

        }],

    }, ],  # Fim do grupo H

    'J': [{
        "01": ["antibacterianos sistêmicos", {
            "A": ["TETRACICLINAS"],
            "B": ["AMFENÍCOLOS"],
            "C": ["ANTIBACTERIANOS BETA-LACTAM, PENICILINAS"],
            "D": ["OUTROS ANTIBACTERIANOS BETA-LACTAM"],
            "E": ["SULFONAMIDAS E TRIMETHOPRIMA"],
            "F": ["MACROLÍDEOS, LINCOSAMIDAS E ESTREPTOGRAMINAS"],
            "G": ["ANTIBACTERIANOS AMINOGLICOSÍDEOS"],
            "M": ["ANTIBACTERIANOS QUINOLONAS"],
            "R": ["COMBINAÇÕES DE ANTIBACTERIANOS"],
            "X": ["OUTROS ANTIBACTERIANOS"],
        }],

        "02": ["antifúngicos sistêmicos", {
            "A": ["ANTIMICÓTICOS PARA USO SISTÊMIC"]
        }],

        "04": ["antimicobacterianos sistêmicos", {
            "A": ["medicamento para o tratamento da tuberculose"],
            "B": ["medicamento para o tratamento da lepra"],
        }],

        "05": ["antivirais sistêmicos", {
            "A": ["ANTIVIRAIS de ação direta"],
        }],

        "06": ["imunossoros e imunoglobulinas", {
            "A": ["SOROS IMUNE, IMUNOSSOROS"],
            "B": ["IMUNOGLOBULINAS"],
        }],

        "07": ["vacinas",{
            "A": ["VACINAS BACTERIANAS"],
            "B": ["VACINAS VIRAIS"],
            "C": ["VACINAS BACTERIANAS E VIRAIS, COMBINADAS"],
            "X": ["OUTRAS VACINAS"],
        }],
    }, ],  # Fim do grupo J


    'L': {
        "01": "antineoplásicos",
        "02": "terapias endócrinas",
        "03": "imunoestimulantes",
        "04": "imunossupressores"
    },
    'M': {
        "01": "anti-inflamatórios e antirreumáticos",
        "02": "produtos tópicos para dores articulares e musculares",
        "03": "relaxantes musculares",
        "04": "antigotosos",
        "05": "tratamento de doenças ósseas",
        "09": "outros medicamentos para o sistema músculo-esquelético"
    },
    'N': {
        "01": "anestésicos",
        "02": "analgésicos",
        "03": "antiepiléticos",
        "04": "antiparksonianos",
        "05A": "antipsicóticos",
        "05B": "ansiolíticos",
        "05C": "hipnóticos e sedativos",
        "06A": "antidepressivos",
        "06B": "psicoestimulantes",
        "06C": "psicoléticos e psicoanapléticos em associação",
        "06D": "tratamento do Alzheimer e demência",
        "07": "outros medicamentos para o sistema nervoso"
    },
    'P': {
        "01": "antiprotozoários",
        "02": "anti-helmínticos",
        "03": "inseticidas, repelentes, escabicidas e ectoparasiticidas"
    },
    'R': {
        "01": "preparados para o uso nasal",
        "02": "preparados para o uso faríngeo",
        "03": "antiasmáticos",
        "05": "medicamentos para tosse e resfriado",
        "06": "anti-histamínicos sistêmicos",
        "07": "outros medicamentos para o sistema respiratório"
    },
    'S': {
        "01": "produtos oftálmicos",
        "02": "produtos otológicos"
    },
    'V': {
        "03AB": "antídotos, agentes desintoxicantes e agentes quelantes",
        "03AN": "gases medicinais",
        "04": "testes e agentes de diagnóstico",
        "07A": "equipamentos, reagentes, solventes e outros insumos farmacêuticos",
        "08": "meios de contraste",
        "10": "radiofármacos",
        "03": "outros produtos terapêuticos",
        "": "antroposóficos, fitoterápicos e homeopáticos fórmulas ou associações manipuladas, medicamentos veterinários"

    }
}

ATC_LABELS = [{"A": "SISTEMA DIGESTIVO E METABOLISMO"},
              {"B": "SANGUE E ÓRGÃOS HEMATOPOIÉTICOS"},
              {"C": "SISTEMA CARDIOVASCULAR"},
              {"D": "PELE E ANEXOS"},
              {"G": "SISTEMA GENITURINÁRIO E HORMÔNIOS SEXUAIS"},
              {"H": "HORMÔNIOS SISTÊMICOS"},
              {"J": "ANTI-INFECCIOSOS DE USO SISTÊMICO"},
              {"L": "ANTINEOPLÁSICOS E IMUNOMODULADORES"},
              {"M": "SISTEMA MÚSCULO-ESQUELÉTICO"},
              {"N": "SISTEMA NERVOSO"},
              {"P": "ANTI-PARASITÁRIOS, INSETICIDAS E REPELENTES"},
              {"R": "SISTEMA RESPIRATÓRIO"},
              {"S": "ÓRGÃOS DO SENTIDO"},
              {"V": "VÁRIOS"}]

# if __name__ == '__main__':
#     print("-----------------------------------------------------------")
#     print("ATC - Anatomical Therapeutic Chemical Classification System")
#     print("-----------------------------------------------------------")
#     print("A - SISTEMA DIGESTIVO E METABOLISMO")
#     print("B - SANGUE E ÓRGÃOS HEMATOPOIÉTICOS")
#     print("C - SISTEMA CARDIOVASCULAR")
#     print("D - PELE E ANEXOS")
#     print("G - SISTEMA GENITURINÁRIO E HORMÔNIOS SEXUAIS")
#     print("H - HORMÔNIOS SISTÊMICOS")
#     print("J - ANTI-INFECCIOSOS DE USO SISTÊMICO")
#     print("L - ANTINEOPLÁSICOS E IMUNOMODULADORES")
#     print("M - SISTEMA MÚSCULO-ESQUELÉTICO")
#     print("N - SISTEMA NERVOSO")
#     print("P - ANTI-PARASITÁRIOS, INSETICIDAS E REPELENTES")
#     print("R - SISTEMA RESPIRATÓRIO")
#     print("S - ÓRGÃOS DO SENTIDO")
#     print("V - VÁRIOS")
#     print("0 - EXIT")
#     print("--------------------------------------------------------")
#     group = input(str("Type a letter to show or zero to exit and press <enter>: "))

# Teste de impressão para verificar a estrutura do dicionário resultante
# print(ATC)

print(ATC['A'][0])
print(ATC['A'][0]['01'])
print(ATC['A'][0]['03'][1]['A'])
print(ATC['A'][0]['05'][1]['B'])
print(ATC['A'][0]['06'][1]['A'])
print(ATC['A'][0]['07'][1]['A'])
print(ATC['A'][0]['08'][1]['A'])
print(ATC['A'][0]['09'][1]['A'])
print(ATC['A'][0]['10'][1]['A'])
print(ATC['A'][0]['11'][1]['A'])
print(ATC['A'][0]['12'][1]['A'])
print(ATC['A'][0]['13'][1]['A'])
print(ATC['A'][0]['14'][1]['A'])
print(ATC['A'][0]['15'][0])
print(ATC['A'][0]['16'])
print(ATC['B'][0]['01'][1]['A'])
print(ATC['B'][0]['02'][1]['A'])
print(ATC['B'][0]['03'][1]['A'])
print(ATC['B'][0]['05'][1]['A'])
print(ATC['B'][0]['05BA'])
print(ATC['B'][0]['06'][1]['A'])
print(ATC['C'][0]['01'][1]['A'])
print(ATC['C'][0]['02'][1]['A'])
print(ATC['C'][0]['03'][1]['A'])
print(ATC['C'][0]['04'][1]['A'])
print(ATC['C'][0]['05'][1]['A'])
print(ATC['C'][0]['07'][1]['A'])
print(ATC['C'][0]['08'][1]['C'])
print(ATC['C'][0]['09'][1]['A'])
print(ATC['C'][0]['10'][1]['A'])
print(ATC['C'][0]['10'][1]['B'])
print(ATC['D'][0]['01'][1]['A'])
print(ATC['D'][0]['02'][1]['A'])
print(ATC['D'][0]['03'][1]['A'])
print(ATC['D'][0]['04'][1]['A'])
print(ATC['D'][0]['05'][1]['A'])
print(ATC['G'][0]['01'][1]['A'])
