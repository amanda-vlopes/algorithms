from challenges.challenge_encrypt_message import encrypt_message
import pytest


def test_encrypt_message():
    "Verifica se ao passar um valor para key que não é int é lançado um erro"
    with pytest.raises(TypeError, match="tipo inválido para key"):
        encrypt_message("teste", 2.5)

    "Verifica se message não for str é lançado um erro"
    with pytest.raises(TypeError, match="tipo inválido para message"):
        encrypt_message(2, 2)

    "Verifica se key for maior que o tamanho da str, a str é revertida"
    assert encrypt_message("teste", 10) == "etset"

    "Verifica se tem retorno correto ao passar um valor par para o key"
    assert encrypt_message("teste", 2) == "ets_et"

    "Verifica se tem retorno correto ao passar um valor ímpar para o key"
    assert encrypt_message("teste", 3) == "set_et"
