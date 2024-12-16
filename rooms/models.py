from django.db import models

class RoomType(models.Model):
    room_type_name = models.CharField(max_length=100)
    base_price = models.DecimalField(max_digits=10, decimal_places=2)
    capacity = models.IntegerField()
    room_size = models.IntegerField()  
    room_description = models.TextField()
    amenities = models.JSONField(default=dict)  
    facilities = models.JSONField(default=dict)  
    image_path = models.ImageField(upload_to='room_images/', null=True, blank=True)  

    def __str__(self):
        return self.room_type_name

class Room(models.Model):
    room_number = models.IntegerField()
    floor_number = models.IntegerField()
    room_status = models.CharField(max_length=20)
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)

    def __str__(self):
        return self.room_number

