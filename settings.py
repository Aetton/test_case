#work database
database_name = 'sql/workdb.db'
#hostname
host_name = '127.0.0.1'
#port to connect
port_name = 8080

#get parameters from settings_local.py
try:
    from settings_local import *
except ImportError:
    pass