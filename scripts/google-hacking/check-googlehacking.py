#Google Hacking
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import unquote
from random import randint


def green_googlesearch(url):
    termo_digitado = "site:" + url
    for inicia_resultados_em in [0, 10, 20, 30, 50]:
        parametros_de_busca = {'q': termo_digitado, 'start': inicia_resultados_em}

        pagina_de_busca = requests.get('https://www.google.com.br/search',
                                       params=parametros_de_busca)

        soup = BeautifulSoup(pagina_de_busca.text, "html.parser")

        for item in soup.find_all('h3', attrs={'class': 'r'}):
            if item.a:
                link_sujo_do_google = item.a.attrs['href']
                # /url?website.com%3Fid%3D100%26x%3Dy&ui=10....

                link_sem_url_inicial = link_sujo_do_google[7:]
                # website.com%3Fid%3D100%26x%3Dy&ui=10....

                link_os_parametros_do_google = link_sem_url_inicial.split('&')[0]
                # website.com%3Fid%3D100%26x%3Dy

                link_final_decodificado = unquote(link_os_parametros_do_google)
                # website.com?id=100&x=y

                print(link_final_decodificado)
        dorme_por = randint(0, 2)
        time.sleep(dorme_por)


#url="businesscorp.com.br"
url="businesscorp.com.br"
print(green_googlesearch(url))