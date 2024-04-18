import time
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def building(driver):
  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "defenceTime")))
  element = driver.find_element(By.ID, "defenceTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    defense =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    defense =  0
  else:
    defense =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(defense)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#traps")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "trapTime")))
  element = driver.find_element(By.ID, "trapTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    trap =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    trap =  0
  else:
    trap =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(trap)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#army")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "armyTime")))
  element = driver.find_element(By.ID, "armyTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    army =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    army =  0
  else:
    army =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(army)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#resources")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "resourceTime")))
  element = driver.find_element(By.ID, "resourceTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    resource =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    resource =  0
  else:
    resource =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(resource)
    
  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#heroes")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "heroTime")))
  element = driver.find_element(By.ID, "heroTime")
  text = element.text.split(":")[1].strip()
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    heros =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    heros =  0
  else:
    heros =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(heros)

  totalBuilding = defense + trap + army + resource + heros
  print('\nBuilding(5 builders): ', round((totalBuilding / 5), 2))
  print('Building(6 builders): ', round((totalBuilding / 6), 2))