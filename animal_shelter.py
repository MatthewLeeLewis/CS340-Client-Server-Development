from pymongo import MongoClient
from bson.objectid import ObjectId

class AnimalShelter(object):
    """ CRUD operations for Animal collection in MongoDB """

    def __init__(self, USER, PASS):
        # Initializing the MongoClient. This helps to 
        # access the MongoDB databases and collections.
        # This is hard-wired to use the aac database, the 
        # animals collection, and the aac user.
        # Definitions of the connection string variables are
        # unique to the individual Apporto environment.
        #
        # You must edit the connection variables below to reflect
        # your own instance of MongoDB!
        #
        # Connection Variables
        #
        HOST = 'nv-desktop-services.apporto.com'
        PORT = 32652
        DB = 'aac'
        COL = 'animals'
        self.client = MongoClient('mongodb://%s:%s@%s:%d' % (USER,PASS,HOST,PORT))
        self.database = self.client['AAC']
        self.collection = self.database['%s' % (COL)]
        

# Method to implement the C in CRUD.
    def create(self, data):
        if data is not None:
            self.database.animals.insert_one(data)
        else:
            raise Exception("Nothing to save, because data parameter is empty")

# Method to implement the R in CRUD.
    def read(self, data):
        result = []
        # Verify search input is valid, or throw exception.
        if data is not None:
            query = self.database.animals.find(data)
            for animal in query:
                result.append(animal)
        else:
            raise Exception("Invalid search criteria")
        return result
            
# Method to implement the U in CRUD
    def update(self, query, record):
 
        #Verify record existence
        if record is not None:
            # update and print documents
            result = self.database.animals.update_many(query, { "$set" : record})
            
            print("Data Updated: ")
            return result.raw_result
        else:
            raise Exception("Record not found.")
        
# Method to implement the D in CRUD
    def delete(self, data):
        
        # Verify the record exists before deleting
        if data is not None:
            # delete the matching documents and display how many.
            result = self.database.animals.delete_many(data)
            
            print("Data Deleted: ")
            return result.raw_result
        else:
            raise Exception("Record not found.")
        