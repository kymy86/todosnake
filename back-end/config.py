import os
import logging

DEBUG = os.getenv('ENVIRONMENT') == 'DEV'
HOST = os.getenv('APPLICATION_HOST')
PORT = int(os.getenv('APPLICATION_PORT', 8000))
DB_CONTAINER = os.getenv('APPLICATION_DB_CONTAINER', 'DB')
APPLICATION_ROOT = os.getenv('APPLICATION_APPLICATION_ROOT', '/application')
POSTGRES = {
    'user': os.getenv('POSTGRES_USER', 'postgres'),
    'pw': os.getenv('POSTGRES_PASSWORD', ''),
    'host': os.getenv(
        'POSTGRES_HOST',
        os.getenv('%s_PORT_5432_TCP_ADDR' % DB_CONTAINER)
    ),
    'port': os.getenv(
        'POSTGRES_PORT',
        os.getenv('%s_PORT_5432_TCP_PORT' % DB_CONTAINER)
    ),
    'db': os.getenv('POSTGRES_DB', 'postgres'),
}
SQLLITE = 'sqlite:///' + os.path.join('test.db')
DB_URI = 'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES

logging.basicConfig(
    filename=os.getenv('SERVICE_LOG', 'server.log'),
    level=logging.DEBUG,
    format='%(levelname)s: %(asctime)s \
        pid:%(process)s module:%(module)s %(message)s',
    datefmt='%d/%m/%y %H:%M:%S',
)
