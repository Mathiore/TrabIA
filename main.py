import pandas as pd

# Ler o arquivo Excel
arquivo_excel = 'tireoidetest.xlsx'
dados_excel = pd.read_excel(arquivo_excel)

# Percorrer as linhas
for indice, linha in dados_excel.iterrows():
    age = linha['age']
    tsh = linha['tsh']
    t3 = linha['t3']
    tt4 = linha['tt4']
    t4u = linha['t4u']
    fti = linha['fti']

    #T4 tiroxina
    #T3 triiodotironina
    #TSH hormônio estimulador da tireoide
    #T4U Utilização da tireoide do hormonio tiroxina
    #FTI Tiroxina livre circulante no sangue

    # Comparar condições específicas para cada paciente (linha)
    if  age <= 40 and tsh < 0.5:
        print("Paciente", indice, "- Hipertireoidismo")
    elif age < 18 and tt4 > 120:
        print("Paciente", indice, "- Hipotireoidismo")
    
    else:
        print("Paciente", indice, "- Condição não identificada")

