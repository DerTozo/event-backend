from flask import Flask
from bson import json_util
from flask_restful import Api
from eventDbHandler import EventDbHandler

app = Flask(__name__)
api = Api(app)


@app.route("/fetchAllEvents", methods=['GET'])
def getEvents():
    events = EventDbHandler.fetchAllData()
    json_data = json_util.dumps(events)
    return json_data


@app.route("/fetchOneEvent", methods=['GET'])
def getEvent():
    events = EventDbHandler.fetchOneEvent()
    json_data = json_util.dumps(events)
    return json_data


if __name__ == "__main__":
    app.run(debug=False)