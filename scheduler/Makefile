run:
	docker-compose up -d

restart:
	docker-compose restart scheduler-api

migrate:
	docker-compose exec scheduler-api su -c "python manage.py migrate"

shell:
	docker-compose exec scheduler-api su -c "python manage.py shell"

test:
	docker-compose exec scheduler-api su -c "python manage.py test -v2"

down:
	docker-compose down

createsuperuser:
	docker-compose exec scheduler-api su -c "python manage.py createsuperuser"
