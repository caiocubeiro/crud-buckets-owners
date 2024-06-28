from dash import register_page, html
from app.dashboard.pages.assets.navbar import navbar

register_page(__name__, path='/dashboard') 

layout = (
    navbar,
    html.Div([
    html.Div(id='page-content'),
])
)