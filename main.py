from bs4 import BeautifulSoup
import requests

##Páginas seleccionadas
##CNN 
##Huffpost
##Vice
##UN NEWS
##El tiempo --eng version 

##DESARROLLO

##CNN
##CNN NEWS SOLO
def noticia_cnn_solo(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    try:
        titulo = soup.find('h1',class_="pg-headline").get_text()
        autor = soup.find('span',class_="metadata__byline__author").get_text()
        fecha = soup.find('p',class_="update-time").get_text()
        cuerpo = soup.find('div',class_="l-container").get_text()
        imagen = soup.find('img',class_="media__image media__image--responsive") ## imagen['data-src-large']
        link = url
        
    except:
        titulo = soup.find('h1',class_="media__video-headline").get_text()
        autor = soup.find('span',class_="metadata__source-name").get_text()
        fecha = "NaN"
        imagen = 'https://pbs.twimg.com/profile_images/500790162775760896/aLM0MMqI_400x400.jpeg'
        cuerpo = soup.find('div',class_="media__video-description media__video-description--inline").get_text()
        link = url

##CNN NEWS LINK
def generar_cnn_varias(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    contenedor = soup.findAll('h3',class_="cd__headline")
    for i in range(0,len(contenedor)):
        try:
            var = contenedor[i].findChild("a")['href']
            var = "https://edition.cnn.com"+ var
            noticia_cnn_solo(var)
        except:
            print("NO SE PUDO")

#generar_cnn_varias('https://edition.cnn.com/business')
##noticia_cnn_solo('https://edition.cnn.com/2022/08/17/business/dodge-electric-muscle-car/index.html')

##Huffpost
##Huffpost solo
def noticia_Huffpost_solo(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    try:
        titulo = soup.find('h1',class_="headline").get_text()
        autor = soup.find('span',class_="entry-wirepartner__byline").get_text()
        fecha = soup.find('time').get_text()
        cuerpo = soup.find('div',class_="entry__content-list-container js-cet-unit-buzz_body").get_text()
        imagen = soup.find('img',class_="img-sized__img landscape") ['src']
        link = url
        print(titulo)
        print(autor)
        print(fecha)
        print(cuerpo)
        print(imagen)
        print(link)
        
    except:
        titulo = soup.find('h1',class_="headline").get_text()
        autor = soup.find('a',class_="js-entry-link cet-internal-link")['data-vars-item-name']
        fecha = soup.find('time')['datetime']
        cuerpo = soup.find('section',class_="entry__content-list js-entry-content js-cet-subunit").get_text()
        imagen = soup.find('img',class_="img-sized__img portrait")['src']
        link = url
        print(titulo)
        print(autor)
        print(fecha)
        print(cuerpo)
        print(imagen)
        print(link)
        

def generar_Huffpost_varias(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    contenedor = soup.findAll('a',class_="card__headline card__headline--long")
    for i in range(0,len(contenedor)):
        try:
            data = contenedor[i]['href']
            noticia_Huffpost_solo(data)
        except:
            print("NO SE PUDO")

#noticia_Huffpost_solo("https://www.huffpost.com/entry/never-have-i-ever-netflix-maitreyi-ramakrishnan_n_62fa49e5e4b045e6f6af1f32")
#generar_Huffpost_varias("https://www.huffpost.com/")

##VICE
##Vice solo
def noticia_vice_solo(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    try:
        titulo = soup.find('h1',class_="smart-header__hed smart-header__hed--size-2").get_text()
        autor_sub = soup.find('div',class_="contributor__meta")
        autor = autor_sub.findChild("a").get_text()
        fecha = soup.find('time')['datetime']
        cuerpo = soup.find('div',class_="article__body-components").get_text()
        imagen = soup.find('source')['srcset']
        link = url
        print(titulo)
        print(autor)
        print(fecha)
        print(cuerpo)
        print(imagen)
        print(link) 
    except:
        print("No se pudo")

##Vice varias
def generar_vice_varias(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    contenedor = soup.findAll('h3',class_="vice-card-hed vice-card-hed--light vice-card__vice-card-hed")
    for i in range(0,len(contenedor)):
        try:
            data = contenedor[i].findChild("a")["href"]
            data = "https://www.vice.com"+ data
            noticia_vice_solo(data)     
        except:
            print("NO SE PUDO")

#noticia_vice_solo("https://www.vice.com/en/article/59qjed/how-westworld-uses-multilingualism-to-explore-prejudice")
#generar_vice_varias("https://www.vice.com/en/topic/english?page=1")

##UN NEWS 
##UN NEWS SOLO 
def noticia_un_solo(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    try:
        titulo = soup.find('h1',class_="story-title").get_text()
        autor = soup.find('span',class_="un-news-full-width scald-credit").get_text()
        fecha = soup.find('div',class_="field-item even").get_text()
        cuerpo_sub = soup.findAll('p')
        imagen = soup.findAll('img',class_="img-responsive")
        imagen = imagen[1]["src"]
        cuerpo = ""
        for i in range(len(cuerpo_sub)):
            cuerpo = cuerpo + cuerpo_sub[i].get_text()
        link = url
        print(titulo)
        print(autor)
        print(fecha)
        print(cuerpo)
        print(imagen)
        print(link) 
    except:
        titulo = soup.find('h2',class_="story-title quote-text").get_text()
        autor = soup.find('span',class_="un-news-feature scald-credit").get_text()
        fecha = soup.find('div',class_="field-item even").get_text()
        cuerpo_sub = soup.findAll('p')
        imagen = soup.findAll('img',class_="img-responsive")
        imagen = imagen[1]["src"]
        cuerpo = ""
        for i in range(len(cuerpo_sub)):
            cuerpo = cuerpo + cuerpo_sub[i].get_text()
        link = url
        print(titulo)
        print(autor)
        print(fecha)
        print(cuerpo)
        print(imagen)
        print(link) 
       

##UN VARIAS
def generar_un_varias(url):
    resultado = requests.get(url)
    contenido = resultado.text
    soup = BeautifulSoup(contenido,'html.parser')
    contenedor = soup.findAll('div',class_="featured-media clearfix")
    contenedor_2 = soup.findAll('h3',class_="story-title")
    for i in range(0,len(contenedor)):
        try:
            data_1 = contenedor[i].findChild("a")["href"]
            data_1 = "https://news.un.org/" + data_1
            noticia_un_solo(data_1)
        except:
            print("NO SE PUDO")

    for i in range(0,len(contenedor_2)):
        try:
            data_2 = contenedor_2[i].findChild("a")["href"]
            data_2 = "https://news.un.org/" + data_2
            noticia_un_solo(data_1)
        except:
            print("NO SE PUDO")

#generar_un_varias("https://news.un.org/en/")
#noticia_un_solo('https://news.un.org//en/story/2022/08/1125522')

##EL TIEMPO
##El tiempo solo
