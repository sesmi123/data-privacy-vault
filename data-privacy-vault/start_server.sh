#!/bin/bash

gunicorn -c data_privacy_vault/gunicornconf.py data_privacy_vault.app:app --bind 0.0.0.0:80
