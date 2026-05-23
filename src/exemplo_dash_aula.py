from dash import Dash, html, dcc, callback, Input, Output
import pandas as pd
import plotly.express as px

app = Dash(__name__)

dataframe = pd.read_csv('data/data_for_callback.csv')

app.layout = html.Div([
    dcc.Graph(id='grafico_tempo'),
    dcc.Slider(
        dataframe['year'].min(),
        dataframe['year'].max(),
        step=None,
        value=dataframe['year'].min(),
        marks={str(year): str(year) for year in dataframe['year'].unique()},
        id='year_slider'
    )
])

@callback(
    Output(component_id='grafico_tempo', component_property='figure'),
    Input(component_id='year_slider', component_property='value')
)
def update_graph(select_year):
    data_filtered = dataframe[dataframe['year'] == select_year]
    graph = px.scatter(data_filtered, x='gdpPercap', y='lifeExp', color='country', size='pop', hover_name='country')
    graph.update_layout(transition_duration=500)
    return graph

if __name__ == '__main__':
    app.run(debug=True)