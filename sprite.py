import requests 
from bs4 import BeautifulSoup
import os

#url = 'https://pokemondb.net/sprites'

def DLimage(url, folder):
    try:
        os.mkdir(os.path.join(os.getcwd(), folder))
    except:
        pass

    os.chdir(os.path.join(os.getcwd(), folder))

    r = requests.get(url).content
    soup = BeautifulSoup(r, 'html.parser')

    images = soup.findAll('span')
    images = images[8:-8]

    for img in images:
        imglink = img.attrs.get("data-src")
        name = img.attrs.get('data-alt')
        with open(name.replace(' ', '').replace('/', '').replace('icon', '') + '.png', 'wb') as f:
            im = requests.get(imglink)
            f.write(im.content)
        
DLimage('https://pokemondb.net/sprites', 'pokemon_sprites')