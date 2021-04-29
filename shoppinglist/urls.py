from django.urls import path
from .views import ShoppinglistListView, ShoppinglistDetailView
urlpatterns = [
	path('post/<int:pk>/', ShoppinglistDetailView.as_view(), name='post_detail'),
	path('', ShoppinglistListView.as_view(), name='home'),
]