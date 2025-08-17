SHELL := /bin/bash

help:
	@echo "make update-pubs      # fetch Scholar -> _publications/"
	@echo "make serve            # local preview"
	@echo "make deploy           # commit & push"

update-pubs:
	python _scripts/scholar_to_publications.py --scholar-id nY889B0AAAAJ --outdir _publications --first-author Masud

serve:
	bundle exec jekyll serve --livereload

deploy:
	git add -A && git commit -m "Update site" && git push
