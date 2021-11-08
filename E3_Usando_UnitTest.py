import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Webdrivers\chromedriver.exe")
    
    def test_buscar_por_xpath(self):
        driver = self.driver
        driver.get("http://www.google.com")
        time.sleep(3)
        buscar_por_xpath= driver.find_element_by_xpath("/html/body/div[1]/div[3]/form/div[1]/div[1]/div[1]/div/div[2]/input")
        time.sleep(3)
        buscar_por_xpath.send_keys("Selenium", Keys.ARROW_DOWN) #ARROW_DOWN
        time.sleep(3)
    
    def tearDown(self):
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()  
    
#XPATH es una estruct de direcciones similar al disco C
#xpath es una estructura de objetos
#PREGUNTA DE EXAMEN EN ENTREVISTAS#
#xpath relativo: permite encontrar elementos dentro de toda una carpeta
# Este es el xpath de buscar de la barra de google --> //*[@id="input"]
#xpath absoluto: es toda la ruta de C