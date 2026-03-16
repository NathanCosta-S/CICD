# Sistema de Carrinho de Compras

Este projeto automatiza a lógica de precificação e aplicação de descontos, servindo como base para a etapa de **Test** em um pipeline de CI/CD.

## Tecnologias e Ferramentas
* **Linguagem:** Python 3.13+
* **Framework de Testes:** Pytest 9.0+

## Estrutura de Arquivos
* `carrinho.py`: Contém as funções de lógica de negócio (`calcular_total` e `aplicar_desconto`).
* `teste_carrinho.py`: Contém 8 cenários de testes automatizados e parametrizados.

## Como Executar os Testes

Para garantir que a lógica de preços está correta, utilize o comando abaixo no terminal do VS Code:

```bash
python -m pytest -v teste_carrinho.py