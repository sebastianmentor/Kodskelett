# Code Template!

This repo is intendend to work as a base template for an assignment in a webdevelopment course! 

## Setup
Setup a empty folder and either navigate to that folder and skip path or paste the path to that folder in <path>
```bash
git clone https://github.com/sebastianmentor/Kodskelett.git <path>
```

### envrionment
Create a environment at the project level!
```bash
py -m venv my_environment
```
Activate it
```bash
.\venv\Scripts\activate
```
Install requirements
```bash
pip install -r requirements.txt
```

Create a .env file 
```python
# Databses
LOCAL_DATABASE_URI = "sqlite:///staff.db"
```

Run app:
```bash
py app.py
```
