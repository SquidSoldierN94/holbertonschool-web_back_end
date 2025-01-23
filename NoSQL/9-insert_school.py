#!/usr/bin/env python3

def insert_school(mongo_collection, **kwargs):
    """
    Inserts a new document in a collection based on kwargs.
    
    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object
    kwargs: The key-value pairs to insert as the document
    
    Returns:
    ObjectId: The _id of the inserted document
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
