from selenium import webdriver
from selenium.webdriver.common.by import By
import pyautogui
import time
import random

# Inicializar el driver de Selenium (asegúrate de tener instalado el controlador correspondiente para tu navegador)
driver = webdriver.Chrome()  # Esto abrirá una ventana del navegador visible

# Abre la página web deseada
# driver.get("https://sodimac.falabella.com/sodimac-cl/product/110307511")
driver.get("https://sodimac.falabella.com/sodimac-cl/product/110308912")

# Localiza el botón por su ID, clase, etiqueta, etc.
boton = driver.find_element(By.ID, "geofinder-button-open")
boton.click()

time.sleep(5)

apretar = driver.find_element(By.ID, "geofinder-input-level1")
apretar2 = driver.find_element("xpath",'//*[@id="zone_modal_wrap"]/div/div/div/div[2]/div[1]/div/div')
apretar.click()

width, height = pyautogui.size()

# Realizar movimientos aleatorios del ratón dentro de la ventana del navegador
for _ in range(10):  # Simular 10 movimientos
    x = pyautogui.randint(0, width)  # Generar una coordenada X aleatoria
    y = pyautogui.randint(0, height)  # Generar una coordenada Y aleatoria
    pyautogui.moveTo(x, y, duration=0.5)  # Mover el ratón a la posición aleatoria
    


time.sleep(10)


losrios = driver.find_element("xpath",'//*[@id="zone_modal_wrap"]/div/div/div/div[2]/div[1]/div/div/ul/li[1]')
losrios.click()


