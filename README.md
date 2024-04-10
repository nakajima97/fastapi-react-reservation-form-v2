# fastapi-react-reservation-form
## Clone後に実行するコマンド
`docker compose build`  
`docker compose run --entrypoint "poetry install --no-root" api`  
`docker compose run --entrypoint "yarn install" front`  

マイグレーションの実行  
`docker compose exec api poetry run python -m source.migrate_db`  

# テストコードの実行
## api
`docker compose run --entrypoint "poetry run pytest" api`