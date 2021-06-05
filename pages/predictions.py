# Imports from 3rd party libraries
import dash
import dash_bootstrap_components as dbc
import dash_core_components as dcc
import dash_html_components as html
from dash.dependencies import Input, Output
import dash_daq as daq
import pandas as pd

# Imports from this application
from app import app

from joblib import load
pipeline = load('assets/pipeline.joblib')

# 2 column layout. 1st column width = 4/12
# https://dash-bootstrap-components.opensource.faculty.ai/l/components/layout
column1 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Metrics

            The below metrics can be altered to determine potential of the song in Spotify

            """
        ),
        dcc.Markdown('#### Acoustiness'),
        dcc.Slider(
            id = 'acousticness',
            min = 0,
            max = 1,
            step = 0.1,
            value = .4
        ),
        dcc.Markdown('#### Danceability'),
        dcc.Slider(
            id = 'danceability',
            min = 0,
            max = 1,
            step = 0.1,
            value = .2
        ),
        dcc.Markdown('#### Energy'),
        dcc.Slider(
            id = 'energy',
            min = 0,
            max = 1,
            step = 0.1,
            value = .8
        ),
        dcc.Markdown('#### Instrumentalness'),
        dcc.Slider(
            id = 'instrumentalness',
            min = 0,
            max = 1,
            step = 0.1,
            value = 0
        ),
        dcc.Markdown('#### Liveness'),
        dcc.Slider(
            id = 'liveness',
            min = 0,
            max = 1,
            step = 0.1,
            value = .7
        ),
        dcc.Markdown('#### Speechiness'),
        dcc.Slider(
            id = 'speechiness',
            min = 0,
            max = 1,
            step = 0.1,
            value = 0
        ),
        dcc.Markdown('#### Valence'),
        dcc.Slider(
            id = 'valence',
            min = 0,
            max = 1,
            step = 0.1,
            value = .6
        ),
        dcc.Markdown('#### Duration'),
        dcc.Slider(
            id = 'duration',
            min = 8042,
            max = 2059336,
            step = 10000,
            value = 100000
        ),
        dcc.Markdown('#### Explicit'),
        dcc.Dropdown(
            id = 'explicit',
            options = [
                {'label':'Non-Explicit Content', 'value':0},
                {'label':'Explicit Content', 'value':1},
            ],
            value = 0
        ),
        dcc.Markdown('#### Mode'),
        dcc.Dropdown(
            id = 'mode',
            options = [
                {'label':'0', 'value':0},
                {'label':'1', 'value':1},
            ],
            value = 1
        ),
        dcc.Markdown('#### Key'),
        dcc.Slider(
            id = 'key',
            min = 0,
            max = 11,
            step = 0.5,
            value = 2
        ),
        dcc.Markdown('#### Tempo'),
        dcc.Slider(
            id = 'tempo',
            min = 0,
            max = 222,
            step = 10,
            value = 100
        ),
        dcc.Markdown('#### Loudness'),
        dcc.Slider(
            id = 'loudness',
            min = -35,
            max = 1,
            step = 2.5,
            value = -8
        ),
    ],
    md=4,
)

column2 = dbc.Col(
    [
        html.H2('Song Potential', className='mb-5'),
        html.Div(id = 'prediction-content', className='lead'),
        html.Div(id='prediction-image') 
       
    ]
)
column3 = dbc.Col(
    [
        dcc.Markdown(
            """
        
            ## Metrics

            This dataset has several variables about the songs listed below:

            Acousticness — The higher the value the more acoustic the song is

            Danceability — The higher the value, the easier it is to dance to this song

            Energy — The energy of a song — the higher the value, the more energetic song

            Instrumentalness - Predicts whether a track contains no vocals

            Liveness — The higher the value, the more likely the song is a live recording

            Speechiness — The higher the value the more spoken word the song contains

            Valence — The higher the value, the more positive mood for the song

            Loudness (dB) — The higher the value, the louder the song

            Duration — The length of the song

            Explicit - Whether or not the track has explicit lyrics

            Mode - Mode indicates the modality (major or minor) of a track, the type of scale from which its melodic content is derived

            Key - The key the track is in. Integers map to pitches using standard Pitch Class notation 

            Tempo - The overall estimated tempo of a track in beats per minute (BPM)
            
            Loudness - The overall loudness of a track in decibels (dB). 

            """
        )
    ]
)


layout = dbc.Row([column1, column2,column3])

@app.callback(
    Output('prediction-content','children'),
    [Input('acousticness','value'),Input('danceability','value'),Input('energy','value'),Input('instrumentalness','value'),Input('liveness','value'),Input('speechiness','value'),Input('valence','value'),Input('duration','value'),Input('explicit','value'),Input('mode','value'),Input('key','value'),Input('tempo','value'),Input('loudness','value')]
)

def predict(acousticness,danceability,energy,instrumentalness,liveness,speechiness,valence,duration_ms,explicit,mode,key,loudness,tempo):
    df = pd.DataFrame(
        columns = ['acousticness','danceability','energy','instrumentalness','liveness','speechiness','valence','duration_ms','explicit','mode','key','loudness','tempo'],
        data = [[acousticness,danceability,energy,instrumentalness,liveness,speechiness,valence,duration_ms,explicit,mode,key,loudness,tempo]]
        )
    y_pred = pipeline.predict(df)[0]
    return f'{y_pred} potential of being a popular song'

@app.callback(
    Output('prediction-image','children'),
    [Input('acousticness','value'),Input('danceability','value'),Input('energy','value'),Input('instrumentalness','value'),Input('liveness','value'),Input('speechiness','value'),Input('valence','value'),Input('duration','value'),Input('explicit','value'),Input('mode','value'),Input('key','value'),Input('tempo','value'),Input('loudness','value')]
)

def predict_image(acousticness,danceability,energy,instrumentalness,liveness,speechiness,valence,duration_ms,explicit,mode,key,loudness,tempo):
    df = pd.DataFrame(
        columns = ['acousticness','danceability','energy','instrumentalness','liveness','speechiness','valence','duration_ms','explicit','mode','key','loudness','tempo'],
        data = [[acousticness,danceability,energy,instrumentalness,liveness,speechiness,valence,duration_ms,explicit,mode,key,loudness,tempo]]
        )
    y_pred = pipeline.predict(df)[0]
    if y_pred == 'High':
        return html.Img(src='assets/coachella-festival.jpeg',className='img-fluid', style = {'height': '300px'})
    elif y_pred == 'Low':
        return html.Img(src='assets/smallpop.jpeg',className='img-fluid', style = {'height': '300px'})  
    else:
        return html.Img(src='assets/mediumpop.jpeg',className='img-fluid', style = {'height': '300px'})