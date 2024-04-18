import time
import re
from selenium import webdriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

def research(driver):
  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#troops")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "troopTime")))
  element = driver.find_element(By.ID, "troopTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    troop =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    troop =  0
  else:
    troop =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(troop)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#spells")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "spellTime")))
  element = driver.find_element(By.ID, "spellTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    spell =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    spell =  0
  else:
    spell =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(spell)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#darktroops")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "darkTroopTime")))
  element = driver.find_element(By.ID, "darkTroopTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    darkTroop =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    darkTroop =  0
  else:
    darkTroop =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(darkTroop)

  driver.get("https://www.clash.ninja/upgrade-tracker/yycgjp8q/home#siegemachines")
  wait = WebDriverWait(driver, 10)
  wait.until(EC.visibility_of_element_located((By.ID, "siegeMachineTime")))
  element = driver.find_element(By.ID, "siegeMachineTime")
  text = element.find_element(By.TAG_NAME, "strong").text
  integers = re.findall(r'\d+', text)
  integers = [int(num) for num in integers]
  if "mo" in text:
    siegeMachine =  integers[0] * 30 + integers[1] + integers[2] / 24
  elif "Complete" in text:
    siegeMachine =  0
  else:
    siegeMachine =  integers[0] + integers[1] / 24 + integers[2] / (24 * 60)
  #print(siegeMachine)

  totalResearch = troop + spell + darkTroop + siegeMachine
  print('\nResearch: ', round(totalResearch, 2))

  week = int(totalResearch / 10)
  remaining = totalResearch - week * 10
  if remaining > 7 :
      remaining -= 3
  print('Research(3 potion weekly): ', round(week * 7 + remaining, 2))