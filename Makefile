install:
	pip install --upgrade pip &&\
		pip install -r requirements.txt

test:
	python -m pytest -vv --nbval -cov=mylib -cov=main test_*.py *.ipynb

format:	
	black *.py 

lint:
	pylint	--disable=C,E,W,R,F	*.py mylib/*.py **/*.py
    # pylint --disable=W0621,W1510,W1514,W0612 *.py mylib/*.py src/**/*.py
	ruff check --ignore E501,F401 *.py mylib/*.py test_*.py *.ipynb
    # pylint --disable=R,C --ignore-patterns=test_.*?py *.py mylib/*.py

container-lint:
	docker run --rm -i hadolint/hadolint < Dockerfile

refactor: format lint

deploy:
	#deploy goes here

all: install lint test format deploy

generate_and_push:
	# Create the markdown file (assuming it's generated from the plot)
	python test_main.py  # Replace with the actual command to generate the markdown

	# Add, commit, and push the generated files to GitHub

	# Check if there are any changes to commit and push
	@if [ -n "$$(git status --porcelain)" ]; then \
		git config --local user.email "sammysismiling@gmail.com"; \
		git config --local user.name "Samantha"; \
		git add .; \
		git commit -m "Add generated plot and report"; \
		git push; \
	else \
		echo "No changes to commit. Skipping commit and push."; \
	fi
