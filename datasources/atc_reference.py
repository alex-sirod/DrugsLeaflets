# https://www.paho.org/pt/oms-uma-organizacao-global-saude

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
               {"A": ["antiácidos"],
                "B": ["inibidores da secreção gástrica"],
                "C": ["tratamento das úlceras"],
                }],

        "03": ["antiespasmódicos, anticolinérgicos e propulsivos",
               {"A": ["Medicamentos para distúrbios gastrointestinais funcionais"],
                "B": ["BELADONA E DERIVADOS, SIMPLES"],
                "C": ["ANTISPASMÓDICOS EM COMBINAÇÃO COM PSICOLÉPTICOS"],
                "D": ["ANTISPASMÓDICOS EM COMBINAÇÃO COM ANALGÉSICOS"],
                "E": ["ANTISPASMÓDICOS E ANTICOLINÉRGICOS EM COMBINAÇÃO COM OUTRAS MEDICAMENTOS"],
                "F": ["PROPULSIVOS"],
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

         "05B": ["nutrição parenteral"],

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

        "07": ["beta-bloqueadores", {
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

        "07": ["vacinas", {
            "A": ["VACINAS BACTERIANAS"],
            "B": ["VACINAS VIRAIS"],
            "C": ["VACINAS BACTERIANAS E VIRAIS, COMBINADAS"],
            "X": ["OUTRAS VACINAS"],
        }],
    }, ],  # Fim do grupo J

    'L': [{
        "01": ["antineoplásicos", {
            "A": ["AGENTES ALQUILANTES"],
            "B": ["ANTIMETABOLITOS"],
            "C": ["ALCALOIDES DE PLANTAS E OUTROS PRODUTOS NATURAIS"],
            "D": ["ANTIBIÓTICOS CITOTÓXICOS E SUBSTÂNCIAS RELACIONADAS"],
            "E": ["INIBIDORES DE PROTEÍNA QUINASE"],
            "F": ["ANTICORPOS MONOCLONAIS E CONJUGADOS DE ANTICORPOS DROGAS"],
            "X": ["OUTROS ANTINEOPLÁSICOS"],
        }],

        "02": ["terapias endócrinas", {
            "A": ["HORMÔNIOS E AGENTES RELACIONADOS"],
            "B": ["ANTAGONISTAS HORMÔNICOS E AGENTES RELACIONADOS"],
        }],

        "03": ["imunoestimulantes", {
            "A": ["IMUNOESTIMULANTES"],
        }],

        "04": ["imunossupressores", {
            "A": ["IMUNOSSUPRESSORES , IMUNOSSUPRESSANTES"],
        }],
    }, ],  # Fim do grupo L

    'M': [{
        "01": ["anti-inflamatórios e antirreumáticos", {
            "A": ["PRODUTOS ANTIINFLAMATÓRIOS E ANTIRREUMÁTICOS, NÃO ESTERÓIDES"],
            "B": ["AGENTES ANTIINFLAMATÓRIOS/ANTIRREUMÁTICOS EM COMBINAÇÃO"],
            "C": ["AGENTES ANTIRREUMÁTICOS ESPECÍFICOS"],

        }],

        "02": ["produtos tópicos para dores articulares e musculares", {
            "A": ["PRODUTOS TÓPICOS PARA DORES ARTICULARES E MUSCULARES"],
        }],

        "03": ["relaxantes musculares", {
            "A": ["RELAXANTES MUSCULARES, AGENTES DE ATUAÇÃO PERIFÉRICA"],
            "B": ["RELAXANTES MUSCULARES, AGENTES DE ATUAÇÃO CENTRAL"],
            "C": ["RELAXANTES MUSCULARES, AGENTES DE AÇÃO DIRETA"],
        }],

        "04": ["antigotosos", {
            "A": ["ANTIGOTOSOS"],
        }],

        "05": ["tratamento de doenças ósseas", {
            "B": ["OUTROS MEDICAMENTOS PARA O TRATAMENTO DE DOENÇAS ÓSSEAS"],
        }],

        "09": ["outros medicamentos para o sistema músculo-esquelético", {
            "A": ["OUTROS MEDICAMENTOS PARA O SISTEMA MÚSCULO-ESQUELÉTICO"],
        }],
    }, ],  # Fim do grupo M

    'N': [{
        "01": ["anestésicos", {
            "A": ["ANESTÉSICOS GERAIS"],
            "B": ["ANESTÉSICOS LOCAIS"],
        }],

        "02": ["analgésicos", {
            "A": ["OPIOIDES"],
            "B": ["OUTROS ANALGÉSICOS E ANTIPIRÉTICOS"],
            "C": ["PREPARAÇÕES ANTIMIGRÂNICAS"],
        }],

        "03": ["antiepiléticos anticonvulsionantes", {
            "A": ["ANTIEPILÉTICOS"],
        }],
        "04": ["antiparksonianos", {
            "A": ["AGENTES ANTICOLINÉRGICOS"],
            "B": ["AGENTES DOPAMINÉRGICOS"],
            "C": ["OUTROS MEDICAMENTOS ANTIPARKINSON"],
        }],

        "05": ["antipsicóticos", {
            "A": ["ANTIPSICÓTICOS"],
            "B": ["Anxiolíticos"],
            "C": ["Hipnóticos e sedativos"],
        }],

        "06A": ["antidepressivos", {

            "A": ["ANTIDEPRESSIVOS"],
            "B": ["PSICOESTIMULANTES, AGENTES USADOS PARA TDAH E NOOTRÓPICOS"],
            "C": ["PSICOLÉPTICOS E PSICANALÉPTICOS EM COMBINAÇÃO"],
            "D": ["MEDICAMENTOS ANTI-DEMÊNCIA"],
        }],

        "07": ["outros medicamentos para o sistema nervoso", {
            "A": ["PARASIMPATHOMIMÉTICOS"],
            "B": ["DROGAS USADAS EM TRANSTORNOS ADICIONAIS"],
            "C": ["AGENTES ANTIVERTIGO"],
            "X": ["OUTROS MEDICAMENTOS PARA O SISTEMA NERVOSO"],
        }],
    }, ],  # Fim do grupo N

    'P': [{
        "01": ["antiprotozoários", {
            "A": ["AGENTES CONTRA AMEBÍASE E OUTRAS DOENÇAS PROTOZOÁRIAS"],
            "B": ["ANTIMALÁRICOS"],
            "C": ["AGENTES CONTRA LEISHMANIOSE E TRIPANOSSOMOSE"],
        }],

        "02": ["anti-helmínticos", {

            "A": ["ANTITREMATÓDICOS"],
            "B": ["ANTINEMATÓDICOS"],
            "C": ["ANTICESTODAIS"],
        }],

        "03": ["inseticidas, repelentes, escabicidas e ectoparasiticidas", {
            "A": ["ECTOPARASITICIDAS, inclusive ESCABICIDAS"],
            "B": ["INSECTICIDAS E REPELENTES"],
        }],

    }, ],  # Fim do grupo P

    'R': [{
        "01": ["preparados para o uso nasal", {
            "A": ["DESCONGESTANTES E OUTRAS PREPARAÇÕES NASAIS PARA USO TÓPICO"],
            "B": ["CORTICOSTEROIDES PARA USO NASAL,  DESCONGESTANTES NASAIS PARA USO SISTÊMICO"],
        }],

        "02": ["preparados para o uso faríngeo", {
            "A": ["PREPARAÇÕES PARA O TRATAMENTO DA DOR DE GARGANTA"],
        }],

        "03": ["antiasmáticos", {
            "A": ["MEDICAMENTOS PARA DOENÇAS OBSTRUTIVAS DAS VIAS AÉREAS"],
            "B": ["OUTROS MEDICAMENTOS PARA DOENÇAS OBSTRUTIVAS DAS VIAS AÉREAS"],
            "C": [" ADRENÉRGICOS PARA USO SISTÊMICO"],
            "D": ["OUTROS MEDICAMENTOS SISTÊMICOS PARA DOENÇAS OBSTRUTIVAS DAS VIAS AÉREAS"],
        }],

        "05": ["medicamentos para tosse e resfriado", {
            "C": ["EXPETORANTES, EXCL. COMBINAÇÕES COM SUPRESSANTES PARA TOSSE"],
            "D": ["EXPECTORANTES E SUPRESSANTES PARA TOSSE EM COMBINAÇÃO"],
            "F": ["SUPRESSANTES PARA TOSSE E EXPECTORANTES EM COMBINAÇÃO"],
            "X": ["OUTROS MEDICAMENTOS PARA TOSSE E RESFRIADO"],

        }],

        "06": ["anti-histamínicos sistêmicos", {
            "A": ["ANTIHISTAMÍNICOS PARA USO SISTÊMICO"],
        }],

        "07": ["outros medicamentos para o sistema respiratório", {
            "A": ["OUTROS MEDICAMENTOS PARA O SISTEMA RESPIRATÓRIO"],
        }],
    }, ],  # Fim do grupo R

    'S': [{
        "01": ["produtos oftálmicos", {
            "A": ["ANTIINFECCIOSOS"],
            "B": ["AGENTES ANTIINFLAMATÓRIOS"],
            "C": ["AGENTES ANTIINFLAMATÓRIOS E ANTIINFECTIVOS EM COMBINAÇÃO"],
            "E": ["PREPARAÇÕES ANTIGLAUCOMA E MIÓTICOS"],
            "F": ["MIDRIÁTICOS E CICLOPLÉGICOS"],
            "G": ["DESCONGESTANTES E ANTIALÉRGICOS"],
            "H": ["ANESTÉSICOS LOCAIS"],
            "J": ["AGENTES DE DIAGNÓSTICO"],
            "K": ["AJUDA CIRÚRGICA"],
            "L": ["AGENTES DE TRANSTORNO VASCULAR OCULAR"],
            "X": ["OUTROS OFTALMOLOGICOS"],

        }],
        "02": ["produtos otológicos", {
            "A": ["ANTIINFECCIOSOS"],
            "B": ["CORTICOSTERÓIDES"],
            "C": ["CORTICOSTERÓIDES E ANTIINFECTIVOS EM COMBINAÇÃO"],
            "D": ["OUTROS OTOLÓGICOS"],
        }],

        "03": ["PREPARAÇÕES OFTALMOLÓGICAS E OTOLÓGICAS", {
            "A": ["ANTIINFECCIOSOS"],
            "B": ["CORTICOSTERÓIDES"],
            "C": ["CORTICOSTERÓIDES E ANTIINFECTIVOS EM COMBINAÇÃO"],
            "D": ["OUTROS OTOLÓGICOS"],
        }],

    }, ],  # Fim do grupo S
    'V': [{
        "01": ["antídotos, agentes desintoxicantes e agentes quelantes", {
            "A": ["Alérgicos e antialérgicos"],
        }],

        "03": ["antídotos, agentes desintoxicantes e agentes quelantes", {
            "A": ["TODOS OS OUTROS PRODUTOS TERAPÊUTICOS"],
        }],
        "03AN": ["gases medicinais"],

        "04": ["testes e agentes de diagnóstico", {
            "A": ["AGENTES DE DIAGNÓSTICO, RADIOFÁRMACOS"],
            "B": ["TESTES DE URINA"],
            "C": ["OUTROS AGENTES DE DIAGNÓSTICO"],

        }],
        "06": ["Nutrientes Gerais", {
            "A": ["FORMULAÇÕES DIETAS PARA TRATAMENTO DA OBESIDADE"],
            "B": ["SUPLEMENTOS DE PROTEÍNA"],
            "C": ["FÓRMULAS INFANTIS"],
            "D": [" OUTROS NUTRIENTES"],
        }],

        "07A": "equipamentos, reagentes, solventes e outros insumos farmacêuticos",
        "08": ["meios de contraste", {
            "A": ["MEIOS DE CONTRASTE PARA USO RADIOLÓGICO  RAIOS X, IODINADO"],
            "B": ["MEIOS DE CONTRASTE PARA USO RADIOLÓGICO  RAIOS X, NÃO IODINADO"],
            "C": ["MEIOS DE CONTRASTE DE IMAGEM RESSONÂNCIA MAGNÉTICA"],
            "D": ["MEIOS DE CONTRASTE DE ULTRASSOM"],
        }],
        "09": ["meios de contraste", {
            "A": ["SISTEMA NERVOSO CENTRAL"],
            "B": ["ESQUELETO"],
            "C": ["SISTEMA RENAL"],
            "D": ["SISTEMA HEPÁTICO E RETÍCULO ENDOTELIAL"],
            "E": ["SISTEMA RESPIRATÓRIO"],
            "F": ["TIREÓIDE"],
            "G": ["SISTEMA CARDIOVASCULAR"],
            "H": ["DETECÇÃO DE INFLAMAÇÃO E INFECÇÃO"],
            "I": ["DETECÇÃO DE TUMORES"],
            "X": ["OUTROS RADIOFARMACÊUTICOS PARA DIAGNÓSTICO"],

        }],
        "10": ["radiofármacos", {
            "A": ["AGENTES ANTIINFLAMATÓRIOS"],
            "B": ["PALIAÇÃO DA DOR, AGENTES DE BUSCA DE OSSO"],
            "X": ["OUTROS RADIOFARMACÊUTICOS TERAPÊUTICOS"],

        }],

        "20": ["CURATIVOS CIRÚRGICOS", {
            "": ["CURATIVOS CIRÚRGICOS"],

        }],

        "": "antroposóficos, fitoterápicos e homeopáticos fórmulas ou associações manipuladas, medicamentos veterinários"

    }]  # Fim do grupo V
}




# the list below is based on the list of ATC codes from the WHO Collaborating Centre for Drug Statistics Methodology
# https://www.whocc.no/atc_ddd_index/
list_group = ['preparados estomatológicos', 'preparados estomatológicos',
              'Agentes profiláticos contra cárie', 'Antiinfecciosos e anti-sépticos',
              'Corticosteróides', 'Outros agentes para tratamento oral local',
              'antiácidos, inibidores da secreção gástrica e tratamento das úlceras', 'antiácidos',
              'inibidores da secreção gástrica', 'tratamento das úlceras',
              'antiespasmódicos, anticolinérgicos e propulsivos',
              'Medicamentos para distúrbios gastrointestinais funcionais', 'BELADONA',
              'ANTISPASMÓDICOS", "PSICOLÉPTICOS', 'ANTISPASMÓDICOS", "ANALGÉSICOS',
              'ANTICOLINÉRGICOS', 'PROPULSIVOS',
              'antieméticos", "antinauseantes', 'ANTIEMÉTICOS E ANTINAUSEANTES', 'Antagonistas da serotonina (5HT3)',
              'Outros antieméticos', 'tratamento biliar e hepático', 'TERAPIA BILE', 'TERAPIA DO FÍGADO, LIPOTRÓPICOS',
              'MEDICAMENTOS PARA TERAPIA BILE E LIPOTRÓPICOS EM COMBINAÇÃO', 'laxativos',
              'Medicamentos para constipação',
              'antidiarréicos, anti-inflamatórios e anti-infecciosos intestinais', 'ANTIINFECCIOSOS INTESTINAIS',
              'ADSORVENTES INTESTINAIS', 'ELETRÓLITOS COM CARBOIDRATOS', 'ANTIPROPULSIVOS',
              'ANTIINFLAMATÓRIOS INTESTINAIS', 'MICRORGANISMOS ANTIDIARRÉICOS', 'ANTIDIARRÉICOS',
              'preparados antiobesidade', 'PREPARAÇÕES ANTIOBESIDADE', 'digestivos e enzimas digestivas',
              'digestivos e enzimas digestivas', 'medicamentos utilizados na diabetes', "INSULINAS",
              'INSULINAS E ANÁLOGOS',
              'REDUÇÃO DA GLICOSE NO SANGUE', 'DIABETES',
              'vitaminas e associações', 'MULTIVITAMINAS', 'MULTIVITAMINAS',
              'VITAMINAS A E D', 'VITAMINA A', 'VITAMINAS D',
              'VITAMINA B1', 'VITAMINA B6', 'VITAMINA B12', 'COMPLEXO DE VITAMINA B',
              'ÁCIDO ASCÓRBICO', 'VITAMINA C',
              'PRODUTOS VITAMINOSOS', 'suplementos minerais e associações', 'suplementos minerais', 'CÁLCIO',
              'POTÁSSIO',
              'OUTROS SUPLEMENTOS MINERAIS', 'tônicos', 'repositores hidroeletrolíticos', 'Tônicos',
              'anabolizantes para o uso sistêmico', 'ESTEROIDES anabolizantes', 'AGENTES ANABÓLICOS',
              'estimulantes do apetite', 'sistema digestivo',
              'sistema digestivo',
              'anticoagulantes, antitrombóticos e trombolíticos', 'anticoagulantes e antitrombóticos',
              'anti-hemorrágicos, fatores de coagulação', 'ANTIFIBRINOLÍTICOS', 'antianêmicos',
              'PREPARAÇÕES DE FERRO', 'VITAMINA B12', 'ÁCIDO FÓLICO', 'ANTIANÊMICAS',
              'hemodiálises', 'diálises', 'soluções para perfusão', 'soluções para perfusão e irrigação',
              'sangue e produtos relacionados',
              'soluções intravenosas', 'soluções de irrigação', 'diálise peritoneal', 'aditivos de solução intravenosa',
              'hemodiálise e hemofiltração', 'nutrição parenteral', 'nutrição parenteral',
              'outros preparados hematológicos',
              'outros preparados hematológicos', 'estimulantes cardíacos, cardiotônicos e glicosídeos',
              'GLICOSÍDEOS CARDÍACOS', 'ANTIARRÍTMICOS CLASSE I', 'ANTIARRÍTMICOS CLASSE III',
              'ESTIMULANTES CARDÍACOS', 'VASODILATADORES',
              'PREPARAÇÕES CARDÍACAS', 'anti-hipertensivos', 'AGENTES ANTIADRENERGICOS',
              'ANTIADRENERGICOS', 'BLOQUEADORES DE GÂNGLIOS', 'AGENTES ANTIADRENERGICOS DE ATUAÇÃO PERIFÉRICA',
              'MÚSCULO LISO ARTERIOLAR', 'ANTI-HIPERTENSIVOS',
              'ANTI-HIPERTENSIVOS', 'DIURÉTICOS', 'ANTI-HIPERTENSIVOS EM ATC-GR. C02',
              'diuréticos', 'DIURÉTICOS DE BAIXO TETO', 'TIAZIDAS', 'DIURÉTICOS DE BAIXO TETO',
              'DIURÉTICOS DE TETO ALTO', 'ANTAGONISTAS DA ALDOSTERONA', 'POUPADORES DE POTÁSSIO',
              'DIURÉTICOS', 'OUTROS DIURÉTICOS',
              'vasodilatadores periféricos', 'VASODILATADORES', 'vasoprotetores',
              'tratamento de hemorróidas', 'hemorróidas', 'fissuras anais', 'Terapia antivaricose',
              'estabilizadores capilares', 'beta-bloqueadores', 'BLOQUEADORES BETA',
              'BLOQUEADORES BETA', 'TIAZIDAS', 'BLOQUEADORES BETA', 'OUTROS DIURÉTICOS',
              'BLOQUEADORES BETA', 'TIAZIDAS', 'DIURÉTICOS', 'BLOQUEADORES BETA', 'VASODILATADORES',
              'BLOQUEADORES BETA', 'bloqueadores de canal de cálcio',
              'BLOQUEADORES DE CANAIS DE CÁLCIO COM EFEITOS PRINCIPALMENTE VASCULARES',
              'BLOQUEADORES SELETIVOS DE CANAIS DE CÁLCIO COM EFEITOS CARDÍACOS DIRETOS',
              'BLOQUEADORES DE CANAIS DE CÁLCIO NÃO SELETIVOS', 'BLOQUEADORES DE CANAIS DE CÁLCIO E DIURÉTICOS',
              'sistema renina-angiotensina', 'INIBIDORES ECA', 'INIBIDORES DA ECA',
              'BLOQUEADORES DO RECEPTOR DE ANGIOTENSINA II (BRA)', 'BLOQUEADORES DO RECEPTOR DE ANGIOTENSINA'
                                                                   'BLOQUEADORES DO RECEPTOR DE ANGIOTENSINA II (BRA) e COMBINAÇÕES',
              'SISTEMA RENINA-ANGIOTENSINA', 'hipolipemiantes',
              'modificadores de lipídeos', 'modificadores de lipídeos',
              'anti-infecciosos', 'antibióticos', 'anti-inflamatórios', 'ANTIFÚNGICOS',
              'ANTIFÚNGICOS PARA USO SISTÊMICO', 'emolientes', 'protetores', 'filtro solar',
              'EMOLIENTES E HIDRATANTES', 'PROTETORES CONTRA RADIAÇÃO UV', 'tratamento de feridas e úlceras',
              'CICATRIZANTES', 'enzimas', 'antipuriginosos',
              'ANTIPRURÍTICOS', 'ANTI-HISTAMÍNICOS', 'ANESTÉSICOS', 'antipsoriáticos',
              'ANTIPSORIÁTICOS PARA USO TÓPICO', 'ANTIPSORIÁTICOS PARA USO SISTÊMICO',
              'ANTIBIÓTICOS E QUIMIOTERAPÊUTICOS PARA USO DERMATOLÓGICO', 'ANTIBIÓTICOS',
              'QUIMIOTERAPÊUTICOS PARA USO TÓPICO', 'ANTIBIÓTICOS'  'QUIMIOTERAPÊUTICOS',
              'corticosteróides dermatológicos', 'CORTICOSTEROIDES',
              'CORTICOSTEROIDES', 'COMBINAÇÕES COM ANTISSÉPTICOS', 'CORTICOSTEROIDES', 'COMBINAÇÕES COM ANTIBIÓTICOS',
              'CORTICOSTEROIDES', 'antissépticos', 'desinfetantes', 'ANTISSÉPTICOS E DESINFETANTES',
              'antiacneicos', 'ANTI-ACNE', 'ANTI-ACNE PARA USO SISTÊMICO',
              'preparados dermatológicos', 'PREPARADOS DERMATOLÓGICOS',
              'anti-infecciosos', 'antissépticos ginecológicos',
              'ANTIINFECTIVOS', 'ANTISSÉPTICOS',
              'ANTIINFECTIVOS/ANTISSÉPTICOS EM COMBINAÇÃO COM CORTICOSTERÓIDES', 'preparados ginecológicos',
              'UTEROTÔNICOS', 'CONTRACEPTIVOS', 'OUTROS GINECOLÓGICOS',
              'anticoncepcionais', 'hormônios sexuais', 'moduladores do sistema genital',
              'ANTICONCEPCIONAIS HORMONAIS', 'ANDRÓGENOS', 'ESTRÓGENOS', 'PROGESTOGÊNIOS',
              'ANDRÓGENOS E HORMÔNIOS SEXUAIS FEMININOS', 'PROGESTOGÊNIOS', 'ESTROGÊNIOS',
              'GONADOTROFINAS', 'ESTIMULANTES DE OVULAÇÃO', 'ANTIANDRÓGENOS',
              'HORMÔNIOS SEXUAIS', 'MODULADORES DO SISTEMA GENITAL', 'medicamentos urológicos',
              'INCONTINÊNCIA URINÁRIA', 'UROLÓGICOS',
              'DROGAS USADAS NA HIPERTROFIA PROSTÁTICA BENIGNA', 'hormônios', 'hipofisários', 'hipotalâmicos',
              'LOBO PITUITÁRIO ANTERIOR', 'LOBO PITUITÁRIO POSTERIOR', 'LOBO PITUITÁRIO'
                                                                       'HORMÔNIOS HIPOTALÂMICOS',
              'corticoesteróides sistêmicos', 'CORTICOSTEROIDES',
              'CORTICOSTEROIDES', 'ANTIADRENAIS', 'tratamento da tireoide',
              'TIREÓIDE', 'ANTICIREÓIDES', 'TERAPIA COM IODO', 'pancreáticos',
              'GLICOGENOLÍTICOS', 'homeostasia do cálcio',
              'PARATIREÓIDEOS', 'ANTI-PARATIREÓIDES', 'antibacterianos',
              'TETRACICLINAS', 'AMFENÍCOLOS', 'ANTIBACTERIANOS BETA-LACTAM', 'PENICILINAS',
              'OUTROS ANTIBACTERIANOS BETA-LACTAM', 'SULFONAMIDAS', 'TRIMETHOPRIMA',
              'MACROLÍDEOS', 'LINCOSAMIDAS', 'ESTREPTOGRAMINAS', 'ANTIBACTERIANOS', 'AMINOGLICOSÍDEOS',
              'ANTIBACTERIANOS QUINOLONAS', 'COMBINAÇÕES DE ANTIBACTERIANOS', 'ANTIBACTERIANOS',
              'antifúngicos', 'ANTIMICÓTICOS', 'antimicobacterianos',
              'tuberculose', 'lepra',
              'antivirais', 'ANTIVIRAIS de ação direta', 'imunossoros', 'imunoglobulinas',
              'SOROS IMUNE', 'IMUNOSSOROS', 'IMUNOGLOBULINAS', 'vacinas', 'VACINAS BACTERIANAS', 'VACINAS VIRAIS',
              'VACINAS BACTERIANAS E VIRAIS', 'OUTRAS VACINAS', 'antineoplásicos', 'ALQUILANTES',
              'ANTIMETABOLITOS', 'ALCALOIDES',
              'ANTIBIÓTICOS CITOTÓXICOS', 'INIBIDORES DE PROTEÍNA QUINASE',
              'ANTICORPOS MONOCLONAIS', 'CONJUGADOS DE ANTICORPOS', 'ANTINEOPLÁSICOS', 'terapias endócrinas',
              'HORMÔNIOS E AGENTES RELACIONADOS', 'ANTAGONISTAS HORMÔNICOS', 'imunoestimulantes',
              'IMUNOESTIMULANTES', 'imunossupressores', 'IMUNOSSUPRESSORES', 'IMUNOSSUPRESSANTES',
              'anti-inflamatórios', 'antirreumáticos', 'ANTIINFLAMATÓRIOS', 'ANTIRREUMÁTICOS',
              'ANTIINFLAMATÓRIOS', 'ANTIRREUMÁTICOS', 'ANTIRREUMÁTICOS ESPECÍFICOS',
              'dores articulares e musculares', 'DORES ARTICULARES', 'DORES MUSCULARES',
              'relaxantes musculares', 'RELAXANTES MUSCULARES', 'AGENTES DE ATUAÇÃO PERIFÉRICA',
              'RELAXANTES MUSCULARES', 'AGENTES DE ATUAÇÃO CENTRAL', 'RELAXANTES MUSCULARES', 'AGENTES DE AÇÃO DIRETA',
              'antigotosos', 'ANTIGOTOSOS', 'tratamento de doenças ósseas',
              'TRATAMENTO DE DOENÇAS ÓSSEAS',
              ' sistema músculo-esquelético',
              'OUTROS MEDICAMENTOS PARA O SISTEMA MÚSCULO-ESQUELÉTICO', 'anestésicos', 'ANESTÉSICOS GERAIS',
              'ANESTÉSICOS LOCAIS', 'analgésicos', 'OPIOIDES', 'OUTROS ANALGÉSICOS E ANTIPIRÉTICOS',
              'ANTIMIGRÂNICOS', 'antiepiléticos', 'ANTIEPILÉTICOS', 'antiparksonianos',
              'ANTICOLINÉRGICOS', 'DOPAMINÉRGICOS', 'ANTIPARKINSON', 'antipsicóticos',
              'ANTIPSICÓTICOS', 'Anxiolíticos', 'Hipnóticos', 'sedativos', 'antidepressivos', 'ANTIDEPRESSIVOS',
              'PSICOESTIMULANTES' 'TDAH E NOOTRÓPICOS', 'PSICOLÉPTICOS', 'PSICANALÉPTICOS EM COMBINAÇÃO',
              'ANTI-DEMÊNCIA', 'sistema nervoso', 'PARASIMPATHOMIMÉTICOS',
              'DROGAS USADAS EM TRANSTORNOS ADICIONAIS', 'ANTIVERTIGO', 'OUTROS MEDICAMENTOS PARA O SISTEMA NERVOSO',
              'antiprotozoários', 'AMEBÍASE', 'DOENÇAS PROTOZOÁRIAS', 'ANTIMALÁRICOS',
              'LEISHMANIOSE', 'TRIPANOSSOMOSE', 'anti-helmínticos', 'ANTITREMATÓDICOS', 'ANTINEMATÓDICOS',
              'ANTICESTODAIS', ' escabicidas', 'ectoparasiticidas',
              'ECTOPARASITICIDAS', 'ESCABICIDAS',
              'DESCONGESTANTES', 'OUTRAS PREPARAÇÕES NASAIS PARA USO TÓPICO',
              'CORTICOSTEROIDES', 'DESCONGESTANTES NASAIS',
              'uso faríngeo', 'TRATAMENTO DA DOR DE GARGANTA', 'antiasmáticos',
              'OBSTRUTIVAS DAS VIAS AÉREAS',
              'OUTROS MEDICAMENTOS PARA DOENÇAS OBSTRUTIVAS DAS VIAS AÉREAS', ' ADRENÉRGICOS',
              'OUTROS MEDICAMENTOS SISTÊMICOS PARA DOENÇAS OBSTRUTIVAS DAS VIAS AÉREAS',
              'tosse', 'resfriado', 'EXPETORANTES',
              'EXPECTORANTES', 'SUPRESSANTES',
              'SUPRESSANTES PARA TOSSE', 'EXPECTORANTES', 'OUTROS MEDICAMENTOS PARA TOSSE E RESFRIADO',
              'anti-histamínicos', 'ANTIHISTAMÍNICOS PARA USO SISTÊMICO',
              'outros medicamentos para o sistema respiratório', 'SISTEMA RESPIRATÓRIO',
              'oftálmicos', 'ANTIINFECCIOSOS', 'ANTIINFLAMATÓRIOS',
              'ANTIINFLAMATÓRIOS', 'ANTIINFECTIVOS', 'ANTIGLAUCOMA', 'MIÓTICOS',
              'MIDRIÁTICOS', 'CICLOPLÉGICOS', 'DESCONGESTANTES', 'ANTIALÉRGICOS', 'ANESTÉSICOS LOCAIS',
              'AGENTES DE DIAGNÓSTICO', 'AJUDA CIRÚRGICA', 'TRANSTORNO VASCULAR OCULAR', 'OFTALMOLOGICOS',
              'otológicos', 'ANTIINFECCIOSOS', 'CORTICOSTERÓIDES',
              'CORTICOSTERÓIDES E ANTIINFECTIVOS', 'OUTROS OTOLÓGICOS',
              'OFTALMOLÓGICAS E OTOLÓGICAS', 'ANTIINFECCIOSOS', 'CORTICOSTERÓIDES',
              'CORTICOSTERÓIDES E ANTIINFECTIVOS EM COMBINAÇÃO', 'OUTROS OTOLÓGICOS',
              'antídotos', 'desintoxicantes', 'agentes quelantes', 'Alérgicos e antialérgicos',
              'antídotos', 'agentes desintoxicantes', 'agentes quelantes', 'TODOS OS OUTROS PRODUTOS TERAPÊUTICOS',
              'gases medicinais', 'agentes de diagnóstico', 'AGENTES DE DIAGNÓSTICO, RADIOFÁRMACOS',
              'TESTES DE URINA', 'OUTROS AGENTES DE DIAGNÓSTICO', 'Nutrientes Gerais',
              'FORMULAÇÕES DIETAS PARA TRATAMENTO DA OBESIDADE', 'SUPLEMENTOS DE PROTEÍNA', 'FÓRMULAS INFANTIS',
              'meios de contraste', 'MEIOS DE CONTRASTE PARA USO RADIOLÓGICO  RAIOS X, IODINADO',
              'MEIOS DE CONTRASTE PARA USO RADIOLÓGICO  RAIOS X, NÃO IODINADO',
              'MEIOS DE CONTRASTE DE IMAGEM RESSONÂNCIA MAGNÉTICA', 'MEIOS DE CONTRASTE DE ULTRASSOM',
              'meios de contraste',
              'SISTEMA NERVOSO CENTRAL', 'ESQUELETO', 'SISTEMA RENAL', 'SISTEMA HEPÁTICO E RETÍCULO ENDOTELIAL',
              'SISTEMA RESPIRATÓRIO', 'TIREÓIDE', 'SISTEMA CARDIOVASCULAR', 'DETECÇÃO DE INFLAMAÇÃO E INFECÇÃO',
              'DETECÇÃO DE TUMORES', 'OUTROS RADIOFARMACÊUTICOS PARA DIAGNÓSTICO', 'radiofármacos',
              'AGENTES ANTIINFLAMATÓRIOS', 'PALIAÇÃO DA DOR', 'BUSCA DE OSSO',
              'RADIOFARMACÊUTICOS TERAPÊUTICOS', 'CURATIVOS CIRÚRGICOS', 'CURATIVOS CIRÚRGICOS',
              'antroposóficos', 'fitoterápicos', 'homeopáticos', 'fórmulas ou associações manipuladas',
              'medicamentos veterinários',

              "Analgésicos e Antitérmicos",
              "Anti-inflamatórios",
              "Antibióticos",
              "Antidepressivos",
              "Antieméticos",
              "Antipiréticos",
              "Antissépticos e Desinfetantes",
              "Antivirais",
              "Corticoides",
              "Hormônios",
              "Anti-hipertensivos",
              "Anticoagulantes",
              "Anticonvulsivantes", "anticonvulsivantes",
              "Antialérgicos",
              "Broncodilatadores",
              "Diuréticos",
              "Antifúngicos",
              "Anti-histamínicos",
              "Imunossupressores",
              "Vitaminas e Suplementos",
              "Tranquilizantes e Ansiolíticos",
              "Antiemergenciais",
              "Antirretrovirais",
              "Antiespasmódicos",
              "Agentes Anestésicos",
              "Antifibrinolíticos",
              "Agentes Imunológicos",
              "Antiprotozoários",
              "Agentes Miorrelaxantes",
              "Antipsicóticos",
              "Agentes Estimulantes do Apetite"

              ]

# def extract_values(dicionario):
#     valores = []
#     for chave, valor in dicionario.items():
#         if isinstance(valor, list):
#             for item in valor:
#                 if isinstance(item, dict):
#                     valores.extend(extract_values(item))
#                 else:
#                     valores.append(item)
#         elif isinstance(valor, dict):
#             valores.extend(extract_values(valor))
#         else:
#             valores.append(valor)
#     return valores
#
# print(extract_values(ATC))


if __name__ == '__main__':
    # print("-----------------------------------------------------------")
    # print("ATC - Anatomical Therapeutic Chemical Classification System")
    # print("-----------------------------------------------------------")
    # print("A - SISTEMA DIGESTIVO E METABOLISMO")
    # print("B - SANGUE E ÓRGÃOS HEMATOPOIÉTICOS")
    # print("C - SISTEMA CARDIOVASCULAR")
    # print("D - PELE E ANEXOS")
    # print("G - SISTEMA GENITURINÁRIO E HORMÔNIOS SEXUAIS")
    # print("H - HORMÔNIOS SISTÊMICOS")
    # print("J - ANTI-INFECCIOSOS DE USO SISTÊMICO")
    # print("L - ANTINEOPLÁSICOS E IMUNOMODULADORES")
    # print("M - SISTEMA MÚSCULO-ESQUELÉTICO")
    # print("N - SISTEMA NERVOSO")
    # print("P - ANTI-PARASITÁRIOS, INSETICIDAS E REPELENTES")
    # print("R - SISTEMA RESPIRATÓRIO")
    # print("S - ÓRGÃOS DO SENTIDO")
    # print("V - VÁRIOS")
    # print("0 - EXIT")
    # print("--------------------------------------------------------")
    # group = input(str("Type a letter to show or zero to exit and press <enter>: "))

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
    print(ATC['G'][0]['02'][1]['A'])
    print(ATC['G'][0]['03'][1]['A'])
    print(ATC['G'][0]['04'][1]['A'])

    print(ATC['H'][0]['01'][1]['A'])

    print(ATC['H'][0]['02'][1]['A'])

    print(ATC['H'][0]['03'][1]['A'])
