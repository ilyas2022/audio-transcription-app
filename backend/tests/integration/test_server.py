import unittest
import os
import sys

sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '../..')))

from app import app

class ServerIntegrationTests(unittest.TestCase):
    def setUp(self):
        self.app = app.test_client()
        self.app.testing = True

    def test_server_running(self):
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)
    
    def test_static_files(self):
	pass
