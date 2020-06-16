
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

cred = credentials.Certificate("/media/varunjaggi/DriveE/firestudents/firestudents-7dc4f-firebase-adminsdk-qic8w-960dc37f43.json")
firebase_admin.initialize_app(cred)


db = firestore.client()

doc_ref = db.collection(u'students').document(u'bestfriend')
doc_ref.set({
    u'first': u'bob',
    u'last': u'x',
    u'age': 42
})