import pandas as pd
import plotly.express as px
import numpy as np
# import dash_table as dt
import dash
from dash import dcc
from dash.dependencies import Input, Output
import plotly.express as px
import dash_bootstrap_components as dbc
from dash import html
import dash_bootstrap_components as dbc

from dash import html
from plotly.subplots import make_subplots
import plotly.graph_objects as go

df = pd.read_excel("https://yajitersoo.github.io/jsonapi/hdx-_06a-dtm-nigeria-round-39-dataset-of-site-assessment.xlsx",
                   sheet_name="Site Assessment Dataset")

### cleaning for filters

available_state = list(df['State'].unique())
available_state = [item for item in available_state if not (pd.isnull(item)) == True]

available_lga = list(df['LGA'].unique())
available_lga = [item for item in available_lga if not (pd.isnull(item)) == True]

### Starting Dashboard layout

# app = JupyterDash(__name__,
# external_stylesheets=[dbc.themes.BOOTSTRAP]
#                  )
app = dash.Dash(__name__)
app = dash.Dash(__name__, external_stylesheets=[dbc.themes.BOOTSTRAP])

server = app.server

app.config.suppress_callback_exceptions = True

### Headers
# https://yajitersoo.github.io/jsonapi/profile-bg.png
logo = [html.Img(src="https://yajitersoo.github.io/jsonapi/logo.png",
                 # width='64.7px', height='70.6px',style={"float":"center"},
                 style={
                     'hieght': '70.6px', 'width': '64.7px',
                     'margin-left': 'auto',
                     'margin-right': 'auto',
                     'padding-left': '25px',
                     'padding-top': '15px',
                     'padding-bottom': '15px',
                     'align': 'center'
                 })]
title = [html.H4("Displacement Tracking Matrix | Site Assessment | North-East Nigeria",
                 style={
                     "font-family": "sans-serif",
                     "font-size": 24,
                     "font-color": "black",
                     "text-align": "left",
                     'float': ';eft'
                 })]

### Dropdowns

state_dpdn = dcc.Dropdown(
    id="select_state",
    multi=False,
    value='All',
    placeholder='Select State',
    options=[{'label': i, 'value': i} for i in np.append(['All'], available_state)],
)

lga_dpdn = dcc.Dropdown(
    id="select_lga",
    multi=False,
    value='All',
    placeholder='Select LGA',
    options=[],
)

### Graphs

# Site number by status
site_num_status = [
    html.H5('Site number by status'),
    dcc.Graph(id='site_number_by_status', style={"height": "100%", "width": "100%"})
]

# Site number by status
population_site_status = [
    html.H5('Population by site status'),
    dcc.Graph(id='pop_site_status', style={"height": "100%", "width": "100%"})
]

# Sites by classification
site_classification = [
    html.H5('Site by classification'),
    dcc.Graph(id='site_classifica', style={"height": "100%", "width": "100%"})
]

# Population by classificcation
site_classification_population = [
    html.H5('Site by classification'),
    dcc.Graph(id='site_classifica_pop', style={"height": "100%", "width": "100%"})
]

# Distribuion of IDPs at LGA level
idps_lga_level = [
    dcc.Graph(id='idps_lga', style={"height": "100%", "width": "100%"})
]

### Cards

# Percentage of men
percentage_men = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/men.png"),
    html.P("Men", className="card-title", style={'font-size': 18}),
    html.Div(id="card_men", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# Percentage of men
percentage_women = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/women.png"),
    html.P("Women", className="card-title", style={'font-size': 18}),
    html.Div(id="card_women", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# Percentage of women and children
percentage_women_children = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/women_children.png"),
    html.P("Women & Children", className="card-title", style={'font-size': 18}),
    html.Div(id="card_women_children", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# Percentage of boys
percentage_boys = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/boys.png"),
    html.P("Boys", className="card-title", style={'font-size': 18}),
    html.Div(id="card_boys", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# Percentage of girls
percentage_girls = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/girls.png"),
    html.P("Girls", className="card-title", style={'font-size': 18}),
    html.Div(id="card_girls", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# Percentage of children
percentage_children = [
    html.Img(src="https://yajitersoo.github.io/jsonapi/children.png"),
    html.P("Children", className="card-title", style={'font-size': 18}),
    html.Div(id="card_children", style={"text-align": "center", "font-size": 20, "font-weight": "bold"}),
]

# In camps/camp-like settings
card_content_1 = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/idps1.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(["{:,}".format(int(np.sum(df['Number of Individuals'])))],
                                     className="card-title text-wrap", style={"text-align": "left",
                                                                              'font-family': 'Calibri Bold',
                                                                              'font-size': '18px',
                                                                              'color': 'black',
                                                                              "font-weight": "bold",

                                                                              })),
                    html.P("Confirmed cases of covid-19",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]
# Percentage of IDPs previously displaced
idps_prev_displaced = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/idps1.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(id="idps_prev_disp", className="card-title text-wrap", style={"text-align": "left",
                                                                                                   'font-family': 'Calibri Bold',
                                                                                                   'font-size': '18px',
                                                                                                   'color': 'black',
                                                                                                   "font-weight": "bold",

                                                                                                   })),
                    html.P("of IDPs have been previously displaced",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs cited traupalin as the most needed shelter material
idps_cited_trap = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/traupalin.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(id="idps_cited_traupalin", className="card-title text-wrap",
                                     style={"text-align": "left",
                                            'font-family': 'Calibri Bold',
                                            'font-size': '18px',
                                            'color': 'black',
                                            "font-weight": "bold",

                                            })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs complained of not having potable water
idps_portable_water = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/portable_water.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(
                        html.H5(id="idps_port_water", className="card-title text-wrap", style={"text-align": "left",
                                                                                               'font-family': 'Calibri Bold',
                                                                                               'font-size': '18px',
                                                                                               'color': 'black',
                                                                                               "font-weight": "bold",

                                                                                               })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs cited blanket/mat as the most needed NFI
idps_blanket_mat_needed_nfi = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/blanket_mat.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(id="idps_blanket_needed_nfi", className="card-title text-wrap",
                                     style={"text-align": "left",
                                            'font-family': 'Calibri Bold',
                                            'font-size': '18px',
                                            'color': 'black',
                                            "font-weight": "bold",

                                            })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of education facilities are located off-sites.
education_facilities = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/education.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(
                        html.H5(id="education_facility", className="card-title text-wrap", style={"text-align": "left",
                                                                                                  'font-family': 'Calibri Bold',
                                                                                                  'font-size': '18px',
                                                                                                  'color': 'black',
                                                                                                  "font-weight": "bold",

                                                                                                  })),
                    html.P("of education facilities are located off-sites.",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs cited malaria as the most common health problem.
idps_cited_mat_malaria = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/malaria.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(id="idps_cited_mal", className="card-title text-wrap", style={"text-align": "left",
                                                                                                   'font-family': 'Calibri Bold',
                                                                                                   'font-size': '18px',
                                                                                                   'color': 'black',
                                                                                                   "font-weight": "bold",

                                                                                                   })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs who do not have access to regular medication
idps_regular_medication = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/medicine.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(
                        html.H5(id="idps_regular_med", className="card-title text-wrap", style={"text-align": "left",
                                                                                                'font-family': 'Calibri Bold',
                                                                                                'font-size': '18px',
                                                                                                'color': 'black',
                                                                                                "font-weight": "bold",

                                                                                                })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

# Percentage of IDPs do not have access to food support.
idps_food_support = [
    dbc.Row([

        dbc.Col(
            dbc.CardImg(src="https://yajitersoo.github.io/jsonapi/food.png", className="img-fluid align-self-center",
                        #                            style = {'height':'48px', 'width':'26px'},
                        style={'hieght': '96px', 'width': '52px', 'margin-left': 'auto', 'margin-right': 'auto',
                               'padding-left': '15px',
                               'padding-top': '15px',
                               'padding-bottom': '15px',
                               'align': 'center'
                               },
                        ),
            className="col-md-2"),

        dbc.Col(
            dbc.CardBody(
                [

                    html.Div(html.H5(id="idps_food_sup", className="card-title text-wrap", style={"text-align": "left",
                                                                                                  'font-family': 'Calibri Bold',
                                                                                                  'font-size': '18px',
                                                                                                  'color': 'black',
                                                                                                  "font-weight": "bold",

                                                                                                  })),
                    html.P("of IDPs cited traupalin as the most needed shelter material",
                           className="card-text",
                           style={"text-align": "left", 'font-family': 'Calibri Light', 'font-size': '16px',
                                  'color': 'black'})
                ]
            )
            , className="col-md-10")

    ])

]

### Dashboard layout

app.layout = dbc.Container([

    ### Header _________________________________________________________________________________________________________________

    dbc.Row([
        dbc.Col(logo, width={'size': 2}),
        dbc.Col(title, width={'size': 8}),
    ], style={'padding-top': '5px', 'padding-bottom': '5px'},
        className="bg-info text-white h-50", align="center"),

    html.Br(),

    ### Dropdowns ______________________________________________________________________________________________________________
    dbc.Row([
        # State filter
        dbc.Col([
            state_dpdn
        ], width={'size': 3}, ),

        # LGA filter
        dbc.Col([
            lga_dpdn
        ], width={'size': 3}),
    ], justify="end"),

    ### Cards __________________________________________________________________________________________________________________
    dbc.Row([
        html.Div(html.H5('Demographic composition:')),
        html.Hr(),
        dbc.Col(percentage_men, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
        dbc.Col(percentage_women, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
        dbc.Col(percentage_women_children, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
        dbc.Col(percentage_boys, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
        dbc.Col(percentage_girls, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
        dbc.Col(percentage_children, style={'padding-top': '15px', "text-align": "center", }, width={'size': 2}),
    ], justify='center'),

    html.Hr(),

    ### Pie charts _____________________________________________________________________________________________________________
    dbc.Row([
        dbc.Col(site_num_status, width={'size': 3}),
        dbc.Col(population_site_status, width={'size': 3}),
        dbc.Col(site_classification, width={'size': 3}),
        dbc.Col(site_classification_population, width={'size': 3}),

    ], ),

    html.Br(),

    dbc.Row([
        dbc.Col([

            dbc.Card(idps_prev_displaced, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_cited_trap, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_portable_water, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_blanket_mat_needed_nfi, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(education_facilities, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_cited_mat_malaria, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_regular_medication, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),
            dbc.Card(idps_food_support, color='#e3e9f5', inverse=True, style={"margin-bottom": "15px"}),

        ], width={'size': 4}, className='p-3 bg-light '),

        dbc.Col(
            idps_lga_level,
            width={'size': 8}, className='p-3 bg-light'),

    ], className='row gx-5'),

    html.Hr(),

    dbc.Row([
        dbc.Col([
            dbc.Button(
                "Click to view data source",
                id="link-centered",
                color="link",
                href='https://data.humdata.org/dataset/nigeria-site-assessment-data',
                target="_blank"
            )
        ]),
    ]),
    html.Br(),

], style={'padding-top': '15px'})


### Dashboard callbacks

#### Filters

### Filters
@app.callback(
    Output('select_lga', 'options'),
    Input('select_state', 'value')
)
def set_lga_options(selected_state):
    if (selected_state == 'All'):
        dff = df
        available_lga = list(dff['LGA'].unique())
        available_lga = [{'label': i, 'value': i} for i in np.append(['All'], available_lga)]
    elif selected_state == None:
        #         available_lga= "All"
        available_lga = list(dff['LGA'].unique())
        available_lga = [{'label': i, 'value': i} for i in np.append(['All'], available_lga)]
    else:
        dff = df.loc[(df['State'] == selected_state)]

        available_lga = list(dff['LGA'].unique())
        available_lga = [item for item in available_lga if not (pd.isnull(item)) == True]

    return (available_lga)


#### charts

@app.callback(
    Output('card_men', 'children'),
    Output('card_women', 'children'),
    Output('card_women_children', 'children'),
    Output('card_boys', 'children'),
    Output('card_girls', 'children'),
    Output('card_children', 'children'),
    Output('site_number_by_status', 'figure'),
    Output('site_classifica', 'figure'),
    Output('pop_site_status', 'figure'),
    Output('site_classifica_pop', 'figure'),
    Output('idps_prev_disp', 'children'),
    Output('idps_cited_traupalin', 'children'),
    Output('idps_port_water', 'children'),
    Output('idps_blanket_needed_nfi', 'children'),
    Output('education_facility', 'children'),
    Output('idps_cited_mal', 'children'),
    Output('idps_regular_med', 'children'),
    Output('idps_food_sup', 'children'),
    Output('idps_lga', 'figure'),
    Input("select_state", 'value'),
    Input("select_lga", 'value'),
)
def update_output(selected_state, selected_lga):
    if (selected_state == 'All') & (selected_lga == 'All'):
        dff = df
    elif (selected_state == None) & (selected_lga == None):
        dff = df
    elif (selected_state == None) & (selected_lga == 'All'):
        dff = df
    elif (selected_state == 'All') & (selected_lga == None):
        dff = df
    elif (selected_state == None):
        dff = df.loc[
            (df['LGA'] == selected_lga)
        ]

    elif (selected_lga == None):
        dff = df.loc[
            (df['State'] == selected_state)
        ]
    elif (selected_state == 'All'):
        dff = df.loc[
            (df['LGA'] == selected_lga)
        ]

    elif (selected_lga == 'All'):
        dff = df.loc[
            (df['State'] == selected_state)
        ]

    else:
        dff = df.loc[(df['State'] == selected_state) & (df['LGA'] == selected_lga)]

    # Cards --------------------------------------------------------------------------------------------------------------------------

    # Percentage of men
    percentage_men = (
                (dff['Men (18 - 59 y)'].sum() + dff['(Elderly men 60+ y)'].sum()) / dff['Number of Individuals'].sum())
    percentage_men = "{:.0%}".format(percentage_men)

    # Percentage of women
    percentage_women = ((dff['Women (18 - 59 y)'].sum() + dff['(Elderly women 60+ y)'].sum()) / dff[
        'Number of Individuals'].sum())
    percentage_women = "{:.0%}".format(percentage_women)

    # Percentage of women and children
    percentage_women_children = ((
                                         dff['Boys (<1)'].sum() +
                                         dff['Girls (<1)'].sum() +
                                         dff['Boys (1 - 5 y)'].sum() +
                                         dff['Girls (1 - 5 y)'].sum() +
                                         dff['Boys 6to12y'].sum() +
                                         dff['Girls 6to12y'].sum() +
                                         dff['Boys 13to17y'].sum() +
                                         dff['Girls 13to17y'].sum() +
                                         dff['Women (18 - 59 y)'].sum() +
                                         dff['(Elderly women 60+ y)'].sum()) /
                                 dff['Number of Individuals'].sum())
    percentage_women_children = "{:.0%}".format(percentage_women_children)

    # Percentage of boys
    percentage_boys = ((dff['Boys (<1)'].sum() + dff['Boys (1 - 5 y)'].sum() + dff['Boys 6to12y'].sum() +
                        dff['Boys 13to17y'].sum()) /
                       dff['Number of Individuals'].sum())
    percentage_boys = "{:.0%}".format(percentage_boys)

    # Percentage of girls
    percentage_girls = ((
                                dff['Girls (<1)'].sum() +
                                dff['Girls (1 - 5 y)'].sum() +
                                dff['Girls 6to12y'].sum() +
                                dff['Girls 13to17y'].sum()) /
                        dff['Number of Individuals'].sum())
    percentage_girls = "{:.0%}".format(percentage_girls)

    # Percentage of girls
    percentage_children = ((
                                   dff['Boys (<1)'].sum() +
                                   dff['Girls (<1)'].sum() +
                                   dff['Boys (1 - 5 y)'].sum() +
                                   dff['Girls (1 - 5 y)'].sum()) /
                           dff['Number of Individuals'].sum())
    percentage_children = "{:.0%}".format(percentage_children)

    # Pie Charts-----------------------------------------------------------------------------------------------------------------
    colors = ['#7fc5eb', '#b3c8e0']

    # site number by status
    fig_1 = px.pie(
        (dff.groupby(['Site Status'])
         .size()
         .reset_index()
         .set_index(['Site Status'])
         .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0).reset_index()
         ).rename({0: 'Percent'}, axis=1),

        values='Percent',
        names='Site Status',
        color_discrete_sequence=colors,

        hover_data=[],
        height=200,
        width=200,

    )
    fig_1.update_layout(

        margin=dict(l=0, r=0, t=0, b=0), showlegend=False
    )
    fig_1.update_traces(
        textposition='outside', textinfo='percent+label', textfont_size=12, hole=0.7,
        marker=dict(line=dict(color='white', width=1))
    )

    # Site number by classification
    fig_2 = px.pie(
        (dff.groupby(['Site Classification'])
         .size()
         .reset_index()
         .set_index(['Site Classification'])
         .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0).reset_index()
         ).rename({0: 'Percent'}, axis=1),

        values='Percent',
        names='Site Classification',
        color_discrete_sequence=colors,
        #              title=f"{df_baseline_.columns.tolist()[7]} : {select_region}",

        hover_data=[],
        height=200,
        width=200,

    )
    fig_2.update_layout(
        margin=dict(l=0, r=0, t=0, b=0), showlegend=False
    )

    fig_2.update_traces(
        textposition='outside', textinfo='percent+label', textfont_size=12, hole=0.7,
        marker=dict(line=dict(color='white', width=1))
    )

    # Population by site status
    fig_3 = px.pie(
        (dff.groupby(['Site Status'])['Number of Individuals']
         .sum()
         .reset_index()
         .set_index(['Site Status'])
         .apply(lambda x: (x * 100 / x.sum()), axis=0)
         .round(0)
         .reset_index()
         ).rename({'Number of Individuals': 'Percent'}, axis=1),

        values='Percent',
        names='Site Status',
        color_discrete_sequence=colors,

        hover_data=[],
        height=200,
        width=200,

    )
    fig_3.update_layout(
        margin=dict(l=0, r=0, t=0, b=0), showlegend=False
    )

    fig_3.update_traces(
        textposition='outside', textinfo='percent+label', textfont_size=12, hole=0.7,
        marker=dict(line=dict(color='white', width=1))
    )

    # Population by classification
    fig_4 = px.pie(
        (dff.groupby(['Site Classification'])['Number of Individuals']
         .sum()
         .reset_index()
         .set_index(['Site Classification'])
         .apply(lambda x: (x * 100 / x.sum()), axis=0)
         .round(0)
         .reset_index()
         ).rename({'Number of Individuals': 'Percent'}, axis=1),

        values='Percent',
        names='Site Classification',
        color_discrete_sequence=colors,
        #              title=f"{df_baseline_.columns.tolist()[7]} : {select_region}",

        hover_data=[],
        height=200,
        width=200,

    )
    fig_4.update_layout(
        margin=dict(l=0, r=0, t=0, b=0), showlegend=False
    )

    fig_4.update_traces(
        textposition='outside', textinfo='percent+label', textfont_size=12, hole=0.7,
        marker=dict(line=dict(color='white', width=1))
    )

    # Percentage of IDPs who have been previously displaced
    percentage_port_water_not = (
        ((dff.groupby(['Is drinking water potable'])
          .size()
          .reset_index()
          .set_index(['Is drinking water potable'])
          .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0).reset_index()).rename({0: 'Percent'}, axis=1))

    )
    percentage_port_water_not = (percentage_port_water_not.loc[
        percentage_port_water_not['Is drinking water potable'] == 'yes', 'Percent'].iloc[0]) / 100
    percentage_port_water_not = "{:.0%}".format(percentage_port_water_not)
    percentage_port_water_not

    # Percentage of idps cited traupalin as the most needed shelter material
    df_traupalin = ((dff.groupby(['Most needed NFI'])
                     .size()
                     .reset_index()
                     .set_index(['Most needed NFI'])
                     .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                     .reset_index()).rename({0: 'Percent'}, axis=1)
                    )
    df_traupalin = (df_traupalin.loc[(df_traupalin['Most needed NFI'] == 'Blankets/Mats') |
                                     (df_traupalin['Most needed NFI'] == 'mosquito nets') |
                                     (df_traupalin['Most needed NFI'] == 'solar lamps'),
                                     'Percent'].sum()) / 100
    df_traupalin = "{:.0%}".format(df_traupalin)

    # Percentage of IDPs complained of not having potable water
    percentage_port_water_not = (
        ((dff.groupby(['Is drinking water potable'])
          .size()
          .reset_index()
          .set_index(['Is drinking water potable'])
          .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0).reset_index()).rename({0: 'Percent'}, axis=1))

    )
    percentage_port_water_not = (percentage_port_water_not.loc[
        percentage_port_water_not['Is drinking water potable'] == 'no', 'Percent'].iloc[0]) / 100
    percentage_port_water_not
    percentage_port_water_not = "{:.0%}".format(percentage_port_water_not)
    percentage_port_water_not

    # Percentage of IDPs cited blanket/mat as the most needed NFI
    df_blanket = (dff.groupby(['Most needed NFI'])
                  .size()
                  .reset_index()
                  .set_index(['Most needed NFI'])
                  .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                  .reset_index()).rename({0: 'Percent'}, axis=1)
    # df_blanket
    df_blanket = (df_blanket.loc[(df_blanket['Most needed NFI'] == 'Blankets/Mats'),
                                 'Percent'].sum()) / 100
    df_blanket = "{:.0%}".format(df_blanket)

    # Percentage of education facilities are located off-sites
    df_edu_offsite = (dff.groupby(['Location of education facilities'])
                      .size()
                      .reset_index()
                      .set_index(['Location of education facilities'])
                      .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                      .reset_index()).rename({0: 'Percent'}, axis=1)
    # df_edu_offsite
    df_edu_offsite = (df_edu_offsite.loc[(df_edu_offsite['Location of education facilities'] == 'offsite'),
                                         'Percent'].sum()) / 100
    df_edu_offsite = "{:.0%}".format(df_edu_offsite)
    df_edu_offsite

    # Percentage of IDPs cited malaria as the most common health problem
    df_malaria = (dff.groupby(['Most health problem'])
                  .size()
                  .reset_index()
                  .set_index(['Most health problem'])
                  .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                  .reset_index()).rename({0: 'Percent'}, axis=1)
    # df_malaria
    df_malaria = (df_malaria.loc[(df_malaria['Most health problem'] == 'malaria'),
                                 'Percent'].sum()) / 100
    df_malaria = "{:.0%}".format(df_malaria)

    # Percentage of idps who do not have access to regular medication
    percentage_regular_med = (dff.groupby(['Regular access to medicine'])
                              .size()
                              .reset_index()
                              .set_index(['Regular access to medicine'])
                              .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                              .reset_index()).rename({0: 'Percent'}, axis=1)
    # percentage_regular_med
    percentage_regular_med = (percentage_regular_med.loc[(percentage_regular_med['Regular access to medicine'] == 'no'),
                                                         'Percent'].sum()) / 100
    percentage_regular_med = "{:.0%}".format(percentage_regular_med)
    percentage_regular_med

    # Percentage of idps do not have acess to food support
    df_access_food = (dff.groupby(['Access to food'])
                      .size()
                      .reset_index()
                      .set_index(['Access to food'])
                      .apply(lambda x: (x * 100 / x.sum()), axis=0).round(0)
                      .reset_index()).rename({0: 'Percent'}, axis=1)
    # df_access_food
    df_access_food = (df_access_food.loc[(df_access_food['Access to food'] == 'no'),
                                         'Percent'].sum()) / 100
    df_access_food = "{:.0%}".format(df_access_food)

    # Distribution of IDPs at LGA level
    lga_bar = dff.groupby('LGA')['Number of Individuals'].sum().reset_index()
    lga_bar = lga_bar.nlargest(20, 'Number of Individuals').sort_values(by=['Number of Individuals'])

    fig_5 = go.Figure()

    fig_5.add_trace(go.Bar(
        y=lga_bar['LGA'],
        x=lga_bar['Number of Individuals'],
        name='Counts',
        marker_color=colors[0],
        text=lga_bar['Number of Individuals'].apply(lambda x: '{0:1.0f}%'.format(x)),
        textposition='outside', )
    )

    fig_5.update_layout(
        xaxis_title="Region",
        yaxis_title="Count of Country",
        #         template='ggplot2',
        font=dict(
            size=12,
            color="Black",
            family="Calibri"),
        #         xaxis=dict(showgrid=False),
        #         yaxis=dict(showgrid=False),
        plot_bgcolor='white',
        title_text='<b>Number of IDPs at LGA Level</b>',
        title_font_family="Open Sans",
        title_font_size=22,
        title_font_color="#000000",
        margin_pad=10
    )

    fig_5.update_traces(orientation='h', marker_autocolorscale=False, opacity=1, width=0.6)

    fig_5.update_xaxes(visible=False, showticklabels=False, title=None)

    fig_5.update_yaxes(visible=True, showticklabels=True, title="",
                       tickfont=dict(family='Calibri', color='#606060', size=12),
                       tickangle=0,
                       zeroline=True,
                       )

    return (
        percentage_men,
        percentage_women,
        percentage_women_children,
        percentage_boys,
        percentage_girls,
        percentage_children,
        fig_1,
        fig_2,
        fig_3,
        fig_4,
        percentage_port_water_not,
        df_traupalin,
        percentage_port_water_not,
        df_blanket,
        df_edu_offsite,
        df_malaria,
        percentage_regular_med,
        df_access_food,
        fig_5,
    )


#### Run app

if __name__ == '__main__':
    app.run_server(debug=True)





