.SILENT:
.DEFAULT_GOAL= help
.PHONY: mercure server help test

COM_COLOR   = \033[0;34m
OBJ_COLOR   = \033[0;36m
OK_COLOR    = \033[0;32m
ERROR_COLOR = \033[0;31m
WARN_COLOR  = \033[0;33m
NO_COLOR    = \033[m

PORT?=8000
CURRENT_DIR=$( shell pwd )
CHOSSEN_FILE?=$(shell pwd)

server: ## Lancer le serveur interne de PHP sur PORT=8000 par defaut
	echo "$(COM_COLOR)Lancement du server sur http://localhost:$(PORT)$(NO_COLOR)" 
	php -S localhost:$(PORT) -t public -d display_errors=1



help: 
	@grep -E '(^[a-zA-Z_-]+:.*?##.*$$)|(^##)' $(MAKEFILE_LIST) | awk 'BEGIN {FS = ":.*?## "}; {printf "\033[32m%-10s\033[0m %s\n", $$1, $$2}' | sed -e 's/\[32m##/[33m/'
mercure: ./mercure/mercure ## lancement de server du mercure
	echo "$(OK_COLOR) ----------lancement de mercure------------"
	./mercure/mercure --jwt-key='!ChangeMe' --addr='localhost:3000' --allow-anonymous --cors-allowed-origins=http://localhost:8000                                      
test: ## run phpunit with chossen file as argemment 