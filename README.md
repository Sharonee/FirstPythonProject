
virtual environment
____________________


creating a new python virtual environment
python -m venv myenv

Activate the virtual environment
source myenv/bin/activate

Deactivate the Virtual Environment
deactivate

Install Python Packages
________________________

pip3 install pipenv  > For env installation
pipenv install fastapi > For API development
pipenv install uvicorn > 

Store all Packages in the Requirements file: pip freeze > requirments.txt

Install Dev Package > pipeve install --dev pytest

############FAST API ################
need to install 2 packages: fastapi and uvicorn

in order to run the app :  uvicorn main:app --reload
reload is for changing reloded 
and connect via browser to 127.0.0.1:800
for documentation : 127.0.0.1:8000/docs

from fastapi import FastAPI
app = FastAPI()
@app.get("/")
def home():
    return "Hello World"

###############################################

Classes

        self._private_var = "This is a private variable"
        self.__secret_var = "This is a secret variable"

##################################################

