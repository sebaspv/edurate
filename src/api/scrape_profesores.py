import time 

 
import pandas as pd 
from selenium import webdriver 
from selenium.webdriver import Chrome 
from selenium.webdriver.chrome.service import Service 
from selenium.webdriver.common.by import By 
from webdriver_manager.chrome import ChromeDriverManager

from bs4 import BeautifulSoup

def calificacion_profe(nombre, nombre_prof):
    options = webdriver.ChromeOptions() 
    options.add_argument("--headless")

    options.page_load_strategy = 'none' 
    chrome_path = ChromeDriverManager().install() 
    chrome_service = Service(chrome_path)

    driver = Chrome(options=options, service=chrome_service) 
    driver.implicitly_wait(2)
    nombre_amigable_url = nombre.replace(" ", "+")
    nombre_amigable_prof = nombre_prof.replace(" ", "+")
    URL = f"https://www.misprofesores.com/Buscar?q={nombre_amigable_url}+{nombre_amigable_prof}"

    driver.get(URL) 
    time.sleep(3)

    content = driver.page_source
    soup = BeautifulSoup(content, "html.parser")

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
            school_url = gs_title_div.find('a', class_='gs-title').get('data-ctorig')
    print(school_url)
    driver.get(school_url)
    time.sleep(3)
    profesor = driver.page_source
    newsoup = BeautifulSoup(profesor, "html.parser")
    calificacion = newsoup.find('div', id='container').find('div', id='body').find('div', id='mainContent').find('div', class_='right-panel').find('div', class_='rating-breakdown').find('div', class_='left-breakdown').find('div', class_='breakdown-wrapper').find('div', class_='breakdown-header quality-header').find('div', class_='breakdown-container quality').find('div').find('div', class_='grade').text
    return {"calificación": float(calificacion)}
