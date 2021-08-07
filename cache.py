import pymongo
import json

with open("json/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

cpath = "release"
if config["debug_mode"]:
    cpath = "debug"

# Connecting the database
db_client = pymongo.MongoClient("mongodb+srv://{}:{}@{}/db?retryWrites=true&w=majority".format(config["db_username"], config["db_password"], config["cluster_url"]))
db = db_client[config[cpath]["db_name"]]
print("Database connected.")

class Collection:
    def __init__(self, collection):
        self.collection = db[collection]
        self.cached = {}

    def add(self, id, data): # Add a new key to document
        idict = {"_id": id}
        self.collection.update_one(idict, {"$set": data}, upsert=True)
        if not id in self.cached:
            self.cached[id] = {}
        for i in data:
            self.cached[id][i] = data[i]

    def remove(self, id): # Remove a document
        idict = {"_id": id}
        self.collection.delete_one(idict)
        del self.cached[id]

    def delete(self, id, data): # Remove a key from document
        idict = {"_id": id}
        self.collection.update_one(idict, {"$unset": data})
        for i in data:
            del self.cached[id][i]

    def load_data(self): # Load data from each document in collection
        results = self.collection.find({})
        for res in results:
            self.cached[res["_id"]] = res
        return self.cached

test = Collection(collection = "test") # Collection name in database
testdata = test.load_data()