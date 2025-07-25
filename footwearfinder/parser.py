from bs4 import BeautifulSoup
from typing import List, Tuple

def parse_backcountry(html: str) -> List[Tuple[str, str, str, str]]:
    """
    Parses product info from Backcountry's HTML page.
    Returns list of (brand, name, price, source).
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='chakra-linkbox')

    parsed = []
    for shoe in products:
        try:
            brand = shoe.find(attrs={"data-id": "brandName"}).text.strip()
            name = shoe.find(attrs={"data-id": "title"}).text.strip()
            price = shoe.find(attrs={"data-id": "price"}).text.strip()
            parsed.append((brand, name, price, "backcountry"))
        except AttributeError:
            continue

    return parsed

def parse_steepandcheap(html: str) -> List[Tuple[str, str, str, str]]:
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='product-tile')
    parsed = []

    for product in products:
        try:
            name = product.find('h3', class_='product-name').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            brand = name.split()[0]
            parsed.append((brand, name, price, 'steepandcheap'))
        except AttributeError:
            continue

    return parsed

def parse_footbeta(html: str) -> List[Tuple[str, str, str, str]]:
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='product-card')
    parsed = []

    for product in products:
        try:
            name = product.find('h3', class_='product-title').text.strip()
            price = product.find('span', class_='product-price').text.strip()
            brand = name.split()[0]
            parsed.append((brand, name, price, 'footbeta'))
        except AttributeError:
            continue

    return parsed