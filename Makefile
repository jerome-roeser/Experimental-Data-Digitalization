install:
	poetry install

clean: clean-build clean-pyc

clean-build:
	@rm -fr build/
	@rm -fr dist/
	@rm -fr .eggs/
	@find . -name '*.egg-info' -exec rm -fr {} +
	@find . -name '*.egg' -exec rm -f {} +

clean-pyc:
	@find . -name '*.pyc' -exec rm -f {} +
	@find . -name '*.pyo' -exec rm -f {} +
	@find . -name '*~' -exec rm -f {} +
	@find . -name '__pycache__' -exec rm -fr {} +

clean-image-files:
	@find . -name '*.png' -exec rm -f {} +
	@find . -name '*.jpg' -exec rm -f {} +

api:
	uvicorn experimental_data_digitalization.api.fast:app --reload

streamlit:
	streamlit run frontend/app.py
