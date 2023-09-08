#!/usr/bin/env python3
"""script that provides some stats about Nginx logs stored in MongoDB """

from pymongo import MongoClient

if __name__ == "__main__":
    # Connexion à la base de données MongoDB
    client = MongoClient('mongodb://localhost:27017/')
    db = client.logs
    collection = db.nginx

    # Compter le nombre total de documents dans la collection "nginx"
    documents = collection.count_documents({})
    # Afficher le nombre total de logs
    print(f"{documents} logs")

    print("Methods:")

    for method in ["GET", "POST", "PUT", "PATCH", "DELETE"]:
        # Compter le num de doc pour chaque méthode
        method_count = collection.count_documents({"method": method})
        print(f"\tmethod {method}: {method_count}")

    # Compter le num de logs avec méthode GET et chemin /status
    status_check_count = collection.count_documents({"$and": [{"path": "/status"}, {"method": "GET"}]})
    print(f"{status_check_count} status check")

    client.close()
