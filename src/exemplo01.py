from dash import Dash, html

app = Dash(__name__)

app.layout = [
    html.H1('Minha Primeira Página Web com Dash'),
    html.P('Essa é minha primeira execução com o Dash!')
]

if __name__ == '__main__':
    app.run(debug=True)
