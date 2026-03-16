def calcular_total(preco, quantidade):
    return preco * quantidade

def aplicar_desconto(total, desconto):
    # O desconto deve ser um valor decimal (ex: 0.1 para 10%)
    return total - (total * desconto)