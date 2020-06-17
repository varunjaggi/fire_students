
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
mykey={
    "private_key": process.env.FIREBASE_PRIVATE_KEY,
    "client_email": process.env.FIREBASE_CLIENT_EMAIL,
  }
cred = credentials.Certificate(mykey)
firebase_admin.initialize_app(cred)
# firebase_admin.initialize_app({
#   credential: admin.credential.cert(),
#  #databaseURL: "https://firestudents-7dc4f.firebaseio.com/students/PsV5VWTkfXLevhhhsAIx"
# });

db = firestore.client()
doc_ref = db.collection(u'students').document()


def insert(first,last,age): #function for inserting to DB
  student = Student(first,last,age)
  doc_ref.set(student.to_dict())



