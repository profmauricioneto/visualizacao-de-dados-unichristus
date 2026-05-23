from dash import dash, dcc, html, Input, Output, callback

app = dash.Dash(__name__)

app.layout = html.Div([
    html.H3(children="Primeiro exemplo de callback"),
    html.Div([
        dcc.Input(id='input-text', type='text', placeholder='Digite alguma coisa'),
    ]),
    html.Div(id='output-text'),
])

@callback(
    Output(component_id='output-text', component_property='children'),
    Input(component_id='input-text', component_property='value')
)
def atualizar_saida(value = ''):
    return f'Saída: {value}'


if __name__ == '__main__':
    app.run(debug=True)