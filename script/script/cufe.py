import pandas

from seleniumbase import Driver
from selenium.webdriver.support import expected_conditions as EC

import time
#import datetime

URL = 'https://catalogo-vpfe.dian.gov.co/User/SearchDocument'
info = pandas.read_excel('cufe.xlsx')
list_cufe = info['CUFE'].tolist()
test_cufe= list_cufe[2]

driver = Driver(uc=True)
driver.set_window_size(1900, 1080)



def search_cufe(cufe):    
    driver.uc_open_with_reconnect(URL,4)
    driver.uc_gui_click_captcha()
    time.sleep(5)   
    driver.type('#DocumentKey',cufe)
    time.sleep(2)
    driver.click('button:contains("Buscar")')
    time.sleep(2)
    #driver.click("Descargar PDF")
    """
    if(eventos asociados){
    pandas.escribirExcel(1)
    }
    """
    file_name = f'./screen/{cufe}.png'
    driver.save_screenshot(file_name)
    time.sleep(2)
    driver.quit()

search_cufe(test_cufe)

