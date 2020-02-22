start-dev:
	docker-compose up

start-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml up

stop:
	@eval docker stop $$(docker ps -a -q)
	docker-compose down

ssh-nginx:
	docker exec -it nginx_server sh

ssh-backend:
	docker exec -it backend sh

ssh-frontend:
	docker exec -it frontend shmake

ssh-db:
	docker exec -it db sh

build-prod:
	docker-compose -f docker-compose.yml -f docker-compose.prod.yml build

build-dev:
	docker-compose build