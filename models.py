""" Modelo de tabalas do banco de dados """

from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import declarative_base

base = declarative_base()

# Armazenar as informações dos projetos
class Projetos(base):
    """ Tabela de projetos """
    __tablename__ = 'projetos'
    id = Column(Integer, primary_key=True, autoincrement=True)
    imagem_local = Column(String(450), nullable=False)
    link_referencia = Column(String(450), nullable=False)
    nome_projeto = Column(String(450), nullable=False)
    linguagem_usada_mais_libs = Column(String(50), nullable=False)
    tipo = Column(String(15), nullable=False)
