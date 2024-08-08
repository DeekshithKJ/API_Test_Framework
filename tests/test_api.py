import unittest
from framework.api_client import APIClient


class TestAPI(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.client = APIClient()

    def test_get_autoident_browser_matrix(self):
        endpoint = "api/v1/ihrebank"
        response = self.client.get(endpoint)
        self.assertIn('autoident', response['settings'], "Key 'autoident' not found in the response")

        browser_matrix = response['settings']['autoident']['web']['browserSupportMatrix']

        expected_browsers = {
            'desktop': {
                'default': {'chrome': {'min': '75'}},
                'linux': {'chrome': {'min': '75'}},
                'macintosh': {'safari': {'min': '11'}, 'chrome': {'min': '75'}},
                'windows': {'edge': {'min': '80'}, 'chrome': {'min': '75'}, 'firefox': {'min': '78'}}
            },
            'mobile': {
                'default': {'chrome': {'min': '75'}},
                'android': {'samsung': {'min': '-1'}, 'chrome': {'min': '75'}, 'firefox': {'min': '78'}},
                'macintosh': {'safari': {'min': '11'}},
                'ios': {'safari': {'min': '11'}, 'chrome': {'min': '75'}}
            }
        }

        self.assertEqual(browser_matrix, expected_browsers, "Browser matrix does not match the expected values")


if __name__ == '__main__':
    unittest.main()
