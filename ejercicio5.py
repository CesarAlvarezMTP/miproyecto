"""
Mostrar por pantalla el nombre de las personas con más de $50 en esta tabla: https://the-internet.herokuapp.com/tables

"""

from selenium import webdriver

URL = "https://the-internet.herokuapp.com/tables"

driver = webdriver.Chrome()
driver.get(URL)

tabla = driver.find_element_by_id("table1")
filas = tabla.find_elements_by_css_selector('tbody tr')

datos_filtrados = []

try:
    for fila in filas:
            columnas = fila.find_elements_by_css_selector('td')
            apellidos = columnas[0].text
            nombre = columnas[1].text
            sueldo = columnas[3].text.replace('$', '').replace(',', '')

            if float(sueldo) > 50:
                datos_filtrados.append((nombre, apellidos, sueldo))


    for datos in datos_filtrados:
        print(datos[0],datos[1],datos[2])

finally:
    driver.quit()