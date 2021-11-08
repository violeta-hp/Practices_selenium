#Cap #9 | Curso Python con Selenium | navegar entre paginas
'''Puede que haya varios menús en los que hay que interactuar sí funcionan varios de los links, si funciona el cargado de las páginas correctamente, 
se autimatizará el proceso de cuando un usuario se regresa a una pagina y estaba ya en otra'''

import unittest
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path = r"C:\Webdrivers\chromedriver.exe")
    
    def test_pagin_siguiet_o_anterior(self):
        driver = self.driver
        driver.get("http://www.gmail.com")
        time.sleep(3)
        driver.get("http://www.google.com")
        time.sleep(3)
        driver.get("http://www.youtube.com")
        time.sleep(3)
        driver.back() #esta es una funcion de selenium, para regresar a la pag anterior
        time.sleep(3) #con esto se puede hacer la lectura del titulo de la pagina y se puede ver que cuando regresar a YT esperas ver google, si carga otra cosa quiere decir que no estamos cargando bien la pagina 
        driver.back()
        driver.sleep(3)
        driver.forward()
        time.sleep(3)
if __name__ == '__main__':
    unittest.main()