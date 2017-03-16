all: build run

build:
	cd client; ng build --base-href /static/

clean: clean-client
	find . -name \*.pyc -delete

clean-client:
	rm -rf client/static client/tmp

run:
	python -m duckomatic

fake:
	python -m duckomatic -f -d

test:
	paver test_all

update:
	git fetch
	git submodule update
	pip install -r requirements.txt
