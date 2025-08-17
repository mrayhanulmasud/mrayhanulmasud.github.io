SHELL := /bin/bash

help:
	@echo "make update-pubs   # uses Google Scholar to refresh _data/publications.yml"
	@echo "make serve         # local preview with jekyll"
	@echo "make deploy        # commit & push to GitHub"

update-pubs:
	python _scripts/scholar_to_yaml.py --scholar-id nY889B0AAAAJ --out _data/publications.yml --first-author Masud

serve:
	bundle exec jekyll serve --livereload

deploy:
	git add .
	git commit -m "Update site"
	git push