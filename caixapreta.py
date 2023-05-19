def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Teste de caixa preta
def test_calcular_media_caixa_preta():
    # Teste com lista vazia
    assert calcular_media([]) == 0

    # Teste com lista de números positivos
    assert calcular_media([1, 2, 3, 4, 5]) == 3

    # Teste com lista de números negativos
    assert calcular_media([-1, -2, -3, -4, -5]) == -3

    # Teste com lista mista de números positivos e negativos
    assert calcular_media([1, -2, 3, -4, 5]) == 0.6

    # Teste com lista de números decimais
    assert calcular_media([1.5, 2.5, 3.5]) == 2.5

    # Teste com lista contendo um único número
    assert calcular_media([10]) == 10

test_calcular_media_caixa_preta()
