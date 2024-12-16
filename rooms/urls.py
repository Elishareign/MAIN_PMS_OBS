from django.urls import path
from . import views 
from .views import RoomTypeCreateView, get_room_types


urlpatterns = [
    # Route to render the React app
    path('room/', views.index, name='index'),

    # Route to fetch the list of rooms via API
    path('api/rooms/', views.RoomListView.as_view(), name='room-list'),

    path('api/roomtype/', RoomTypeCreateView.as_view(), name='create_room_type'),

    path('api/rooms/', views.create_room, name='create_room'),
    
    path('get_room_types/', get_room_types, name='get_room_types'),
]
