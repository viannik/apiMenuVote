from datetime import date

from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from .models import Menu, Vote
from .serializers import RestaurantSerializer, MenuSerializer, EmployeeSerializer, VoteSerializer


class RestaurantView(APIView):
	"""
	API endpoint for creating a new restaurant.
	"""

	@staticmethod
	def post(request):
		serializer = RestaurantSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class MenuView(APIView):
	"""
	API endpoint for uploading a menu for a restaurant for a specific date.
	"""

	@staticmethod
	def post(request):
		serializer = MenuSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class EmployeeView(APIView):
	"""
	API endpoint for creating a new employee.
	"""

	@staticmethod
	def post(request):
		serializer = EmployeeSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class CurrentMenuView(APIView):
	"""
	API endpoint for getting the current day's menu for a restaurant.
	"""

	@staticmethod
	def get(request, restaurant_id):
		today = date.today()
		menu = Menu.objects.filter(restaurant_id=restaurant_id, date=today).first()
		if menu:
			serializer = MenuSerializer(menu)
			return Response(serializer.data)
		return Response(status=status.HTTP_404_NOT_FOUND)


class CurrentResultsView(APIView):
	"""
	API endpoint for getting the current day's voting results for a menu.
	"""

	@staticmethod
	def get(request, restaurant_id):
		today = date.today()
		menus = Menu.objects.filter(restaurant_id=restaurant_id, date=today)
		results = []
		for menu in menus:
			serializer = MenuSerializer(menu)
			result = serializer.data
			result['votes'] = Vote.objects.filter(menu_id=menu.id).count()
			results.append(result)
		results.sort(key=lambda x: x['votes'], reverse=True)

		return Response(results)


class VoteView(APIView):
	"""
	API endpoint for employees to vote for a menu.
	"""

	@staticmethod
	def post(request):
		serializer = VoteSerializer(data=request.data)
		if serializer.is_valid():
			serializer.save()
			return Response(serializer.data, status=status.HTTP_201_CREATED)
		return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
