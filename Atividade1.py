import pandas as pd

def calcular_salario(vendas, num_carros, salario_fixo=2000, comissao_fixa=300):
    total_vendas = vendas
    salario_final = salario_fixo
    
    if num_carros == 0:
        return salario_final

    salario_final += num_carros * comissao_fixa + 0.05 * total_vendas

    if num_carros > 10:
        salario_final += 0.1 * total_vendas
    
    return salario_final

cenarios = [
    {"Carros Vendidos": 0, "Total de Vendas": 0},
    {"Carros Vendidos": 5, "Total de Vendas": 50000},
    {"Carros Vendidos": 10, "Total de Vendas": 100000},
    {"Carros Vendidos": 12, "Total de Vendas": 120000},
]

df = pd.DataFrame(cenarios)

df["Salário Final"] = df.apply(lambda x: calcular_salario(x["Total de Vendas"], x["Carros Vendidos"]), axis=1)

print("Tabela de Cálculo do Salário:")
print(df)
