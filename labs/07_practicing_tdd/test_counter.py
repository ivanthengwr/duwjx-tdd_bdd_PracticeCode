"""
Test Cases for Counter Web Service
"""
from unittest import TestCase
import status
from counter import app

class CounterTest(TestCase):
    """Test Cases for Counter Web Service"""

    def setUp(self):
        self.client = app.test_client()

    def test_create_a_counter(self):
        """It should create a counter"""
        result = self.client.post("/counters/foo")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        self.assertIn("foo", data)
        self.assertEqual(data["foo"], 0)

    def test_duplicate_counter(self):
        """It should return an error for duplicates"""
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        result = self.client.post("/counters/bar")
        self.assertEqual(result.status_code, status.HTTP_409_CONFLICT)
    
    def test_update_a_counter(self):
        """It should increment the counter"""
        result = self.client.post("/counters/lee")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        data = result.get_json()
        baseline = data["lee"]

        #Update the counter
        result = self.client.put("/counters/lee")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["lee"], baseline+1)
        
    def test_read_a_counter(self):
        """It should read from the counter"""
        result = self.client.post("/counters/lol")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)
        
        #Read the counter
        result = self.client.get("/counters/lol")
        self.assertEqual(result.status_code, status.HTTP_200_OK)
        data = result.get_json()
        self.assertEqual(data["lol"], 0)

    def test_delete_a_counter(self):
        """It should delete a counter"""
        result = self.client.post("/counters/del")
        self.assertEqual(result.status_code, status.HTTP_201_CREATED)

        #delete a counter
        result = self.client.delete("/counters/del")
        self.assertEqual(result.status_code, status.HTTP_204_NO_CONTENT)

