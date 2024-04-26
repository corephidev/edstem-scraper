from selenium import webdriver 
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options

from bs4 import BeautifulSoup

import os, time

baseUrl = input("Edstem course URL: ")
username = input("Username/email: ")
password = input("Password: ")

options = Options()
# options.add_argument("headless")
# options.add_argument("--start-minimized")

with webdriver.Chrome(options=options, service=ChromeService(ChromeDriverManager().install())) as driver: 
    driver.get(baseUrl)

    # Handle login

    email_field_present = EC.presence_of_element_located((By.NAME, 'email'))
    WebDriverWait(driver, 10).until(email_field_present)

    time.sleep(1)
    
    email_field = driver.find_element(By.NAME, 'email')
    email_field.send_keys(username)

    email_btn = driver.find_element(By.CLASS_NAME, 'start-btn')
    email_btn.click()

    # Handle password

    password_field_present = EC.presence_of_element_located((By.NAME, 'password'))
    WebDriverWait(driver, 10).until(password_field_present)

    time.sleep(1)
    
    password_field = driver.find_element(By.NAME, 'password')
    password_field.send_keys(password)

    password_btn = driver.find_element(By.CLASS_NAME, 'start-btn')
    password_btn.click()

    # Handle loading all elements

    time.sleep(10)

    show_more_buttons = driver.find_elements(By.CLASS_NAME, "dtl-group-more")

    for btn in show_more_buttons:
        btn.click()
        time.sleep(1)

    time.sleep(10)
    
    load_more_buttons = driver.find_elements(By.CLASS_NAME, "dtl-load-more")

    exhaustion_count = 0

    while len(load_more_buttons) > 0 and exhaustion_count < 15:
        for btn in load_more_buttons:
            btn.click()
            time.sleep(1)
        time.sleep(2)
        load_more_buttons = driver.find_elements(By.CLASS_NAME, "dtl-load-more")
        exhaustion_count += 1

    print("Loaded all threads!")

    threadLinks = driver.find_elements(By.CLASS_NAME, "dtl-thread")

    urls = []

    for link in threadLinks:
        is_private = "hidden" in link.find_element(By.CLASS_NAME, "dft-body").find_element(By.CLASS_NAME, "dft-type-icon").get_attribute("class")
        if is_private:
            continue
        urls.append(link.get_attribute("href"))

    print(f"Reading {len(urls)} page sources...")

    names = []

    for url in urls:
        driver.get(url)
        time.sleep(3)
        source = driver.page_source

        soup = BeautifulSoup(source, 'html.parser')
        for name in soup.find_all(class_="disthrb-user-name"):
            print(name.get_text())
            names.append(name.get_text())
        for name in soup.find_all(class_="discom-user-name"):
            print(name.get_text())
            names.append(name.get_text())
    
    f = open(input("Filename: "), "w")
    f.write("\n".join(names))
    f.close()
