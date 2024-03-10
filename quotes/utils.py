from pymongo import MongoClient

def get_mongodb():
    uri = "mongodb+srv://userhw8:<PASS>@atlascluster.dkms1wa.mongodb.net/?retryWrites=true&w=majority&appName=AtlasCluster"

    client = MongoClient(uri)

    db = client.hw9
    return db
