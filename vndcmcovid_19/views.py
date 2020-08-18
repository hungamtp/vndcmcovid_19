from django.shortcuts import render   , HttpResponse
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium import webdriver
# Create your views here.
def index(request):
    
    PATH ='/home/khunglongbaochua/Desktop/chromedriver'
    driver = webdriver.Chrome(PATH)
    driver.get('https://ncov.moh.gov.vn/?fbclid=IwAR0WTvaWHDTbf52Ojb9OmsHMJdt2QCl1TXMYZyJh90vwYs2NcS8K7utmwt0')
    try:
        provinces = driver.find_element_by_tag_name('tbody').text
    except:
        return HttpResponse('not found')
        driver.quit()
    finally:
        driver.close()
    table = dict()

    for line in provinces.splitlines():
        line = line.replace('-' , '')
        line = line.replace('  ' , ' ')
        line = ' '.join(line.split())
        word = line.split(' ')
        word1 = line.split(' ')
        if word1[2].isnumeric():
            table[word1[0] + ' ' +word1[1]] = [word1[2] , word1[3] , word1[4] , word[5]]
            
        elif word1[3].isnumeric() and not word1[2].isnumeric():

            table[word1[0] + ' ' +word1[1] + ' ' + word1[2]] = [word1[3] , word1[4] , word1[5] , word[6]]       

        else:

            table[word1[0] + ' ' +word1[1] + ' ' + word1[2] +' ' +word1[3]] = [ word1[4] , word1[5] , word1[6] , word[7] ]
    driver.quit()
    # string ='hunghung'
    # table =({'hung':'a11' , 'tung':'a12'})
    context={
        # 'string':string,
        'table' :table,
    }
    return render(request , 'home.html' , context)