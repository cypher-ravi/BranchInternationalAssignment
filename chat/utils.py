from django.shortcuts import render
import pandas as pd
from .models import Message,CustomUser,Room
from django.http import HttpResponse
from django.db.models import Q

import names
# Create your views here.
df = pd.read_csv('D:/projects/finaltry/data.csv',usecols=[0,1,2])

def create_message_data(request):
    for row in df["content"]:
        user = CustomUser.objects.create(username=names.get_first_name())
        room = Room.objects.create(room_name=f"room_name_{user.username}",user1=user)
        Message.objects.create(content=row,room=room,sender=user)  

    return HttpResponse("done")




   


 
     

