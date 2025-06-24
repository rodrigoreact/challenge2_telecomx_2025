import requests
from IPython.display import Markdown, display

url = "https://raw.githubusercontent.com/ingridcristh/challenge2-data-science-LATAM/main/TelecomX_diccionario.md"
response = requests.get(url)

# Mostrar como Markdown
display(Markdown(response.text))
