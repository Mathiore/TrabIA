import pandas as pd
from scipy.spatial import distance
#Matheus da Costa, Bruno Pereira, Marco Antonio
# Ler o arquivo Excel
df = pd.read_excel('tireoidetest.xlsx')

# Ler os dados das colunas
dados_planilha = df[['age', 'tsh', 't3', 'tt4', 't4u', 'fti']].values

# Definir os valores máximos para cada coluna
valores_maximos = [100, 4.0, 200, 150, 1.5, 100]

# Função para normalizar os dados
def normalizar_dados(dados, max_valor):
    return dados / max_valor

# Função para calcular a similaridade com pesos e dados normalizados
def calcular_similaridade_com_pesos(novos_dados, dados_existentes, pesos, valores_maximos):
    # Normalizar os novos dados
    novos_dados_normalizados = [normalizar_dados(dado, max_valor) for dado, max_valor in zip(novos_dados, valores_maximos)]
    
    # Normalizar os dados existentes
    dados_existentes_normalizados = [[normalizar_dados(dado, max_valor) for dado, max_valor in zip(dados, valores_maximos)] for dados in dados_existentes]
    
    # Multiplicar cada valor das variáveis normalizadas pelos pesos correspondentes
    dados_com_pesos = [[valor * peso for valor, peso in zip(dados, pesos)] for dados in dados_existentes_normalizados]
    
    # Calcular a distância euclidiana entre os novos dados normalizados e cada linha dos dados existentes normalizados com pesos
    distancias = [distance.euclidean(novos_dados_normalizados, dados) for dados in dados_com_pesos]
    
    # Calcular a similaridade como o inverso da distância
    similaridade = [1 / (1 + distancia) for distancia in distancias]
    
    return similaridade

# Entrada dos novos dados pelo console
novo_dado = []
for coluna, valor_maximo in zip(['age', 'tsh', 't3', 'tt4', 't4u', 'fti'], valores_maximos):
    valor = float(input(f"Digite o valor de {coluna}: "))
    novo_dado.append(valor)

# Definir os pesos de importância
pesos = [0.15, 0.5, 0.45, 0.4, 0.3, 0.2]

# Calcular a similaridade dos novos dados em relação aos dados existentes na planilha com pesos e normalização
similaridade = calcular_similaridade_com_pesos(novo_dado, dados_planilha, pesos, valores_maximos)

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
