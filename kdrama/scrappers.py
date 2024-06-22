import requests
from bs4 import BeautifulSoup
from sessions import add_movie
import re

def nkiri():
    base_url = 'https://nkiri.com/category/asian-movies/download-korean-movies/'
    n = range(1,8)
    for num in n:
        url = f'{base_url}page/{num}'
        print(f"Getting data for page {num}")
        if num == 7:
            print("Successfully added into Database!")
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        for text in soup.find_all('article'):
            title = text.find('h2', {'class': 'blog-entry-title entry-title'})
            stripped_data = title.text.strip()
            original_string = stripped_data
            pattern_to_remove = r"\s*\|\s*Download Korean Movie"
            final_title = re.sub(pattern_to_remove, "", original_string)

            date = text.find('div', {'class': 'blog-entry-date clr'})
            f_date = date.text.strip()
            link = title.find('a')['href']
            img = text.find('img')
            if img:
                image = img.get('src')

            re_response = requests.get(link)
            re_soup = BeautifulSoup(re_response.text, 'html.parser')
            for shit in re_soup.find_all('a', {'class': 'elementor-button elementor-button-link elementor-size-md'}):
                download = shit.get('href')
                if 'html' in download:
                    downloadlnk = download

                    
            for item in re_soup.find_all('div', {'class': 'overview'}):
                desc = item.find('p')
                desc_text = desc.text.strip()

                add_movie(final_title, f_date, desc_text, image, downloadlnk)


def awafim():
    n = range(1,10)
    for num in n:
        url = f'https://www.awafim.tv/browse/page/{num}?type=movie&country%5B0%5D=KOR'
        print(f"Getting data for page {num}")
        if num == 7:
            print("Successfully added into Database!")

        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')


        for data in soup.find_all('article', {'class': 'titles-one'}):
            head = data.find('h3', {'class': 'to-h3'})
            f_head = head.text.strip()
            
            date = data.find('div', {'class': 'toi-year'})
            f_date = date.text.strip()
            
            image = data.find('img', {'class': 'to-thumb'})
            f_image = image.get('src')
        
            
            link = data.find('a')['href']

            re_response = requests.get(link)
            re_soup = BeautifulSoup(re_response.text, 'html.parser')

            for down in re_soup.find_all('div', {'class': 'rlo-link-dl'}):
                download_link = down.find('a')
                if download_link:
                    download = download_link['href']
                    

            re_response = requests.get(link)
            re_soup = BeautifulSoup(re_response.text, 'html.parser')
            for desc in re_soup.find('p', {'class': 'tei-plot'}):
                desciption =  desc.text.strip()

            add_movie(f_head, f_date, desciption, f_image, download)



awafim ()       
            
   

        