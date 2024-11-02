import pandas as pd

def valida_entrada(idade):
    try:
        idade = int(idade)
        if idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        return idade
    except ValueError:
        print("Erro: A idade deve ser um número inteiro positivo.")
        return None

def obter_idades():
    idades = {}
    for pessoa in ['primeiro homem', 'segundo homem', 'primeira mulher', 'segunda mulher']:
        while True:
            idade = input(f"Digite a idade do {pessoa}: ")
            idade_validada = valida_entrada(idade)
            if idade_validada is not None:
                idades[pessoa.replace(" ", "_")] = idade_validada
                break
            else:
                print("Por favor, insira uma idade válida.\n")
    
    return idades

def calcular_soma_produto(idades):
    homens = [idades['primeiro_homem'], idades['segundo_homem']]
    mulheres = [idades['primeira_mulher'], idades['segunda_mulher']]

    homem_mais_velho = max(homens)
    homem_mais_novo = min(homens)
    mulher_mais_velha = max(mulheres)
    mulher_mais_nova = min(mulheres)

    soma = homem_mais_velho + mulher_mais_nova
    produto = homem_mais_novo * mulher_mais_velha

    return {
        "Homem Mais Velho": homem_mais_velho,
        "Homem Mais Novo": homem_mais_novo,
        "Mulher Mais Velha": mulher_mais_velha,
        "Mulher Mais Nova": mulher_mais_nova,
        "Soma (Homem Mais Velho + Mulher Mais Nova)": soma,
        "Produto (Homem Mais Novo * Mulher Mais Velha)": produto
    }

def exibir_resultados(resultados):
    print("\nResultados:")
    print(f"Homem Mais Velho: {resultados['Homem Mais Velho']}")
    print(f"Homem Mais Novo: {resultados['Homem Mais Novo']}")
    print(f"Mulher Mais Velha: {resultados['Mulher Mais Velha']}")
    print(f"Mulher Mais Nova: {resultados['Mulher Mais Nova']}")
    print(f"Soma (Homem Mais Velho + Mulher Mais Nova): {resultados['Soma (Homem Mais Velho + Mulher Mais Nova)']}")
    print(f"Produto (Homem Mais Novo * Mulher Mais Velha): {resultados['Produto (Homem Mais Novo * Mulher Mais Velha)']}")

def main():
    idades = obter_idades()
    resultados = calcular_soma_produto(idades)
    exibir_resultados(resultados)

main()
