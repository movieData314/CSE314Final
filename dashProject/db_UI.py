# External Modules
from dash import Dash, html, dcc, Input, Output, State
import dash_bootstrap_components as dbc
import plotly.express as px
import sys
import plotly

# Path to local modules
sys.path.append("/home/themaster/workspace/cse314final/")

# Local modules
import data_process as dp
from RDlite import all_features
from RDlite import accessor


def default_graph_factory(toy_fig: plotly.graph_objects.Figure) -> html:
    """
    ### default_graph_factory
    Return a simple example used as the layout of the dashboard app.

    Note:
        This function is deprecated. The default html layout for a simple dashboard app.

    Arguments:
        toy_fig (plotly.graph_objects.Figure): A default figure to display, which serves as a placeholder

    Returns:
        html
            A Dash.html object which is the basic layout of the dashbaord app
    """
    return html.Div(
        [
            html.H1("Dash Demo"),
            dcc.Graph(id="graph", figure=toy_fig),
            html.Div(
                [dcc.Dropdown(["x"], "Select something", id="xlabel")],
                style={"width": "48%", "display": "inline-block"},
            ),
            html.Div(
                [dcc.Dropdown(["y", "z"], "Select something", id="ylabel")],
                style={"width": "48%", "display": "inline-block"},
            ),
        ]
    )


def advanced_graph_factory(app: Dash) -> html:
    """
    ### advanced_graph_factory
    Return a layout for the dashboard app.

    This function returns a dashboard layout for basic data exploration, statistics analysis and
    visualization.

    Arguments:
        app (dash.Dash): The actual dash board object itself. It is used to implement callback fucntions.

    Returns:
        html
            A Dash.html object which is the basic layout of the dashbaord app
    """

    data = accessor.agg(*all_features, peek=True)
    table = dp.data2table(
        data,
        page_size=10,
        style_table={"overflowX": "auto"},
        style_cell={
            "minWidth": "180px",
            "width": "180px",
            "maxWidth": "180px",
            "overflow": "hidden",
            "textOverflow": "ellipsis",
        },
    )
    variables = list(data.columns)
    default_fig = dp.get_toyFig()

    @app.callback(
        Output("graph", "figure"),
        State("xlabel", "value"),
        State("ylabel", "value"),
        State("limiter", "value"),
        Input("submit", "n_clicks"),
    )
    def update_figure(xlabel_name, ylabel_name, range, n_clicks):
        data = accessor.agg(xlabel_name, ylabel_name)
        if data.dtypes[xlabel_name] == "object" or data.dtypes[ylabel_name] == "object":
            cat, other = (
                (xlabel_name, ylabel_name)
                if data.dtypes[xlabel_name] == "object"
                else (ylabel_name, xlabel_name)
            )
            stats = data.groupby(cat).mean().reset_index()
            return px.bar(
                data_frame=stats.iloc[
                    int(stats.shape[0] * range[0] / 100) : int(
                        stats.shape[0] * range[1] / 100
                    ),
                    :,
                ],
                x=cat,
                y=other,
            )
        else:
            return px.scatter(data_frame=data, x=xlabel_name, y=ylabel_name)

    @app.callback(
        Output("select_stats", "children"),
        Input("xlabel", "value"),
        Input("ylabel", "value"),
    )
    def update_statTable(xlabel_name, ylabel_name):
        data = accessor.agg(xlabel_name, ylabel_name)
        return [dp.get_statsTable(data[[xlabel_name, ylabel_name]])]

    return html.Div(
        [
            dbc.NavbarSimple(
                children=[
                    dbc.NavItem(dbc.NavLink("Documentation", href="#")),
                    dbc.DropdownMenu(
                        children=[
                            dbc.DropdownMenuItem("More pages", header=True),
                            dbc.DropdownMenuItem("Page 2", href="#"),
                            dbc.DropdownMenuItem("Page 3", href="#"),
                        ],
                        nav=True,
                        in_navbar=True,
                        label="More",
                    ),
                ],
                brand="MovieDataset",
                brand_href="#",
                color="primary",
                dark=True,
            ),
            dbc.Row(
                id="uppper-table",
                children=dbc.Col(
                    [table],
                    style={"background-color": "#F7f7f9"},
                    width={"size": 10, "offset": 1},
                ),
            ),
            dbc.Row(
                id="lower-table",
                children=[
                    dbc.Col(
                        id="left-col",
                        width={"size": 5, "offset": 1},
                        style={"background-color": "#F7f7f9"},
                        children=[
                            html.H2("Data Explorer"),
                            html.P(
                                "Explore data by selecting X and Y variable. Use the slider below to limit the percent of data to present. It is recommended when ploting categorical variables."
                            ),
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dcc.Dropdown(
                                                variables,
                                                "X variable",
                                                id="xlabel",
                                            )
                                        ],
                                        width={"size": 3},
                                    ),
                                    dbc.Col(
                                        [
                                            dcc.Dropdown(
                                                variables,
                                                "Y variable",
                                                id="ylabel",
                                            )
                                        ],
                                        width={"size": 3},
                                    ),
                                    dbc.Col(
                                        [
                                            html.Button(
                                                id="submit",
                                                n_clicks=0,
                                                children="Submit",
                                            )
                                        ],
                                        width={"size": 3},
                                    ),
                                ]
                            ),
                            dbc.Row(
                                id="slider",
                                children=[
                                    dcc.RangeSlider(
                                        min=0,
                                        max=100,
                                        step=5,
                                        value=[0, 100],
                                        id="limiter",
                                    )
                                ],
                            ),
                            dbc.Row(id="select_stats", children=[]),
                        ],
                    ),
                    dbc.Col(
                        id="right-col",
                        children=[dcc.Graph(id="graph", figure=default_fig)],
                        style={"background-color": "#F7f7f9"},
                        width={"size": 5},
                    ),
                ],
                style={"padding-bottom": "30px"},
            ),
        ],
        style={"background-color": "#E8EFF3", "padding-bottom": "30px"},
    )
