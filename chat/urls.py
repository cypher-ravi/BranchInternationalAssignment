from django.urls import path

from . import views
from .utils import create_message_data

app_name="chat"
urlpatterns = [
    path("", views.index, name="index"),
    path("roomee/<str:room_name>/<str:username>/", views.room, name="room"),
    path("agent-user/<str:agent_name>/", views.agent, name="agent"),
    path("create-data/",create_message_data),
]