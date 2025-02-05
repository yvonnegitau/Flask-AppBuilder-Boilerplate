import logging

from flask import Flask
from flask_appbuilder import AppBuilder, SQLA
from flask_migrate import Migrate
import os
from flask_appbuilder.security.sqla.models import User, Role
"""
 Logging configuration
"""

logging.basicConfig(format="%(asctime)s:%(levelname)s:%(name)s:%(message)s")
logging.getLogger().setLevel(logging.DEBUG)

app = Flask(__name__)
app.config.from_object("config")
db = SQLA(app)
appbuilder = AppBuilder(app, db.session)
Migrate(app, db, compare_type=True)

"""
from sqlalchemy.engine import Engine
from sqlalchemy import event

#Only include this for SQLLite constraints
@event.listens_for(Engine, "connect")
def set_sqlite_pragma(dbapi_connection, connection_record):
    # Will force sqllite contraint foreign keys
    cursor = dbapi_connection.cursor()
    cursor.execute("PRAGMA foreign_keys=ON")
    cursor.close()
"""

user_name = os.getenv("ADMIN_EMAIL")
email = os.getenv("ADMIN_EMAIL")
password = os.getenv("ADMIN_PASSWORD")
first_name = os.getenv("ADMIN_FIRST_NAME")
last_name = os.getenv("ADMIN_LAST_NAME")

def create_admin_user(appbuilder):
    with app.app_context():
        session = appbuilder.get_session
        admin_user = session.query(User).select_from(User).join(Role, User.roles).filter(Role.name == 'Admin').first()
        if not admin_user:
            role_admin = session.query(Role).filter_by(name='Admin').first()
            new_admin = appbuilder.sm.add_user(
                username=user_name,
                email=email,
                role=role_admin,
                password=password,
                first_name=first_name,
                last_name=last_name

            )
            session.commit()

create_admin_user(appbuilder)
from . import views
