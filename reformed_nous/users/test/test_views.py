from django.core.urlresolvers import reverse
from django.forms.models import model_to_dict
from django.contrib.auth.hashers import check_password
from rest_framework.test import APITestCase
from faker import Faker
from users.models import User
from .factories import UserFactory

fake = Faker()


class TestUserAPI(APITestCase):
    """
    Tests the /users endpoint.
    """

    def setUp(self):
        self.url = reverse('user-list')
        self.user_data = model_to_dict(UserFactory.build())

    def test_post_request_with_no_data_fails(self):
        response = self.client.post(self.url, {})
        assert response.status_code == 400

    def test_post_request_with_valid_data_succeeds(self):
        response = self.client.post(self.url, self.user_data)
        assert response.status_code == 201

        user = User.objects.get(pk=response.data.get('id'))
        assert user.username == self.user_data.get('username')
        assert check_password(self.user_data.get('password'), user.password)


class TestUserDetailAPI(APITestCase):
    def setUp(self):
        self.user = UserFactory()
        self.url = reverse('user-detail', kwargs={'pk': self.user.pk})
        self.client.credentials(
            HTTP_AUTHORIZATION='Token {}'.format(self.user.auth_token)
        )

    def test_get_request_returns_a_given_user(self):
        response = self.client.get(self.url)
        assert response.status_code == 200

    def test_put_request_updates_a_user(self):
        new_first_name = fake.first_name()
        payload = {'first_name': new_first_name}
        response = self.client.put(self.url, payload)
        assert response.status_code == 200

        user = User.objects.get(pk=self.user.id)
        assert user.first_name == new_first_name
