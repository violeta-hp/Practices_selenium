import unittest
from selenium import webdriver
#from selenium.webdriver.common.keys import Keys

class SearchText(unittest.TestCase):
    @classmethod
    def setUp(self): # crea la nueva seccion del navegador
        self.driver = webdriver.Chrome(executable_path = r"C:\Webdrivers\chromedriver.exe")
        self.driver.implicitly_wait(30)
        self.driver.maximize_window()
    # navega hasta la url
        self.driver.get("http://www.google.com/")

    def test_search_by_text(self): # obtener el cuadro de texto de búsqueda
        self.search_field = self.driver.find_element_by_name("q")

    # escribe la palabra clave de búsqueda y la envía
        self.search_field.send_keys("aprender python")
        self.search_field.submit()

    #obtener la lista de elementos que se muestran después de la búsqueda
    #actualmente en la página de resultados usando find_elements_by_class_namemethod
        
        lists = self.driver.find_elements_by_class_name("r")
        no=len(lists)
        self.assertEqual(10, len(lists))
    
    def test_search_by_name(self): # obtener el cuadro de texto de búsqueda
        self.search_field = self.driver.find_element_by_name("q") # se introduce la palabra clave y se submite
        self.search_field.send_keys("Python class")
        self.search_field.submit() '''obtener la lista de elementos que se muestran después de la búsqueda 
        actualmente en la página de resultados usando find_elements_by_class_namemethod'''
        list_new = self.driver.find_elements_by_class_name("r")
        self.assertEqual(10, len(list_new))    
    
    @classmethod
    def tearDown(self): # close the browser window
        self.driver.quit()
        
if __name__ == '__main__':
    unittest.main()
    
