""" Inicialização do banco de dados """
from asyncio import run
from connection import engine
from models import base

async def criando_database():
    """ Gerar um banco de dados """
    async with engine.begin() as connection:
        await connection.run_sync(base.metadata.drop_all)
        await connection.run_sync(base.metadata.create_all)

if __name__ == "__main__":
    run(criando_database())
