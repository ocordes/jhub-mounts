# jhub-mounts/config.py

# written by: Oliver Cordes 2022-03-25
# changed by: Oliver Cordes 2022-03-25


import os

basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    API_TOKEN = os.environ.get('API_TOKEN') or 'jhub-mounts-api-token'

    SERVICE_NAME = os.environ.get('SERVICE_NAME') or 'jhub-mounts'

    SERVICE_PREFIX = os.environ.get('JUPYTERHUB_SERVICE_PREFIX') or '/services/test/'
