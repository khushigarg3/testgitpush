import pymongo

client = pymongo.MongoClient("mongodb+srv://ineuron:khushi123@cluster0.ql94anu.mongodb.net/?retryWrites=true&w=majority")
db = client.test
print(db)

database = client['mogotest']
collection = database['test2']
data = [
        {
            "item": "canvas",
            "qty": 100,
            "size": {"h": 28, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "journal",
            "qty": 25,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mat",
            "qty": 85,
            "size": {"h": 27.9, "w": 35.5, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "mousepad",
            "qty": 25,
            "size": {"h": 19, "w": 22.85, "uom": "cm"},
            "status": "P",
        },
        {
            "item": "notebook",
            "qty": 50,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "P",
        },
        {
            "item": "paper",
            "qty": 100,
            "size": {"h": 8.5, "w": 11, "uom": "in"},
            "status": "D",
        },
        {
            "item": "planner",
            "qty": 75,
            "size": {"h": 22.85, "w": 30, "uom": "cm"},
            "status": "D",
        },
        {
            "item": "postcard",
            "qty": 45,
            "size": {"h": 10, "w": 15.25, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketchbook",
            "qty": 80,
            "size": {"h": 14, "w": 21, "uom": "cm"},
            "status": "A",
        },
        {
            "item": "sketch pad",
            "qty": 95,
            "size": {"h": 22.85, "w": 30.5, "uom": "cm"},
            "status": "A",
        },
    ]

#collection.insert_many(data)


# we can convert a table into a dictionary(json) and then dump into nosql also


'''record = collection.find()
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({'item':'mat'})
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({'status':'A'})
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({'qty':80})                               # matching a record to fetch it
for i in record:
    print(i)'''


'''print("\n")
record = collection.find({'status':{'$in':['A','P']}})            # filter data where status is either A or P
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({'status':{'$gt':'C'}})                  # filter data where status is greater than C
for i in record:
    print(i)'''


'''print("\n")
record = collection.find({'qty':{'$gte' :75}})                     # qty is greater than or equal o 75
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({'item': 'sketch pad','qty': 95})
for i in record:
    print(i)'''



'''print("\n")
record = collection.find({ 'item': 'sketch pad' , 'qty' :{"$gte" : 75}})
for i in record:
    print(i)'''




'''print("\n")
record = collection.find({'$or' : [{ 'item': 'sketch pad'} , {'qty': {"$gte": 75}}]})             # either item = sketchpad or qty >= 75
for i in record:
    print(i)'''





# update records - update_one  &  update_many
collection.update_one({'item': 'canvas'} , {'$set':{'item': 'sudhanshu'} })
d = collection.find({'item':'sudhanshu'})
for i in d :
    print(i)



# deleting a record
collection.delete_one({'item': 'sudhanshu'})
d = collection.find({'item':'sudhanshu'})
for i in d :
    print(i)








