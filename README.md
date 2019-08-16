# The Werewolf Web App
goTenna internal werewolf web app!

## Getting started (for Linux/Mac OS)
### 1. Install virtualenv
```
$ pip install virtualenv
```

### 2. Activate your virtualenv
```
$ virtualenv venv
$ source venv/bin/activate
```

### 3. Run requirements.txt
```
pip install -r requirements.txt
```

### 4. Export the run.py to a variable
```
$ export FLASK_APP=run.py
```

### 5. Run the App
```
$ flask run
```
Go to the IP address that shows up on the terminal and you should see the Flask web App!

### To deactivate the virtual env:
```
$ deactivate
```
