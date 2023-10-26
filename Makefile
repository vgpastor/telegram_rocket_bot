# Construye la imagen utilizando docker-compose
build:
	docker-compose build

# Inicia el servicio utilizando docker-compose
up:
	docker-compose up -d

# Detiene y elimina el contenedor utilizando docker-compose
down:
	docker-compose down

# Muestra los logs del contenedor
logs:
	docker-compose logs -f

# Reconstruye y reinicia el contenedor
rebuild: down build up

.PHONY: build up down logs rebuild
