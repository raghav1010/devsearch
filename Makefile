build:
	docker compose -f local.yml up --build -d --remove-orphans

up:
	docker compose -f local.yml up -d

down:
	docker compose -f local.yml down

show_logs:
	docker compose -f local.yml logs

migrate:
	docker compose -f local.yml run --rm django-backend-service python3 manage.py migrate

makemigrations:
	docker compose -f local.yml run --rm django-backend-service python3 manage.py makemigrations

collectstatic:
	docker compose -f local.yml run --rm django-backend-service python3 manage.py collectstatic --no-input --clear

superuser:
	docker compose -f local.yml run --rm django-backend-service python3 manage.py createsuperuser

down-v:
	docker compose -f local.yml down -v

devsearch-db:
	docker compose -f local.yml exec postgres psql --username=postgres_user --dbname=devsearch-live

flake8:
	docker compose -f local.yml exec django-backend-service flake8 .

black-check:
	docker compose -f local.yml exec django-backend-service black --check --exclude=migrations .

black-diff:
	docker compose -f local.yml exec django-backend-service black --diff --exclude=migrations .

black:
	docker compose -f local.yml exec django-backend-service black --exclude=migrations .

isort-check:
	docker compose -f local.yml exec django-backend-service isort . --check-only --skip env --skip migrations

isort-diff:
	docker compose -f local.yml exec django-backend-service isort . --diff --skip env --skip migrations

isort:
	docker compose -f local.yml exec django-backend-service isort . --skip env --skip migrations