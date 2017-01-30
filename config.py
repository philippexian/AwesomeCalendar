import os
import yaml

SQL_ALCHEMY_MYSQL = "mysql://{username}:{password}@{host}:{port}/{db_name}"


def load_config():
    base_path = os.path.abspath(os.path.dirname(__file__))
    config_file = os.path.join(base_path, "config.yml")
    with open(config_file, 'r') as ymlfile:
        return yaml.load(ymlfile)


def load_app_config():
    config = load_config()
    app_config = {
        'basedir': os.path.abspath(os.path.dirname(__file__)),
        'DEBUG': config['debug'],
        'SECRET_KEY': os.urandom(24),
        #'SQLALCHEMY_DATABASE_URI': SQL_ALCHEMY_MYSQL.format(**config['database']),
        'GOOGLE_ID': config['oauth']['google']['id'],
        'FACEBOOK_ID': config['oauth']['facebook']['id'],
        'GOOGLE_SECRET': config['oauth']['google']['secret'],
        'FACEBOOK_SECRET': config['oauth']['facebook']['secret'],
    }
    return app_config
