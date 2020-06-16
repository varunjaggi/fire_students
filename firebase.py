
import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore
class Student(object): #class for student
    def __init__(self, first, last, born):
        self.first = first
        self.last = last
        self.age = born

    def to_dict(self): #function to convert attributes to a dictionary
        return self.__dict__

cred = credentials.Certificate("/media/varunjaggi/DriveE/firestudents/firestudents-7dc4f-firebase-adminsdk-qic8w-960dc37f43.json")
firebase_admin.initialize_app(cred)
db = firestore.client() # connection for Firebase
doc_ref = db.collection(u'students').document() # creating a reference for the collection/document


def insert(first,last,age): #function for inserting to DB
  student = Student(first,last,age)
  doc_ref.set(student.to_dict())



