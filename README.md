# technica15
Technica Hack Project

Requirements:
* Python 2.7 - http://www.python.org
* pip - http://pip.readthedocs.org/en/latest
* virtualenv - http://virtualenv.readthedocs.org/en/latest
* Flask 

Setup Steps: 
* Pip (see below in Notes)
* Once pip is installed, in terminal run: sudo pip install virtualenv
* Create virtual environment, run: virtualenv --no-site-packages venv
* Start virtual environment, run: 
	- For Mac / Unix: source venv/bin/activate
	- For Windows: source bin/activate
* Install Flask, run: pip install flask
* Start Development Server, run: python app.py
	- Open a new browser window and go to: localhost:5000


Notes:
* Most recent version of pip (as of Nov 15) is included in project directory
	- If you don't have pip installed, open terminal, cd into your project directory and run: python get-pip.py
	- If you get a permission error, run: sudo python get-pip.py

