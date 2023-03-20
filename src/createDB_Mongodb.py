import pymongo

myclient = pymongo.MongoClient('mongodb://localhost:27017/')

mydb = myclient['mydatabase']
# database created!


dblist = myclient.list_database_names()
if "mydatabase" in dblist:
  print("The database exists.")
else:
  print("The database doesn't exists.")
  

# create a collection = table
mycol = mydb["customers"]
collist = mydb.list_collection_names()
if "customers" in collist:
  print("The collection exists.")
else:
  print("The collection doesn't exists.")
  
# Crea un item:registro en una colección
mydict = { "name": "John", "address": "Highway 37" }
x = mycol.insert_one(mydict)

mydict = { "name": "Peter", "address": "Lowstreet 27" }
x = mycol.insert_one(mydict)
print(x.inserted_id)


