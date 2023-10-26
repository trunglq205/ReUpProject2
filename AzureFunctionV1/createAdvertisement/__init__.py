import azure.functions as func
import pymongo

def main(req: func.HttpRequest) -> func.HttpResponse:

    request = req.get_json()

    if request:
        try:
            url = "mongodb://myazurecomosdbtrunglq9:2ORbEKnDHrvxmszfS5STBbmMsUB5qxxK4spPkLCPRfOfVkoDUJFZDldHRkf7Y9NbABwObJpKHSLuACDbPJG19A==@myazurecomosdbtrunglq9.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@myazurecomosdbtrunglq9@"
            client = pymongo.MongoClient(url)
            database = client['trunglq9database']
            collection = database['advertisements']

            rec_id1 = collection.insert_one(eval(request))

            return func.HttpResponse(req.get_body())

        except ValueError:
            print("could not connect to mongodb")
            return func.HttpResponse('Could not connect to mongodb', status_code=500)

    else:
        return func.HttpResponse(
            "Please pass name in the body",
            status_code=400
        )