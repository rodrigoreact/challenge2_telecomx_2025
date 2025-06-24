import requests
from IPython.display import Markdown, display

# URL RAW del archivo .md en GitHub
url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_diccionario.md"

# Hacer la solicitud y obtener el texto
response = requests.get(url)

# Mostrarlo como Markdown en el notebook
display(Markdown(response.text))
