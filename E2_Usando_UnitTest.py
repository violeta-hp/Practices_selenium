import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys #para poder enviar acciones de teclado
import time

class usando_unittest(unittest.TestCase): #nuestra clase se trata de un test case
    def setUp(self): '''setUp para incializar el driver, self es el valor de regreso, setUp funciona como punto de entrada
        para los casos de prueba'''
        self.driver = webdriver.Chrome(executable_path= r"C:\Webdrivers\chromedriver.exe")
    
    def test_buscar(self): #después del setUp el programa va a usar la palabra test que debe usarse con la var
        driver = self.driver
        driver.get("http://www.google.com")
        self.assertIn("Google", driver.title) #verifica que Google está en el título, si no está entonces el dev debe corregir
        elemento = driver.find_element_by_name("q") #para buscar la barra de búsqueda
        elemento.send_keys("Selenium")
        elemento.send_keys(Keys.RETURN)
        time.sleep(5)
        assert "No se encontró el elemento" not in driver.page_source
        
    def tearDown(self): #Cierre al driver
        self.driver.close()
    
if __name__ == '__main__':
    unittest.main()        #para cerrar la clase
