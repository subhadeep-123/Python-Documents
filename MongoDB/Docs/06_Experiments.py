from pymongo import MongoClient, errors
import logging
import gc
import datetime

logger = logging.getLogger(__name__)
logger.setLevel(10)
logging.basicConfig(level=10)
try:
    client = MongoClient('localhost', 27017)
except errors.ConnectionFailure as ef:
    logger.exception(ef)
except errors.ServerSelectionTimeoutError as sste:
    logger.exception(sste)
else:
    logger.debug("[CONNECTED TO MONGO CLIENT]")


db = client.OpenUp
col = db.records


class ToDatabase:
    def __init__(self, major: int, minor: int) -> None:
        self.major = major
        self.minor = minor
        self.timestamp = str(datetime.datetime.now())

    def insert_data(self) -> None:
        data = {
            'Major': self.major,
            'Minor': self.minor,
            'Timestamp': self.timestamp
        }
        data_id = col.insert_one(data).inserted_id
        logger.debug(f'[DATA INSERTED] - object_id - {data_id}')
        gc.collect()

    def exists(self):
        # if col.find({'Email': {"$in": self.email}}).count() > 0: # For If self.email is an array
        if col.find({'Major': self.major, 'Minor': self.minor}).count() > 0:
            logger.debug(f'[DOCUMENT EXISTS] - {self.major}-{self.minor}')
        else:
            logger.debug(
                f'[DOCUMENT DOES NOT EXISTS] - {self.major}-{self.minor}')
            self.insert_data()

    @staticmethod
    def fetch_data_from_db() -> None:
        for data in col.find():
            print(data)

    @staticmethod
    def drop_col() -> None:
        col.drop()
        if 'one' not in db.list_collection_names():
            logger.debug("[SUCESSFULLY DROPPED COLLECTION]")


# Helper Function
def main():
    majors = ['00', '01', '02', '03', '04', '05', '06', '07', '08', '09', '10']
    minors = ['21', '22', '22', '21', '23', '21', '22', '22', '21', '23', '30']
    for i in range(len(majors)):
        obj = ToDatabase(majors[i], minors[i])
        obj.exists()
        # obj.insert_data()

    obj.fetch_data_from_db()
    # obj.drop_col()
    # print(db.list_collection_names())


if __name__ == '__main__':
    main()
