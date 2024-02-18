# Data Privacy Vault

The data privacy vault is built based on the concept of [tokenization service](https://en.wikipedia.org/wiki/Tokenization_(data_security)).


Data persistence: Redis

Data encryption: Fernet symmetric key encryption

Programming Language: Python

Framework: Flask

Auth: Basic Auth


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

    Optionally, install Redis Insight.

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

## Docker Setup

```sh
docker pull sesmi/data-privacy-vault:latest
docker pull redis:latest

docker network create private_vault_network

docker volume create redis_data

docker run -p 9000:6379 -d --name my_redis -v redis_data:/data --network private_vault_network redis redis-server --appendonly yes
docker run -p 7000:80 -d --name my_vault -e DB_HOST=my_redis --network private_vault_network sesmi/data-privacy-vault:latest
```

#### Cleanup

```sh
docker stop my_redis my_vault
docker rm my_redis my_vault

docker volume rm redis_data

docker network rm private_vault_network
```

## Kubernetes Setup

**TODO**

## Going Further

- Integrate with a key management system like Azure Keyvault to keep the cryptographic keys secure.

- Extend the authentication to integrate with common identity and access management solutions.
