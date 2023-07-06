""""
marcar los checks de esta url https://the-internet.herokuapp.com/checkboxes
con el resultado de hacer una petición GET a esta otra url:
https://mtp.alejmans.dev/maas/proxy/test/checkbox . true => debe estar marcado, false => debe estar desmarcado
"""
import requests

URL1 = "https://the-internet.herokuapp.com/checkboxes"
URL2 = "https://mtp.alejmans.dev/maas/proxy/test/checkbox"

response = requests.get(URL2)

valor_checkbox_1 = response.json()["valor_checkbox_1"]
valor_checkbox_2 = response.json()["valor_checkbox_2"]

print(valor_checkbox_1)
print(valor_checkbox_2)
