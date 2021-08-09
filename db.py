import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore


def init_db():
    cred = credentials.Certificate('service_account.json')
    firebase_admin.initialize_app(cred)


init_db()
db = firestore.client()
