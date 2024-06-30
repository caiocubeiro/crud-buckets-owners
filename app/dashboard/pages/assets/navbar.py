import dash_bootstrap_components as dbc

navbar = dbc.Navbar(
    dbc.Container(
        [
            dbc.Row(
                [
                    dbc.Col(
                        dbc.NavbarBrand(
                            "Voltar a Lista",
                            href="/",
                            external_link=True,
                            className="btn",
                        ),
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
