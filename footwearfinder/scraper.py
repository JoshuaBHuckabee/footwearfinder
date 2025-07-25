from pathlib import Path
import requests

def save_html(url: str, filename: str, folder: str = "saved_html") -> Path:
    """Downloads HTML content from a URL and saves it to a file."""
    Path(folder).mkdir(parents=True, exist_ok=True)
    file_path = Path(folder) / filename

    headers = {
        "User-Agent": (
            "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
            "AppleWebKit/537.36 (KHTML, like Gecko) "
            "Chrome/114.0.0.0 Safari/537.36"
        )
    }

    response = requests.get(url, headers=headers)
    if response.status_code != 200:
        raise Exception(f"Failed to fetch {url} (status: {response.status_code})")

    file_path.write_text(response.text, encoding="utf-8")
    print(f"Saved HTML to: {file_path}")
    return file_path

def load_html(file_path: str) -> str:
    """Loads saved HTML content from a file."""
    return Path(file_path).read_text(encoding="utf-8")
