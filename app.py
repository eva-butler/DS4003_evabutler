# import dependencies

import dash
from dash import Dash, dash_table, html, dcc

import pandas as pd
import plotly.express as px
from dash.dependencies import Input, Output, State
import random

goodreads_df = pd.read_csv("data.csv")

app = Dash(__name__)

server = app.server
# all of the genres
genres = [
    "adult",
    "art",
    "audiobook",
    "biography",
    "business",
    "childrens",
    "classics",
    "comics",
    "comedy",
    "contemporary",
    "culture",
    "food_and_drink",
    "comedy",
    "crime",
    "fantasy",
    "fiction",
    "sexuality_and_gender",
    "literature",
    "graphic_Novels",
    "historical",
    "history",
    "horror",
    "magna",
    "memoir",
    "music",
    "mystery",
    "nonfiction",
    "paranormal",
    "philosophy",
    "poetry",
    "psychology",
    "religion",
    "romance",
    "science",
    "science_fiction",
    "self_help",
    "suspense",
    "spirituality",
    "sports",
    "thriller",
    "travel",
    "young_adult",
]

# i wanted to generate a random color palette for all of the genres. For now i will leave it as random, but later on it might be nice to select the colors for each genre by hand
# color_palette = [px.colors.qualitative.Plotly[random.randint(0, len(px.colors.qualitative.Plotly) - 1)] for _ in range(len(genres))]
color_palette = [
    "#1f77b4",
    "#ff7f0e",
    "#2ca02c",
    "#d62728",
    "#9467bd",
    "#8c564b",
    "#e377c2",
    "#7f7f7f",
    "#bcbd22",
    "#17becf",
    "#9edae5",
    "#393b79",
    "#5254a3",
    "#6b6ecf",
    "#9c9ede",
    "#637939",
    "#8ca252",
    "#b5cf6b",
    "#cedb9c",
    "#e7cb94",
    "#e7ba52",
    "#bd9e39",
    "#8c6d31",
    "#bd3939",
    "#ad494a",
    "#843c39",
    "#ad494a",
    "#d6616b",
    "#e7969c",
    "#7b4173",
    "#a55194",
    "#ce6dbd",
    "#de9ed6",
    "#3182bd",
    "#6baed6",
    "#9ecae1",
    "#c6dbef",
    "#e6550d",
    "#fd8d3c",
    "#fdae6b",
    "#fdd0a2",
    "#31a354",
    "#74c476",
    "#a1d99b",
    "#c7e9c0",
    "#756bb1",
]


# map the genre to a color (they should all be somewhat different for now)
color_mapping = {genre: color_palette[i] for i, genre in enumerate(genres)}

# creastes a series whcih conects the name of the genre to the total number of books in that genre
genre_counts = goodreads_df.iloc[:, 9:].sum()

# define the car graph
fig = px.bar(
    x=genre_counts.index,  # on the x you have the names of the genres
    y=genre_counts.values,  # on the y you have the number of books in that genre
    labels={"x": "Genre", "y": "Number of Books"},
)

# begin the layout of the app
app.layout = html.Div(
    [
        # this is the nav bar. it is not implemented yet, but it was helpful to figure out the layout
        html.Nav(
            [
                html.Ul(
                    [
                        # nav components! - i ended up not making multiple pages because i would have had to test using render
                        html.Li(
                            html.P(
                                "Goodreads 10,000 Dashboard",
                                style={
                                    "padding": "10px 20px",
                                    "margin": "0",
                                    "background-color": "#666666",
                                    "border-radius": "5px",
                                    "list-style-type": "none",
                                    "color": "white",
                                    "text-decoration": "none",
                                    "font-family": "Arial",
                                },
                            )
                        ),
                        html.Li(
                            html.A(
                                "Github",
                                href="https://github.com/eva-butler/DS4003_evabutler",
                                style={
                                    "color": "white",
                                    "text-decoration": "none",
                                    "font-family": "Arial",
                                },
                            ),
                            style={
                                "padding": "5px 10px",
                                "margin": "0",
                                "background-color": "#666666",
                                "border-radius": "5px",
                                "list-style-type": "none",
                            },
                        ),
                    ],
                    className="nav",
                    # i want to change this styling later I dont like the way things are spaced out rn
                    style={
                        "display": "flex",
                        "justify-content": "space-between",
                        "padding": "5px",
                        "margin": "0",
                    },
                )
            ],
            # styling for the navbar
            style={
                "background-color": "lightgray",
                "padding": "5px",
                "width": "99%",
                "margin-right": "0px",
                "margin-left": "10px",
                "box-sizing": "border-box",
                "border-radius": "15px",
            },
        ),
        # holds teh columns
        html.Div(
            [
                #######################################################################
                ###########################COLUMN 1 BOOK INFORMATION###################
                #######################################################################
                html.Div(
                    [
                        html.Div(
                            [
                                ##heading value basically titles the section
                                html.H3(
                                    "Book Information",
                                    style={
                                        "text-align": "center",
                                        "padding": "10px 20px",
                                        "margin": "0",
                                        "background-color": "#666666",
                                        "border-radius": "5px",
                                        "list-style-type": "none",
                                        "color": "white",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            # i used seperate divs here so that i could adjust spacing between the differetnt
                            # parts inside of the sectinos
                            style={"margin-bottom": "20px"},
                        ),
                        # note for instruction
                        html.Div(
                            [
                                html.H5(
                                    "Search for and select a book title to see book information",
                                    style={
                                        "text-align": "center",
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                                # the dropdown works as a search function as well.
                                dcc.Dropdown(
                                    id="book-dropdown",
                                    options=[
                                        {"label": title, "value": title}
                                        for title in goodreads_df["title"]
                                    ],
                                    value="The Control of Nature",  # just have it automatically set to The Control of Nature so that a cover loads.
                                    placeholder="Select a book title",
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        html.Div(
                            [
                                # this is the place holder for the book cover. i connected the OpenLibrary API so that I could use it
                                html.Img(
                                    id="book-cover",  # id to connect to
                                    style={  # very similar styling as before. this allows be to make sure the image size is the same everytimer it is called
                                        "margin-top": "20px",
                                        "display": "block",
                                        "margin-left": "auto",
                                        "margin-right": "auto",
                                        "width": "300px",
                                        "height": "400px",
                                        "border": "2px solid #333",
                                        "border-radius": "5px",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        # THE FOLLOWING INFORMATION CHANGES AS THE USER SELECTS A DIFFERENT TITLE.
                        # Author information
                        html.Div(
                            [
                                # Author text
                                html.H5(
                                    "Author:",
                                    style={
                                        # same styling as instruction text
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                                html.P(
                                    id="author",
                                    style={
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        # Number of pages information
                        html.Div(
                            [
                                html.H5(
                                    "Number of Pages:",
                                    style={
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                                html.P(
                                    id="num-pages",
                                    style={
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        # Genres information
                        html.Div(
                            [
                                html.H5(
                                    "Genres:",
                                    style={
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                                html.P(
                                    id="genres",
                                    style={
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        # I added this button to update the authors books table. So if you want to see other books by the authtor you can select the button and it would update the table on the right
                        html.Div(
                            [
                                html.Button(
                                    "See Other Books by this Author",
                                    id="author-books-button",
                                    n_clicks=0,
                                )
                            ]
                        ),
                    ],
                    # styling for the div container. creates that background affect
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
                        "border-radius": "15px",
                    },
                ),
                #######################################################################
                ###########################COLUMN 2 DROPDOWN GRAPH#####################
                #######################################################################
                html.Div(
                    [
                        html.Div(
                            [
                                ##heading value basically titles the section
                                html.H3(
                                    "Genre versus Quantity of Books",
                                    style={
                                        "text-align": "center",
                                        "padding": "10px 20px",
                                        "margin": "0",
                                        "background-color": "#666666",
                                        "border-radius": "5px",
                                        "list-style-type": "none",
                                        "color": "white",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            # i used seperate divs here so that i could adjust spacing between the differetnt
                            # parts inside of the sectinos
                            style={"margin-bottom": "20px"},
                        ),
                        # note for instruction
                        html.Div(
                            [
                                html.H5(
                                    "Select genres using the dropdown to populate the graph.",
                                    style={
                                        "text-align": "center",
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        html.Div(
                            # first element
                            ######################### DROPDOWN ##########################
                            [
                                dcc.Dropdown(
                                    id="genre-dropdown",
                                    options=[
                                        {
                                            "label": genre.capitalize().replace(
                                                "_", " "
                                            ),
                                            "value": genre,
                                        }
                                        for genre in genres
                                    ],  # basically just gets all of the genres in genres list i made above
                                    value=[],
                                    multi=True,  # select multiple
                                    persistence=True,
                                    style={"width": "100%"},
                                )
                            ],
                            style={
                                "width": "100%",
                                "margin": "auto",
                                "margin-bottom": "20px",
                                "maxHeight": "300px",
                            },
                        ),
                        ######################### GRAPH ##########################
                        dcc.Graph(id="genre-graph", figure=fig),  # defined above
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
                        "border-radius": "15px",
                    },
                ),
                ###############################################################################
                #################################Author Table##################################
                ###############################################################################
                html.Div(
                    [
                        html.Div(
                            [
                                # title for section
                                html.H3(
                                    "Find an Author's Top Books",
                                    style={
                                        "text-align": "center",
                                        "padding": "10px 20px",
                                        "margin": "0",
                                        "background-color": "#666666",
                                        "border-radius": "5px",
                                        "list-style-type": "none",
                                        "color": "white",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        html.Div(
                            [
                                # explination of use
                                html.H5(
                                    "Select an author from the drop down or use the search functionality to find an author and populate the table below with their top books.",
                                    style={
                                        "text-align": "center",
                                        "margin": "0",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "text-decoration": "none",
                                        "font-family": "Arial",
                                        "fontWeight": "bold",
                                    },
                                ),
                            ],
                            style={"margin-bottom": "20px"},
                        ),
                        html.Div(
                            [
                                html.Div(
                                    [
                                        ######################### DROPDOWN ##########################
                                        # allows you to select or search for an author based on those in the dataframe
                                        dcc.Dropdown(
                                            id="author-dropdown",
                                            options=[
                                                {"label": author, "value": author}
                                                for author in goodreads_df[
                                                    "author"
                                                ].unique()
                                            ],  # gets all unique authors from the df
                                            multi=False,  # only want to select one
                                            placeholder="Select author",
                                        ),
                                    ],
                                    style={"margin-bottom": "20px"},
                                ),
                                ######################### DATA TABLE ##########################
                                dash_table.DataTable(
                                    id="author-books-table",
                                    columns=[  # these are the columns that are going to be present in the datatable. they connect to the df
                                        {"name": "Title", "id": "title"},
                                        {
                                            "name": "Average Rating",
                                            "id": "average_rating",
                                        },
                                        {
                                            "name": "Ratings Count",
                                            "id": "ratings_count",
                                        },
                                    ],
                                    sort_action="native",  # settings used in class
                                    page_size=10,
                                    # adding styling because of overflow problems
                                    style_table={"overflowX": "auto"},
                                    style_cell={
                                        "overflow": "hidden",
                                        "textOverflow": "ellipsis",
                                        "maxWidth": 250,
                                    },
                                ),
                                # this is the container for the text that changes based off the selected author! most of the implementation is in the function below
                                html.Div(
                                    id="author-output-text",
                                    # had to adjust styling of the font so that it sort of matched the header explinations above
                                    style={
                                        "margin-top": "20px",
                                        "text-align": "center",
                                        "list-style-type": "none",
                                        "color": "black",
                                        "font-family": "Arial",
                                        "fontWeight": "bold",
                                        "fontSize": "0.85em",
                                    },
                                ),
                            ],
                            style={
                                "width": "100%",
                                "margin": "auto",
                                "margin-bottom": "20px",
                                "maxHeight": "300px",
                            },
                        ),
                    ],
                    style={
                        # style for the section
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
                        "border-radius": "15px",
                    },
                ),
            ],
            style={
                "margin": "10px auto",
                "max-width": "4000px",
                "width": "100%",
                "text-align": "center",
                "display": "flex",
            },  # Set width to 100% of parent container
        ),
    ],
    style={"background-color": "#444444", "padding": "15px"},
)
###################################################################
########################CALLBACKS AND FUNCTIONS####################
###################################################################


############## GENRE GRAPH CALLBACK AND UPDATE FUNCTION ###########
@app.callback(
    Output(
        "genre-graph", "figure"
    ),  # updates the genre graph usign its id. the output if figure
    [
        Input("genre-dropdown", "value")
    ],  # takes input from the genre dropdown . basically gets all the selected genres
)
def update_genre_graph(selected_genres):
    if not selected_genres:  # if no genre is selected return an empty graph
        # settings for an empty graph (found cool settings to make the background clear)
        return {
            "data": [],
            "layout": {
                "title": "Number of Books in Selected Genres",
                "xaxis": {"title": "Genre"},
                "yaxis": {"title": "Number of Books"},
                "showlegend": False,  # legend looks UGLY
                "paper_bgcolor": "rgba(255, 255, 255, 0)",
                "plot_bgcolor": "rgba(255, 255, 255, 0)",
                "xaxis_showgrid": False,
                "yaxis_showgrid": False,
            },
        }

    data = []  # initialize data
    for genre in selected_genres:  # go through all of the selected genres
        trace = {  # begin a bar trace for the selected genre
            "x": [genre],  # as stated before x is genre
            "y": [genre_counts[genre]],  # y is the number of books for that genre
            "type": "bar",
            "marker": {
                "color": color_mapping[genre]
            },  # the color is  based on the mapping
            "text": [genre_counts[genre]],  # want to see values on the graph
            "textposition": "auto",  # make it look nice
        }
        data.append(trace)  # add to data

    return {  # now we are returning the data for the graph based on user input
        "data": data,  # created abv
        "layout": {
            "xaxis": {"title": "Genre"},  # x axis tittle
            "yaxis": {
                "title": "Number of Books"
            },  # ect ect used same as abv to figure out how to do clear background
            "showlegend": False,
            "paper_bgcolor": "rgba(255, 255, 255, 0)",
            "plot_bgcolor": "rgba(255, 255, 255, 0)",
            "xaxis_showgrid": False,
            "yaxis_showgrid": False,
        },
    }


############## AUTHOR BOOKS TABLE CALLBACK AND UPDATE FUNCTION ###########


@app.callback(
    Output("author-books-table", "data"),  # gonna output the table data
    [Input("author-dropdown", "value")],  # based on the input of the author name
)
def update_author_books_table(selected_author):
    # if not author selected dont need to update
    if not selected_author:
        return dash.no_update
    # otherwise author is selected, so get the corresponding data from the goodreads df with the appropriate columns
    author_books = goodreads_df[goodreads_df["author"] == selected_author][
        ["title", "average_rating", "ratings_count"]
    ]
    # retuns in dict format
    return author_books.to_dict("records")


############## AUTHOR POPULAR BOOK TEXT CALLBACK AND UPDATE FUNCTION ######
@app.callback(
    Output(
        "author-output-text", "children"
    ),  # outputs text indicating most popular book
    [Input("author-dropdown", "value")],  # based on the selected author
)
def update_author_output(selected_author):
    # if an author is selected,
    if selected_author:
        # get the books written by the author
        author_books = goodreads_df[goodreads_df["author"] == selected_author]
        # i think the most popular book should be based on the maximum of rating times number of reviews
        # this is just what comes to mind i might want to change the way i determine this later
        most_popular_book = author_books.loc[
            (author_books["average_rating"] * author_books["ratings_count"]).idxmax()
        ]  # find the max as said abv
        # prints out the statement
        return f"{selected_author}'s most popular book is '{most_popular_book['title']}' with an average rating of {most_popular_book['average_rating']} and {most_popular_book['ratings_count']} reviews."
    else:
        # if there is not selected author, then there is no text that needs to be outputed
        return ""


@app.callback(
    Output("book-cover", "src"),  # outputs the book cover image
    [Input("book-dropdown", "value")],  # based on the dropdown value
)
def update_book_cover(selected_title):
    if selected_title:
        # retrieve the corresponding ISBN from the DataFrame
        isbn = goodreads_df.loc[goodreads_df["title"] == selected_title, "isbn"].iloc[0]
        # insert the url into the link
        cover_url = f"https://covers.openlibrary.org/b/isbn/{isbn}-L.jpg"
        return cover_url  # return the url
    else:
        return ""  # otw nothing was found


@app.callback(
    Output("author", "children"),  # outputs the author name
    Input("book-dropdown", "value"),  # based on the dropdown value
)
def update_author_info(title):
    if title is None:
        return ""
    else:
        # based on the selected title, get the row in the dataframe
        book_info = goodreads_df[goodreads_df["title"] == title].iloc[0]
        # then get the authors name based on the row
        author = book_info["author"]
        return author


# callback function for updating the number of pages information
@app.callback(
    Output("num-pages", "children"),  # outputs the number of pages
    Input("book-dropdown", "value"),  # based on the dropdown value
)
def update_num_pages_info(title):
    if title is None:
        return ""
    else:
        # based on the selected title, get the row in the dataframe
        book_info = goodreads_df[goodreads_df["title"] == title].iloc[0]
        # tehn get the number of pages based on the row information
        num_pages = book_info["num_pages"]
        return f"{num_pages}"


# callback function for updating the genres information
@app.callback(
    Output("genres", "children"),  # ouputs the generes
    Input("book-dropdown", "value"),  # based on the bookdrop down value
)
def update_genres_info(title):
    if title is None:
        return ""
    else:
        # based on the selected title, get the row in the dataframe
        book_info = goodreads_df[goodreads_df["title"] == title].iloc[0]
        # get the genres from the dataframe row where the values are 1
        genres = [column for column, value in book_info.items() if value == 1]
        # get the names of the columns cuz thats where the names are
        genres = [column.capitalize() for column in genres]
        # add them together for the thing
        genres_str = ", ".join(genres)
        # return the genres
        return f"Genres: {genres_str}"


# this is the callback function for the view more books by this author button
@app.callback(
    Output(
        "author-dropdown", "value"
    ),  # output is the author drop down on the far right column
    [
        Input("author-books-button", "n_clicks")
    ],  # based on the number of clicks of the button
    [
        State("book-dropdown", "value")
    ],  # and the current state of the book-dropdown on the far left column
)
def update_author_dropdown_from_button(n_clicks, selected_title):
    # if both exist
    if n_clicks and selected_title:
        # find the author based on the title of the book
        author = goodreads_df.loc[
            goodreads_df["title"] == selected_title, "author"
        ].iloc[0]
        # return the author
        return author
    else:
        # otw dont need to update anything
        return dash.no_update


# run app
if __name__ == "__main__":
    app.run(jupyter_mode="tab", debug=False)
