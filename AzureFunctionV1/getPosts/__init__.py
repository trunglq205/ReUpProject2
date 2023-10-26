import logging
import azure.functions as func
import pymongo
import json
from bson.json_util import dumps


def main(req: func.HttpRequest) -> func.HttpResponse:

    logging.info('Python getPosts trigger function processed a request.')

    try:
        url = "mongodb://myazurecomosdbtrunglq9:2ORbEKnDHrvxmszfS5STBbmMsUB5qxxK4spPkLCPRfOfVkoDUJFZDldHRkf7Y9NbABwObJpKHSLuACDbPJG19A==@myazurecomosdbtrunglq9.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myazurecomosdbtrunglq9@"
        client = pymongo.MongoClient(url)
        database = client['trunglq9database']
        collection = database['posts']

        result = collection.find({})
        result = dumps(result)

        return func.HttpResponse(result, mimetype="application/json", charset='utf-8', status_code=200)
    except:
        return func.HttpResponse("Bad request.", status_code=400)