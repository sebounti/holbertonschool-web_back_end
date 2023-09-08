#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB """

import pymongo


client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["logs"]
collection = db["nginx"]

total_logs = collection.count_documents({})

methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
method_counts = {method: collection.count_documents({"method": method
                                                     }) for method in methods}

specific_criteria_count = collection.count_documents({"method": "GET", "path":
                                                                "/status"})


print(f"{total_logs} logs")
print("Methods:")
for method in methods:
    print(f"\tmethod {method}: {method_counts[method]}")
print(f"{specific_criteria_count} status check")
