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
    'A': [
        ("2101", "01", "preparados estomatológicos (boca e dentes)"),
        ("2102", "02", "antiácidos, inibidores da secreção gástrica e tratamento das úlceras"),
        ("2103", "03", "antiespasmódicos, anticolinérgicos e propulsivos"),
        ("2104", "04", "antieméticos e antinauseantes"),
        ("2105", "05", "tratamento biliar e hepático"),
        ("2106", "06", "laxativos"),
        ("2107", "07", "antidiarréicos, anti-inflamatórios e anti-infecciosos intestinais"),
        ("2108", "08", "preparados antiobesidade"),
        ("2109", "09", "digestivos e enzimas digestivas"),
        ("2110", "10", "medicamentos utilizados na diabetes"),
        ("2111/A12", "11/12", "vitaminas, suplementos minerais e associações"),
        ("2112", "13", "tônicos e repositores hidroeletrolíticos orais"),
        ("2113", "14", "anabolizantes para o uso sistêmico"),
        ("2114", "15", "estimulantes do apetite"),
        ("2115", "16", "outros medicamentos para o sistema digestivo e o metabolismo")
    ],
    'B': [
        ("2116", "01", "anticoagulantes, antitrombóticos e trombolíticos"),
        ("2117", "02", "anti-hemorrágicos, fatores de coagulação e correlatos"),
        ("2118", "03", "preparados antianêmicos"),
        ("2119", "05", "hemodiálises, diálises e soluções para perfusão e irrigação"),
        ("2120", "05BA", "nutrição parenteral"),
        ("2121", "06", "outros preparados hematológicos")
    ],
    'C': [
        ("2122", "01", "estimulantes cardíacos, cardiotônicos e glicosídeos"),
        ("2123", "02", "anti-hipertensivos"),
        ("2124", "03", "diuréticos"),
        ("2125", "04", "vasodilatadores periféricos"),
        ("2126", "05", "vasoprotetores"),
        ("2127", "07", "beta-bloqueadores"),
        ("2128", "08", "bloqueadores de canal de cálcio"),
        ("2129", "09", "sistema renina-angiotensina"),
        ("2130", "10", "hipolipemiantes")
    ],
    'D': [
        ("2131", "01/06/07", "anti-infecciosos, antibióticos e anti-inflamatórios tópicos"),
        ("2132", "02", "emolientes, hidratantes, protetores e filtro solar"),
        ("2133", "03", "tratamento de feridas e úlceras"),
        ("2134", "04/05", "antipuriginosos e antipsoriáticos"),
        ("2135", "08", "antissépticos e desinfetantes"),
        ("2136", "10", "antiacneicos"),
        ("2137", "11", "outros preparados dermatológicos")
    ],
    'G': [
        ("2138", "01", "anti-infecciosos e antissépticos ginecológicos"),
        ("2139", "02", "outros preparados ginecológicos"),
        ("2140", "03", "anticoncepcionais, hormônios sexuais e moduladores do sistema genital"),
        ("2141", "04", "medicamentos urológicos")
    ],
    'H': [
        ("2142", "01", "hormônios, hipofisários hipotalâmicos e análogos"),
        ("2143", "02", "corticoesteróides sistêmicos"),
        ("2144", "03", "tratamento da tireoide"),
        ("2145", "04", "hormônios pancreáticos"),
        ("2146", "05", "medicamentos relacionados à homeostasia do cálcio")
    ],
    'J': [
        ("2147", "01", "antibacterianos sistêmicos"),
        ("2148", "02", "antifúngicos sistêmicos"),
        ("2149", "04", "antimicobacterianos sistêmicos"),
        ("2150", "05", "antivirais sistêmicos"),
        ("2151", "06", "imunossoros e imunoglobulinas"),
        ("2152", "07", "vacinas")
    ],
    'L': [
        ("2153", "01", "antineoplásicos"),
        ("2154", "02", "terapias endócrinas"),
        ("2155", "03", "imunoestimulantes"),
        ("2156", "04", "imunossupressores")
    ],
    'M': [
        ("2157", "01", "anti-inflamatórios e antirreumáticos"),
        ("2158", "02", "produtos tópicos para dores articulares e musculares"),
        ("2159", "03", "relaxantes musculares"),
        ("2160", "04", "antigotosos"),
        ("2161", "05", "tratamento de doenças ósseas"),
        ("2162", "09", "outros medicamentos para o sistema músculo-esquelético")
    ],
    'N': [
        ("2163", "01", "anestésicos"),
        ("2164", "02", "analgésicos"),
        ("2165", "03", "antiepiléticos"),
        ("2166", "04", "antiparksonianos"),
        ("2167", "05A", "antipsicóticos"),
        ("2168", "05B", "ansiolíticos"),
        ("2169", "05C", "hipnóticos e sedativos"),
        ("2170", "06A", "antidepressivos"),
        ("2171", "06B", "psicoestimulantes"),
        ("2172", "06C", "psicoléticos e psicoanapléticos em associação"),
        ("2173", "06D", "tratamento do Alzheimer e demência"),
        ("2174", "07", "outros medicamentos para o sistema nervoso")
    ],
    'P': [
        ("2175", "01", "antiprotozoários"),
        ("2176", "02", "anti-helmínticos"),
        ("2177", "03", "inseticidas, repelentes, escabicidas e ectoparasiticidas")
    ],
    'R': [
        ("2180", "01", "preparados para o uso nasal"),
        ("2181", "02", "preparados para o uso faríngeo"),
        ("2182", "03", "antiasmáticos"),
        ("2183", "05", "medicamentos para tosse e resfriado"),
        ("2184", "06", "anti-histamínicos sistêmicos"),
        ("2185", "07", "outros medicamentos para o sistema respiratório")
    ],
    'S': [
        ("2186", "01", "produtos oftálmicos"),
        ("2187", "02", "produtos otológicos")
    ],
    'V': [
        ("2188", "03AB", "antídotos, agentes desintoxicantes e agentes quelantes"),
        ("2189", "03AN", "gases medicinais"),
        ("2190", "04", "testes e agentes de diagnóstico"),
        ("2191", "07A", "equipamentos, reagentes, solventes e outros insumos farmacêuticos"),
        ("2192", "08", "meios de contraste"),
        ("2193", "10", "radiofármacos"),
        ("2194", "03", "outros produtos terapêuticos"),
        ("2195", "", "antroposóficos, fitoterápicos e homeopáticos"),
        ("2196", "", "fórmulas ou associações manipuladas"),
        ("2197", "", "medicamentos veterinários")
    ]
}

if __name__ == '__main__':
    print("-----------------------------------------------------------")
    print("ATC - Anatomical Therapeutic Chemical Classification System")
    print("-----------------------------------------------------------")
    print("A - SISTEMA DIGESTIVO E METABOLISMO")
    print("B - SANGUE E ÓRGÃOS HEMATOPOIÉTICOS")
    print("C - SISTEMA CARDIOVASCULAR")
    print("D - PELE E ANEXOS")
    print("G - SISTEMA GENITURINÁRIO E HORMÔNIOS SEXUAIS")
    print("H - HORMÔNIOS SISTÊMICOS")
    print("J - ANTI-INFECCIOSOS DE USO SISTÊMICO")
    print("L - ANTINEOPLÁSICOS E IMUNOMODULADORES")
    print("M - SISTEMA MÚSCULO-ESQUELÉTICO")
    print("N - SISTEMA NERVOSO")
    print("P - ANTI-PARASITÁRIOS, INSETICIDAS E REPELENTES")
    print("R - SISTEMA RESPIRATÓRIO")
    print("S - ÓRGÃOS DO SENTIDO")
    print("V - VÁRIOS")
    print("0 - EXIT")
    print("--------------------------------------------------------")
    group = input(str("Type a letter to show or zero to exit and press <enter>: "))
    while group != '0':
        for key, value in ATC.items():
            if key == group.upper():
                print(f"The drugs of category \"{group.upper()}\" is:", value[0][2])
                # for item in value:
        group = input(str("Choose other letter: "))
