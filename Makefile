init:
	pip install pipenv
	pipenv install --dev --skip-lock 
test:
	pipenv run pytest 