# <h1 align="center">PI_DSM_FATEC_2SEM2024 - GRUPO 3</h1>
<h2>Nome do nosso projeto: Ferteliz</h2>
<img src="https://github.com/marquesluana/PI_DSM_FATEC_GRUPO3_1SEM2024/blob/6a8de795a296957d3ffd7ddf9b6bf30891a36d5b/designer/logo.jpg" width="400px" text-align="center">

Repositório utilizado para o Projeto Interdisciplinar do 1º semestre de 2024 do curso de Desenvolvimento de Software Multiplataforma da Fatec Araras. O tema abordado é da ODS 2 - Fome Zero, e o grupo decidiu fazer um sistema web que fomenta o comércio com os pequenos agricultores da região.

## PARTICIPANTES:
- [Leandro Alves Rodirgues](https://github.com/)<br>
- [Luana Marques](https://github.com/marquesluana)<br>
- [Lucas Fernando Arantes](https://github.com/Arantees)<br>
- [Lucas Ferreira](https://github.com/)<br>
- [Lucas Luiz Assis](https://github.com/Luhcyy)<br>
- [Maikon Gino](https://github.com/MaikonGino)<br>

## TECNOLOGIAS UTILIZADAS:
<div>
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/django/django-plain.svg" width="50px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/mongodb/mongodb-plain-wordmark.svg" width="50px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/github/github-original-wordmark.svg" width="50px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/html5/html5-plain-wordmark.svg" width="50px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon@latest/icons/python/python-original-wordmark.svg" width="50px">
  <img src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/vscode/vscode-original-wordmark.svg" width="50px">
</div>

# COMO RODAR ESSE PROJETO?
## Pré-requisitos

Certifique-se de ter os seguintes softwares instalados em sua máquina:

- [Python](https://www.python.org/downloads/) (versão 3.x)
- [pip](https://pip.pypa.io/en/stable/installation/)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html)
- [Git](https://git-scm.com/downloads)

## Clonando o Repositório

Para clonar o repositório, execute o seguinte comando no seu terminal:

    git clone https://github.com/marquesluana/PI_DSM_FATEC_GRUPO3_1SEM2024.git

## Configurando o Ambiente Virtual

- Navegue até o diretório do projeto:

      cd ferteliz

- Crie um ambiente virtual:

      python -m venv venv

- Ative o ambiente virtual:
  
  No Windows:

      venv\Scripts\activate

  No macOS e Linux:

      source venv/bin/activate

## Instalando as Dependências

- Com o ambiente virtual ativado, instale as dependências necessárias:

      pip install pymongo
      python -m pip install Pillow
      pip install -r requirements.txt

## Configurando o Banco de Dados

- Aplique as migrações do banco de dados:

      python manage.py migrate

- (Opcional) Crie um superusuário para acessar o admin do Django:

      python manage.py createsuperuser

## Executando o Servidor de Desenvolvimento

- Para iniciar o servidor de desenvolvimento, execute:

      python manage.py runserver
  
O servidor estará disponível em http://127.0.0.1:8000/

## Testes

Para rodar os testes do projeto, execute:

    python manage.py test

## Estrutura do Projeto

Uma breve descrição da estrutura dos diretórios e arquivos principais do projeto.

Ferteliz/
│

├── manage.py

├── Ferteliz/

│   ├── __init__.py

│   ├── settings.py

│   ├── urls.py

│   ├── wsgi.py

│   └── ...

├── requirements.txt

└── ...
