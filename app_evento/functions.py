import os
from random import choice


def gerar_codigo_alfanumerico(qtd_chars):
    chars_a_sortear = '123456789123456789BCDFGHJKLMNPQRSTVWXYZ'
    codigo = ''
    for c in range(qtd_chars):
        codigo += choice(chars_a_sortear)
    return codigo


def obter_extensao_arquivo(nome_do_arquivo):
    return os.path.splitext(nome_do_arquivo)[-1]
