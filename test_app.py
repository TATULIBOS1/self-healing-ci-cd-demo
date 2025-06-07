import unittest
import app

class TestApp(unittest.TestCase):
    def test_home(self):
        with app.app.test_client() as client:
            response = client.get('/')
            self.assertEqual(response.status_code, 200)

if __name__ == '__main__':
    unittest.main()
