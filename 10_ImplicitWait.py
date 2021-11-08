#IMPLICIT WAIT es parecido al timer.sleep
#Espera un tiempo en especifico, pero no se usa tanto

import unittest 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #modulo para llamar los implicits

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Webdrivers\chromedriver.exe")
        
    def test_usando_implicit_wait(self):
        driver = self.driver
        driver.implicitly_wait(5) #5 seg #ESTE ES EL TIEMPO ESPECIFICO QUE ESPERA, si no encuentra el elemento se sale a los 5 seg pero si lo encuentra en menos tiempo se sale.
        driver.get("http://www.google.com")
        myDynamicElement = driver.find_element_by_name("q") #un componente dinamico es el que cambia su nombre y lo cambia una vez que lo mandas llamar

if __name__ == '__main__':
    unittest.main()