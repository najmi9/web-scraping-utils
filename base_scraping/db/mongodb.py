import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["mydatabase"]

dblist = myclient.list_database_names()

if not  "customers" in mydb.list_collection_names():
	mycol = mydb["customers"]
	print("The database does not exists.")

mydict = { "name": "John", "address": "Highway 37" }

x = mycol.insert_one(mydict)

x = mycol.find_one()

print(x)