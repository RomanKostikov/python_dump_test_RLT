import json
from datetime import datetime

from pymongo import MongoClient

from .repository import Repository
from .config import db_settings
from .interaction_with_date import InteractionWithDate
from .schemas import InputDatasSchema, OutputDatasSchema


class Service:

    def __init__(self):
        self.repository: Repository = Repository(
            client=MongoClient(db_settings.db_connection_string),
            db_name=db_settings.db_name,
        )

    def get_datas_from_db(
            self,
            input_data: InputDatasSchema
    ) -> OutputDatasSchema:
        """
        Метод для получения статистических данных о зарплатах.
        :param input_data:
        :return:
        """
        dataset = []
        labels = []

        include_end_date = False
        interval_begin = input_data.dt_from
        interval_end = InteractionWithDate.increment_date(
            interval_begin,
            input_data.group_type
        )

        while interval_begin <= input_data.dt_upto:
            get_sum = self.get_sum_in_interval(
                interval_begin,
                interval_end,
                include_end_date
            )

            dataset.append(get_sum[0])
            labels.append(get_sum[1])

            interval_begin = interval_end
            interval_end = InteractionWithDate.increment_date(
                interval_begin,
                input_data.group_type
            )

            if interval_end > input_data.dt_upto:
                if include_end_date:
                    break

                interval_end = input_data.dt_upto
                include_end_date = True

        return OutputDatasSchema(
            dataset=dataset,
            labels=labels
        )

    def get_sum_in_interval(
            self,
            interval_beginning: datetime,
            interval_end: datetime,
            include_end_date: bool,
    ) -> tuple[int, str]:
        """
        Метод для посчёта суммы между датами.
        :param interval_beginning:
        :param interval_end:
        :param include_end_date:
        :return:
        """
        amount_of_payment = 0
        datas = self.repository.get_datas_between_dates(
            collection_name="sample_collection",
            dt_from=interval_beginning,
            dt_upto=interval_end,
            include_end_date=include_end_date,
        )
        for data in datas:
            amount_of_payment += data["value"]

        return amount_of_payment, f'"{interval_beginning.isoformat()}"'

    @staticmethod
    def get_input_data(row_input_data: str) -> InputDatasSchema:
        """
        Метод для преобразования строкового представления входных данных в объект InputDataSchema.
        :param row_input_data:
        :return:
        """
        input_data = json.loads(row_input_data)
        return InputDatasSchema(**input_data)
