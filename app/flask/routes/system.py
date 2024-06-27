from flask import Blueprint, render_template

page = Blueprint("system", __name__, url_prefix="/")

buckets_data = [
    {
        "bucket_id": 1,
        "bucket_name": "bucket1",
        "owner_name": "Alice",
        "owner_email": "alice@example.com",
        "created_at": "2024-01-01 10:00:00",
    },
    {
        "bucket_id": 2,
        "bucket_name": "bucket2",
        "owner_name": "Bob",
        "owner_email": "bob@example.com",
        "created_at": "2024-01-02 11:00:00",
    },
    {
        "bucket_id": 3,
        "bucket_name": "bucket3",
        "owner_name": "Alice",
        "owner_email": "alice@example.com",
        "created_at": "2024-01-03 12:00:00",
    },
]


@page.route("/")
def index():
    return render_template("index.html", buckets=buckets_data)


@page.route("/edit/<int:bucket_id>", methods=["POST"])
def edit_bucket(bucket_id):
    return render_template("index.html", buckets=buckets_data)


@page.route("/delete/<int:bucket_id>", methods=["POST"])
def delete_bucket(bucket_id):
    return render_template("index.html", buckets=buckets_data)
