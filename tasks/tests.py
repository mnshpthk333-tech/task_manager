from rest_framework.test import APITestCase
from django.contrib.auth.models import User
from rest_framework import status
from .models import Task
from rest_framework_simplejwt.tokens import RefreshToken


class TaskTests(APITestCase):
    def setUp(self):
        # Create a user
        self.user = User.objects.create_user(
            username='testuser', password='pass123')

        # Generate JWT token for the user
        refresh = RefreshToken.for_user(self.user)
        self.token = str(refresh.access_token)

        # Include token in the header
        self.client.credentials(HTTP_AUTHORIZATION=f'Bearer {self.token}')

    def test_create_task(self):
        response = self.client.post(
            '/api/tasks/', {'title': 'Test Task', 'description': 'Test Desc'})
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data['title'], 'Test Task')

    def test_get_tasks(self):
        Task.objects.create(title='Task 1', user=self.user)
        response = self.client.get('/api/tasks/')

    # Check if pagination is applied
        if isinstance(response.data, dict) and 'results' in response.data:
           tasks_list = response.data['results']
        else:
           tasks_list = response.data  # fallback if pagination not applied
           
           self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(tasks_list), 1)
        self.assertEqual(tasks_list[0]['title'], 'Task 1')
