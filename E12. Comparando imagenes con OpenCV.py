#Cap12. Comparando imagenes con OpenCV https://www.youtube.com/watch?v=6LLh3B0HUjs&list=PLas30d-GGNa2UW9-1H-NCNrUocvWD9cyh&index=13&t=18s

import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import cv2

class usando_unittest(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome(executable_path= r"C:\Webdrivers\chromedriver.exe")
        
    def test_usando_opencv(self):
        driver = self.driver
        driver.get("http://www.google.com")
        driver.save_screenshot("img2.png")
        time.sleep(3)
    
    def test_comparando_imagenes(self):
        img1= cv2.imread('img1.png')
        img2= cv2.imread('img2.png')
        
        diferencia = cv2.absdiff(img1, img2)
        imagen_gris = cv2.cvtColor(diferencia, cv2.COLOR_BGR2GRAY)
        contours,_ = cv2.findContours(image_gris, cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
        
        for c in contours:
            if cv2.contourArea(c) >= 28: #Escalacion a nivel grises
                posicion_x,posicion_y,ancho,alt = cv2.boundingRect(c) #dimensiones que va a encontrar en la imagen
                cv2.rectangle(img1,(posicion_x, posicion_y),(posicion_x+ancho, posicion_y + alto),(0,0,255),2)
        
        while(1):
            cv2.imShow('Imagen1', img1)
            cv2.imShow('Imagen2', img2)
            cv2.imShow('Diferencias detectadas', diferencia)
            teclado = cv2.waitKey(5) & 0xFF
            if teclado == 27:
                break
        cv2.destroyAllWindows()
        
if __name__ == '__main__':
    unittest.main()