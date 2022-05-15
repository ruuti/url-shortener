build:
	docker build . -t shorter

dev-run:
	docker-compose -f ./docker-compose.yml up --build

test:
	docker-compose -f ./docker-compose-test.yml up --build --abort-on-container-exit app-test-runner
