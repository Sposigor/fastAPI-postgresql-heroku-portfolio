"""
Backend para a aplicação

imagem
link_referencia
nome_projeto
linguagem_usada_mais_libs
"""

from fastapi import FastAPI, Request, Depends, HTTPException
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from fastapi.security import OAuth2PasswordRequestForm
import fastapi.middleware.cors as _cors
from services import ServicosProjetos
from schemas import User, Projeto
from autenticação import get_current_active_user, usuario, UserInDB, fake_hash_password


app = FastAPI()

app.add_middleware(
    _cors.CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
)


@app.post("/token")
async def login(form_data: OAuth2PasswordRequestForm = Depends()):
    """ Login para usar o FastAPI """
    user_dict = usuario.get(form_data.username)
    if not user_dict:
        raise HTTPException(status_code=400, detail="Login ou Senha, incorreto")
    user = UserInDB(**user_dict)
    hashed_password = fake_hash_password(form_data.password)
    if not hashed_password == user.hashed_password:
        raise HTTPException(status_code=400, detail="Login ou Senha, incorreto")

    return {"access_token": user.username, "token_type": "bearer"}


@app.get("/users/me")
async def read_users_me(current_user: User = Depends(get_current_active_user)):
    """ Validação de usuário ativo """
    return current_user


app.mount("/static", StaticFiles(directory="static"), name="static")
template = Jinja2Templates(directory="./")

@app.get("/", response_class = HTMLResponse)
async def index(request: Request, projeto: Projeto = Depends(ServicosProjetos.list_projects)):
    """ Rendereriza a pagina inicial """
    return template.TemplateResponse("index.html", {"request": request, "projetos":projeto})

@app.post("/novo_projeto", description="Cadastrar um novo projeto, filtros disponiveis .vis .ccode .ml .deep .ia")
async def novo_projeto(imagem_local: str, link_referencia: str, nome_projeto: str, linguagem_usada_mais_libs: str, tipo: str):
    """ Cadastrar um novo projeto """
    return await ServicosProjetos.create_project(imagem_local, link_referencia, nome_projeto, linguagem_usada_mais_libs, tipo)
