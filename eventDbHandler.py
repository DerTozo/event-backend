from pymongo import MongoClient
from dotenv import load_dotenv, find_dotenv
import os
import pprint
import random
import datetime

# Important for the deployment command at the bottom
from eventModel import EventModel

printer = pprint.PrettyPrinter()
load_dotenv(find_dotenv())

# Connection to Mongo DB
dbUserPassword = os.environ.get("MONGO_PWD")
dbConnectionString = f"mongodb+srv://TOZO:{dbUserPassword}@wg-hub.6lbdthu.mongodb.net/?retryWrites=true&w=majority"
client = MongoClient(dbConnectionString)

_db = client.Event
collaction = _db.events


class EventDbHandler():

    # In this part the variables random are written
    processors = ["Tomasz", "Finn"]
    rdmProcessor = random.choice(processors)

    colors = ["lightBlue", "purple", "orange", "green", "blue"]
    rdmColor = random.choice(colors)

    creationDates = random.randint(1, 15)
    
    rdmEventId = random.randint(0, 2000000)

    time = datetime.datetime.now()
    fromatTime = time.strftime("%Y-%m-%d %H:%M:%S")

    def insertData(self):
        data = {
            "name": self.name,
            "processor": self.processor,
            "color": self.color,
            "creationDate": self.creationDate,
            "startDate": self.startDate,
            "eventId": self.eventId
        }
        collaction.insert_one(data)

    def fetchAllData():
        data =[]
        for x in collaction.find({}).sort("creationDate"):
            data.append(x)
        return data

    def fetchOneEvent():
        event = collaction.find_one({}, sort=[('creationDate', 1)])
        return event

    # def deleteById(event_id):
    #     from bson.objectid import ObjectId
    #     _id = ObjectId(event_id)
    #     collaction.delete_one({"_id": _id})

    # This is used to write a new event into the database

    # insertModel = EventModel(name="Flur Saugen", processor=rdmProcessor, color=rdmColor, creationDate=creationDates, startDate=fromatTime, eventId=rdmEventId)
    # insertData(insertModel)


