import dash
import dash_core_components as dcc
import dash_html_components as html
from graph_collection import temperature


print(temperature)

app = dash.Dash()

app.layout = html.Div([
    # represents the URL bar, doesn't render anything
    dcc.Location(id='url', refresh=False),

    dcc.Link('Navigate to "index"', href='/'),
    html.Br(),

    # content will be rendered in this element
    html.Div(id='page-content')
])

index_page = html.Div([
    dcc.Link('Go to Temperature graph', href='/Temperature'),
    html.Br()
])


@app.callback(dash.dependencies.Output('page-content', 'children'),
              [dash.dependencies.Input('url', 'pathname')])
def display_page(pathname):
    if pathname == '/Temperature':
        return temperature.build_graph()

    else:
        return index_page


app.css.append_css({
    'external_url': 'https://codepen.io/chriddyp/pen/bWLwgP.css'
})


if __name__ == '__main__':
    app.run_server(debug=True)
