# Add Data

from crud import *

# First Method

number = input("Enter Your Mobile Number : ")
name = input("Enter Your Name : ")
password = input("Enter Your Password : ")

doc_ref = db.collection(u'collection_id').document(number)
doc_ref.set({
    u'name': name,
    u'mobile': number,
    u'password': password
})

# Second Method

doc_ref = db.collection(u'collection_id').document(u'doc_id')
doc_ref.set({
    u'name': name,
    u'mobile': number,
    u'password': password
})