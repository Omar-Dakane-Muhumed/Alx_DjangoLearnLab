

from rest_framework.test import APITestCase
from rest_framework import status
from django.urls import reverse
from api.models import Book
from api.serializers import BookSerializer


class BookAPITests(APITestCase):

    def setUp(self):
        self.book1 = Book.objects.create(title="Book One", author="Author A", publication_year=2020)
        self.book2 = Book.objects.create(title="Book Two", author="Author B", publication_year=2021)
        self.valid_data = {"title": "New Book", "author": "Author C", "publication_year": 2022}
        self.update_data = {"title": "Updated Book", "author": "Author D", "publication_year": 2023}
        self.url_list = reverse('book-list')  # Update with your URL names
        self.url_detail = lambda pk: reverse('book-detail', args=[pk])


def test_create_book(self):
    response = self.client.post(self.url_list, self.valid_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_201_CREATED)
    self.assertEqual(Book.objects.count(), 3)
    self.assertEqual(Book.objects.last().title, "New Book")


def test_retrieve_book(self):
    response = self.client.get(self.url_detail(self.book1.id))
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.assertEqual(response.data['title'], self.book1.title)


def test_update_book(self):
    response = self.client.put(self.url_detail(self.book1.id), self.update_data, format='json')
    self.assertEqual(response.status_code, status.HTTP_200_OK)
    self.book1.refresh_from_db()
    self.assertEqual(self.book1.title, "Updated Book")


def test_delete_book(self):
    response = self.client.delete(self.url_detail(self.book1.id))
    self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
    self.assertEqual(Book.objects.count(), 1)
    self.client.login()

        def test_unauthenticated_access(self):
        self.client.logout()
        response = self.client.get("/api/books/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
