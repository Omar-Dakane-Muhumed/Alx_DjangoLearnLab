from django.test import TestCase, Client
from django.contrib.auth.models import User

class CSRFProtectionTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_form_submission_with_csrf(self):
        response = self.client.get('/register/')
        csrf_token = response.context['csrf_token']
        response = self.client.post('/register/', {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
            'csrfmiddlewaretoken': csrf_token,
        })
        self.assertEqual(response.status_code, 200)  # Or a redirect status like 302

    def test_form_submission_without_csrf(self):
        response = self.client.post('/register/', {
            'username': 'testuser',
            'password1': 'securepassword123',
            'password2': 'securepassword123',
        })
        self.assertEqual(response.status_code, 403)

