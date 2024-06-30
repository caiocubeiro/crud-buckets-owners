from flask import Blueprint, redirect, request, flash, url_for, render_template, jsonify
from uuid import uuid4
from datetime import datetime
import pandas as pd
from app.flask.db.db import connect_db, execute_query

page = Blueprint("system", __name__, url_prefix="/")

def print_hora(msg):
     print(f"{str(datetime.now())[:-7]} >> {msg}")
    
@page.route("/")
def index():
    buckets_data = execute_query("""
        SELECT b.*, 
            o.owner_name, 
            o.owner_email, 
            o.owner_role, 
            o.owner_department, 
            o.owner_manager
        FROM buckets AS b
        INNER JOIN owners AS o ON b.owner_uuid = o.uuid;
    """)
    owners_data = execute_query("SELECT * FROM owners")
    return render_template("index.html", buckets=buckets_data, owners=owners_data)

#Buckets Routes
@page.route('/add_bucket', methods=['POST'])
def add_bucket():
    try:
        new_bucket = {
            "uuid": str(uuid4()), 
            "bucket_name": request.form['bucket_name'],
            "size_gb": request.form['bucket_size'],
            "owner_uuid": request.form['owner_uuid'],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }

        query = """
            INSERT INTO buckets (uuid, bucket_name, size_gb, owner_uuid, created_at, updated_at)
            VALUES (%(uuid)s, %(bucket_name)s, %(size_gb)s, %(owner_uuid)s, %(created_at)s, %(updated_at)s)
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
            "size_gb": request.form['bucket_size'],
            "owner_uuid": request.form['owner_uuid'], 
            "updated_at": datetime.now()
        }
        query = """
            UPDATE buckets 
            SET bucket_name = %(bucket_name)s, size_gb = %(size_gb)s, owner_uuid = %(owner_uuid)s, updated_at = %(updated_at)s
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

@page.route('/search_bucket', methods=['POST'])
def search_bucket():
    search_value = request.form['search_value']
    query = """
    SELECT b.*, 
           o.owner_name, 
           o.owner_email, 
           o.owner_role, 
           o.owner_department, 
           o.owner_manager 
    FROM buckets AS b
    INNER JOIN owners AS o ON b.owner_uuid = o.uuid
    WHERE b.uuid = %s OR b.bucket_name = %s;
    """
    try:
        result = execute_query(query, (search_value, search_value))
        if result:
            bucket = result[0]
            return jsonify(bucket)
        else:
            return jsonify({"error": "Não localizado"}), 404
    except Exception as e:
        print(e)
        return jsonify({"error": "Não localizado"}), 404


#Owners Routes
@page.route('/add_owner', methods=['POST'])
def add_owner():
    try:
        new_owner = {
            "uuid": str(uuid4()), 
            "owner_name": request.form['owner_name'],
            "owner_email": request.form['owner_email'],
            "owner_role": request.form['owner_role'],
            "owner_department": request.form['owner_department'],
            "owner_manager": request.form['owner_manager'],
            "created_at": datetime.now(),
            "updated_at": datetime.now()
        }
        
        print(new_owner)

        query = """
            INSERT INTO owners (uuid, owner_name, owner_email, owner_role, owner_department, owner_manager, created_at, updated_at)
            VALUES (%(uuid)s, %(owner_name)s, %(owner_email)s, %(owner_role)s, %(owner_department)s, %(owner_manager)s, %(created_at)s, %(updated_at)s)
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
            "owner_role": request.form['owner_role'],
            "owner_department": request.form['owner_department'],
            "owner_manager": request.form['owner_manager'],
            "updated_at": datetime.now()
        }
        print(owner)
        query = """
            UPDATE owners 
            SET owner_name = %(owner_name)s, owner_email = %(owner_email)s, owner_role = %(owner_role)s, owner_department = %(owner_department)s, owner_manager = %(owner_manager)s, updated_at = %(updated_at)s
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
    try:
        query_buckets = "DELETE FROM buckets WHERE owner_uuid = %(uuid)s"
        execute_query(query_buckets, {"uuid": owner_uuid}, commit=True)
        query_owner = "DELETE FROM owners WHERE uuid = %(uuid)s"
        execute_query(query_owner, {"uuid": owner_uuid}, commit=True)
        flash(f'Deletado com sucesso!', 'success')
        print_hora(f"Owner {owner_uuid} deletado")
    except Exception as e:
        flash('Falha ao deletar', 'error')
        print_hora(f"Falha ao deletar owner, erro: {e}")
    return redirect(url_for('system.index'))



