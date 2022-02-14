""" Esquemas para validar os dados pelo pydantic """

from pydantic import BaseModel


class User(BaseModel):
    """ Usuario para autenticação """
    username: str
    disabled: bool | None = None


class Projeto(BaseModel):
    """ Projeto para o backend """
    imagem_local: str
    link_referencia: str
    nome_projeto: str
    linguagem_usada_mais_libs: str
    tipo: str
