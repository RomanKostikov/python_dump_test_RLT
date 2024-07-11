import calendar
from datetime import datetime


class InteractionWithDate:
    @staticmethod
    def increment_hour(date: datetime) -> datetime:
        """
        Добавить 1 час к дате.
        :param date:
        :return:
        """
        if date.hour == 23:
            return date.replace(day=date.day + 1, hour=0)

        return date.replace(hour=date.hour + 1)

    @staticmethod
    def increment_day(date: datetime) -> datetime:
        """
        Добавить 1 день к дате.
        :param date:
        :return:
        """
        if (
                (date.month in [1, 3, 5, 7, 8, 10, 12] and date.day == 31) or
                (date.month in [4, 6, 9, 11] and date.day == 30) or
                (
                        date.year == 28
                        and date.month == 2
                        and not calendar.isleap(date.year)
                )
        ):
            return date.replace(month=date.month + 1, day=1)

        return date.replace(day=date.day + 1)

    @staticmethod
    def increment_month(date: datetime) -> datetime:
        """
        Добавить 1 месяц к дате.
        :param date:
        :return:
        """
        if date.month == 12:
            return date.replace(year=date.year + 1, month=1)

        return date.replace(month=date.month + 1)

    @staticmethod
    def increment_date(date: datetime, group_type: str) -> datetime:
        """
        Инкрементировать дату в зависимости от типа.
        :param date:
        :param group_type: string with value "hour", "day" or "month"
        :return:
        """
        if group_type == "hour":
            return InteractionWithDate.increment_hour(date)
        elif group_type == "day":
            return InteractionWithDate.increment_day(date)
        elif group_type == "month":
            return InteractionWithDate.increment_month(date)
        else:
            raise ValueError("group_type must be hour, day or month")
