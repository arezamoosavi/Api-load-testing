run-locust:
	locust -f main/tests/test_locust.py -P 8090

remove-containers:
	docker container prune -f

docker-build:
	docker-compose build
	docker-compose rm -f

docker-start:
	docker-compose up

docker-stop:
	docker-compose down

docker-cleanup:
	docker-compose down -v