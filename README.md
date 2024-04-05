# Bursary Scraper Documentation

## Introduction

The Bursary Scraper is a Python-based web scraping tool designed to extract links to open bursaries from the Graduates24 website. The scraper utilizes Selenium for web automation, BeautifulSoup for HTML parsing, and custom utility classes for handling dates and file operations.

## Installation

To use the Bursary Scraper, ensure you have the required dependencies installed. You can install them using the following command:

```bash
pip install -r requirements.txt
```

## Usage

### 1. Scraper Configuration

Adjust the scraper's configuration by modifying the `source/scaper.py` file. Key configuration parameters include:

- `NUMBER_OF_PAGES_TO_SEARCH`: Set the number of pages to search for open bursaries.
- `OPTIONS`: Configure Chrome options, such as running in headless mode.

### 2. Executing the Scraper

To execute the scraper, run the `source/run.py` script:

```bash
python run.py
```

This script initializes the scraper and triggers the extraction process.

### 3. Result Storage

The extracted open bursary links are stored in the `data/open_bursaries_links` file. Each link is appended to a new line in the file.

## Scraper Workflow

### 1. Web Scraping

The `Scraper` class in `source/scaper.py` handles the web scraping process. It navigates through the specified number of pages on the Graduates24 website, extracts bursary information, and filters open bursaries based on their posted date.

### 2. Filtering by Posted Date

The `filter_bursaries_by_posted_date` method checks the posted date of each bursary. Bursaries posted on or after the specified start date (e.g., "01 January 2023") are considered.

### 3. Checking Bursary Status

The `is_bursary_open` method further verifies the status of each open bursary by visiting its individual page. It extracts the closing date and compares it with the current date to determine if the bursary is still open.

### 4. Result Storage

Open bursary links are stored in the `data/open_bursaries_links` file using the `FileUtilities` class in `source/file_utils.py`.

## Utility Classes

### 1. DateUtilities

The `DateUtilities` class in `source/date_utils.py` provides functions for handling date-related operations. It includes methods to get today's date, check if one date is greater than or equal to another, and convert string dates to datetime objects.

### 2. FileUtilities

The `FileUtilities` class in `source/file_utils.py` offers a method for appending data to a specified file. In this case, it is used to store open bursary links.
