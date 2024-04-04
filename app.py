# import dependencies

import dash
from dash import Dash,dash_table, html, dcc 

import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output
import random
goodreads_df = pd.read_csv('data.csv')

app = Dash(__name__)

server = app.server
#all of the genres
genres = [
    'adult', 'art', 'audiobook', 'biography', 'business', 'childrens', 'classics', 'comics',
    'comedy', 'contemporary', 'culture', 'food_and_drink', 'comedy', 'crime', 'fantasy',
    'fiction', 'sexuality_and_gender', 'literature', 'graphic_Novels', 'historical', 'history',
    'horror', 'magna', 'memoir', 'music', 'mystery', 'nonfiction', 'paranormal', 'philosophy',
    'poetry', 'psychology', 'religion', 'romance', 'science', 'science_fiction', 'self_help',
    'suspense', 'spirituality', 'sports', 'thriller', 'travel', 'young_adult'
]

#i wanted to generate a random color palette for all of the genres. For now i will leave it as random, but later on it might be nice to select the colors for each genre by hand
color_palette = [px.colors.qualitative.Plotly[random.randint(0, len(px.colors.qualitative.Plotly) - 1)] for _ in range(len(genres))]

#map the genre to a color (they should all be somewhat different for now)
color_mapping = {genre: color_palette[i] for i, genre in enumerate(genres)}

#creastes a series whcih conects the name of the genre to the total number of books in that genre
genre_counts = goodreads_df.iloc[:, 9:].sum()

#define the car graph
fig = px.bar(
    x=genre_counts.index, #on the x you have the names of the genres
    y=genre_counts.values,#on the y you have the number of books in that genre
    labels={'x': 'Genre', 'y': 'Number of Books'}
)

#begin the layout of the app
app.layout = html.Div([
    #this is the nav bar. it is not implemented yet, but it was helpful to figure out the layout
   html.Nav(
        [
            html.Ul(
    [
        #nav components!
        html.Li(html.P("Goodreads Top 10,000 Dashboard", style={"padding": "10px 20px", "margin": "0", "background-color": "#666666",
                                   "border-radius": "5px", "list-style-type": "none","color": "white", "text-decoration": "none", "font-family": "Arial"})),
        html.Li(html.A("Personal Books", href="#", style={"color": "white", "text-decoration": "none", "font-family": "Arial"}),
                style={"padding": "5px 10px", "margin": "0", "background-color": "#666666",
                       "border-radius": "5px", "list-style-type": "none"}), 
        html.Li(html.A("Public Books", href="#", style={"color": "white", "text-decoration": "none", "font-family": "Arial"}),
                style={"padding": "5px 10px", "margin": "0", "background-color": "#666666",
                       "border-radius": "5px", "list-style-type": "none"}),  
        html.Li(html.A("About this Dashboard", href="#", style={"color": "white", "text-decoration": "none", "font-family": "Arial"}),
                style={"padding": "5px 10px", "margin": "0", "background-color": "#666666",
                       "border-radius": "5px", "list-style-type": "none"}), 
    ],
    className="nav",
    #i want to change this styling later I dont like the way things are spaced out rn
    style={"display": "flex", "justify-content": "space-between","padding": "5px", "margin": "0"} 
)
        ],
        #styling for the navbar
        
        style={"background-color": "lightgray",
               "padding": "5px",
               "width": "99%",
               "margin-right": "0px",
               "margin-left": "10px",
               "box-sizing": "border-box",
               "border-radius": "15px"
               }
    ),
    #holds teh columns
    html.Div(
        [
            #######################################################################
            ###########################COLUMN 1 NOT IMPLEMENTED####################
            #######################################################################
            html.Div(
                [html.Label("Col 1", style={"color": "black"})],
                #styling for the div container. creates that background affect
                style={
                    "background-color": "lightgray",
                    "width": "32.5%",
                    "display": "inline-block",
                    "padding": "5px",
                    "margin-left": "5px",
                    "margin-right": "10px",
                    "margin-bottom": "20px",
                    "min-width": "350px",
                    "height": "100vh",  
                    "box-sizing": "border-box", 
                    "border-radius": "15px" 
                },
            ),


            #######################################################################
            ###########################COLUMN 2 DROPDOWN GRAPH#####################
            #######################################################################
             html.Div(
                 [html.Div([
                     ##heading value basically titles the section
                    html.H3("Genre versus Quantity of Books", style={"text-align": "center","padding": "10px 20px", "margin": "0", "background-color": "#666666",
                                   "border-radius": "5px", "list-style-type": "none","color": "white", "text-decoration": "none", "font-family": "Arial"}),
                ],
                #i used seperate divs here so that i could adjust spacing between the differetnt
                #parts inside of the sectinos
                style={"margin-bottom": "20px"}
                 ),
                 #note for instruction
                 html.Div([
                    html.H5("Select genres using the dropdown to populate the graph.", style={"text-align": "center", "margin": "0",
                                    "list-style-type": "none","color": "black", "text-decoration": "none", "font-family": "Arial"}),
                ],

                style={"margin-bottom": "20px"}
                 ),
        html.Div(
            #first element
            ######################### DROPDOWN ##########################
            [dcc.Dropdown(
                id='genre-dropdown',
                options=[{'label': genre.capitalize().replace('_', ' '), 'value': genre} for genre in genres],#basically just gets all of the genres in genres list i made above
                value=[],
                multi=True,#select multiple
                persistence=True,
                style={'width': '100%',
                       }
            )],
            style={'width': '100%', 'margin': 'auto', 'margin-bottom': '20px','maxHeight': '300px',  } 
                
        ),
        ######################### GRAPH ##########################
        dcc.Graph(
        id='genre-graph',
        figure=fig #defined above
    ), 
    ],
    style={
        "background-color": "lightgray",
        "width": "32.5%",
        "display": "inline-block",
        "border-right": "2px solid #333",
        "padding": "10px",
        "margin-left": "5px",
        "margin-right": "10px",
        "margin-bottom": "20px",
        "min-width": "350px",
        "height": "100vh",  
        "box-sizing": "border-box",
          "border-radius": "15px"  
    },
),
###############################################################################
#################################Author Table##################################
###############################################################################
          html.Div(
                 [html.Div([
                     #title for section
                    html.H3("Find an Author's Top Books", style={"text-align": "center","padding": "10px 20px", "margin": "0", "background-color": "#666666",
                                   "border-radius": "5px", "list-style-type": "none","color": "white", "text-decoration": "none", "font-family": "Arial"}),
                ],

                style={"margin-bottom": "20px"}
                 ),
                 html.Div([
                     #explination of use
                    html.H5("Select an author from the drop down or use the search functionality to find an author and populate the table below with their top books.", style={"text-align": "center", "margin": "0",
                                    "list-style-type": "none","color": "black", "text-decoration": "none", "font-family": "Arial",'fontWeight': 'bold'}),
                ],

                style={"margin-bottom": "20px"}
                 ),
        html.Div(
            [
                
            html.Div([
                ######################### DROPDOWN ##########################
             dcc.Dropdown(
                id='author-dropdown',
                options=[{'label': author, 'value': author} for author in goodreads_df['author'].unique()], #gets all unique authors from the df
                multi=False,  #only want to select one 
                placeholder='Select author'
            ),
            ],
             style={'margin-bottom': '20px'}
            ),
            ######################### DATA TABLE ##########################
            dash_table.DataTable(
                id='author-books-table',
                columns=[#these are the columns that are going to be present in the datatable. they connect to the df
                    {"name": "Title", "id": "title"},
                    {"name": "Average Rating", "id": "average_rating"},
                    {"name": "Ratings Count", "id": "ratings_count"}
                ],
                sort_action="native", #settings used in class
                page_size=10,
                #adding styling because of overflow problems
                style_table={"overflowX": "auto"}, 
                style_cell={ 
                    'overflow': 'hidden',
                    'textOverflow': 'ellipsis',
                    'maxWidth': 250,  
                }
            ),
            #this is the container for the text that changes based off the selected author! most of the implementation is in the function below
            html.Div(
                id='author-output-text',
                #had to adjust styling of the font so that it sort of matched the header explinations above
                style={'margin-top': '20px',"text-align": "center",
                                    "list-style-type": "none","color": "black", "font-family": "Arial" ,'fontWeight': 'bold','fontSize': '0.85em'}
            )
      ],
            style={'width': '100%', 'margin': 'auto', 'margin-bottom': '20px','maxHeight': '300px'}   
        ),
    ],
    style={
        #style for the section
        "background-color": "lightgray",
        "width": "32.5%",
        "display": "inline-block",
        "border-right": "2px solid #333",
        "padding": "10px",
        "margin-left": "5px",
        "margin-right": "10px",
        "margin-bottom": "20px",
        "min-width": "350px",
        "height": "100vh", 
        "box-sizing": "border-box",
          "border-radius": "15px"  
    },
),
        ],
        style={"margin": "10px auto", "max-width": "4000px", "width": "100%","text-align": "center","display": "flex"}  # Set width to 100% of parent container
    ),
],
style={"background-color": "#444444", "padding": "15px"}
)
###################################################################
########################CALLBACKS AND FUNCTIONS####################
###################################################################

############## GENRE GRAPH CALLBACK AND UPDATE FUNCTION ###########
@app.callback(
    Output('genre-graph', 'figure'), #updates the genre graph usign its id. the output if figure
    [Input('genre-dropdown', 'value')] #takes input from the genre dropdown . basically gets all the selected genres
)
def update_genre_graph(selected_genres):
    if not selected_genres: #if no genre is selected return an empty graph
        #settings for an empty graph (found cool settings to make the background clear)
        return {
            'data': [],
            'layout': {
                'title': 'Number of Books in Selected Genres',
                'xaxis': {'title': 'Genre'},
                'yaxis': {'title': 'Number of Books'},
                'showlegend': False, #legend looks UGLY
                'paper_bgcolor': 'rgba(255, 255, 255, 0)', 
                'plot_bgcolor': 'rgba(255, 255, 255, 0)',  
                'xaxis_showgrid': False,                   
                'yaxis_showgrid': False,                    
            }
        }

    data = [] #initialize data
    for genre in selected_genres: #go through all of the selected genres
        trace = {#begin a bar trace for the selected genre
            'x': [genre],#as stated before x is genre
            'y': [genre_counts[genre]],#y is the number of books for that genre
            'type': 'bar',
            'marker': {'color': color_mapping[genre]},  #the color is  based on the mapping
            'text': [genre_counts[genre]], #want to see values on the graph             
            'textposition': 'auto',  #make it look nice                   
        }
        data.append(trace) #add to data
    
    return { #now we are returning the data for the graph based on user input
        'data': data, #created abv
        'layout': { 
            'xaxis': {'title': 'Genre'}, #x axis tittle
            'yaxis': {'title': 'Number of Books'}, #ect ect used same as abv to figure out how to do clear background
            'showlegend': False,
            'paper_bgcolor': 'rgba(255, 255, 255, 0)',  
            'plot_bgcolor': 'rgba(255, 255, 255, 0)',   
            'xaxis_showgrid': False,                    
            'yaxis_showgrid': False,                  
        }
    }


############## AUTHOR BOOKS TABLE CALLBACK AND UPDATE FUNCTION ###########

@app.callback(
    Output('author-books-table', "data"), #gonna output the table data
    [Input('author-dropdown', "value")] #based on the input of the author name
)
def update_author_books_table(selected_author):
    #if not author selected dont need to update
    if not selected_author:
        return dash.no_update
    #otherwise author is selected, so get the corresponding data from the goodreads df with the appropriate columns
    author_books = goodreads_df[goodreads_df['author'] == selected_author][['title', 'average_rating', 'ratings_count']]
    #retuns in dict format
    return author_books.to_dict("records")

############## AUTHOR POPULAR BOOK TEXT CALLBACK AND UPDATE FUNCTION ######
@app.callback(
    Output('author-output-text', 'children'), #outputs text indicating most popular book
    [Input('author-dropdown', 'value')] #based on the selected author
)
def update_author_output(selected_author):
    #if an author is selected,
    if selected_author:
        #get the books written by the author
        author_books = goodreads_df[goodreads_df['author'] == selected_author]
        #i think the most popular book should be based on the maximum of rating times number of reviews
        #this is just what comes to mind i might want to change the way i determine this later
        most_popular_book = author_books.loc[(author_books['average_rating'] * author_books['ratings_count']).idxmax()] #find the max as said abv 
        #prints out the statement
        return f"{selected_author}'s most popular book is '{most_popular_book['title']}' with an average rating of {most_popular_book['average_rating']} and {most_popular_book['ratings_count']} reviews."
    else:
        #if there is not selected author, then there is no text that needs to be outputed
        return ""

#run app
if __name__ == "__main__":
    app.run(jupyter_mode = 'tab', debug=False)
