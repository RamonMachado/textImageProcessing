
init:
	python -m venv venv
	source venv/bin/activate
	pip install -r requirements.txt

initWindows:
	python -m venv venv
	venv\Scripts\Activate
	pip install -r requirements.txt

activate: 
	source venv/bin/activate

activateWindows:
	venv\Scripts\Activate

deactivate:
	deactivate

delete:
	rm -r venv

deleteWindows:
	rmdir /s venv

run:
	python src/main.py