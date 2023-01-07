import pymongo


client = pymongo.MongoClient("mongodb+srv://ineuron:khushi123@cluster0.ql94anu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

data = {
    "name":"preeti",
    "mail_id":"preeti5@gmail.com",
    "subject":["data science","big data","data analytics"]
}

db1 = client['mogotest']
coll = db1['test']
coll.insert_one(data)

