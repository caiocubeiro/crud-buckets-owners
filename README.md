# crud-buckets-owners

Este projeto é um exemplo de CRUD desenvolvido com Flask e Plotly Dash

## Bibliotecas utilizadas:

- **Flask**
- **dotenv**
- **mysql.connector**
- **uuid**
- **Dash**
- **Dash Bootstrap Components**
- **Plotly**
- **Jinja**
- **Pandas**

Para rodar este projeto localmente, siga os passos abaixo:
```bash
    git clone https://github.com/caiocubeiro/crud-buckets-owners
    cd crud-buckets-owners

    sudo apt install python3
    sudo apt install python3.11-venv

    python3 -m venv .venv
    source .venv/bin/activate
```

Crie um arquivo .venv com as credenciais:
```bash
    SECRET_KEY = ""

    #DB Credentials
    MARIA_USER = ""
    MARIA_KEY = ""
    MARIA_HOST = ""
```

Install das [bibliotecas](#Bibliotecas) utilizadas:
```bash
    pip install -r requirements.txt

    sudo apt install mariadb-server

    sudo mysql_secure_installation
```

Configure o banco mariadb:
```bash
    sudo mariadb

    >> GRANT ALL ON *.* TO 'admin'@'localhost' IDENTIFIED BY 'password' WITH GRANT OPTION;
    >> FLUSH PRIVILEGES;
    exit
```

Executar as queries do arquivo: 
```bash
app\flask\db\bucket_owners.sql
```

Inicie a aplicação:
```bash
    python wsgi.py     
```

Para novos commits sempre aplicar formatação e verificação bandit
```bash
    black .
    bandit . 
```



