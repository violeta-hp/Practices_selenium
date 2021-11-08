#ABRIR PESTAÑAS NUEVAS Y NAVEGAR EN ELLAS
import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Webdrivers\chromedriver.exe")
        
    def test_cambiar_ventana(self):
        driver = self.driver #para cargar nuestras páginas
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.execute_script("window.open('');") #es una instrucción para decirle que abra una nueva ventana en python
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[1]) #para cargar una nueva ventana
        driver.get("http://stackoverflow.com") #esta es la nueva ventana
        time.sleep(3)
        driver.switch_to.window(driver.window_handles[0])
        time.sleep(3)
        
        
if __name__ == '__main__':
    unittest.main()
    
#Puede servir para poder hacer varios log in en varias páginas