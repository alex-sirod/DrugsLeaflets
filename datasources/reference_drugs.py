# https://www.paho.org/pt/oms-uma-organizacao-global-saude
ATC = {
    'A': {
        "01": ["preparados estomatológicos (boca e dentes)",
               {"A": "preparados estomatológicos"}],

        "02": ["antiácidos, inibidores da secreção gástrica e tratamento das úlceras",
               {"A": "antiácidos",
                "B": "inibidores da secreção gástrica",
                "C": "tratamento das úlceras",
                }],

        "03": "antiespasmódicos, anticolinérgicos e propulsivos",
        "04": "antieméticos e antinauseantes",
        "05": "tratamento biliar e hepático",
        "06": "laxativos",
        "07": "antidiarréicos, anti-inflamatórios e anti-infecciosos intestinais",
        "08": "preparados antiobesidade",
        "09": "digestivos e enzimas digestivas",
        "10": "medicamentos utilizados na diabetes",
        "11/12": "vitaminas, suplementos minerais e associações",
        "13": "tônicos e repositores hidroeletrolíticos orais",
        "14": "anabolizantes para o uso sistêmico",
        "15": "estimulantes do apetite",
        "16": "outros medicamentos para o sistema digestivo e o metabolismo"
    },
    'B': {
        "01": "anticoagulantes, antitrombóticos e trombolíticos",
        "02": "anti-hemorrágicos, fatores de coagulação e correlatos",
        "03": "preparados antianêmicos",
        "05": "hemodiálises, diálises e soluções para perfusão e irrigação",
        "05BA": "nutrição parenteral",
        "06": "outros preparados hematológicos"
    },
    'C': {
        "01": "estimulantes cardíacos, cardiotônicos e glicosídeos",
        "02": "anti-hipertensivos",
        "03": "diuréticos",
        "04": "vasodilatadores periféricos",
        "05": "vasoprotetores",
        "07": "beta-bloqueadores",
        "08": "bloqueadores de canal de cálcio",
        "09": "sistema renina-angiotensina",
        "10": "hipolipemiantes"
    },
    'D': {
        "01/06/07": "anti-infecciosos, antibióticos e anti-inflamatórios tópicos",
        "02": "emolientes, hidratantes, protetores e filtro solar",
        "03": "tratamento de feridas e úlceras",
        "04/05": "antipuriginosos e antipsoriáticos",
        "08": "antissépticos e desinfetantes",
        "10": "antiacneicos",
        "11": "outros preparados dermatológicos"
    },
    'G': {
        "01": "anti-infecciosos e antissépticos ginecológicos",
        "02": "outros preparados ginecológicos",
        "03": "anticoncepcionais, hormônios sexuais e moduladores do sistema genital",
        "04": "medicamentos urológicos"
    },
    'H': {
        "01": "hormônios, hipofisários hipotalâmicos e análogos",
        "02": "corticoesteróides sistêmicos",
        "03": "tratamento da tireoide",
        "04": "hormônios pancreáticos",
        "05": "medicamentos relacionados à homeostasia do cálcio"
    },
    'J': {
        "01": "antibacterianos sistêmicos",
        "02": "antifúngicos sistêmicos",
        "04": "antimicobacterianos sistêmicos",
        "05": "antivirais sistêmicos",
        "06": "imunossoros e imunoglobulinas",
        "07": "vacinas"
    },
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
print(ATC)
print(ATC['V']['03'])
print(ATC['A']['01'][1]['A'])
print(ATC['A']['02'][1]['B'])