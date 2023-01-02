from django.db import models
from django.contrib.auth import get_user_model
# from .managers import RoomManager

from django.db.models import Q





class CustomUser(models.Model):
    USER_ROLE = (
        ("agent","agent"),
        ("customer","customer")
    )
    username= models.CharField(max_length=255)
    user_role = models.CharField(choices=USER_ROLE, max_length=50,blank=True,null=True)

    def __str__(self):
        return self.username

class TrackingModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)
    updated_at = models.DateTimeField(auto_now_add=True,blank=True,null=True)

    class Meta:
        abstract = True

class Room(TrackingModel):
    ROOM_TYPE = (
        ('personal','Personal'),
        ('group','Group'),
    )
    room_name = models.CharField(max_length=100, unique=True)
    room_type = models.CharField(max_length=15,choices=ROOM_TYPE,default="group",blank=True, null=True)
    user1 = models.ForeignKey(CustomUser,related_name='user1', on_delete=models.CASCADE,blank=True,null=True)
    user2 = models.ForeignKey(CustomUser,related_name='user2', on_delete=models.CASCADE,unique=False,blank=True, null=True)
    room_taken = models.BooleanField(default=False,null=True,blank=True)
    
 
    # objects = RoomManager()
    
    
    def __str__(self):
        # if self.room_type == 'personal':
        #     return f'{self.user1}-personal-room'
        # elif self.room_type == 'group':
        #     return f'{self.user1}-and-{self.user2}-room'

        return f'{self.room_name}'

    


# class MessageManager(models.Manager):
    
#     def fetch_last_10_messages(self,room_name,user1,user2):
#         room = Room.objects.filter(room_name=room_name)
#         room = room.filter(Q(user1__id=user1,user2__id=user2) | Q(user1__id=user2,user2__id=user1))
        
#         if room.exists():
#             return Message.objects.filter(room=room[0]).order_by('timestamp').all()
#         else:
#             raise ValueError('No room exist')

class Message(TrackingModel):
    PRIORITY = {
        ('high', 'high'),
        ('medium', 'medium'),
        ('low', 'low'),
    }
    room = models.ForeignKey(Room, related_name='users_room', on_delete=models.CASCADE, blank=True, null=True)
    sender = models.ForeignKey(CustomUser,related_name='sender', on_delete=models.CASCADE, blank=True, null=True)
    receiver = models.ForeignKey(CustomUser,related_name='receiver', on_delete=models.CASCADE,  blank=True, null=True)
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)
    has_seen = models.BooleanField(default=False,blank=True,null=True)
    priority = models.CharField(choices=PRIORITY, max_length=50,blank=True,null=True)
    
    
    # objects=MessageManager()
    
    
    def __str__(self):
        return f'{self.sender.username}'
    
    def save(self, *args, **kwargs):
                
        super(Message, self).save(*args, **kwargs)
        
       



class Connected(models.Model):
    room = models.ForeignKey(Room, related_name='connected_room', on_delete=models.CASCADE)
    sender = models.ForeignKey(CustomUser,related_name='connected_user', on_delete=models.CASCADE)
    is_connected_to_room = models.BooleanField(default=False)

    

    class Meta:
        verbose_name = ("Connected with room")
        verbose_name_plural = ("Connected User with room")

    def __str__(self):
        return self.room.room_name