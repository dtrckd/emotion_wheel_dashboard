import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output

from app import app

layout = html.Div([
    dcc.Dropdown(
        id='app2-dropdown',
        options=[
            {'label': i, 'value': i} for i in [
                'raw text', 'pre-process text',
            ]
        ]
    ),
    html.Div(id='app2-display'),
])


@app.callback(
    Output('app2-display', 'children'),
    Input('app2-dropdown', 'value'))
def display_value(value):
    return 'You have selected "{}"'.format(value)
