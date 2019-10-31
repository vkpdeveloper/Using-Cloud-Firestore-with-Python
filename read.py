from crud import *

# Read Data

users_ref = db.collection(u'collection_id')
docs = users_ref.stream()

for doc in docs:
    print(u'{} => {}'.format(doc.id, doc.to_dict()))