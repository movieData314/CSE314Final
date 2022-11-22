# External Modules
from dash import Dash, html, dcc, Input, Output
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
    Deprecated: The default html layout for a simple dashboard app.
    It serves as a simple example to understand the nature of dashboard.

    Parameters
    ----------
    toy_fig: plotly.graph_objects.Figure
        A default figure to display, which serves as a placeholder

    Returns
    -------
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


def advanced_graph_factory(app: Dash):
    """
    This function returns a dashboard layout for basic data exploration, statistics analysis and
    visualization.

    Parameters
    ----------
    app: dash.Dash
        The actual dash board object itself. It is used to implement callback fucntions.

    Returns
    -------
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
        Output("graph", "figure"), Input("xlabel", "value"), Input("ylabel", "value")
    )
    def update_figure(xlabel_name, ylabel_name):
        data = accessor.agg(xlabel_name, ylabel_name)
        if data.dtypes[xlabel_name] == "object" or data.dtypes[ylabel_name] == "object":
            cat, other = (
                (xlabel_name, ylabel_name)
                if data.dtypes[xlabel_name] == "object"
                else (ylabel_name, xlabel_name)
            )
            return px.bar(
                data_frame=data.groupby(cat).mean().reset_index(), x=cat, y=other
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
                    dbc.NavItem(dbc.NavLink("Page 1", href="#")),
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
                brand="NavbarSimple",
                brand_href="#",
                color="primary",
                dark=True,
            ),
            dbc.Row(
                id="up-table",
                children=dbc.Col(
                    [table],
                    style={"background-color": "red"},
                    width={"size": 10, "offset": 1},
                ),
            ),
            dbc.Row(
                id="lower-table",
                children=[
                    dbc.Col(
                        id="left-col",
                        width={"size": 5, "offset": 1},
                        children=[
                            dbc.Row(
                                [
                                    dbc.Col(
                                        [
                                            dcc.Dropdown(
                                                variables,
                                                "Select something",
                                                id="xlabel",
                                            )
                                        ],
                                        width={"size": 2},
                                    ),
                                    dbc.Col(
                                        [
                                            dcc.Dropdown(
                                                variables,
                                                "Select something",
                                                id="ylabel",
                                            )
                                        ],
                                        width={"size": 2},
                                    ),
                                ]
                            ),
                            dbc.Row(
                                id="select_stats",
                                children=[],
                            ),
                        ],
                    ),
                    dbc.Col(
                        id="right-col",
                        children=[dcc.Graph(id="graph", figure=default_fig)],
                        style={"background-color": "blue"},
                        width={"size": 5},
                    ),
                ],
            ),
        ]
    )
