import pandas as pd
from dash import dash_table
import numpy as np
import plotly.express as px
import plotly


def data2table(data: pd.DataFrame, **kwargs) -> dash_table.DataTable:
    """
    ### data2table
    Take a dataframe and make a DataTable object that can be shown in the dashboard app

    Arguments:
        data (pd.DataFrame): The dataframe object that holds the data to present. The data should not be too large for fast loading.

        kwargs: Keyword arguments for initializing DataTable objects

    Returns:
        dash_table.DataTable
            The DataTable object that can be readily incoporated into the dash.html framework

    """
    return dash_table.DataTable(
        data.to_dict("records"),
        columns=[{"id": c, "name": c} for c in data.columns],
        tooltip_data=[
            {
                column: {"value": str(value), "type": "markdown"}
                for column, value in row.items()
            }
            for row in data.to_dict("records")
        ],
        tooltip_duration=None,
        **kwargs
    )


def get_stats(data: pd.DataFrame) -> pd.DataFrame:
    """
    ### get_stats
    Return a dataframe that provides numerical description of the input data

    Arguments:
        data (pd.DataFrame): The data to calculate statistics on

    Returns:
        pd.DataFrame
            The basic statistics of the data including quantiles, max, min and correlation
    """
    temp = data.describe().T.reset_index()
    if "object" not in data.dtypes.values and "bool" not in data.dtypes.values:
        corr = data.corr().iloc[0, 1]
        temp["correlation"] = corr
    return temp


def get_statsTable(data: pd.DataFrame) -> dash_table.DataTable:
    """
    ### get_statsTable
    Turn the statistics dataframe into a DataTable object

    Arguments:
        data (pd.DataFrame): The data to calculate statistics on

    Returns:
        dash_table.DataTable
            The basic statistics of the data including quantiles, max, min and correlation
    """
    return data2table(get_stats(data), style_table={"overflowX": "auto"})


def get_toyFig() -> plotly.graph_objects.Figure:
    """
    ### get_toyFig
    Return a placeholder figure

    Arguments:
        None

    Returns:
        plotly.graph_objects.Figure
            A toy figure used as a placeholder in the app layout
    """
    x = np.random.randint(0, 100, size=20)
    y = np.random.randint(0, 100, size=20)
    return px.scatter(x=x, y=y, title="A placeholder figure")
