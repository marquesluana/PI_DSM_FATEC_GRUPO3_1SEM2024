from pymongo import MongoClient
import pymongo

from Ferteliz.settings import MONGODB_SETTINGS

#def get_db():
 #   client = MongoClient('mongodb://localhost:27017/')
  #  db = client['Ferteliz_DataBase']
   # return db

def get_db():
    client = pymongo.MongoClient(
        host=MONGODB_SETTINGS['host'],
        port=MONGODB_SETTINGS['port'],
        username=MONGODB_SETTINGS['username'],
        password=MONGODB_SETTINGS['password'],
        authSource=MONGODB_SETTINGS['authentication_source']
    )
    return client['Ferteliz_DataBase']