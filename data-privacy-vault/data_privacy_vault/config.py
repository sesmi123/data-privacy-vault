import os

redis = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", 6379),
    "db": os.environ.get("DB_NAME", 0),
}