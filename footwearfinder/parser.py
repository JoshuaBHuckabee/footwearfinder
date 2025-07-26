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
            brand = product.find(attrs={"data-id": "brandName"}).text.strip()
            name = product.find(attrs={"data-id": "title"}).text.strip()
            price = product.find(attrs={"data-id": "price"}).text.strip()
            parsed.append((brand, name, price, 'steepandcheap'))
        except AttributeError:
            continue

    return parsed

def parse_footbeta(html: str) -> List[Tuple[str, str, str, str]]:
    """
    Parses product info from Footbeta's HTML page.
    Returns list of (brand, name, price, source).
    """
    soup = BeautifulSoup(html, 'html.parser')
    products = soup.find_all('div', class_='split-intro')
    parsed = []

    for product in products:
        try:
            brand = product.find('p', class_='brand-title').text.strip()
            name = product.find('a', class_='tagline').text.strip()

            # Find the <a> with the price info (usually contains an arrow)
            price_link = product.find('a', href=re.compile(r'/s/ls_fin/'), string=re.compile(r'\$?\d+.*→.*\d+'))
            
            if price_link:
                price_text = price_link.get_text(strip=True)
                # Use regex to extract the two prices
                match = re.match(r'\$?(\d+(?:\.\d+)?)[^\d]+(\d+(?:\.\d+)?)', price_text)
                if match:
                    current_price = f"${match.group(1)}"
                    original_price = f"${match.group(2)}"
                    price = f"{current_price} (was {original_price})"
                else:
                    price = "Price not found"
            else:
                price = "Price not found"

            parsed.append((brand, name, price, 'footbeta'))
        except AttributeError:
            continue

    return parsed
