import unittest
import azure.functions as func

from app.HttpTrigger1 import my_function


class TestFunction(unittest.TestCase):
    def test_my_function(self):
        req = func.HttpRequest(
            method='GET',
            body=None,
            url='/api/HttpTrigger',
            params={'name': 'World'})

        resp = my_function(req)

        self.assertEqual(
            resp.get_body(),
            b'Hello World',
        )
