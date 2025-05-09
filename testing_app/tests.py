from rest_framework.test import APITestCase
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .models import PrivateItem  

class PrivateItemAccessTests(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(username='testuser', password='testpass123')
        self.url = '/api/private-items/' 

    def get_token(self):
        refresh = RefreshToken.for_user(self.user)
        return str(refresh.access_token)

    def test_unauthenticated_access(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


    def test_authenticated_access(self):
        token = self.get_token()
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {token}')
        
        PrivateItem.objects.create(name="Secret", description="Only for me", owner=self.user)
        
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.data, list) 
