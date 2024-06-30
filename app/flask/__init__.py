from flask import Flask
import os
from dotenv import load_dotenv


def init_app():
    load_dotenv()

    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")

    with app.app_context():
        from app.flask.routes.system import page

        app.register_blueprint(page)

        from app.dashboard import init_dashboard

        app = init_dashboard(app)

    return app
