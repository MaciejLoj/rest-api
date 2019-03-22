containers-tool = docker-compose
dev-dockerfile = -f docker-compose.yml
FIXTURES-FILES = fixtures/demo_exams_fixtures.json

### Build & start app ###

.PHONY: build-dev
build-dev:
	$(containers-tool) $(dev-dockerfile) build

.PHONY: dev
dev:
	$(containers-tool) $(dev-dockerfile) up

.PHONY: load-fixtures
load-fixtures:
	 docker-compose exec -d backend bash -c "./manage.py migrate \
	 	&& ./manage.py loaddata $(FIXTURES-FILES)"