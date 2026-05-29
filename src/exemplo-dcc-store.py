from dash import Dash, dcc, html, Input, Output, callback
import plotly.express as px
import pandas as pd

app = Dash(__name__)

app.layout = html.Div([
    html.H2("Exemplo 1 — dcc.Store"),

    # Componente invisível que armazena os dados no navegador
    dcc.Store(id="store-dados"),

    html.Button("Carregar Dados", id="btn-carregar", n_clicks=0),
    dcc.Graph(id="grafico-store"),
])


# Callback: carregando os dados e os salva no Store
@callback(
    Output("store-dados", "data"),
    Input("btn-carregar", "n_clicks"),
)
def carregar_dados(n_clicks):
    if n_clicks == 0:
        return None

    df = pd.DataFrame({
        "Fruta": ["Maçã", "Banana", "Uva", "Laranja"],
        "Quantidade": [30, 45, 20, 55],
    })
    # Serializando como lista de dicionários para armazenar em JSON
    return df.to_dict("records")


# Callback: lendo os dados do Store e gera o gráfico
@callback(
    Output("grafico-store", "figure"),
    Input("store-dados", "data"),
)
def atualizar_grafico(dados):
    if dados is None:
        return {}

    df = pd.DataFrame(dados)
    return px.bar(df, x="Fruta", y="Quantidade", title="Vendas por Fruta")

if __name__ == '__main__':
    app.run(debug=True)