import pymongo

# connecting python with mongodb

# url of cloud server
client = pymongo.MongoClient("mongodb+srv://ineuron:khushi123@cluster0.ql94anu.mongodb.net/?retryWrites=true&w=majority")
db = client.test

print(db)

d = {
    "name":"rohan",
    "email_id":"rohan@gmail.com"
}

# data insertion in mongodb
db1 = client['mogotest']                # database name
coll = db1['test']                      # collection name(same as sql table)
coll.insert_one(d)







