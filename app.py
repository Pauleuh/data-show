import dash
import dash_core_components as dcc
import dash_html_components as html
from plotly import graph_objs as go
import pandas as pd
import numpy as np

print(dcc.__version__)  # 0.6.0 or above is required

app = dash.Dash()

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "/"', href='/'),
    html.Br(),
    dcc.Link('Navigate to "/page-2"', href='/page-2'),

    # content will be rendered in this element
    html.Div(id='page-content')
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
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
        html.H3('Coucou tu veux voir mon graphe'.format(pathname)),
        dcc.Graph(
            id='temp-graph',
            figure=fig
        )
    ])


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True)
