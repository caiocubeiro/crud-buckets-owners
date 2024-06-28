from dash import Dash
import dash_bootstrap_components as dbc

external_stylesheets = ['base.css', dbc.themes.BOOTSTRAP]

def init_dashboard(app):
    dash_module = Dash(
        server=app,
        use_pages=True,
        pages_folder="../dashboard/pages",
        assets_folder="../dashboard/pages",
        external_stylesheets=external_stylesheets
    )
    dash_module.enable_dev_tools(debug=None)
    return dash_module.server