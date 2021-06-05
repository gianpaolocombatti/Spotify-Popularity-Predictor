# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import plotly.express as px

# Imports from this application
from app import app

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Allocate Ad $ in Proportion to a Song's Popularity


            Use this educational app to analyze how different paramenters affect the popularity of a song in Spotify. 

            Instead of allocating Ad Budget for songs/albums randomly based on the belief of potential success, 
            this app analyzes how a song's structure will dictate its popularity for a better $ allocation.

            """
        ),
        dcc.Link(dbc.Button('Predict Popularity', color='primary'), href='/predictions')
    ],
    md=4,
)



column2 = dbc.Col(
    [
        html.Img(src='assets/spotify_logo.webp',className='img-fluid', style = {'height': '350px'})
    ]
)

layout = dbc.Row([column1, column2])