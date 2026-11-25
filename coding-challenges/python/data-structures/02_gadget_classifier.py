"""
Desafio 02 - Classificação de Gadgets

Objetivo:
Implementar uma função que recebe o código de um gadget
e retorna sua categoria de acordo com o primeiro caractere.

Regras:
- T: tablet
- P: phone
- N: notebook
- Outros: unknown

Conceitos:
- Funções
- Manipulação de strings
- Estruturas condicionais
- Parâmetros e argumentos
- Retorno de valores

Fonte: DIO - Desafios de Código Python
"""


def identificar_categoria_gadget(codigo):
    """
    Recebe uma string 'codigo' e retorna a categoria associada:
    - 'T': tablet
    - 'P': phone
    - 'N': notebook
    Se não corresponder, retorna 'unknown'.
    """
    # TODO: Implemente a lógica para identificar a categoria do gadget
    # Dica: Verifique a primeira letra do código para determinar a categoria
    # Tipo esperado: 'codigo' é uma string não vazia

    match codigo[0]:
        case "T":
            return "tablet"
        case "P":
            return "phone"
        case "N":
            return "notebook"
        case _:
            return "unknown"


# Leitura da entrada (espera-se uma string representando o código do gadget)
codigo_gadget = input().strip()

# Chamada da função e saída do resultado
categoria = identificar_categoria_gadget(codigo_gadget)

print(categoria)  # Deve imprimir uma das categorias ou 'unknown'
