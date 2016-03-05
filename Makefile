
install:
	pip install -r ./requirements.txt

save:
	pip freeze > requirements.txt

test:
	python run.py out.jpg $(shell ls ./test-imgs/8*.jpg)
