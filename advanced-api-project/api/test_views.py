from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from .models import Author, Book

class BookAPITests(APITestCase):
    """
    Test suite for the Book API endpoints.
    """

    def setUp(self):
        """
        Set up the test data for all test cases.
        """
        # Create a test user for authenticated requests
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.token = self.get_token(self.user)

        # Create author and book instances for testing
        self.author1 = Author.objects.create(name="Chinua Achebe")
        self.author2 = Author.objects.create(name="Toni Morrison")
        self.book1 = Book.objects.create(title="Things Fall Apart", author=self.author1, publication_year=1958)
        self.book2 = Book.objects.create(title="Beloved", author=self.author2, publication_year=1987)
        self.book3 = Book.objects.create(title="The River Between", author=self.author1, publication_year=1965)
        
    def get_token(self, user):
        """
        Helper method to get an authentication token for a user.
        """
        from rest_framework.authtoken.models import Token
        token, _ = Token.objects.get_or_create(user=user)
        return token.key
        
    def test_list_books(self):
        """
        Ensure we can retrieve a list of books without authentication.
        """
        response = self.client.get('/api/books/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 3)

    def test_retrieve_book(self):
        """
        Ensure we can retrieve a single book by its ID.
        """
        response = self.client.get(f'/api/books/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['title'], "Things Fall Apart")

    def test_create_book_authenticated(self):
        """
        Ensure a new book can be created by an authenticated user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        data = {'title': 'New Book Title', 'author': self.author2.id, 'publication_year': 2024}
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Book.objects.count(), 4)

    def test_create_book_unauthenticated(self):
        """
        Ensure a new book cannot be created by an unauthenticated user.
        """
        data = {'title': 'Forbidden Book', 'author': self.author1.id, 'publication_year': 2024}
        response = self.client.post('/api/books/create/', data, format='json')
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_update_book_authenticated(self):
        """
        Ensure an existing book can be updated by an authenticated user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        updated_data = {'title': 'Updated Title', 'author': self.author1.id, 'publication_year': 2020}
        response = self.client.put(f'/api/books/update/{self.book1.id}/', updated_data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.book1.refresh_from_db()
        self.assertEqual(self.book1.title, 'Updated Title')

    def test_delete_book_authenticated(self):
        """
        Ensure an existing book can be deleted by an authenticated user.
        """
        self.client.credentials(HTTP_AUTHORIZATION=f'Token {self.token}')
        response = self.client.delete(f'/api/books/delete/{self.book1.id}/')
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Book.objects.count(), 2)

    def test_filter_by_year(self):
        """
        Ensure the API can filter books by publication year.
        """
        response = self.client.get('/api/books/', {'publication_year': 1958})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Things Fall Apart')

    def test_search_by_title(self):
        """
        Ensure the API can search for a book by its title.
        """
        response = self.client.get('/api/books/', {'search': 'Beloved'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['title'], 'Beloved')

    def test_order_by_year_descending(self):
        """
        Ensure the API can order books by publication year in descending order.
        """
        response = self.client.get('/api/books/', {'ordering': '-publication_year'})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        # Check if the books are in the correct order: 1987, 1965, 1958
        self.assertEqual(response.data[0]['publication_year'], 1987)
        self.assertEqual(response.data[1]['publication_year'], 1965)
        self.assertEqual(response.data[2]['publication_year'], 1958)