# Flask application
# June 4, 2021
# Jason Rideout

import unittest
import utils
import requests


class TestUtils(unittest.TestCase):
    """Test utils for Flask application"""
    def test_get_wiki_page_html(self):
        """Ensures that a response containing html is returned from the request."""
        html = utils.get_wiki_page_html("dogs")
        self.assertIsNotNone(html)
        self.assertNotEqual(html, "")

    def test_extract_links(self):
        """
        Tests the number of correct links extracted from test pages.
        Excludes additional links in descriptions.
        """
        ordinary_category = requests.get("https://en.wikipedia.org/wiki/Ordinary").text
        ordinary_category = utils.remove_footer(ordinary_category)
        self.assertEqual(len(utils.extract_links(ordinary_category)), 18)

        sleepy_category = requests.get("https://en.wikipedia.org/wiki/Sleepy").text
        sleepy_category = utils.remove_footer(sleepy_category)
        self.assertEqual(len(utils.extract_links(sleepy_category)), 17)

    def test_package_links(self):
        """Tests correct structure of dictionary"""
        sleepy_category = requests.get("https://en.wikipedia.org/wiki/Sleepy").text
        sleepy_category = utils.remove_footer(sleepy_category)
        links = utils.extract_links(sleepy_category)
        packaged_links = utils.package_links(links)
        self.assertEqual(len(packaged_links['links']), 17)

if __name__ == "__main__":
    unittest.main()