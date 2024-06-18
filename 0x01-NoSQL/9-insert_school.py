#!/usr/bin/env python3
""" Inserts a new document in the collection school """

def insert_school(mongo_collection, **kwargs):
    """ Insert a new document with specified fields """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
