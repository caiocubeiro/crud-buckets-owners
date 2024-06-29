from flask import Blueprint, redirect, request, flash, url_for, render_template
from uuid import uuid4
from datetime import datetime
import pandas as pd
from app.flask.db.db import connect_db, execute_query

page = Blueprint("system", __name__, url_prefix="/")

def print_hora(msg):
     print(f"{str(datetime.now())[:-7]} >> {msg}")
    
@page.route("/")
def index():
    buckets_data = execute_query("SELECT * FROM buckets")
    owners_data = execute_query("SELECT * FROM owners")
    return render_template("index.html", buckets=buckets_data, owners=owners_data)

#Buckets Routes
@page.route('/add_bucket', methods=['POST'])
def add_bucket():
    try:
        new_bucket = {
            "uuid": str(uuid4()), 
            "bucket_name": request.form['bucket_name'],
            "owner_uuid": request.form['owner_uuid'],
            "owner_name": request.form['owner_name'],
            "owner_email": request.form['owner_email'],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        query = """
            INSERT INTO buckets (uuid, bucket_name, owner_uuid, owner_name, owner_email, created_at, updated_at)
            VALUES (%(uuid)s, %(bucket_name)s, %(owner_uuid)s, %(owner_name)s, %(owner_email)s, %(created_at)s, %(updated_at)s)
        """
        execute_query(query, new_bucket, commit=True)
        
        flash('Bucket adicionado com sucesso!', 'success')
        print_hora(f"Bucket {new_bucket} criado")
    except Exception as e:
        flash('Falha ao adicionar', 'error')
        print_hora(f"Falha na criação do bucket, erro: {e}")
        
    return redirect(url_for('system.index'))


@page.route("/edit_bucket/<bucket_uuid>", methods=["POST"])
def edit_bucket(bucket_uuid):
    try:
        bucket = {
            "uuid": bucket_uuid,
            "bucket_name": request.form['bucket_name'],
            "owner_name": request.form['owner_name'],
            "owner_email": request.form['owner_email'],
            "owner_uuid": request.form['owner_uuid'], 
            "updated_at": datetime.now()
        }
        query = """
            UPDATE buckets 
            SET bucket_name = %(bucket_name)s, owner_name = %(owner_name)s, owner_email = %(owner_email)s, owner_uuid = %(owner_uuid)s, updated_at = %(updated_at)s
            WHERE uuid = %(uuid)s
        """
        execute_query(query, bucket, commit=True)
        flash(f'{bucket["bucket_name"]} foi editado com sucesso!', 'success')
        print_hora(f"Bucket {bucket} editado")
    except Exception as e:
        flash('Falha ao editar', 'error')
        print_hora(f"Falha ao editar bucket, erro: {e}")
    return redirect(url_for('system.index'))


@page.route("/delete_bucket/<bucket_uuid>", methods=["POST"])
def delete_bucket(bucket_uuid):
    try:
        query = "DELETE FROM buckets WHERE uuid = %(uuid)s"
        execute_query(query, {"uuid": bucket_uuid}, commit=True)
        flash(f'Deletado com sucesso!', 'success')
        print_hora(f"Bucket {bucket_uuid} deletado")
    except Exception as e:
        flash('Falha ao deletar', 'error')
        print_hora(f"Falha ao deletar bucket, erro: {e}")
    return redirect(url_for('system.index'))


#Owners Routes
@page.route('/add_owner', methods=['POST'])
def add_owner():
    try:
        new_owner = {
            "uuid": str(uuid4()), 
            "owner_name": request.form['owner_name'],
            "owner_email": request.form['owner_email'],
            "owner_department": request.form['owner_department'],
            "owner_manager": request.form['owner_manager'],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        print(new_owner)

        query = """
            INSERT INTO owners (uuid, owner_name, owner_email, owner_department, owner_manager, created_at, updated_at)
            VALUES (%(uuid)s, %(owner_name)s, %(owner_email)s, %(owner_department)s, %(owner_manager)s, %(created_at)s, %(updated_at)s)
        """
        execute_query(query, new_owner, commit=True)
        
        flash('Owner adicionado com sucesso!', 'success')
        print_hora(f"Owner {new_owner} criado")
    except Exception as e:
        flash('Falha ao adicionar', 'error')
        print_hora(f"Falha na criação do owner, erro: {e}")
        
    return redirect(url_for('system.index'))


@page.route("/edit_owner/<owner_uuid>", methods=["POST"])
def edit_owner(owner_uuid):
    try:
        owner = {
            "uuid": owner_uuid,
            "owner_name": request.form['owner_name'],
            "owner_email": request.form['owner_email'],
            "owner_department": request.form['owner_department'],
            "owner_manager": request.form['owner_manager'],
            "updated_at": datetime.now()
        }
        print(owner)
        query = """
            UPDATE owners 
            SET owner_name = %(owner_name)s, owner_email = %(owner_email)s, owner_department = %(owner_department)s, owner_manager = %(owner_manager)s, updated_at = %(updated_at)s
            WHERE uuid = %(uuid)s
        """
        execute_query(query, owner, commit=True)
        flash(f'{owner["owner_name"]} foi editado com sucesso!', 'success')
        print_hora(f"Owner {owner} editado")
    except Exception as e:
        flash('Falha ao editar', 'error')
        print_hora(f"Falha ao editar owner, erro: {e}")
    return redirect(url_for('system.index'))


@page.route("/delete_owner/<owner_uuid>", methods=["POST"])
def delete_owner(owner_uuid):
    if request.method == 'POST':
        print("Método POST recebido")
        try:
            query = "DELETE FROM owners WHERE uuid = %(uuid)s"
            execute_query(query, {"uuid": owner_uuid}, commit=True)
            flash(f'Deletado com sucesso!', 'success')
            print_hora(f"Owner {owner_uuid} deletado")
        except Exception as e:
            flash('Falha ao deletar', 'error')
            print_hora(f"Falha ao deletar owner, erro: {e}")
    return redirect(url_for('system.index'))

@page.route("/test_delete_owner/<owner_uuid>", methods=['GET', 'POST'])
def test_delete_owner(owner_uuid):
    print(owner_uuid)
    print("Método POST recebido")
    return "Teste de rota bem-sucedido"



