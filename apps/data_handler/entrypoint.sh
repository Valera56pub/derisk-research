#!/bin/bash

echo "Run migrations..."
cd shared && alembic upgrade head
cd ../

echo "Starting the server and bot..."
exec "$@"

uvicorn data_handler.main:app --host 0.0.0.0 --port 8000 --reload
