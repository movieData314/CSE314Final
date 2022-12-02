# external dependencies
import plotly.express as px
from dash import Dash
import dash_bootstrap_components as dbc

# local dependencies
import db_UI
import data_process as dp

# Load Data
df = px.data.tips()

# Build App UI
app = Dash(external_stylesheets=[dbc.themes.BOOTSTRAP])
app.layout = db_UI.advanced_graph_factory(app)

# Run app and display result inline in the notebook
if __name__ == "__main__":
    app.run_server(debug="True")
