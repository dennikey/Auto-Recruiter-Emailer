import bs4
import requests

def getTextWeb(website_url, website_elem):
    # Retrieves info from the website domain
    res = requests.get(website_url)
    res.raise_for_status()

    # Retrieves info from the specific text under a certain HTML element
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    section = soup.select(website_elem)

    return section[0].text.strip()
