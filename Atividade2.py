import pandas as pd

def valida_entrada(idade):
    """Valida se a entrada é um número inteiro positivo."""
    try:
        idade = int(idade)
        if idade <= 0:
            raise ValueError("A idade deve ser um número inteiro positivo.")
        return idade
    except ValueError as e:
        print(e)
        return None

def obter_idades():
    idades = {}
    idades['homem1'] = valida_entrada(input("Digite a idade do primeiro homem: "))
    idades['homem2'] = valida_entrada(input("Digite a idade do segundo homem: "))
    idades['mulher1'] = valida_entrada(input("Digite a idade da primeira mulher: "))
    idades['mulher2'] = valida_entrada(input("Digite a idade da segunda mulher: "))
    
    if None in idades.values():
        print("Por favor, insira todas as idades corretamente.")
        return None
    
    return idades

def calcular_soma_produto(idades):
    """Calcula a soma e o produto das idades conforme as regras do problema."""
    homens = [idades['homem1'], idades['homem2']]
    mulheres = [idades['mulher1'], idades['mulher2']]

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
    if idades is None:
        return  
    resultados = calcular_soma_produto(idades)
    
    exibir_resultados(resultados)

main()
