from dash import Dash, dcc, html
import plotly.express as px
import pandas as pd

app = Dash(__name__)

df = pd.read_csv('data/gpd_countries.csv')
fig = px.scatter(df, x="gdp per capita",
                y="life expectancy",
                size="population",
                color="continent",
                hover_name="country",
                log_x=True,
                size_max=60)
app.layout = html.Div(children=[
   dcc.Graph(
       id='thrid-example-graph',
       figure=fig
   )
])

if __name__ == '__main__':
   app.run(debug=True)