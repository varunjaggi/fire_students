
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class Student(object):
    def __init__(self, first, last, born):
        self.first = first
        self.last = last
        self.age = born

    def to_dict(self):
        return self.__dict__

# cred = credentials.Certificate("/media/varunjaggi/DriveE/firestudents/firestudents-7dc4f-firebase-adminsdk-qic8w-960dc37f43.json")
# firebase_admin.initialize_app(cred)
firebase_admin.initializeApp({
  credential: admin.credential.cert({
    "private_key": process.env.FIREBASE_PRIVATE_KEY,
    "client_email": process.env.FIREBASE_CLIENT_EMAIL,
  }),
#   databaseURL: "https://firestudents.firebaseio.com"
});

db = firestore.client()
doc_ref = db.collection(u'students').document()


def insert(first,last,age): #function for inserting to DB
  student = Student(first,last,age)
  doc_ref.set(student.to_dict())



