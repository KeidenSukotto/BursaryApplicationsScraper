from selenium import webdriver
from bs4 import BeautifulSoup
from date_utils import DateUtilities
from file_utils import FileUtilities


class Scraper:

    OPTIONS = webdriver.ChromeOptions()
    OPTIONS.add_argument("--headless=new")
    DRIVER = webdriver.Chrome(options=OPTIONS)

    NUMBER_OF_PAGES_TO_SEARCH = 1

    @classmethod
    def number_of_pages_to_search(cls) -> int:
        return cls.NUMBER_OF_PAGES_TO_SEARCH + 1

    @classmethod
    def get_website_markup(cls, url: str) -> str:
        cls.DRIVER.get(url=url)
        cls.DRIVER.implicitly_wait(15)

        return cls.DRIVER.page_source

    @classmethod
    def get_bursaries(cls) -> list:
        data = []
        num_of_pages = cls.number_of_pages_to_search()

        for number in range(1, num_of_pages):
            url = fr"https://graduates24.com/bursaries?page={number}"
            website_markup = cls.get_website_markup(url=url)

            soup = BeautifulSoup(markup=website_markup, features="html.parser")
            bursaries_container = soup.find(name="div", attrs={"class": "col-sm-12 col-md-8 col-sm-8"})

            bursaries = bursaries_container.find_all(name="div", attrs={"class": "job-list"})
            bursaries = [bursary for bursary in bursaries if bursary["class"][0] == "job-list"]

            data = data + bursaries

        return data

    @classmethod
    def filter_bursaries_by_posted_date(cls) -> list:
        bursaries = cls.get_bursaries()
        data = []

        for bursary in bursaries:
            date_tag = bursary.find(name="div", attrs={"class": "meta-tag"})
            date_tag = date_tag.find(name="span")
            bursary_posted_date = date_tag.text.strip()
            bursary_posted_date = bursary_posted_date.replace("Posted:", " ").strip()

            bursary_posted_date = DateUtilities.convert_str_date_to_datetime_object(string_date=bursary_posted_date)
            start_search_date = DateUtilities.convert_str_date_to_datetime_object(string_date="01 January 2023")

            if DateUtilities.is_date_greater_than_or_equal(first_date=bursary_posted_date,
                                                           second_date=start_search_date):
                data.append(bursary)

        return data

    @classmethod
    def is_bursary_open(cls) -> None:
        bursaries = cls.filter_bursaries_by_posted_date()

        for bursary in bursaries:
            bursary_link = bursary.find(name="a")
            bursary_link = bursary_link["href"]

            website_markup = cls.get_website_markup(url=bursary_link)
            soup = BeautifulSoup(markup=website_markup, features="html.parser")

            header_content = soup.find(name="div", attrs={"class": "header-content pull-left"})
            header_content = header_content.text
            header_content = header_content.strip()

            bursary_closing_date = header_content.split(":")[-1].strip()

            try:
                bursary_closing_date = DateUtilities.convert_str_date_to_datetime_object(
                    string_date=bursary_closing_date)

            except ValueError:
                continue

            today_date = DateUtilities.get_today_date()
            today_date = DateUtilities.convert_str_date_to_datetime_object(string_date=today_date)

            if DateUtilities.is_date_greater_than_or_equal(first_date=bursary_closing_date, second_date=today_date):
                FileUtilities.store(data=bursary_link)

    @classmethod
    def execute_scraper(cls) -> None:
        cls.NUMBER_OF_PAGES_TO_SEARCH = 1
        cls.is_bursary_open()

