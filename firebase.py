import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
import os
class Student(object):
    def __init__(self, first, last, born):
        self.first = first
        self.last = last
        self.age = born

    def to_dict(self):
        return self.__dict__
pkey=os.environ['FIREBASE_PRIVATE_KEY']
mykey={
  "type": "service_account",
  "project_id": "firestudents-7dc4f",
  "private_key_id": "960dc37f43069c2c8fd55f9a6e8e98c6285c8578",
  "private_key": pkey ,
  "client_email": "firebase-adminsdk-qic8w@firestudents-7dc4f.iam.gserviceaccount.com",
  "client_id": "105345324411146928723",
  "auth_uri": "https://accounts.google.com/o/oauth2/auth",
  "token_uri": "https://oauth2.googleapis.com/token",
  "auth_provider_x509_cert_url": "https://www.googleapis.com/oauth2/v1/certs",
  "client_x509_cert_url": "https://www.googleapis.com/robot/v1/metadata/x509/firebase-adminsdk-qic8w%40firestudents-7dc4f.iam.gserviceaccount.com"
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
