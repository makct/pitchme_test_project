deploy:
	docker-compose down web
	git pull
	docker-compose up -d web