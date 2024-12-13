#!/usr/bin/env python3
from pymongo import MongoClient

def list_all(mongo_collection):
    """
    Lists all documents in a collection.
    
    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object
    
    Returns:
    list: A list of all documents in the collection, or an empty list if no documents are found
    """
    return list(mongo_collection.find())
