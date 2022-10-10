init:
	pip3 install --trusted-host pypi.python.org --trusted-host pypi.org -r requirements.txt


test:
	nosetests tests