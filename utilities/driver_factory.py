from selenium import webdriver
from selenium.webdriver.chrome.service import Service

def get_chrome_driver():
    service=Service()
    driver=webdriver.Chrome(service=service)
    return driver