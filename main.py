from bs4 import BeautifulSoup
import requests

from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By

form_url = 'google_form'


url = 'rental_website'

options = Options()
options.add_experimental_option("detach", True)

driver = webdriver.Chrome(
    service=Service(ChromeDriverManager().install()), options=options)

res = requests.get(url)
web_page = res.text
soup = BeautifulSoup(web_page, "html.parser")

num_of_pages = int(soup.select_one('.pagination-list').text.split("...")[1])

for page in range(1, num_of_pages+1):
    if page != 1:
        url = f'{url}?currency=EUR&page={page}'

    res = requests.get(url)
    web_page = res.text
    soup = BeautifulSoup(web_page, "html.parser")

    properties_link = [
        link.get("href") for link in soup.select(".css-1sw7q4x a")]
    properties_price = [
        price.text for price in soup.select(".css-10b0gli")]
    properties_location = [
        location.text.split(" - ")[0] for location in soup.select(".css-veheph")]

    driver.get(form_url)
    for house in range(len(properties_location)):
        print(
            f"Processing property {house + 1} out of {len(properties_location)}")
        print(f"Page {page} out of {num_of_pages}")

        address_of_property = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable(
                (By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[1]/div/div/div[2]/div/div[1]/div/div[1]/input')))
        address_of_property.click()
        address_of_property.send_keys(properties_location[house])

        price_of_property = driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/input')
        price_of_property.click()
        price_of_property.send_keys(properties_price[house])

        link_to_property = driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[2]/div[3]/div/div/div[2]/div/div[1]/div/div[1]/input')
        link_to_property.click()
        if properties_link[house].startswith('/d'):
            link_to_property.send_keys(
                f"{url}{properties_link[house]}")
        else:
            link_to_property.send_keys(properties_link[house])

        submit_btn = driver.find_element(
            By.XPATH, '//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
        submit_btn.click()

        back_to_form_btn = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, '/html/body/div[1]/div[2]/div[1]/div/div[4]/a')))
        back_to_form_btn.click()
    driver.close()
