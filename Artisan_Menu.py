from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import csv


file =open("menu.csv", "w")
writer = csv.writer(file)
writer.writerow(["name", "ingredients", "price"])