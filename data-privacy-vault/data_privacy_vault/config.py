import os

auth = {
    "username": os.environ.get("VAULT_USER", "user"),
    "password": os.environ.get("VAULT_PASSWORD", "12password34")
}

data_encryption_key = os.environ.get("DATA_ENCRYPTION_KEY", b"T6LT0uLYdnu1nJcPPDwidOKSomLMg5icKKO4DfkanCw=")

redis = {
    "host": os.environ.get("DB_HOST", "localhost"),
    "port": os.environ.get("DB_PORT", 6379),
    "db": os.environ.get("DB_NAME", 0),
}