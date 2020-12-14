import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    dcc.Dropdown(
        id='app1-dropdown',
        options=[
            {'label': v, 'value': i} for i, v in enumerate(
                ['raw text',
                 'pre-process text',
                ])
        ]
    ),
    html.Div(id='app1-display'),
])


@app.callback(
    Output('app1-display', 'children'),
    Input('app1-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
