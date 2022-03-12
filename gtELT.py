import json, os
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sites"]
gtPath = r'C:\Users\YAKIRSHCHIGELSKI\Documents\MyLearning\playground\python_scripts\SightX\groundTruth'

for d in os.scandir(gtPath):
    if d.is_dir():
        jsonDirPath = gtPath + '//' + d.name
        collection = db[d.name]  
        for f in os.scandir(jsonDirPath):
            if f.is_file() and f.name.endswith(".json"):
                jsonFilePath = jsonDirPath + '//' + f.name
                with open(jsonFilePath) as j:
                    data = json.load(j)
                    x = collection.insert_one(data)
                    
    
    

