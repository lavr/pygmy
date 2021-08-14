import os

from pygmy.model import *
from pygmy.config import config
from pygmy.database.sqlite import SqliteDatabase
from pygmy.database.postgresql import PostgreSQLDatabase
from pygmy.database.mysql import MySQLDatabase
from pygmy.database.base import Model


class DatabaseFactory:

    @staticmethod
    def create():
        """Get db class from config.db.engine"""
        # TODO: make a utli.mapping
        engine = os.environ.get('DB_ENGINE') or config.database['engine']
        if engine == 'sqlite3':
            database = SqliteDatabase()
        elif engine == 'postgresql':
            database = PostgreSQLDatabase()
        elif engine == 'mysql':
            database = MySQLDatabase()
        else:
            raise Exception(
                "Unsupported DB type. Supported types are "
                "postgresql/sqlite3 and mysql")
        database.initialize(config.debug)
        # Create all tables, if not already exists.
        Model.metadata.create_all(database.engine)
        # TODO DB: Run migrations
        return database
