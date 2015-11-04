from pymongo import MongoClient
from dalmongo import configuration

# get the instance of MongoDB client
client = MongoClient(configuration.MONGODB_HOST, configuration.MONGODB_PORT)

# get the main application database
db = getattr(client, configuration.MONGODB_NAME)