build:
	docker-compose -f docker-compose.yml build

build-no-cache:
	docker-compose -f docker-compose.yml build --no-cache

start:
	docker-compose -f docker-compose.yml up -d

stop:
	docker-compose -f docker-compose.yml stop

rebuild:
	docker-compose -f docker-compose.yml up -d --build

bash:
	docker-compose -f docker-compose.yml exec app bash

shell-plus:
	docker-compose -f docker-compose.yml exec app bash -c "./manage.py shell_plus"

createsuperuser:
	docker-compose -f docker-compose.yml exec app bash -c "./manage.py createsuperuser"
