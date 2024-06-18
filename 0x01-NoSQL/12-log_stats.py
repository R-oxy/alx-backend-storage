#!/usr/bin/env python3
"""
Provides some stats about Nginx logs stored in MongoDB:
- Displays total number of logs
- Displays counts for each HTTP method (GET, POST, PUT, PATCH, DELETE)
- Displays count for logs with method=GET and path=/status
"""

from pymongo import MongoClient


def log_stats(mongo_collection):
    """ Provides stats about Nginx logs stored in MongoDB """
    total_logs = mongo_collection.count_documents({})
    print(f"{total_logs} logs")

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")
    for method in methods:
        count = mongo_collection.count_documents({"method": method})
        print(f"\tmethod {method}: {count}")

    status_check_count = mongo_collection.count_documents({"method": "GET", "path": "/status"})
    print(f"{status_check_count} status check")

if __name__ == "__main__":
    client = MongoClient('mongodb://127.0.0.1:27017')
    db = client.logs
    nginx_collection = db.nginx
    log_stats(nginx_collection)
