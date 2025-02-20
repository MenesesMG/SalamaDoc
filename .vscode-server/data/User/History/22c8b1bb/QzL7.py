from django.test import TestCase
from myapp.forms import CreateUserForm

class TestForms(TestCase):
    def test_create_user_form_valid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        
    def test_create_user_form_invalid_data(self):
        form_data = {
            'username': 'testuser',
            'email': 'test@example.com',
            'password1': 'testpassword',
            'password2': 'testpassword1',
        }
        form = CreateUserForm(data=form_data)
        self.assertTrue(form.is_valid())
        