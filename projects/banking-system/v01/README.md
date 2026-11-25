# Sistema Bancário — V01

## Sobre o projeto

Primeira versão do sistema bancário desenvolvido em Python como parte dos desafios de projeto da plataforma Digital Innovation One (DIO).

O projeto consiste na implementação de um caixa eletrônico simplificado, executado através do terminal, permitindo realizar operações bancárias básicas e aplicar regras de negócio utilizando os fundamentos da linguagem Python.

Esta versão utiliza programação procedural, concentrando toda a lógica da aplicação em um único arquivo.

## Objetivos

- Aplicar os fundamentos da programação com Python.
- Desenvolver um menu interativo.
- Implementar operações bancárias básicas.
- Trabalhar com estruturas condicionais e de repetição.
- Realizar validações de entrada e regras de negócio.
- Desenvolver o raciocínio lógico através de uma aplicação prática.

## Funcionalidades

### Depósito

- Realizar depósitos na conta bancária.
- Validar valores maiores que zero.
- Atualizar o saldo disponível.
- Registrar a movimentação no extrato.

### Saque

- Realizar saques na conta bancária.
- Verificar o saldo disponível.
- Validar o valor solicitado.
- Controlar o limite por operação.
- Controlar a quantidade de saques realizados.
- Registrar a movimentação no extrato.

### Extrato bancário

- Exibir as movimentações realizadas.
- Apresentar os valores dos depósitos e saques.
- Exibir o saldo atual.
- Informar quando não existem movimentações.

### Encerramento

- Permitir o encerramento do sistema através do menu principal.

## Regras de negócio

| Regra                     | Definição                                 |
| ------------------------- | ----------------------------------------- |
| Saldo inicial             | R$ 0,00                                   |
| Valor mínimo de depósito  | Maior que zero                            |
| Valor mínimo de saque     | Maior que zero                            |
| Limite por saque          | R$ 500,00                                 |
| Limite de saques          | 3 por execução                            |
| Saldo insuficiente        | Operação não permitida                    |
| Registro de movimentações | Depósitos e saques realizados com sucesso |

## Conceitos aplicados

- Variáveis e constantes.
- Tipos de dados.
- Operadores aritméticos.
- Operadores relacionais e lógicos.
- Estruturas condicionais (`if`, `elif`, `else`).
- Estruturas de repetição (`while`).
- Controle de fluxo (`break`, `continue`).
- Manipulação de strings.
- Formatação de valores com f-strings.
- Entrada e saída de dados (`input`, `print`).

## Tecnologias utilizadas

- Python 3
- Git
- GitHub
- Visual Studio Code

O projeto não necessita de bibliotecas externas.

## Estrutura do projeto

```
v01/
├── 01_desafio_cx_eletronico.py
└── README.md
```

## Como executar

Acesse o diretório desta versão através do terminal:

```bash
cd projects/banking-system/v01
```

Execute o programa:

```bash
python 01_desafio_cx_eletronico.py
```

## Menu de operações

```
===== CAIXA ELETRÔNICO =====

[1] - Sacar
[2] - Depositar
[3] - Extrato
[0] - Sair
```

## Limitações da versão

Por se tratar da primeira implementação, esta versão possui algumas limitações:

- Dados armazenados exclusivamente em memória.
- Perda dos dados após o encerramento do programa.
- Ausência de cadastro de clientes.
- Ausência de gerenciamento de múltiplas contas.
- Ausência de modularização com funções.
- Ausência de tratamento de exceções para entradas não numéricas.
- Limite de saques reiniciado a cada execução.

Essas limitações fazem parte do escopo inicial do projeto e representam oportunidades de evolução nas próximas versões.

## Evolução do projeto

Esta versão representa a aplicação inicial dos fundamentos da linguagem Python.

As versões posteriores serão destinadas à implementação de funções, modularização, gerenciamento de clientes e contas, programação orientada a objetos e persistência de dados.

O código original é preservado para documentar a evolução técnica durante o processo de aprendizado.

## Referências

- [Digital Innovation One (DIO)](https://www.dio.me/)
- [Repositório oficial da Trilha Python — DIO](https://github.com/digitalinnovationone/trilha-python-dio)
- [Documentação oficial do Python](https://docs.python.org/pt-br/3/)

## Status

**Implementação inicial concluída — versão preservada para fins educacionais.**
