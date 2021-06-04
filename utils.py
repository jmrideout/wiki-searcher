# utilities for use with wiki_search
# June 2, 2021
# Jason Rideout


import requests
import re


BASE_URL = "https://en.wikipedia.org/w/index.php?redirect=no&title="
FOOTER_STRING = "printfooter"
ANCHOR_REGEX_PATTERN = '<li>.*?<a href=\"(\/wiki\/[^:]+?)\".+?title=\".+?\">[^:]*?<\/a>'
# REDIRECT_PAGE_PATTERN = "Redirect Page"
# REFERENCES_PATTERN = "<.+?>references<\/.+?>"

class RequestsResponseException(Exception):
    pass

def get_wiki_page_html(keywords: str) -> str:
    """
    Requests resulting wikipedia page(s) from search using keywords.
    Raises Exception if the response is bad.
    Returns dict of url, html.
    """
    request_url = BASE_URL + keywords.replace(" ", "%20")
    response = requests.get(request_url)
    
    if response.status_code == 200:
        return response.text
    raise RequestsResponseException(f"Error " + response.status_code)

# def is_single_page(html: str) -> bool:
#     """Returns true if the requested wikipedia page is a single entry's page (not a page of links or redirect)"""
#     # Single Wikipedia pages have references for page information.
#     found_references = re.search(REFERENCES_PATTERN, html, re.IGNORECASE)
#     print(found_references)
#     return found_references != None

# def is_redirect_page(html: str) -> bool:
#     """Returns true if the page is a redirect page."""
#     return re.search(REDIRECT_PAGE_PATTERN, html, re.IGNORECASE) != None

def remove_footer(html: str) -> str:
    """Removes the footer and navigation from the page, removing unneccessary links."""
    modified_html = html.split(FOOTER_STRING)[0]
    return modified_html

def extract_links(html: str) -> list:
    """Parses html and returns a list of all links"""
    print("Extracting links...")
    matches = re.findall(ANCHOR_REGEX_PATTERN, html)
    print("Found " + str(len(matches)) + " matches.")
    matches = list(map(lambda href: href.split(" ")[0], matches))
    print("matches:")
    print(matches)
    return matches

def package_links(links: list) -> dict[str, list]:
    """Returns links wrapped in a dictionary for sending as JSON."""
    modified_links = list(map(lambda href: "https://en.wikipedia.org" + href, links))
    return {"links": modified_links}

