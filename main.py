from fake_useragent import UserAgent
from bs4 import BeautifulSoup
import aiohttp


headers = {
    'user-agent': UserAgent().random
}


async def get_html(page: int):
    async with aiohttp.ClientSession() as session:
        html = await session.get(url=f'https://scrapingclub.com/exercise/list_basic/?page={page}', headers=headers)
        yield html


async def save_document(name='', price='', img_url='', mode='a'):
    with open('All products from scraping-club.txt', mode) as file:
        file.write(f"\nНазвание товара: {name}\nЦена: {price}\nСсылка на товар: {img_url}\n-------------")


async def collect_data(page: int):
    html = await get_html(page).__anext__()

    soup = BeautifulSoup(await html.text(), 'lxml')
    cards = soup.find_all('div', class_='col-lg-4 col-md-6 mb-4')

    for card in cards:
        name = card.find('h4', class_='card-title').text.strip()
        price = card.find('h5').text.strip()[1:] + '$'
        img_url = 'https://scrapingclub.com' + card.find('a').get('href')
        await save_document(name, price, img_url)

    yield f"All products from scraping-club.txt"
    await save_document(mode='w')
