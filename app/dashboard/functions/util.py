import plotly.graph_objects as go

def atualizaFiltros(col, df):
    return list(df[col].unique())

def montaBarChartBuckets(df):
    grouped_df = df.groupby('owner_name')['bucket_name'].nunique().reset_index()
    grouped_df.columns = ['owner', 'qtd_buckets']
    
    total_buckets = grouped_df['qtd_buckets'].sum()
    grouped_df['porcent'] = (grouped_df['qtd_buckets'] / total_buckets) * 100
    grouped_df = grouped_df.sort_values(by=['qtd_buckets'], ascending=True)
    
    fig = go.Figure(data=[
        go.Bar(name='Buckets', x=grouped_df['owner'], y=grouped_df['qtd_buckets'])
    ])
    
    legenda = []
    for idx, row in grouped_df.iterrows():
        legenda.append(
            dict(
                x=row['owner'],
                y=row['qtd_buckets'],
                text=f"{row['qtd_buckets']} - {row['porcent']:.2f}%",
                showarrow=False,
                yshift=10
            )
        )

    fig.update_layout(
        title='Quantidade de Buckets por Proprietário',
        xaxis_title='Proprietário',
        yaxis_title='Quantidade de Buckets',
        template='plotly_white',
        annotations=legenda
    )
    return fig

def montaPieChartBuckets(df):
    grouped_df = df.groupby('owner_department')['bucket_name'].nunique().reset_index()
    grouped_df.columns = ['department', 'qtd_buckets']
    
    fig = go.Figure(data=[
        go.Pie(labels=grouped_df['department'], values=grouped_df['qtd_buckets'], hole=.3)
    ])

    fig.update_layout(
        title='Quantidade de Buckets por Departamento',
        template='plotly_white'
    )
    return fig

def montaBarChartSize(df):
    grouped_df = df.groupby('owner_name')['size_gb'].sum().reset_index()
    grouped_df.columns = ['owner', 'gbs']
    
    total_buckets = grouped_df['gbs'].sum()
    grouped_df['porcent'] = (grouped_df['gbs'] / total_buckets) * 100
    grouped_df = grouped_df.sort_values(by=['gbs'], ascending=True)
    
    fig = go.Figure(data=[
        go.Bar(name='Size', x=grouped_df['owner'], y=grouped_df['gbs'])
    ])
    
    legenda = []
    for idx, row in grouped_df.iterrows():
        legenda.append(
            dict(
                x=row['owner'],
                y=row['gbs'],
                text=f"{row['gbs']} - {row['porcent']:.2f}%",
                showarrow=False,
                yshift=10
            )
        )

    fig.update_layout(
        title='Quantidade de Espaço Alocado por Proprietário (GB)',
        xaxis_title='Proprietário',
        yaxis_title='Espaço Alocado',
        template='plotly_white',
        annotations=legenda
    )
    return fig

def montaPieChartSize(df):
    grouped_df = df.groupby('owner_department')['size_gb'].sum().reset_index()
    grouped_df.columns = ['department', 'gbs']
    
    fig = go.Figure(data=[
        go.Pie(labels=grouped_df['department'], values=grouped_df['gbs'], hole=.3)
    ])

    fig.update_layout(
        title='Quantidade de Espaço Alocado por Departamento',
        template='plotly_white'
    )
    return fig
