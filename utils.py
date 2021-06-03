# utilities for use with wiki_search
# June 2, 2021
# Jason Rideout

import requests
import re


BASE_URL = "https://en.wikipedia.org/w/index.php?title="
ANCHOR_REGEX_PATTERN = "<a (href=\"\/wiki\/[^:]+?\") (title=\".+?\")>([^:]*?)<\/a>"
FOOTER_STRING = "printfooter"

def get_wiki_page(keywords):
    """Requests resulting wikipedia page(s) from search using keywords."""
    url = BASE_URL + keywords.replace(" ", "%20")
    response = requests.get(url)
    print("Requesting " + url)
    print(response)
    if response.status_code == 200:
        return response.text
    print(f"Error: " + response.status_code)

def remove_footer(html):
    return html.split(FOOTER_STRING)[0]

def extract_links(html):
    """Parses html and returns a list of all links"""
    print("Extracting links...")
    matches = re.findall(ANCHOR_REGEX_PATTERN, html)
    print("Found " + str(len(matches)) + " matches.")
    for match in matches:
        print(match)
    return matches

def package_links(links):
    return {"links": links}

if __name__ == "__main__":
    print(get_wiki_page("dogs"))
