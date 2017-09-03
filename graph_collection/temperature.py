from plotly import graph_objs as go
import pandas as pd
import numpy as np
import dash_html_components as html
import dash_core_components as dcc


def build_graph():

    df = pd.read_csv('data/GLB.Ts+dSST.csv', skiprows=1)
    df.replace("***", np.nan, inplace=True)
    trace = go.Scatter(
        x=df['Year'],
        y=df["SON"],
        name='Temperatures'
    )
    layout = go.Layout(
        title='Evolution of mean temperature during the year'
    )
    fig = go.Figure(
        data=[trace],
        layout=layout
    )

    return html.Div([
        html.H3('Coucou tu veux voir mon graphe'),
        dcc.Graph(
            id='temp-graph',
            figure=fig
        )
    ])