from datetime import datetime


class DateUtilities:

    @staticmethod
    def get_today_date() -> str:
        date = datetime.now().date().strftime("%d %B %Y")
        return date

    @staticmethod
    def is_date_greater_than_or_equal(first_date, second_date) -> bool:
        return first_date >= second_date

    @staticmethod
    def convert_str_date_to_datetime_object(string_date):
        return datetime.strptime(string_date, "%d %B %Y").date()
