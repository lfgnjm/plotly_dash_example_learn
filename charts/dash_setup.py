import dash
from dash import dcc, html
from dash.dependencies import Input, Output
import plotly.express as px
import pandas as pd


def create_dash_app(requests_pathname_prefix=None):
    app = dash.Dash(
        __name__,
        requests_pathname_prefix=requests_pathname_prefix,
        external_stylesheets=['https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css']
    )

    df = pd.DataFrame({
        'Mes': ['Jan', 'Fev', 'Mar', 'Abr', 'Mai', 'Jun', 'Jul', 'Ago', 'Set', 'Out', 'Nov', 'Dez'],
        'Vendas': [1200, 1900, 3000, 2500, 2800, 3500, 3200, 4100, 3800, 4200, 4800, 5500],
        'Lucro': [400, 700, 1200, 900, 1100, 1500, 1300, 1800, 1600, 2000, 2200, 2800]
    })

    app.layout = html.Div([
        html.H2("Dashboard de Vendas - 2024", className="text-center my-4"),
        html.Div([
            dcc.Dropdown(
                id='metric-select',
                options=[
                    {'label': 'Vendas', 'value': 'Vendas'},
                    {'label': 'Lucro', 'value': 'Lucro'}
                ],
                value='Vendas',
                className="mb-4"
            )
        ], className="container"),

        dcc.Graph(id='main-chart', className="container"),

        html.Div([
            html.Div([
                dcc.Graph(figure=px.bar(df, x='Mes', y='Vendas', title='Vendas por Mês', color_discrete_sequence=['#3498db']))
            ], className="col-md-6"),
            html.Div([
                dcc.Graph(figure=px.line(df, x='Mes', y='Lucro', title='Lucro por Mês', color_discrete_sequence=['#2ecc71']))
            ], className="col-md-6"),
        ], className="row container mt-4")
    ], className="container-fluid")

    @app.callback(
        Output('main-chart', 'figure'),
        Input('metric-select', 'value')
    )
    def update_chart(selected_metric):
        fig = px.line(
            df, 
            x='Mes', 
            y=selected_metric,
            title=f'{selected_metric} ao Longo do Ano',
            markers=True,
            color_discrete_sequence=['#e74c3c']
        )
        fig.update_layout(
            plot_bgcolor='white',
            paper_bgcolor='white',
            font=dict(family="Arial", size=14)
        )
        return fig

    return app