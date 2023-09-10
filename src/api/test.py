import time 
 
 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

options = webdriver.ChromeOptions() 
options.add_argument("--headless")

options.page_load_strategy = 'none' 
chrome_path = ChromeDriverManager().install() 
chrome_service = Service(chrome_path)

driver = Chrome(options=options, service=chrome_service) 
driver.implicitly_wait(2)
nombre = "UAM Iztapalapa"
nombre_amigable_url = nombre.replace(" ", "+")
URL = f"https://www.misprofesores.com/Buscar?q={nombre_amigable_url}"

driver.get(URL) 
time.sleep(3)

content = driver.page_source
soup = BeautifulSoup(content, "html.parser")


# mátenme por favor

results = soup.find('div', id='container').find('div', id='content').find('div', id='___gcse_0')
school = results.find('div', class_='gsc-control-cse gsc-control-cse-es').find('div', class_='gsc-control-wrapper-cse').find('div', class_='gsc-results-wrapper-nooverlay gsc-results-wrapper-visible').find('div', class_='gsc-wrapper').find('div', class_='gsc-resultsbox-visible')

if school:
    div_ids = ['gsc-resultsRoot gsc-tabData gsc-tabdActive', 'gsc-results gsc-webResult', 'gsc-expansionArea', 'gsc-webResult gsc-result', 'gs-webResult gs-result', 'gsc-thumbnail-inside']
    current_div = school
    for div_id in div_ids:
        specific_div = current_div.find('div', class_=div_id)
        if specific_div:
            current_div = specific_div
    gs_title_div = current_div.find('div', class_='gs-title')
    if gs_title_div:
        print(gs_title_div.find('a', class_='gs-title').get('data-ctorig'))