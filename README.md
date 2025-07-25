# FootwearFinder 🧗‍♂️

A Python web scraper that collects climbing shoe data from Backcountry.com.

## Features

- Scrapes brand, name, price, and source
- Saves data to CSV and text formats
- Modular structure — easy to expand with new retailers

## Project Structure

footwearfinder/
├── footwearfinder/
│ ├── scraper.py
│ ├── parser.py
│ ├── output.py
│ └── ...
├── saved_html/
├── saved_data/
├── main.py
├── .gitignore
├── requirements.txt
└── README.md

## Usage

1. Create and activate a virtual environment:

    **On macOS/Linux:**
    ```bash
    python -m venv .venv
    source .venv/bin/activate

    **On Windows:**
    ```bash
    python -m venv .venv
    .venv\Scripts\activate

2. Install dependencies:

   ```bash
   pip install -r requirements.txt

3. Run the main script:

   ```bash
   python main.py
