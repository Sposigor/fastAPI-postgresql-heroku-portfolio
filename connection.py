""" Conexão com o banco de dados postgresql """
from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


DATABASE_URL = "INSERIR AQUI O CAMINHO PARA O BANCO DE DADOS"
engine = create_async_engine(DATABASE_URL)

sessio = sessionmaker(bind=engine, class_=AsyncSession)
