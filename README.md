# SpyCloud Simple Login App

### Notes
* Additional hash functions needed to be added
* Passwords are not being checked against a database, only the SpyCloud API


### Alternative implementation notes
Ideally I would have created this application using a Flask API with a Vue.JS frontend. I typically prefer to split the web application from the backend calls. That said, for a simple app like this one, purely Flask was sufficient.

### Run Instructions
Setup (Windows)
```cmd
python -m venv venv
 .\venv\Scripts\activate
pip install -r requirements.txt
```
Setup (Linux)
```cmd
python -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```

Start Flask from main directory
```cmd
python run.py
```