## Barbearia PDV ##
Sistema de gerenciamento de uma barbearia, desenvolvido em **Django**, com funcionalidades para cadastro de clientes, serviços, agendamentos e vendas.
Possui interface responsiva com estilos modernos usando CSS.

---

## Funcionalidades

- **Autenticação**
  - Login de usuário
  - Registro de novos usuários
- **Clientes**
  - Cadastro de clientes
  - Listagem de clientes
- **Serviços**
  - Cadastro de serviços
  - Listagem de serviços
- **Agendamentos**
  - Cadastro de agendamentos
  - Listagem de agendamentos
- **Relatórios**
  - Visualização de total de vendas
  - Listagem de agendamentos com cliente, serviço e data/hora

---

## Tecnologias

- **Backend:** Django 5.2.7
- **Frontend:** HTML, CSS (estilos modernos com blur e efeitos glass)
- **Banco de Dados:** SQLite (padrão Django)
- **Outros:** Python 3.12

---

## Estrutura do Projeto

'''
barbearia_pdv/
├── barbearia_pdv/
│   ├── __init__.py
│   ├── asgi.py
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── db.sqlite3
├── manage.py
└── pdv/
    ├── __init__.py
    ├── admin.py
    ├── apps.py
    ├── forms.py
    ├── migrations/
    │   ├── 0001_initial.py
    │   └── __init__.py
    ├── models.py
    ├── static/
    │   ├── global/
    │   │   └── styles.css
    │   └── login/
    │       └── login.css
    ├── templates/
    │   └── pdv/
    │       ├── agendamentos.html
    │       ├── base.html
    │       ├── clientes.html
    │       ├── criar_agendamento.html
    │       ├── criar_cliente.html
    │       ├── criar_servico.html
    │       ├── dashboard.html
    │       ├── login.html
    │       ├── register.html
    │       ├── relatorios.html
    │       └── servicos.html
    ├── tests.py
    ├── urls.py
    └── views.py
'''
