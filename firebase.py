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
    
mykey={
  "type": "service_account",
  "project_id": os.environ.get('PROJECT_ID'),
  "private_key_id": os.environ.get('PRIVATE_KEY_ID'),
  "private_key": "-----BEGIN PRIVATE KEY-----\nMIIEvgIBADANBgkqhkiG9w0BAQEFAASCBKgwggSkAgEAAoIBAQDkpp37KLTapCQm\nNvudgkzjNTmjslP6LyT70XP8vaZwGML5GLnCtKwx6x0jhxmYQrhto0PTm1CkMRn9\npSxA9Y8/X3Ef1G5xlArLOn5rzbhDrZCz/WdoR5tmepLG9k2vDg9gAyb6a4R9vKa0\ngi1TsJI22dv2WCv69OLZHM/hoqMsSzd5F37rjJKdsl95fQ1Wld+wj9LT2btKYEXm\nR7RuPser3YgJtXJDcYdkBJFogK159Zv9vYQmSCjFXdjFUfhjgz6uBVj/+Vba9xjX\nnyR3bcIwqXhEVCmHvBfnkP60tLVEPd+B6IGEP5P8V61vHsyy7Ia0+JqkBuw9uZYJ\nW9GYg1c5AgMBAAECggEAAbYh7DnkUh0u9S0tosiLn+B6HOFhMbgGb+8BDiizEMXq\nT7DS9gnE5I2rbLYbnu/GuxQVZ7QTAES2i//ZmDiyroTvRmD9aHWvN7nX/vLwtFPj\nh5J06GtGnK7ZGa2apoabUzftAPIfQqpnMKwnUT866mYwhAcqBGIjDC8p7y1V7BAH\ntvYx2cJUz8ogkwOrcY+nNoLdXMr+Tw1YEa9im1YCRkaSn4U6u+RNbN8OTGrLa58M\ncKXsZ2JTPhLvxJmTDYxYNRmj30c9eYsvq5pznbf1qqzhBgTXAMgo3ZnBTvvJkJjx\nVetXSPcaP80aPmrQyQnXcpN7cLe454MvT78Xv+O/MQKBgQD8YUSHTeZAWNFRAnsk\nK4D9TRFcGfWGBznn/jyGBF68ANZgozyHmPk3zZwmQ70amLlArQkRD4lhcmGm5Gc/\nR9ZTgAL+RdF55jenBM24FQZUb9Qmi+eAAud447K5lgLcYitFyMrT8N7tOJEQeGKU\n2HUOmUEI0dp8z1qmQm1aLTuk9wKBgQDn7jeARkKtxSXxZ1Go8/NFRJ2m6qqbbgeD\naxSEekDv0CkIg5WIuoiz7seMDyEGhHphKqfx7pug+NiBccUj1lgfwE6DnidHxGQZ\n1SBlRijvgmYUz1zyfj77Rg8KeZeQABN9SDqnV99CMHkRiybn2LdbnVG/1LK0hv6T\n6q6WUDdJTwKBgQCX5KaM1Fp2cb4QhnC8dR5d1MtU5h65upGkSYP9mJW3ir17TeM5\nLN0ZM7r94Jjob/BWt42UYghpyKBzBFYLZN3eRVYH2NdZCTCHacGyP50epmtFg8Ah\ncB4FyOyg+2LfZonqpw1Df1174iaUhg+2y4uv7JaSi1J2+YjyNVqBAmY6QwKBgEr3\n9XjBPUxuLZWakArM0BXT2CHcOMmFB2izdC5eVh8uahUWc39+zDFdPaNIQKSarfQ6\nlY7eUe/2gAVXgSHUZyfcQYTJ2miYUsMG4THbO+Avhk+zt5eqtzEBtFrucs9ZNvOI\nJW1yOfhrMrc5A5ptstcqQwJ+/kTcXe3yLfzocPaBAoGBALKUeOoYCt94Vn0H2ntK\n8MMME1PzI/jECfLLtxXF/43lEwaAcC6SF8ng+Qy6y0/SH2iShnGr5zgb5dJvO0jr\ny0JjqSUpqtrMsDqaoO2B3cxLzIccfAxe34L4m0OR1kwQLfm3hcO/MeDk3Zamn3i4\n72T/lZkxlpQlT5/XxiiStB3D\n-----END PRIVATE KEY-----\n",
  "client_email": os.environ.get('FIREBASE_CLIENT_EMAIL'),
  "client_id": os.environ.get('CLIENT_ID'),
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



def insert(first,last,age): #function for inserting to DB
  doc_ref = db.collection(u'students').document(first)
  student = Student(first,last,age)
  doc_ref.set(student.to_dict())
