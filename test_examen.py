from examen import comprueba
import pytest

def test_comprueba():
    assert comprueba(-1, 1), "Valor negativo inválido"

def test_comprueba():
    assert comprueba(200, 1), "Valor demasiado grande"

def test_comprueba():
    assert comprueba(-100, 1), "Valor demasiado pequeño"






