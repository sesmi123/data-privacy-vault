import gunicorn

workers = 4
worker_class = "sync"
worker_connections = 1000
timeout = 30
keepalive = 2

errorlog = "-"
loglevel = "info"
accesslog = "-"
access_log_format = '%(t)s "%(r)s" %(s)s %(b)s "%(f)s" %(h)s %(l)s %(u)s  "%(a)s"'

gunicorn.SERVER = "undisclosed"
