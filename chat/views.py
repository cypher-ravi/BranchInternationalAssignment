from django.shortcuts import render,redirect
from django.db.models import Q
from .models import Room,CustomUser,Message

# Create your views here.
def index(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        role = request.POST.get("user")
        print(role)
        user = CustomUser.objects.filter(username=username).first()
        if role == 'customer':
            if user:
                db_room =Room.objects.get(Q(user1=user) | Q(user2=user))
                return redirect("chat:room",room_name=db_room.room_name,username=username)
            else:
                user_created = CustomUser.objects.create(username=username)
                db_room = Room.objects.create(room_name=f'room_{username}',user1=user_created)
                return redirect("chat:room",room_name=db_room.room_name,username=username)
        elif role=="agent":
            return redirect("chat:agent",agent_name=username)


    return render(request, "chat/index.html")

def room(request, room_name,username):
    room = Room.objects.filter(room_name=room_name).first()
    agent = CustomUser.objects.filter(username=username).first()

    if room:
        if room.user1 == None:
            room.user1 = agent
            # room.room_name = f"room_name_{room.user1.username}_{agent.username}"
            room.save()
            messages = Message.objects.filter(room=room) #
            for message in messages:
                message.has_seen=True
                message.save()
            return render(request, "chat/room.html", {"room_name": room.room_name,"username": username})
        elif room.user2 == None:
            room.user2 = agent
            # room.room_name = f"room_name_{room.user2.username}_{agent.username}"
            room.save()
            return render(request, "chat/room.html", {"room_name": room.room_name,"username": username})

    return render(request, "chat/room.html", {"room_name": room_name,"username": username})


def agent(request, agent_name):
    
        # user_created = CustomUser.objects.create(username=agent_name,user_role="agent")
    user = CustomUser.objects.filter(username=agent_name).first()
    # rooms = Room.objects.none()

    # rooms_medium =Room.objects.filter(users_room__has_seen=False,users_room__priority='medium')
    rooms_high =Room.objects.filter(users_room__has_seen=False,users_room__priority='high')
    rooms_low =Room.objects.filter(users_room__has_seen=False,users_room__priority='low')
    rooms =Room.objects.filter(users_room__has_seen=False)
    
    # rooms_high.union(rooms_medium,rooms_low,rooms)
   
    
    
    # rooms_high.filter(Q(user1=user)|Q( user2=user))

    # rooms = set(rooms_high)
    # print(rooms_high)

   
    if user:
        return render(request, "chat/agent.html",{
        "rooms":set(rooms),
        "username":user.username,
    })
    else:
        user_created = CustomUser.objects.create(username=agent_name)
        return render(request, "chat/agent.html",{
        "rooms":rooms,
        "username":user_created.username,
    })

        # return redirect("chat:room",room_name=db_room.room_name)





