import csv
from pymongo import MongoClient

# MongoDB connection URI
uri = "mongodb+srv://agustinsso:1234@cluster0.tbwegic.mongodb.net/?retryWrites=true&w=majority"

# Name of the target database and collection
database_name = "conaf_reports"
collection_name = "reports"

# Path to the CSV file
csv_file_path = "csv.csv"

# Create a new client and connect to the MongoDB server
client = MongoClient(uri)

# Access the target database and collection
db = client[database_name]
collection = db[collection_name]

# Read the CSV file and insert its contents into the collection
with open(csv_file_path, "r") as file:
    reader = csv.DictReader(file)
    data = list(reader)
    collection.insert_many(data)

# Close the MongoDB connection
client.close()
