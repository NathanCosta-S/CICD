import pytest
from carrinho import calcular_total, aplicar_desconto

@pytest.mark.parametrize("preco, quantidade, esperado", [
    (10.0, 2, 20.0),   
    (5.5, 3, 16.5),    
    (0, 10, 0),       
    (100, 0, 0)      
])
def test_calcular_total(preco, quantidade, esperado):
    assert calcular_total(preco, quantidade) == esperado


@pytest.mark.parametrize("total, desconto, esperado", [
    (100.0, 0.10, 90.0),  
    (50.0, 0.50, 25.0),   
    (100.0, 0.0, 100.0), 
    (100.0, 1.0, 0.0) 
])
def test_aplicar_desconto(total, desconto, esperado):
    assert aplicar_desconto(total, desconto) == esperado