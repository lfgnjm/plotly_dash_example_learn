# Dashboard Django + Dash

Projeto web que integra Django como framework backend com Dash/Plotly para visualização de dados interativos.

## Requisitos

- Python 3.11+
- conda (opcional)

## Instalação

### Com conda

```bash
conda env create -f environment.yml
conda activate dash_django
```

### Com pip

```bash
pip install django dash plotly pandas
```

## Executar o projeto

```bash
cd teste_entrev
python manage.py runserver
```

Acesse: http://127.0.0.1:8000/dash/

## Estrutura do Projeto

```
.
├── dashboard_project/   # Configurações Django
│   ├── settings.py
│   └── urls.py
├── charts/             # App Django com Dash
│   ├── views.py        # View que integra Dash ao Django
│   ├── urls.py
│   ├── dash_setup.py  # Configuração do Dash com dados fictícios
│   └── dash_middleware.py
├── environment.yml     # Dependências conda
├── manage.py
└── README.md
```

## Funcionalidades

- Gráfico de linha interativo com seletor Vendas/Lucro
- Gráfico de barras por mês
- Layout responsivo com Bootstrap

## Dados Fictícios

Os dados para teste estão inclusos em `charts/dash_setup.py`:

| Mês   | Vendas | Lucro |
|-------|--------|-------|
| Jan   | 1200   | 400   |
| Fev   | 1900   | 700   |
| Mar   | 3000   | 1200  |
| Abr   | 2500   | 900   |
| Mai   | 2800   | 1100  |
| Jun   | 3500   | 1500  |
| Jul   | 3200   | 1300  |
| Ago   | 4100   | 1800  |
| Set   | 3800   | 1600  |
| Out   | 4200   | 2000  |
| Nov   | 4800   | 2200  |
| Dez   | 5500   | 2800  |

Para alterar os dados, edite o DataFrame na função `create_dash_app` em `charts/dash_setup.py`.