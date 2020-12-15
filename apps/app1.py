import dash_core_components as dcc
import dash_html_components as html
import dash_table
from dash.dependencies import Input, Output
from app import app


from time import time
from collections import defaultdict

import numpy as np
import pandas as pd
import plotly.graph_objs as go
import plotly.express as px

#import seaborn as sns

from sklearn.feature_extraction.text import CountVectorizer, TfidfVectorizer, TfidfTransformer
from sklearn.metrics import f1_score, accuracy_score
from sklearn.model_selection import ShuffleSplit
from sklearn.pipeline import Pipeline, FeatureUnion
from sklearn.linear_model import SGDClassifier, LogisticRegression, LogisticRegressionCV
from sklearn.svm import SVC, LinearSVC
from sklearn.naive_bayes import MultinomialNB, CategoricalNB, ComplementNB, BernoulliNB
from sklearn.decomposition import FastICA, KernelPCA, TruncatedSVD, SparsePCA, NMF, FactorAnalysis, LatentDirichletAllocation

import nltk

from data_analysis import lemmatize


### Encapsulate this
stopwords = nltk.corpus.stopwords.words("english")

# load data from https://www.kaggle.com/ishantjuyal/emotions-in-text
d1 = pd.read_csv("../data/Emotion_final.csv")

# replace happy by joy
d1["Emotion"].replace("happy", "joy", inplace=True)

d1_prep = d1.copy()
d1_prep["Text"] = d1_prep["Text"].apply(lemmatize)


layout = html.Div([
    dcc.Dropdown(
        id='app1-dropdown',
        value=0,
        options=[
            {'label': v, 'value': i} for i, v in enumerate(
                ['raw text',
                 'pre-process text',
                ])
        ]
    ),
    html.Br(),
    html.Div(id='app1-display'),
    html.Br(),
    html.Br(),
    html.Br(),
    dcc.Graph(id="hist-labels"),
    html.P("To define:"),
    dcc.Slider(id="treshold", min=1, max=3, value=1,
               marks={1: '1', 2: '2'}),
])


@app.callback(
    Output('app1-display', 'children'),
    Input('app1-dropdown', 'value'))
def display_table(value):
    if value == 0:
        df = d1
    elif value == 1:
        df = d1_prep

    table = dash_table.DataTable(
        id='table-text',
        columns=[{"name": i, "id": i} for i in d1.columns],
        style_cell={'textAlign': 'left',
                    'whiteSpace': 'normal',
                    'height': 'auto',
                    'width': "90%",
                   },
        #style_as_list_view=True,
        sort_action="native",
        page_size=15,
        data=df.to_dict(orient="records"),
    )
    return table


@app.callback(
    Output("hist-labels", "figure"),
    Input("treshold", "value"))
def display_labels_hist(value):
    fig = px.histogram(d1, x="Emotion", color="Emotion").update_xaxes(categoryorder="total descending")
    return fig
