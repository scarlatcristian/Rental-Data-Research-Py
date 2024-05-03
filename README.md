# Rental-Data-Research-Py

## Introduction
This Python script is designed to scrape rental property data from a website and submit it to a Google Form for further processing. It utilizes BeautifulSoup for web scraping and Selenium for web automation.

## Requirements
- Python 3.x
- BeautifulSoup (`bs4`)
- Requests (`requests`)
- Selenium (`selenium`)
- Chrome WebDriver (automatically managed using `webdriver_manager`)
- Google Form URL (to submit the scraped data)

## Setup
1. Install the required Python packages using pip:
   pip install bs4 requests selenium webdriver_manager

2. Ensure that you have Google Chrome installed on your system.

## Usage
1. Update the `url` variable with the URL of the rental website from which you want to scrape data.

2. Update the `form_url` variable with the URL of the Google Form to which you want to submit the data.

3. Run the script. It will scrape rental property data from the specified website, format it, and submit it to the specified Google Form.

## Notes
- The script assumes that the rental website has pagination, and it automatically retrieves data from all pages.
- It extracts property links, prices, and locations from the rental website's HTML structure.
- Ensure that the Google Form fields match the expected input fields for property address, price, and link.
- The script opens a Chrome browser window using Selenium for form submission. Make sure you have a stable internet connection.

## Disclaimer
This script is provided as-is and may require customization based on the specific structure of the rental website and Google Form.
