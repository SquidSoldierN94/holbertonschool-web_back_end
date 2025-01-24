#!/usr/bin/env python3
"""
Module Mongo
"""

def schools_by_topic(mongo_collection, topic):
    """
    Returns the list of schools having a specific topic.

    Parameters:
    mongo_collection (pymongo.collection.Collection): The pymongo collection object
    topic (str): The topic to search for

    Returns:
    list: A list of schools (documents) that have the specified topic
    """
    return list(mongo_collection.find({"topics": topic}))
