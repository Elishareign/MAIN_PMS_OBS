from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Room, RoomType
from .serializers import RoomSerializer, RoomTypeSerializer
from django.shortcuts import render
from rest_framework import status 
from rest_framework.decorators import api_view
from django.http import JsonResponse, HttpRequest



def index(request):
    return render(request, 'index.html')


class RoomListView(APIView):
    def get(self, request):
        rooms = Room.objects.all()
        serializer = RoomSerializer(rooms, many=True)
        return Response(serializer.data)
    
class RoomTypeCreateView(APIView):
    def post(self, request):
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
@api_view(['POST'])
def create_room_type(request):
    try:
        print(request.data)  # Log the incoming data
        serializer = RoomTypeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response({"message": "Room type created successfully"}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    except Exception as e:
        return Response({"message": f"Failed to add room type: {str(e)}"}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    
@api_view(['POST'])
def create_room(request):
    if request.method == 'POST':
        serializer = RoomSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
def get_room_types(request):
    room_types = RoomType.objects.values("id", "room_type_name")  
    room_types_data = list(room_types) 
    print(room_types_data)  
    return JsonResponse(room_types_data, safe=False)