from dash import Dash, html, Input, Output, callback, dcc

app = Dash(__name__)

# Variável global que armazenará os dados entre callbacks
dados_globais = {}

app.layout = html.Div([
    html.H2("Exemplo 2 — Variável Global"),

    dcc.Input(id="input-nome", placeholder="Digite seu nome", debounce=True),
    html.Button("Salvar", id="btn-salvar", n_clicks=0),
    html.Div(id="saida-salvar"),

    html.Hr(),

    html.Button("Ler Dado Salvo", id="btn-ler", n_clicks=0),
    html.Div(id="saida-ler"),
])


# Callback: salvando o valor na variável global
@callback(
    Output("saida-salvar", "children"),
    Input("btn-salvar", "n_clicks"),
    Input("input-nome", "value"),
    prevent_initial_call=True,
)
def salvar_dado(n_clicks, nome):
    global dados_globais
    if not nome:
        return "Digite um nome antes de salvar."
    dados_globais["nome"] = nome
    return f"Nome '{nome}' salvo na variável global."


# Callback: lendo o valor da variável global
@callback(
    Output("saida-ler", "children"),
    Input("btn-ler", "n_clicks"),
    prevent_initial_call=True,
)
def ler_dado(n_clicks):
    nome = dados_globais.get("nome")
    if nome is None:
        return "Nenhum dado salvo ainda."
    return f"Dado recuperado: '{nome}'"

if __name__ == '__main__':
    app.run(debug=True)