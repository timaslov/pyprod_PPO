rebuild-docker:
	docker compose build --pull

infra:
	docker compose up -d postgres nginx

back:
	docker compose up back --build

back-exec:
	docker compose exec back bash

down:
	docker compose down
