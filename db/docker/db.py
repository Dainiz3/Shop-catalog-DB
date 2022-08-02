from typing import List
from pymongo import MongoClient
from pymongo.collection import Collection
from pymongo.database import Database


class Database:
    def __init__(self, ip_adress: str, port: int, name: str, collection_name: str) -> None:
        self.client = MongoClient(ip_adress, port)
        self.db = self.create_db(name)
        self.collection_name = self.create_collection(collection_name)

    def create_db(self, name: str) -> Database:
        return self.client[name]

    def create_collection(self, collection_name: str) -> Collection:
        return self.db[collection_name]


    def insert(self, record: dict) -> None:
        self.collection_name.insert_one(record)

    def insert_many(self, records: List[dict]) -> None:
        self.collection_name.insert_many(records)

    def read(self, parameters: dict) -> dict:
        return self.collection_name.find_one(parameters)

    def read_many(self, parameters: dict) -> List[dict]: 
        return [x for x in self.collection_name.find(parameters)]

    def update(self, condition: dict) -> None:
        self.collection_name.update_one(condition)
        # TODO check condition statement


    def delete(self, parameters: dict) -> None:
        self.collection_name.delete_one(parameters)

    def delete_all(self) -> None:
        self.collection_name.delete_many({})
    
    def delete_many(self, parameters: dict) -> None:
        self.collection_name.delete_many(parameters)

if __name__=="__main__":
    pass

    # database = Database("localhost", 50000, "berlinki")
    # print(type(database.create_collection("berlinki")))