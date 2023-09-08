#!/usr/bin/env python3
"""Script that provides some stats about Nginx logs stored in MongoDB"""

from pymongo import MongoClient

def main():
    # Connexion à la base de données MongoDB
    with MongoClient("mongodb://localhost:27017/") as client:
        db = client["logs"]
        collection = db["nginx"]

        # Nombre total de logs
        total_logs = collection.count_documents({})

        # Méthodes HTTP et leurs comptages
        methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
        method_counts = {method: collection.count_documents({"method": method}) for method in methods}

        # Comptage spécifique selon les critères
        specific_criteria_count = collection.count_documents({"method": "GET", "path": "/status"})

        # Affichage des résultats
        print(f"{total_logs} logs")
        print("Methods:")
        for method in methods:
            print(f"\tMethod {method}: {method_counts[method]}")
        print(f"{specific_criteria_count} status check")

if __name__ == "__main__":
    main()
