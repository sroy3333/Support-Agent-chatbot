import requests
from bs4 import BeautifulSoup

CDP_URLS = {
    "segment": "https://segment.com/docs/",
    "mparticle": "https://docs.mparticle.com/",
    "lytics": "https://learn.lytics.com/",
    "zeotap": "https://developer.zeotap.com/"
}

def scrape_cdp_docs():
    for cdp, url in CDP_URLS.items():
        response = requests.get(url)
        soup = BeautifulSoup(response.text, "html.parser")

        # Extract main text from docs
        paragraphs = [p.get_text() for p in soup.find_all("p")]
        doc_text = "\n".join(paragraphs)

        # Save to file
        with open(f"data/{cdp}.txt", "w", encoding="utf-8") as f:
            f.write(doc_text)

if __name__ == "__main__":
    scrape_cdp_docs()
    print("CDP documentation scraped and saved.")