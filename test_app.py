import unittest

from app import app


class AppTestCase(unittest.TestCase):
    def setUp(self):
        self.client = app.test_client()

    def test_homepage_shows_project_title_and_running_status(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertIn(b"My DevOps CI/CD Project", response.data)
        self.assertIn(b"Application is running", response.data)

    def test_health_endpoint_returns_healthy_status(self):
        response = self.client.get("/health")

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.get_json(), {"status": "healthy"})


if __name__ == "__main__":
    unittest.main()
