import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app
from apps import app1, app2


app.layout = html.Div([
    dcc.Location(id='url', refresh=False),
    html.Div(id='page-content')
])

home = html.Div([
    html.H1('Dashboard Homepage'),
    dcc.Link('Go to the Results Dashboard',
             href='/apps/app1'),
    html.Br(),
    dcc.Link('Go to the Classification Results Dashboard', href='/apps/app2')
])

home_link = html.Div([dcc.Link('back to home', href='/'),
                      html.Br(),
                      html.Br(),
                     ])

@app.callback(Output('page-content', 'children'),
              Input('url', 'pathname'))
def display_page(pathname):
    if pathname == "/":
        return home
    elif pathname == '/apps/app1':
        return [home_link, app1.layout]
    elif pathname == '/apps/app2':
        return [home_link, app2.layout]
    else:
        return '404'


if __name__ == '__main__':
    app.run_server(debug=True)
