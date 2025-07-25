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
