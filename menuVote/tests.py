from datetime import date, timedelta

from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Restaurant, Menu, Employee, Vote


class AuthenticationTests(APITestCase):
	def test_token_refresh(self):
		response = self.client.post('/api/token/refresh/', {
			'refresh': 'eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTY4Mzk5MzYzNCwiaW'
			           'F0IjoxNjgzOTA3MjM0LCJqdGkiOiJhNDg0NDdkODA5NTY0YmNhOTQyOGMzMjk4ZDBmNjhhZCIsInVzZXJfaWQiOjF9.jLFL'
			           '-cppzhR6KB0btPs-eYmT1-lPxOy7CDXMQ1ExpoM'})
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertIn('access', response.data)


class RestaurantTests(APITestCase):
	def setUp(self):
		self.restaurant = Restaurant.objects.create(name='Test Restaurant', address='Test Address',
		                                            phone_number='1234567890')
		self.url = reverse('menuVote:restaurant_list')

	def test_create_restaurant(self):
		response = self.client.post(self.url, {'name': 'Test Restaurant', 'address': 'Test Address',
		                                       'phone_number': '1234567890'})
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Restaurant.objects.count(), 2)


class MenuTests(APITestCase):
	def setUp(self):
		self.restaurant = Restaurant.objects.create(name='Test Restaurant', address='Test Address',
		                                            phone_number='1234567890')
		self.menu = Menu.objects.create(restaurant=self.restaurant, date=date.today(), items='Test Menu')
		self.url = reverse('menuVote:menu_upload')

	def test_upload_menu(self):
		data = {'restaurant': self.restaurant.id, 'date': date.today(), 'items': 'Test Menu'}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Menu.objects.count(), 2)

	def test_upload_menu_next_day(self):
		data = {'restaurant': self.restaurant.id, 'date': date.today() + timedelta(1), 'items': 'Test Menu'}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Menu.objects.count(), 2)

	def test_get_current_day_menu(self):
		response = self.client.get(reverse('menuVote:current_menu', kwargs={'restaurant_id': self.restaurant.id}))
		self.assertEqual(response.status_code, status.HTTP_200_OK)
		self.assertEqual(response.data, {'id': self.restaurant.id, 'date': str(date.today()), 'items': 'Test Menu',
		                                 'restaurant': self.restaurant.id})


class EmployeeTests(APITestCase):
	def test_create_employee(self):
		data = {'name': 'John Doe', 'email': '123@123.13', 'password': '123456', 'is_active': True}
		response = self.client.post(reverse('menuVote:employee_create'), data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Employee.objects.count(), 1)


class VoteTests(APITestCase):
	def setUp(self):
		self.restaurant = Restaurant.objects.create(name='Test Restaurant', address='Test Address',
		                                            phone_number='1234567890')
		self.menu = Menu.objects.create(date=date.today(), items='Test Menu', restaurant=self.restaurant)
		self.employee = Employee.objects.create(name='John Doe', email='123@123.13', password='123456', is_active=True)
		self.url = reverse('menuVote:vote_create')

	def test_create_vote(self):
		data = {'menu': self.menu.id, 'employee': self.employee.id}
		response = self.client.post(self.url, data, format='json')
		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Vote.objects.count(), 1)
