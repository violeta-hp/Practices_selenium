from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time #toda la sec de automatización va a marcar sin pausa y puede provocar error
driver = webdriver.Chrome(executable_path=r"C:\Webdrivers\chromedriver.exe") #para agarrar driver
driver.get("https://gmail.com") #abrir ruta de gmail
usuario = driver.find_element_by_id("identifierId")
usuario.send_keys("viioletahp@gmail.com")
usuario.send_keys(Keys.ENTER)
time.sleep(3)

clave= driver.find_element_by_id("password")
clave.send_keys("MiPassword") #debería dar error
clave.send_keys(Keys.ENTER)


