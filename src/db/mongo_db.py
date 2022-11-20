import logging
import ulid

from datetime import datetime
from pymongo import MongoClient
from src.common.settings import InfoMsgs, Config


class MongoDatabase:
    def __init__(self):
        """
        Initialize the database connection
        """
        self.app = Config.MONGO_APP
        self.link = Config.MONGO_LINK
        self.db_pass = Config.MONGO_PASS
        self.client = MongoClient(self.app + self.db_pass + self.link)

        # TODO: Change these below to the real db and collection names
        self.db = self.client.typerspace
        self.user_collection = self.db.users
        self.stats_collection = self.db.stats

        logging.basicConfig(format="%(asctime)s %(message)s")

    def exception_handler(self, func):
        """
        Decorator to handle exceptions in the database
        :param func: function to be decorated
        :return: decorated function
        """

        def inner_function(*args, **kwargs):
            try:
                func(*args, **kwargs)
            except Exception as e:
                print(f"Caught error in function: {func.__name__}. Error: {e}")

        return inner_function

    @exception_handler
    def store_user(self, data) -> None:
        """
        Stores user data in the database
        :param data: user data to be stored
        :return: None
        """
        user_name = data.get("name")
        user_email = data.get("email")
        current_timestamp = datetime.now()
        user_id = ulid.new().str

        if self.user_collection.find({"name": user_name}).count() == 0:
            self.user_collection.insert_one(
                {
                    "user_id": user_id,
                    "name": user_name,
                    "email": user_email,
                    "created_timestamp": current_timestamp,
                }
            )
            logging.info(
                InfoMsgs.user_added_to_db.format(name=user_name, email=user_email)
            )

        else:
            logging.info(
                InfoMsgs.user_already_in_db.format(name=user_name, email=user_email)
            )

    @exception_handler
    def retrieve_user(self, id) -> dict:
        """
        Retrieves user data from the database
        :param id: user id to be retrieved
        :return: user data
        """
        return self.user_collection.find_one({"user_id": id})

    @exception_handler
    def retrieve_stats(self, id) -> dict:
        """
        Retrieves user stats from the database
        :param id: user id to be retrieved
        :return: user stats
        """
        return self.stats_collection.find_one({"user_id": id})

    @exception_handler
    def update_stats(self, id, stats):
        """
        Updates user stats in the database
        :param id: user id to be updated
        :param stats: user stats to be updated
        :return: None
        """
        self.stats_collection.update_one({"user_id": id}, {"$set": stats})

    @exception_handler
    def store_stats(self, id, stats):
        """
        Stores user stats in the database
        :param id: user id to be stored
        :param stats: user stats to be stored
        :return: None
        """
        self.stats_collection.insert_one({"user_id": id, **stats})
