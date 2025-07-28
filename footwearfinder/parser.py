from bs4 import BeautifulSoup
from typing import List, Tuple
import re

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
            #TODO convert text.strip to get_text(strip=True)
            brand = shoe.find(attrs={"data-id": "brandName"}).text.strip()
            name = shoe.find(attrs={"data-id": "title"}).text.strip()
            price = shoe.find(attrs={"data-id": "price"}).text.strip()
            parsed.append((brand, name, price, "backcountry"))
        except AttributeError:
            continue

    return parsed

def parse_steepandcheap(html: str) -> List[Tuple[str, str, str, str]]:
    """
    Parses product info from Steep and Cheap's HTML page.
    Returns list of (brand, name, price, source).
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all(attrs={"data-id": "PLI"})
    parsed = []

    for product in products:
        try:
            #TODO convert text.strip to get_text(strip=True)
            brand = product.find(attrs={"data-id": "brandName"}).text.strip()
            name = product.find(attrs={"data-id": "title"}).text.strip()
            price = product.find(attrs={"data-id": "price"}).text.strip()
            parsed.append((brand, name, price, 'steepandcheap'))
        except AttributeError:
            continue

    return parsed

def parse_footbeta(html: str) -> List[Tuple[str, str, str, str]]:
    """
    Parses product info from Footbeta's HTML.
    Returns list of (brand, model, price_string, 'footbeta').
    """
    soup = BeautifulSoup(html, "html.parser")
    products = soup.find_all("div", class_="split-intro")
    parsed = []

    for product in products:
        try:
            brand = product.find("p", class_="brand-title").find("a").get_text(strip=True)
            tags = product.find_all("a", class_="tagline")

            name = tags[0].get_text(strip=True)
            price = tags[1].get_text(strip=True)
            parsed.append((brand, name, price, 'footbeta'))
        except AttributeError:
            continue
        
    return parsed


