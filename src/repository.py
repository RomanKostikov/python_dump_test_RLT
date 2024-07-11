from datetime import datetime

from pymongo import MongoClient


class Repository:

    def __init__(
            self,
            client: MongoClient,
            db_name: str,
    ):
        self.db = client[db_name]

    def get_datas_between_dates(
            self,
            collection_name: str,
            dt_from: datetime,
            dt_upto: datetime,
            include_end_date: bool = False,
    ):
        """
        Метод для получения данных, дата которых, находится между dt_from и dt_upto.
        :param collection_name: название колекции, откуда необходимо взять данные.
        :param dt_from: дата от
        :param dt_upto: дата до
        :param include_end_date: флаг для показания необходимости включения конечной даты.
        :return:
        """
        collection = self.db[collection_name]

        if include_end_date:
            right_border = "$lte"
        else:
            right_border = "$lt"

        return collection.find(
            {"dt": {"$gte": dt_from, right_border: dt_upto}}
        )
