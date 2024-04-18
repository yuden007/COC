import time
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def pets(driver):
  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#pets")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "petTime")))
  element = driver.find_element(By.ID, "petTime")
  text = element.text.split(":")[1].strip()
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    pets =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    pets =  0
  else:
    pets =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(pets)

  print('\nPets: ', round(pets, 2))
  week = int(pets / 10)
  remaining = pets - week * 10
  if remaining > 7 :
      remaining -= 3
  print('Pets(3 potion weekly): ', round(week * 7 + remaining, 2))
