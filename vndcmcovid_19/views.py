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
    case =0
    deaths = 0
    treating = 0
    recovered =0
    for line in provinces.splitlines():
        line = line.replace('-' , '')
        line = line.replace('  ' , ' ')
        line = ' '.join(line.split())
        word = line.split(' ')
        word1 = line.split(' ')
        if word1[2].isnumeric():
            table[word1[0] + ' ' +word1[1]] = [word1[2] , word1[3] , word1[4] , word[5]]
            case += int(word1[2])
            treating += int(word1[3])
            recovered   += int(word1[4])          
            deaths += int(word1[5])
        elif word1[3].isnumeric() and not word1[2].isnumeric():
            table[word1[0] + ' ' +word1[1] + ' ' + word1[2]] = [word1[3] , word1[4] , word1[5] , word[6]]       
            case += int(word1[3])
            treating += int(word1[4])
            recovered   += int(word1[5])          
            deaths += int(word1[6])
        else:

            table[word1[0] + ' ' +word1[1] + ' ' + word1[2] +' ' +word1[3]] = [ word1[4] , word1[5] , word1[6] , word[7] ]
            case += int(word1[4])
            treating += int(word1[5])
            recovered   += int(word1[6])          
            deaths += int(word1[7])
    driver.quit()
    context={
        # 'string':string,
        'table' :table,
        'case' :case ,
        'treating': treating, 
        'recovered' :recovered ,       
        'deaths': deaths ,
    }
    return render(request , 'home.html' , context)

def test(request):
    d = {'one':'itemone', 'two':'itemtwo', 'three':'itemthree'}
    a = 5
    context={
        'd': d,
        'a':a
    }
    return render(request  , 'test.html' , context)