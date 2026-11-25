"""
Desafio 01 - Padronização de Mensagens

Objetivo:
Padronizar uma mensagem, convertendo seus caracteres
para minúsculas e removendo espaços desnecessários.

Conceitos:
- Funções
- Manipulação de strings
- Estruturas condicionais
- Early return
- Métodos strip(), lower(), split() e join()

Fonte: DIO - Desafios de Código Python
"""


def formatar_mensagem(texto):
    # Remove espaços extras do início e do fim da string
    texto = texto.strip()

    # TODO: Se a string ficou vazia após o strip, retorne a string vazia
    # Dica: verifique se o texto ficou vazio após retirar espaços
    if not texto:
        return ""

    # TODO: Processar o texto para garantir:
    #   - letras minúsculas
    #   - apenas um espaço separando as palavras (não podem haver múltiplos espaços)
    # Dica: separe a string em palavras e depois una novamente, garantindo um espaço entre elas

    # Retorne o texto já formatado conforme as regras
    # return mensagem_formatada
    texto = texto.lower()
    palavras = texto.split()
    mensagem_formatada = " ".join(palavras)

    return mensagem_formatada


# Lê a mensagem enviada ao robô via input padrão
entrada = input()  # Tipo de dado esperado: str

# Chama a função formatar_mensagem (você irá implementar a lógica)
saida = formatar_mensagem(entrada)

# Exibe a mensagem padronizada
print(saida)
