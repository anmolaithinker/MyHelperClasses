import pymongo
import pprint
from pymongo import MongoClient
import pprint
from bson.objectid import ObjectId
import pandas as pd
import requests
from bs4 import BeautifulSoup as bs
import numpy as np

import time

class MyMongoDb:
    
    def __init__(self,url,port=27017,username='',password='',dbname=''):
        print '<<<<----------------------Initializing MongoDb Client ------------------------->>>>>'
        
        self.client = MongoClient('mongodb://'+str(username) +':' + str(password) + '@' + str(url)+ '/' + str(dbname))
        self.db = self.client[dbname]
        print self.db
        print 'Database Created Successfully'
        print 'Functions Available : -------'
        print 'db <- getDataBase() - to retrieve database instance '
        print '----------------------------------------------------------------------------------------'
        print 'collection_name <- makeCollection(collection_name)  - to make collection inside database'
        print '----------------------------------------------------------------------------------------'        
        print 'Object_id <- InsertOneIntoCollection(collection_name , object_to_be_inserted) - Make one object insert into collection'
        print '----------------------------------------------------------------------------------------'
        print 'getCollectionNames - getting all names of collection'
        print '----------------------------------------------------------------------------------------'
        print 'findOne(collec_name , object_query) - Finding One from Collection'
        print '----------------------------------------------------------------------------------------'
        print 'TotalInCollection(collectionName)'
        
        
    def getDataBase(self):
        return self.db
    
    def makeCollection(self,collec_name):
        collec_name = self.db[collec_name]
        print 'Successfully Made Collection'
        return collec_name
    
    def InsertOneIntoCollection(self,collec_name , object_data):
        collec_id = collec_name.insert_one(object_data).inserted_id
        print collec_id
        print 'Inserted Successfully'
        return collec_id

    def InsertManyIntoCollection(self,collec_name , object_data):
        collec_id = collec_name.insert_many(object_data)
        print collec_id
        print 'Inserted Successfully'
        return collec_id
    
    
    def getCollectionNames(self,include_system_collection = False):
        names = self.db.collection_names(include_system_collections = include_system_collection)
        return names
    
    def findOne(self,collec_name , object_query = {}):
        result = collec_name.find_one(object_query)
        pprint.pprint(result)
        return result
    
    def getTotalinCollection(self,CollectionName):
        return CollectionName.count()