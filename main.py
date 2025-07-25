from footwearfinder.scraper import save_html, load_html
from footwearfinder.parser import parse_backcountry
from footwearfinder.output import output_to_text, output_to_csv

def main():
    # URL to scrape
    url = "https://www.backcountry.com/search?s=u&q=climbing+shoes"
    html_file = "climbing_shoes_backcountry.html"

    # Step 1: Download and save HTML
    save_html(url, html_file)

    # Step 2: Load HTML from file
    html = load_html(f"saved_html/{html_file}")

    # Step 3: Parse the HTML
    parsed_data = parse_backcountry(html)

    # Step 4: Output to text and CSV
    output_to_text(parsed_data)
    output_to_csv(parsed_data)

if __name__ == "__main__":
    main()
