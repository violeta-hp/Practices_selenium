# Cap #10 | Curso Python con Selenium | Como usar Explicit Wait
#https://www.youtube.com/watch?v=SNIeI3XLzxU&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=11

#Cuando usas páginas con muchos elementos se usa el Explicit wait
#Podemos dar condiciones para cargar cientos de componentes en un script.
#No inicies la automatización hasta que no veas el id de tal componente

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC #este es el modulo que se va a llamar 

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver= webdriver.Chrome(executable_path = r"C:\Webdrivers\chromedriver.exe")
        
    def test_usando_Explicit_wait(self):
        driver = self.driver
        driver.get("http://www.google.com")
        try: #ciclando hasta que cargue el componente que estamos esperando
            element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.NAME, "q")))
        finally:
            driver.quit()
            
if __name__ == '__main__':
    unittest.main()