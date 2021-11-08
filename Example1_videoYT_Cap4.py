from selenium import webdriver
driver = webdriver.Chrome(executable_path = r"C:\Webdrivers\chromedriver.exe")
driver.get("http://python.org")
driver.close() #para cerrar el servicio 