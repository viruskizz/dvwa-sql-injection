NAME=dvwa

$(NAME): all

all: up

up:
	docker compose up --detach --build

exec:
	docker exec -it ${NAME}-web /bin/bash

stop:
	docker compose stop

down:
	docker compose down

re: down up

clean: down
	-docker rmi -f $$(docker images "${NAME}-*" | awk 'NR!=1 {print}' | awk '{print $$1}')
	-docker rmi -f $$(docker images --filter "dangling=true" -q --no-trunc)

fclean: clean
	-docker run --rm -v "$(PWD):/app" -w /app alpine rm -rf mydata pgdata dvwa/db.sqlite3
	-rm -rf $$(find dvwa/*/migrations ! -name __init__.py -type f)

.PHONY: up down stop clean fclean re exec