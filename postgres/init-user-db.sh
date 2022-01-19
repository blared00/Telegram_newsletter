#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" <<-EOSQL
    CREATE USER devuser;
    CREATE DATABASE t_news;
    GRANT ALL PRIVILEGES ON DATABASE t_news TO devuser;
EOSQL