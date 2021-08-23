import firebase_admin
from firebase_admin import credentials
from firebase_admin import firestore

def data_base(collection):
    cred = credentials.Certificate("firestorekey.json")
    firebase_admin.initialize_app(cred)
    db = firestore.client()
    return db.collection(collection)


def addUser(user):
    #return usersDB.document().set(user)
    return usersDB.add(user)


def updateUser(user, id):
    return usersDB.document(id).update(user)


def deleteUser(id):
    return usersDB.document(id).delete()


def getUserById(id):
    return usersDB.document(id).get().to_dict()


def listUser():
    #return usersDB.get()
    #return usersDB.where("age", ">", 40).get()
    #return usersDB.where("age", ">", 30).get()
    #return usersDB.where("age", "<", 10).get()
    return usersDB.where("age", ">", 10).where("age", "<", 40).get()
 
 
usersDB = data_base("users")
user = {"firstName":"Rafael", "lastName":"Coutinho","age":34}

#addUser(user)
#updateUser(user,"s6z524XreTGDSBtAmBIM")
#deleteUser("9CZTF8DAopMg1VZaZbNz")
#print(getUserById("3QVo2JIFafJQOdwTaAVK"))
users = listUser()
for u in users:
    print(u.to_dict())
