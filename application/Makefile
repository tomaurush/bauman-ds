build:
	docker build -t bauman .

run:
	docker run -dp 5000:5000 bauman

clean:
	docker stop $$(docker ps -aq)

rerun: clean build run
