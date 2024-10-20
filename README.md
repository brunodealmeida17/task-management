
# Tasks manager com Django

## Descrição do Projeto

Este projeto é uma aplicação web de controle de tarefas e registro de tempo, desenvolvida em Django. A aplicação permite que os usuários:

- **Criem Tarefas**: Adicionem novas tarefas com detalhes específicos.
- **Registrem o Tempo Trabalhado**: Façam o acompanhamento do tempo investido em cada tarefa.
- **Listem Registros**: Visualizem os registros com filtros por data, usuário e gestão de tempo.

Além disso, a aplicação possibilita o controle do status das tarefas, que podem ser marcadas como: pendente, feito, reavaliar e em andamento.

A aplicação conta com um gráfico que exibe a quantidade de horas estimadas para cada tarefa, com base em uma jornada de trabalho de 44 horas semanais e 8 horas diárias, permitindo uma estimativa realista do tempo de trabalho.

Cada funcionalidade é gerenciada por grupos de usuários, garantindo um controle de acesso eficiente. Para atender às necessidades específicas do projeto e demonstrar conhecimento técnico, desenvolvi um modelo de autenticação personalizado.

A estimativa de tempo é integrada diretamente na criação e atualização de cada tarefa, eliminando a necessidade de alternar entre telas. Essa abordagem proporciona uma experiência de usuário mais fluida e prática.

### Tecnologias e Recursos Adicionais

- **Editor de Texto Rico**: Para o campo de descrição das tarefas e estimativas de tempo, utilizei o [Django CKEditor](https://django-ckeditor.readthedocs.io/), que oferece editabilidade avançada, permitindo a inserção de trechos de código e formatação de texto.

- **Ambiente de Desenvolvimento**: O projeto foi configurado para rodar com [Docker](https://www.docker.com/) e [Nginx](https://www.nginx.com/), simulando um ambiente de produção onde o Nginx serve arquivos estáticos e de mídia, além de redirecionar requisições para a aplicação Django em execução.

- **Visualização de Dados**: A inclusão de gráficos para estimativas de tarefas não só melhora a usabilidade, mas também demonstra habilidades em desenvolvimento front-end.


## Estrutura do Projeto

Aqui está uma breve descrição da estrutura do projeto Django:

```
task-management/
├── env/
│   ├── .env
├── nginx/
│   ├── nginx.conf
│   └── Dockerfile
├── src/
│   ├── home/
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── home/
│   │   │   │   ├── home.html
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── perfil_users/
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── perfil_users/
│   │   │   │   ├── group_crud.html
│   │   │   │   ├── login.html
│   │   │   │   ├── position_form.html
│   │   │   │   ├── profile_confirm_delete.html
│   │   │   │   ├── profile_form.html
│   │   │   │   ├── profile_list.html
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── static/
│   │   ├── css/
│   │   ├── js/
│   │   └── img/
│   ├── task_manager/
│   │   ├── __init__.py
│   │   ├── asgi.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   ├── wsgi.py
│   ├── TaskContextProcessors/
│   │   ├── contextProcessors.py
│   ├── tasks/
│   │   ├── __init__.py
│   │   ├── migrations/
│   │   ├── templates/
│   │   │   ├── perfil_users/
│   │   │   │   ├── task_confirm_delete.html
│   │   │   │   ├── task_form.html
│   │   │   │   ├── task_list.html
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── templates/
│   │   ├── base.html
│   │   ├── nav.html
│   ├── db.sqlite3
│   ├── manage.py
├── .env-exemple
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── entrypoint.sh
├── README.md
└── requirements.txt
```

## Pré-requisitos

Antes de começar, você precisará ter o seguinte instalado em sua máquina:

- [Python](https://www.python.org/downloads/) (3.8 ou superior)
- [pip](https://pip.pypa.io/en/stable/installation/) (gerenciador de pacotes do Python)
- [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html) (opcional, mas recomendado)
- [Git](https://git-scm.com/) (opcional, para controle de versão)

## Instalação manual

Siga as etapas abaixo para configurar seu projeto Django.

### 1. Clone o repositório
```bash
git clone https://github.com/brunodealmeida17/task-management
cd task-management
```
### 2. Crie e ative um ambiente virtual

É uma boa prática usar um ambiente virtual para gerenciar as dependências do projeto.
```
# Crie o ambiente virtual
python -m venv venv

# Ative o ambiente virtual
# No Windows
venv\Scripts\activate

# No macOS/Linux
source venv/bin/activate
```


### 3. Instale as dependências

Com o ambiente virtual ativado, instale as bibliotecas necessárias com o `pip
```
pip install -r requirements.txt
```

### 4. Configure o banco de dados

Edite o arquivo `settings.py` para configurar seu banco de dados. Por exemplo, para usar o SQLite (padrão):
```
# settings.py
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / "db.sqlite3",
    }
}
```

### 5. Realize as migrações do banco de dados

Após configurar o banco de dados, execute as migrações para criar as tabelas necessárias:

    python manage.py migrate

### 6. Crie um superusuário

Para acessar o painel de administração do Django, crie um superusuário:

    python manage.py createsuperuser

### 7. Execute o servidor de desenvolvimento

Agora você pode iniciar o servidor de desenvolvimento para ver seu projeto em ação:

    python manage.py runserver

### 8. Acesse o projeto

Abra seu navegador e vá para `http://127.0.0.1:8000/` para acessar a aplicação. Para acessar o painel de administração, vá para `http://127.0.0.1:8000/admin/` e faça login com o superusuário que você criou.

## Configurar e rodar o projeto com docker

Este projeto é uma aplicação Django configurada para rodar em containers Docker. Abaixo estão as instruções para clonar o repositório, instalar dependências e rodar o projeto.

## Pré-requisitos

Certifique-se de ter as seguintes ferramentas instaladas no seu ambiente de desenvolvimento:

- [Git](https://git-scm.com/)
- [Docker](https://docs.docker.com/get-docker/)
- [Docker Compose](https://docs.docker.com/compose/install/)

## Instalação

### 1. Clonar o repositório

Clone este repositório para sua máquina local:

```bash
git clone https://github.com/brunodealmeida17/task-management
cd task-management
```
### 2. Configurar as variáveis de ambiente

Renomei o arquivo `.env-exemple para .env na raiz do projeto e edite as seguintes variáveis de ambiente:

    SECRET_KEY=6@z33cbp=(+55*cjix&ed58-l9rd2lc*!(!dc01%cv6om5)!08
    DEBUG=True  # Mude para False em produção
    
    ## Super-User Credentials
    SUPER_USER_NAME='root'
    SUPER_USER_PASSWORD='root'
    SUPER_USER_EMAIL='admin@email.com'
    
    ## Databases
    DATABASE_DB=nome_banco_de_dados
    DATABASE_USER=nome_de_usuario
    DATABASE_PASSWORD=senha_do_banco

> **Nota:** Lembre-se de alterar as credenciais do superusuário e do banco de dados conforme necessário.

### 3. Construir e rodar o projeto com Docker

Com o Docker instalado, você pode facilmente construir e rodar o projeto com o seguinte comando:

    docker-compose up --build
    

> Isso fará o Docker Compose construir os containers definidos no
> `docker-compose.yml` e iniciar os serviços.

### 4. Acessar a aplicação

Após a conclusão da execução, a aplicação estará disponível em:

    http://localhost/home

> Não precisa passar a porta 8000, pois o nginx configurado no projeto com docker
> faz o redirecionamento para porta 80

Se precisar de acesso ao container:

    docker exec -it nome_do_container bash


> Não é necessário criar um superusuário manualmente nem aplicar as
> migrações ao usar Docker, pois o script `entrypoint.sh` já trata
> dessas operações automaticamente durante o processo de inicialização
> do container.
> 
> O projeto em Docker cria três containers e três volumes. Um container
> executa a aplicação Django com Gunicorn, outro gerencia o banco de
> dados, e o terceiro funciona como proxy reverso usando Nginx,
> responsável por servir os arquivos estáticos e de mídia. Os volumes
> incluem um para o banco de dados, garantindo a persistência dos dados,
> e dois volumes para armazenar os arquivos estáticos e de mídia,
> garantindo que esses arquivos estejam disponíveis e gerenciáveis entre
> os diferentes containers.
> **Importante**: Embora o banco de dados seja gerenciado via Docker neste projeto de desenvolvimento, não é uma boa prática utilizá-lo
> dessa forma em ambientes de produção. Isso ocorre porque o
> gerenciamento de backups e a persistência de dados são mais
> complicados nesse contexto. Para produção, é recomendável utilizar um
> cluster de banco de dados externo, garantindo alta disponibilidade,
> segurança e uma estratégia adequada de backups.

