

ATC = {'A': {"01": "preparados estomatológicos (boca e dentes)",
                "02": "antiácidos, inibidores da secreção gástrica e tratamento das úlceras",
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
                "16": "outros medicamentos para o sistema digestivo e o metabolismo"},
        'B': {"01": "anticoagulantes, antitrombóticos e trombolíticos",
                "02": "anti-hemorrágicos, fatores de coagulação e correlatos",
                "03": "preparados antianêmicos",
                "05": "hemodiálises, diálises e soluções para perfusão e irrigação",
                "05BA": "nutrição parenteral",
                "06": "outros preparados hematológicos"}
       }




if __name__ == '__main__':
    print("--------------------------------------------------------")
    p = "A"
    d = "10"
    print (ATC[p][d])
    for i in ATC:
        print(i, ATC[i])
        for j in ATC[i]:
            print(j, ATC[i][j])