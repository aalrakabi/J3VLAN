from django.urls import path
from .views import (
	ShoppinglistListView, 
	ShoppinglistDetailView, 
	ShoppinglistCreateView, 
	ShoppinglistUpdateView,
	ShoppinglistDeleteView,
)

urlpatterns = [
	path('post/<int:pk>/delete/', ShoppinglistDeleteView.as_view(), name='post_delete'),
	path('post/<int:pk>/edit/', ShoppinglistUpdateView.as_view(), name='post_edit'),
	path('post/new/', ShoppinglistCreateView.as_view(), name='post_new'), 
	path('post/<int:pk>/', ShoppinglistDetailView.as_view(), name='post_detail'),
	path('', ShoppinglistListView.as_view(), name='home'),
]