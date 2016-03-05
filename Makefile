
activate:
	source ./venv/bin/activate

install:
	pip install -r ./requirements.txt

save:
	pip freeze > requirements.txt

test:
	python run.py test.jpg $(shell ls ./test-imgs/*.jpg)
