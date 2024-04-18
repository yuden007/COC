import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from building import building
from research import research
from pets import pets

import time

name = input("Name: ")
passw = input("Pass: ")

service = Service(executable_path="chromedriver.exe")
driver = webdriver.Chrome(service=service)

driver.get("https://www.clash.ninja/login")
wait = WebDriverWait(driver, 10)
wait.until(EC.visibility_of_element_located((By.ID, "cphBody_txtUsername")))
username = driver.find_element(By.ID, "cphBody_txtUsername")
username.send_keys(name, Keys.ENTER)
password = driver.find_element(By.ID, "cphBody_txtPassword")
password.send_keys(passw, Keys.ENTER)

building(driver)
research(driver)
pets(driver)

driver.quit()