from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from .views import (
    RestaurantView,
    MenuView,
    EmployeeView,
    CurrentMenuView,
    CurrentResultsView,
    VoteView,
)

app_name = 'menuVote'

urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('api/restaurants/', RestaurantView.as_view(), name='restaurant_list'),
    path('api/restaurants/<int:restaurant_id>/results/', CurrentResultsView.as_view(), name='current_results'),
    path('api/menus/', MenuView.as_view(), name='menu_upload'),
    path('api/menus/<int:restaurant_id>/', CurrentMenuView.as_view(), name='current_menu'),
    path('api/employees/', EmployeeView.as_view(), name='employee_create'),
    path('api/votes/', VoteView.as_view(), name='vote_create'),
]
