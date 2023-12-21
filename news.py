import requests
from bs4 import BeautifulSoup

response = requests.get('https://g1.globo.com/')

content = response.content

site = BeautifulSoup(content, 'html.parser')

#HTML da noticia
noticia = site.find('div', attrs={'class': 'feed-post-body'})

#Titulo da noticia
titulo = noticia.find('a', attrs={'class': 'feed-post-link'})

#Subtítulo
subtitulo = noticia.find('div', attrs={'class': 'feed-post-body-resumo'})
print(titulo.text)
print(subtitulo.text)