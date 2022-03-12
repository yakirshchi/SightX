import pandas as pd
import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["sites"]
siteNames = ['Alegro_2020_11_24','Nachsholim_2020_11_26','RazHome_2020_11_24','SightxOffice_2020_11_24','YuvalHome_2020_11_25']
zeroFrames = []
siteData = []

for site in siteNames:
    collection = db.site
    for doc in collection.find():
       df = pd.DataFrame(list(doc.find()))
       zeroFrames.append(df.loc[0])
    df = pd.concat(zeroFrames)
    siteData.append(df)
s = pd.concat(siteData, keys=siteNames)
    

# 