from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class TodoTestCase(APITestCase):

    def setUp(self):
        self.data = {
            "id": "123",
            "label": "helloworld",
            "done": False
        }
        self.response = self.client.post(reverse("task-create"), self.data)

    def test_create(self):
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)

    def test_read(self):
        res = self.client.get(reverse("task-list"))
        self.assertEqual(res.data[0]["label"], self.data["label"])

    def test_update(self):
        new_data = {
            "id": "123",
            "label": "goodbye",
            "done": False
        }
        res = self.client.post("/api/task-update/123/", new_data)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data["label"], new_data["label"])

    def test_delete(self):
        res = self.client.delete("/api/task-delete/123/")
        self.assertEqual(res.status_code, status.HTTP_200_OK)

