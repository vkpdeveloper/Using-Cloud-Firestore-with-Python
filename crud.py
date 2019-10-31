# How to Connect with Cloud Firestore

import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

crud = credentials.Certificate('ServiceAccount.json')
firebase_admin.initialize_app(crud)

db = firestore.client()