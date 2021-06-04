import unittest
import utils
import requests


class TestUtils(unittest.TestCase):
    def test_get_wiki_page_html(self):
        html = utils.get_wiki_page_html("dogs")
        self.assertIsNotNone(html)
        self.assertNotEqual(html, "")

    # def test_is_single_page_false(self):
    #     dogs_redirect = requests.get("https://en.wikipedia.org/w/index.php?title=Dogs&redirect=no")
    #     self.assertFalse(utils.is_single_page(dogs_redirect.text))
    #     java_category = requests.get("https://en.wikipedia.org/wiki/Java_(disambiguation)")
    #     self.assertFalse(utils.is_single_page(java_category.text))

    # def test_is_single_page_true(self):
    #     computer_page = requests.get("https://en.wikipedia.org/wiki/Computer")
    #     self.assertTrue(utils.is_single_page(computer_page.text))
    #     neutron_page = requests.get("https://en.wikipedia.org/wiki/Neutron")
    #     self.assertTrue(utils.is_single_page(neutron_page.text))

    # def test_is_redirect_page_true(self):
    #     dogs_redirect = requests.get("https://en.wikipedia.org/w/index.php?title=Dogs&redirect=no")
    #     self.assertTrue(utils.is_redirect_page(dogs_redirect.text))
    #     phones_redirect = requests.get("https://en.wikipedia.org/w/index.php?title=Phones&redirect=no")
    #     self.assertTrue(utils.is_redirect_page(phones_redirect.text))

    # def test_is_redirect_page_false(self):
    #     ordinary_category = requests.get("https://en.wikipedia.org/wiki/Ordinary")
    #     self.assertFalse(utils.is_redirect_page(ordinary_category.text))
    #     smartphone_page = requests.get("https://en.wikipedia.org/wiki/Smartphone")
    #     self.assertFalse(utils.is_redirect_page(smartphone_page.text))

    def test_extract_links(self):
        ordinary_category = requests.get("https://en.wikipedia.org/wiki/Ordinary").text
        ordinary_category = utils.remove_footer(ordinary_category)
        self.assertEqual(len(utils.extract_links(ordinary_category)), 18)

        sleepy_category = requests.get("https://en.wikipedia.org/wiki/Sleepy").text
        sleepy_category = utils.remove_footer(sleepy_category)
        self.assertEqual(len(utils.extract_links(sleepy_category)), 17)

    def test_package_links(self):
        sleepy_category = requests.get("https://en.wikipedia.org/wiki/Sleepy").text
        sleepy_category = utils.remove_footer(sleepy_category)
        links = utils.extract_links(sleepy_category)
        packaged_links = utils.package_links(links)
        self.assertEqual(len(packaged_links['links']), 17)

if __name__ == "__main__":
    unittest.main()