from users.models import CustomUserfrom django.test import TestCase
from django.urls import reverse


class RegistrationTestCase(TestCase):
    def test_user_account_is_created(self):
        # Post data to the registration endpoint
        response = self.client.post(reverse('users:register'), {
            'username': 'test',
            'email': 'email@gmail.com',
            'first_name': 'testName',
            'last_name': 'testNameLast',
            'password': '4444as4da4sd4as4dasdasdasdasdgv',
        })

        # Ensure the response status code is as expected (e.g., 201 or 302)
        self.assertEqual(response.status_code, 201)  # or 302 if it's redirecting

        # Fetch the user from the database
        user = User.objects.get(username='test')

        # Check if the user's data matches what was posted
        self.assertEqual(user.email, 'email@gmail.com')
        self.assertEqual(user.username, 'test')
        self.assertEqual(user.first_name, 'testName')
        self.assertEqual(user.last_name, 'testNameLast')

        # Check if the password was set correctly
        self.assertTrue(user.check_password('4444as4da4sd4as4dasdasdasdasdgv'))
