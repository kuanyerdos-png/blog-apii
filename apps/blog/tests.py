from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase


class BlogTests(APITestCase):
    def test_get_posts(self):
        url = reverse("post-list")
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
