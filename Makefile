help:
	@echo
	@echo "🕸 SCRAPE"
	@echo
	@echo "crawl:        crawl airline site"
	@echo "pic:          open screenshots"
	@echo
	@echo "🛠 TOOLING"
	@echo
	@echo "fmt:         auto format code using Black"
	@echo "lint:        lint using flake8"
	@echo "repl:        debug using bpython"
	@echo
	@echo "📦 DEPENDENCIES"
	@echo
	@echo "freeze:      freeze dependencies into requirements.txt"
	@echo "install:     install dependencies from requirements.txt"
	@echo "purge:       remove any installed pkg *not* in requirements.txt"
	@echo

crawl:
	python script.py

pic:
	open *.png

qing:
	rm *.png

fmt:
	black script.py

lint:
	flake8 script.py

repl:
	bpython

freeze:
	pip freeze > requirements.txt

install:
	pip install -r requirements.txt

purge:
	@echo "🔍 - DISCOVERING UNSAVED PACKAGES\n"
	pip freeze > pkgs-to-rm.txt
	@echo
	@echo "📦 - UNINSTALL ALL PACKAGES\n"
	pip uninstall -y -r pkgs-to-rm.txt
	@echo
	@echo "♻️  - REINSTALL SAVED PACKAGES\n"
	pip install -r requirements.txt
	@echo
	@echo "🗑  - UNSAVED PACKAGES REMOVED\n"
	diff pkgs-to-rm.txt requirements.txt | grep '<'
	@echo
	rm pkgs-to-rm.txt
	@echo
