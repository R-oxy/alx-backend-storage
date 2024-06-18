#!/usr/bin/env python3
""" Returns the list of schools having a specific topic """


def schools_by_topic(mongo_collection, topic):
    """ Retrieve schools by specific topic """
    return mongo_collection.find({"topics": topic})
