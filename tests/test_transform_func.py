# Conteúdo do arquivo test_soma.py

from src.conexao_db import soma_dois_numeros  # Substitua "sua_pasta" pelo caminho correto
import pytest

def test_soma_dois_numeros():
    # Casos de teste
    assert soma_dois_numeros(2, 3) == 5
    assert soma_dois_numeros(0, 0) == 0
    assert soma_dois_numeros(-1, 1) == 0
    assert soma_dois_numeros(-5, -7) == -12

    # Teste com números grandes
    assert soma_dois_numeros(1000000, 9999999) == 10999999

    # Teste com números negativos e positivos
    assert soma_dois_numeros(-10, 10) == 0
    assert soma_dois_numeros(10, -10) == 0

    # Teste com zero
    assert soma_dois_numeros(0, 100) == 100
    assert soma_dois_numeros(100, 0) == 100

    # Teste com números muito pequenos
    assert soma_dois_numeros(-0.000001, 0.000001) == 0.0

    # Teste com números decimais (deve falhar, pois a função soma_dois_numeros aceita apenas inteiros)
    # with pytest.raises(TypeError):
    #     soma_dois_numeros(2.5, 3.5)

    # Teste com tipos diferentes (deve falhar)
    with pytest.raises(TypeError):
        soma_dois_numeros("1", 2)

    with pytest.raises(TypeError):
        soma_dois_numeros(1, "2")

    # with pytest.raises(TypeError):
    #     soma_dois_numeros("1", "2")

if __name__ == "__main__":
    pytest.main()
