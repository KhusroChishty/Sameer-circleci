import unittest
from app import create_app

class TestViews(unittest.TestCase):
    def setUp(self):
        self.app = create_app().test_client()

    def test_index(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
        self.assertIn(b'Hello, World!', response.data)

if __name__ == '__main__':
    unittest.main()
