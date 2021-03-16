import logging
import azure.functions as func
import pymongo

def main(IoTHubMessages: func.EventHubEvent):
    uri = "mongodb://mongo-cosmos-iot:yIecXn1WU0PxPqmnUlUvHJfvMb9vQpWXDLnvRs6ns5VPgjwNoe6R3uRcAyGubNPlLR06clEhxNzLmk52IOP7kw==@mongo-cosmos-iot.mongo.cosmos.azure.com:10255/?ssl=true&retrywrites=false&replicaSet=globaldb&maxIdleTimeMS=120000&appName=@mongo-cosmos-iot@"
    client = pymongo.MongoClient(uri)
    logging.info('Request: %s' % IoTHubMessages.get_body())
    numero = IoTHubMessages.metadata['messageId']
    temperature = IoTHubMessages.metadata['Temperature']
    humidity = IoTHubMessages.metadata['Humidity']
    logging.info('messageId: %s' % numero)
    logging.info('Temperature: %s' % temperature)
    logging.info('Humidity: %s' % humidity)

    mydb = client["info_ecg"]
    mycol = mydb["ecg"]

    newItem = { 
        "_id": numero,
        "id_ecg": numero,
        "T": temperature,
        "H": humidity 
        }

    insert_item = mycol.insert_one(newItem)
