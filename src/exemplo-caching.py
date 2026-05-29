import time
from dash import Dash, html, Input, Output, callback, dcc
from flask_caching import Cache

app = Dash(__name__)

# Configura o cache em memória simples
cache = Cache(app.server, config={"CACHE_TYPE": "SimpleCache"})

app.layout = html.Div([
    html.H2("Exemplo 3 — Cache de Memória (flask_caching)"),

    dcc.Input(id="input-valor", type="number",
              placeholder="Digite um número", debounce=True),

    html.Button("Calcular", id="btn-calcular", n_clicks=0),

    html.Div(id="saida-callback-1"),
    html.Div(id="saida-callback-2"),
])

# Função "pesada" simulada — executada apenas uma vez por valor único
@cache.memoize(timeout=60)  # resultado em cache por 60 segundos
def processamento_pesado(valor):
    time.sleep(2)           # simula processamento demorado
    return valor * valor    # exemplo: calcula o quadrado

# Callback: usa o resultado em cache
@callback(
    Output("saida-callback-1", "children"),
    Input("btn-calcular", "n_clicks"),
    Input("input-valor", "value"),
    prevent_initial_call=True,
)
def callback_um(n_clicks, valor):
    if valor is None:
        return "Informe um número."
    resultado = processamento_pesado(valor)  # usa cache
    return f"[Callback 1] Quadrado de {valor} = {resultado}"

# Callback 2: reutiliza o mesmo cache, sem reprocessar
@callback(
    Output("saida-callback-2", "children"),
    Input("btn-calcular", "n_clicks"),
    Input("input-valor", "value"),
    prevent_initial_call=True,
)
def callback_dois(n_clicks, valor):
    if valor is None:
        return ""
    resultado = processamento_pesado(valor)  # retorna do cache
    return f"[Callback 2] Resultado em cache confirmado: {resultado}"


if __name__ == "__main__":
    app.run(debug=True)