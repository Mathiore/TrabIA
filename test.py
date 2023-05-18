import pandas as pd
from scipy.spatial import distance

# Ler o arquivo Excel
df = pd.read_excel('tireoidetest.xlsx')

# Ler os dados das colunas
dados_planilha = df[['age', 'tsh', 't3', 'tt4', 't4u', 'fti']].values

# Função para calcular a similaridade
def calcular_similaridade(novos_dados, dados_existentes):
    # Calcular a distância euclidiana entre os novos dados e cada linha dos dados existentes
    distancias = [distance.euclidean(novos_dados, dados) for dados in dados_existentes]
    
    # Calcular a similaridade como o inverso da distância
    similaridade = [1 / (1 + distancia) for distancia in distancias]
    
    return similaridade

# Entrada dos novos dados pelo console
novo_dado = []
for coluna in ['age', 'tsh', 't3', 'tt4', 't4u', 'fti']:
    valor = float(input(f"Digite o valor de {coluna}: "))
    novo_dado.append(valor)

# Calcular a similaridade dos novos dados em relação aos dados existentes na planilha
similaridade = calcular_similaridade(novo_dado, dados_planilha)

# Criar uma lista de tuplas contendo a similaridade e o índice correspondente
resultados = [(sim, indice) for indice, sim in enumerate(similaridade)]

# Ordenar os resultados em ordem decrescente de similaridade
resultados_ordenados = sorted(resultados, key=lambda x: x[0], reverse=True)

# Imprimir os resultados em ordem decrescente
print()
print('Caso:', novo_dado)
print("Similaridade em ordem decrescente:")
for sim, indice in resultados_ordenados:
    print(f"Registro {indice+1}:")
    print(f"  Age: {dados_planilha[indice][0]}, TSH: {dados_planilha[indice][1]}, T3: {dados_planilha[indice][2]}, TT4: {dados_planilha[indice][3]}, T4U: {dados_planilha[indice][4]}, FTI: {dados_planilha[indice][5]}")
    print(f"  Similaridade: {sim * 100:.2f}%")
    if  dados_planilha[indice][0] <= 40 and dados_planilha[indice][1] < 0.5 and dados_planilha[indice][2] > 180 :
        print("Paciente", indice+1, "- Hipertireoidismo")
    elif dados_planilha[indice][0] <=40 and dados_planilha[indice][1] > 0.5 and dados_planilha[indice][3] > 11 :
        print("Paciente", indice+1, "-Hipertireoidismo")
    elif dados_planilha[indice][0] <=40 and dados_planilha[indice][1] > 0.5 and dados_planilha[indice][2] > 180 :
        print("Paciente", indice+1, "-Hipertireoidismo Secundário")
    elif dados_planilha[indice][0] >=40 and dados_planilha[indice][1] < 0.4 and dados_planilha[indice][2] > 140 :
        print("Paciente", indice+1, "-Hipertireoidismo")
    elif dados_planilha[indice][0] <=40 and dados_planilha[indice][1] > 3.0 and dados_planilha[indice][2] < 80 :
        print("Paciente", indice+1, "-Hipotireoidismo")
    elif dados_planilha[indice][0] <=40 and dados_planilha[indice][1] > 3.0 and dados_planilha[indice][3] < 5 :
        print("Paciente", indice+1, "-Hipotireoidismo")
    elif dados_planilha[indice][0] <=40 and dados_planilha[indice][1] < 1.0 and dados_planilha[indice][2] < 80 :
        print("Paciente", indice+1, "-Hipotireoidismo Secundario")
    elif dados_planilha[indice][0] >40 and dados_planilha[indice][1] > 2.0 and dados_planilha[indice][2] < 60 :
        print("Paciente", indice+1, "-Hipotireoidismo")
        
    else:
        print("Paciente", indice, "- Condição não identificada")
    print()
