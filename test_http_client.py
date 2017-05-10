import unittest, requests

from httpclient import get_posts, describe_post, add_post


class TestHttpClient(unittest.TestCase):
    url = "https://jsonplaceholder.typicode.com/posts/"

    def test_get_post(self):
        """ test is the get posts returns a json object"""
        self.assertIsInstance(get_posts(), requests.models.Response)

    def test_describe_post(self):
        self.assertIsInstance(describe_post(6), requests.models.Response)

    def test_describe_post_limits(self):
        with self.assertRaises(IndexError):
            describe_post(200)

    def test_update_post_limits(self):
        with self.assertRaises(IndexError):
            describe_post(200)

    def test_add_post_returns_object(self):
        self.assertIsInstance(add_post("title", "body"), requests.models.Response)


if __name__ == '__main__':
    unittest.main()