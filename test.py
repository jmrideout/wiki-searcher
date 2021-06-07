# Flask application
# June 4, 2021
# Jason Rideout

import unittest
import utils
import os.path

CUR_DIR = os.path.dirname(__file__)
ORDINARY_FILEPATH   = os.path.join(CUR_DIR, "test_files", "ordinary.txt")
DOGS_FILEPATH       = os.path.join(CUR_DIR, "test_files", "dogs.txt")
SLEEPY_FILEPATH     = os.path.join(CUR_DIR, "test_files", "sleepy.txt")

class TestUtils(unittest.TestCase):
    """Test utils for link extracting Flask application"""

    def setUp(self) -> None:
        super().setUp()
        with open(ORDINARY_FILEPATH, "r", encoding="utf-8") as f:
            self.ordinary_html = f.read()
        with open(DOGS_FILEPATH, "r", encoding="utf-8") as f:
            self.dogs_html = f.read()
        with open(SLEEPY_FILEPATH, "r", encoding="utf-8") as f:
            self.sleepy_html = f.read()


    def test_get_wiki_page_html(self) -> None:
        """Ensures that a response containing html is returned from the request."""
        html = utils.get_wiki_page_html("dogs")
        self.assertIsNotNone(html)
        self.assertNotEqual(html, "")


    def test_extract_links(self) -> None:
        """
        Tests the number of correct links extracted from test pages.\n
        Excludes additional links in descriptions.
        """
        ordinary_category = utils.remove_footer(self.ordinary_html)
        ordinary_links = utils.extract_links(ordinary_category)
        self.assertEqual(len(ordinary_links), 18)

        sleepy_category = utils.remove_footer(self.sleepy_html)
        sleepy_links = utils.extract_links(sleepy_category)
        self.assertEqual(len(sleepy_links), 17)

        dog_redirect = utils.remove_footer(self.dogs_html)
        dog_links = utils.extract_links(dog_redirect)
        self.assertEqual(len(dog_links), 1)


    def test_package_links(self) -> None:
        """Tests correct structure of dictionary"""
        sleepy_category = utils.remove_footer(self.sleepy_html)
        links = utils.extract_links(sleepy_category)
        packaged_links = utils.package_links(links)
        self.assertEqual(len(packaged_links['links']), 17)


if __name__ == "__main__":
    unittest.main()