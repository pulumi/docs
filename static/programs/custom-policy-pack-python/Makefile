ensure: venv install

venv: requirements.txt
	python -m venv venv

install:
	./venv/bin/pip install -r requirements.txt

test: ensure
	. venv/bin/activate; pytest --spec --disable-warnings policy_tests.py

clean:
	rm -rf venv
	find . -type f -name *.pyc -delete
	find . -type d -name __pycache__ -delete

.PHONY: test ensure 