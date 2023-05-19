def calcular_media(numeros):
    if len(numeros) == 0:
        return 0
    soma = sum(numeros)
    media = soma / len(numeros)
    return media

# Teste de caixa branca
def test_calcular_media():
    # Teste com lista vazia
    assert calcular_media([]) == 0

    # Teste com lista de números positivos
    assert calcular_media([1, 2, 3, 4, 5]) == 3

    # Teste com lista de números negativos
    assert calcular_media([-1, -2, -3, -4, -5]) == -3

    # Teste com lista mista de números positivos e negativos
    assert calcular_media([1, -2, 3, -4, 5]) == 0.6
calcular_media([1,3,4,6])
test_calcular_media()
