from footwearfinder.scraper import save_html, load_html
from footwearfinder.parser import parse_backcountry, parse_steepandcheap, parse_footbeta
from footwearfinder.output import output_to_text, output_to_csv

def main():
    sites = [
        {
            "url": "https://www.backcountry.com/search?s=u&q=climbing+shoes",
            "html_file": "climbing_shoes_backcountry.html",
            "parser": parse_backcountry,
            "source": "backcountry"
        },
        {
            "url": "https://www.steepandcheap.com/cat/climbing-shoes",
            "html_file": "climbing_shoes_steepandcheap.html",
            "parser": parse_steepandcheap,
            "source": "steepandcheap"
        },
        {
            "url": "https://www.footbeta.com/popular/all-round/",
            "html_file": "climbing_shoes_footbeta.html",
            "parser": parse_footbeta,
            "source": "footbeta"
        }
    ]

    all_parsed = []

    for site in sites:
        print(f"Processing {site['source']}...")
        # Step 1: Download and save HTML
        save_html(site["url"], site["html_file"])

        # Step 2: Load HTML from saved file
        html = load_html(f"saved_html/{site['html_file']}")

        # Step 3: Parse HTML content
        parsed_data = site["parser"](html)

        all_parsed.extend(parsed_data)

    # Step 4: Output combined data to text and CSV
    output_to_text(all_parsed)
    output_to_csv(all_parsed)

if __name__ == "__main__":
    main()
