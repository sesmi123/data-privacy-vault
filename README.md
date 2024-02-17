# Data Privacy Vault

The data privacy vault is built based on the concept of [tokenization service](https://en.wikipedia.org/wiki/Tokenization_(data_security)).


Data persistence: Redis

Data encryption: Fernet symmetric key encryption


## Local setup

1. Install and setup redis with data persistence enabled.

    Follow [installation guide](https://redis.io/docs/install/install-redis/)

    OR

    Use docker: 
    ```sh
    mkdir redis-data
    docker run -d --name my-redis -p 6379:6379 -v $(pwd)/redis-data:/data redis:latest --appendonly yes
    ```

    OR 

    Use free redis database in the cloud. Create a [free account](https://redis.com/try-free/).

    **Note**: Authentication in redis is not supported as of now. However, it can be considered for implementation as a potential enhancement in the future.

2. Configure your redis connection in `config.py`
3. Configure the key used for Fernet encryption and decryption in the `config.py`. The key must be 32 url-safe base64-encoded bytes.

    To generate a key run the following in your Python interactive shell:
    ```py
    from cryptography.fernet import Fernet
    Fernet.generate_key()
    ```
4. Create a virtual environment and install dependencies.

    Run `pip install poetry` if required.

    ```sh
    python -m venv venv
    . venv/bin/activate
    poetry install
    ```

5. Run the application:

    ```sh
    cd data_privacy_vault
    python app.py
    ```

6. Run unit tests:

    ```sh
    cd tests
    python -m unittest
    ```

## Kubernetes Setup

**TODO**