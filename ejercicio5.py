"""
Mostrar por pantalla el nombre de las personas con más de $50 en esta tabla: https://the-internet.herokuapp.com/tables

"""

from selenium import webdriver

URL = "https://the-internet.herokuapp.com/tables"
# Inicializar el navegador y abrir la URL
driver = webdriver.Chrome()
driver.get(URL)

# Encontrar la tabla y obtener los datos de cada fila
tabla = driver.find_element_by_id("table1")
filas = tabla.find_elements_by_css_selector('tbody tr')

datos_filtrados = []

for fila in filas:
    # Obtener los datos de cada columna en la fila
    columnas = fila.find_elements_by_css_selector('td')
    nombre = columnas[0].text
    apellido = columnas[1].text
    edad = columnas[2].text
    sueldo = columnas[3].text.replace('$', '').replace(',', '')

    # Filtrar por sueldo mayor a $50
    if float(sueldo) > 50:
        datos_filtrados.append((nombre, apellido, edad, sueldo))

# Imprimir los nombres de las personas con sueldo mayor a $50
for datos in datos_filtrados:
    print(datos[0])

# Cerrar el navegador
driver.quit()