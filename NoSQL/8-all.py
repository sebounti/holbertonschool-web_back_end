#!/usr/bin/python3
'''lists all documents in a collection'''

import pymongo


def list_all(mongo_collection):
    "list all  collection"
    return list(mongo_collection.find())
