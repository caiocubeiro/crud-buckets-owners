from dash import register_page, html, dcc, callback
from dash.dependencies import Input, Output
import pandas as pd

from app.dashboard.pages.assets.navbar import navbar
from app.flask.db.db import execute_query
from app.dashboard.functions.util import atualizaFiltros, montaBarChartBuckets, montaBarChartSize, montaPieChartBuckets, montaPieChartSize

register_page(__name__, path='/dashboard') 

opcoes_filtros = {
    "owner_name": [],
    "owner_department": [],
}


layout = (
    navbar,
    html.Div([
    html.Div([
        dcc.Loading(   
            overlay_style={"visibility":"visible", "filter": "blur(2px)"},
            children=[
                html.Div([
                    dcc.Dropdown(id="owner_name", multi=True, className="dropdown", placeholder="Selecione um Proprietário"),
                    dcc.Dropdown(id="owner_department", multi=True, className="dropdown", placeholder="Selecione um Departamento")
                ], className="filters_div"),
                html.Div([
                    dcc.Graph(
                        id='buckets_by_owner',
                    ),
                    dcc.Graph(
                        id='buckets_by_department',
                    )
                ], className="figures_div"),
                    html.Div([
                    dcc.Graph(
                        id='size_by_owner',
                    ),
                    dcc.Graph(
                        id='size_by_department',
                    )
                ], className="figures_div"),
            ]
        )
    ]
             ,className='page-content'),
])
)

@callback(
    Output("buckets_by_owner", "figure"),
    Output("buckets_by_department", "figure"),
    Output("size_by_owner", "figure"),
    Output("size_by_department", "figure"),
    Output("owner_name", "options"),
    Output("owner_department", "options"),
    Input("owner_name", "value"),
    Input("owner_department", "value"),
)

def update_data(
    owner_name,
    owner_department):
    
    # Define um dict com os nomes da coluna e os valores vindo dos dropdowns
    filtro_dict = {
        "owner_name": owner_name,
        "owner_department": owner_department,
    }
    
    query = """
        SELECT b.*, 
            o.owner_name, 
            o.owner_email, 
            o.owner_role, 
            o.owner_department, 
            o.owner_manager
        FROM buckets AS b
        INNER JOIN owners AS o ON b.owner_uuid = o.uuid;
    """
    
    df = pd.DataFrame(execute_query(query))
    
    # Para coluna do filtro_dict, filtra o df com os valores recebidos do drop
    for col, valores in list(filtro_dict.items()):
        if valores is not None and len(valores) > 0:
            df = df[df[col].isin(valores)]
            # Remove qualquer coluna já filtrada pois as opções não precisam ser filtradas
            filtro_dict.pop(col)

    num_var_preenchidas = sum(1 for valor in filtro_dict.values() if valor is not None and valor != [] and valor != "")
    
     # Verificar se mais de uma variável foi preenchida
    if num_var_preenchidas <= 1:
        for col in filtro_dict:
            opcoes_filtros[col] = atualizaFiltros(col, df)
    
    figChartBuckets = montaBarChartBuckets(df)
    figPieBuckets = montaPieChartBuckets(df)
    figChartSize = montaBarChartSize(df)
    figPieSize = montaPieChartSize(df)
    
    return figChartBuckets, figPieBuckets, figChartSize, figPieSize, opcoes_filtros["owner_name"], opcoes_filtros["owner_department"],