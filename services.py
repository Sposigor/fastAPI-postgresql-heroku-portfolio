""" Serviços para o backend """
from sqlalchemy.future import select
from models import Projetos
from connection import sessio


class ServicosProjetos:
    """ Metodo async para conversa com o banco de dados postgresql """
    async def create_project(imagem_local, link_referencia, nome_projeto, linguagem_usada_mais_libs, tipo):
        """ Criar o projeto """
        async with sessio() as session:
            session.add(Projetos(imagem_local=imagem_local, link_referencia=link_referencia, nome_projeto=nome_projeto, linguagem_usada_mais_libs=linguagem_usada_mais_libs, tipo=tipo))
            await session.commit()

    async def list_projects():
        """ Listar os projetos """
        async with sessio() as session:
            result = await session.execute(select(Projetos))
            return result.scalars().all()
