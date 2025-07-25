import csv
from pathlib import Path
from typing import List, Tuple

def output_to_text(data: List[Tuple[str, str, str, str]], path: str = "saved_data/scraped_data.txt") -> None:
    """
    Writes raw tuple data to a text file for debugging or review.
    """
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', encoding='utf-8') as f:
        for item in data:
            f.write(str(item) + '\n')
    print(f"Text output written to: {path}")

def output_to_csv(data: List[Tuple[str, str, str, str]], path: str = "saved_data/shoes_list.csv") -> None:
    """
    Writes structured data to a CSV file with headers.
    """
    headers = ['Brand', 'Name', 'Price', 'Source']
    Path(path).parent.mkdir(parents=True, exist_ok=True)
    with open(path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(headers)
        writer.writerows(data)
    print(f"CSV output written to: {path}")
