import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavbarBrand("Lista de Buckets", href="/", external_link=True),
                    ),
                ],
                align="center",
            ),
        ],
        fluid=True,
    ),
    color="dark",
    dark=True,
)