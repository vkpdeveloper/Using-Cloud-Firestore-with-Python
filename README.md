# Using-Cloud-Firestore-with-Python

<img src="https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcQKK8cOQP97pHWFTndmRcLQoR5cvSoL3SVprpD1OikA3dRqRUTy&s" width=1050 heigth=525>

## What is Cloud Firestore

Cloud Firestore is a flexible, NoSQL, scalable database for mobile, web, and server development from Firebase and Google Cloud Platform.

## Why use Firestore with Python

Firestore is serverless NoSQl database in which data stored in collection of documents and the things that we store in Firestore is stored in the form of key value pair's. So it the good to for python developers to use it in major projects. It is so cheap and it works more faster then MySql. It is compatible like MongoDB.

## How to connect Firestore with Python

First of all you want to go to console.cloud.google.com and then make a project and enable the billing for this project and then go to IAM & Admin and then go for serviceAccount and export the json file and copy it in the main directory of project and follow the below code :- 

```python
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

crud = credentials.Certificate('ServiceAccount.json')
firebase_admin.initialize_app(crud)

db = firestore.client()
```

## Requirement for Firestore

1. firebase-admin

## How to setup Virtual Environment

Fire the command in CMD or Terminal (Powershell also Bro 🤣🤣)

```python
pip install virtualenv
```

then restart the terminal and go and fire below command

```python
virtualenv your_env_name
```

It will create a Python virtual env which is used the prefix of your already installed python 3 or 2.

Thanks for comming here. I think it helps you alot in your project.
