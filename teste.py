import pandas as pd


base = pd.read_csv('dados historicos bitcoin.csv')

# Convertendo tipos da coluna "Data"
base['Data'] = pd.to_datetime(base['Data'], format='%d.%m.%Y')

# Modificando valores para que fiquem no formato númerico sem vírgulas
base['Último'] = base['Último'].str.replace('.', '')
base['Último'] = base['Último'].str.replace(',', '.')
base['Abertura'] = base['Abertura'].str.replace('.', '')
base['Abertura'] = base['Abertura'].str.replace(',', '.')

# Convertendo tipos das colunas "Último" e "Aabertura"
base['Último'] = pd.to_numeric(base['Último'])
base['Abertura'] = pd.to_numeric(base['Abertura'])

# Criação de colunas
base['Mês'] = base['Data'].dt.month
base['Ano'] = base['Data'].dt.year

''' Selecionando o mês '''
meses = list(range(1, 13))
cont = 0

# loop que escolhe um mês especifico e adiciona a coluna "Mês" dentro de uma variavel.
for mes in meses:
    mes_selecionado = base[base['Mês'] == mes]
    

for l in mes_selecionado[['Var%']].iterrows():
    linhas_str = str(l)
    linha_negativa = linhas_str.find("-")
    
    if linha_negativa != -1:
        cont += 1
            
'''para cada mês que o loop for percorrer, esse print deverá ser repetido informando quantos valores negativos foram encontrados e o mês '''
for mes in meses:
    print(f"Foram encontrados {cont} valores negativos no mês {mes}.")
    print(l)
