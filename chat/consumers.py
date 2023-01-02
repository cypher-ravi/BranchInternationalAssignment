


import json

from asgiref.sync import async_to_sync
from channels.generic.websocket import WebsocketConsumer
from .models import Message,Room,CustomUser


class ChatConsumer(WebsocketConsumer):
    def fetch_messages(self, data):
       
        room = Room.objects.filter(room_name=self.room_name).first()
        messages = Message.objects.filter(room=room)
        for message in messages:
            message.has_seen = True
            message.save()

        content = {
            'command': 'fetching_messages',
            'messages': self.messages_to_json(messages)
        }
        self.send_message(content)

    def send_message(self, message):
        self.send(text_data=json.dumps(message))

    def connect(self):
        self.room_name = self.scope["url_route"]["kwargs"]["room_name"]
        self.sender = self.scope["url_route"]["kwargs"]["username"]
        self.room_group_name = "chat_%s" % self.room_name

        # Join room group
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name, self.channel_name
        )

        self.accept()

    def disconnect(self, close_code):
        # Leave room group
        async_to_sync(self.channel_layer.group_discard)(
            self.room_group_name, self.channel_name
        )
    def new_message(self, data):
        message = data['message']
        user = CustomUser.objects.filter(username=self.sender).first()
        room = Room.objects.filter(room_name=self.room_name).first()
        Message.objects.create(room=room, content=message,sender=user)

        content = {
             'command': 'new_message',
             'message': message,
            #  'message': self.message_to_json(message)
        }

        self.send_chat_message(content)

    def messages_to_json(self, messages):
        result = []
        for message in messages:
            result.append(self.message_to_json(message))
        return result

    def message_to_json(self, message):
        return {
            # 'id': message.id,
            'sender': message.sender.username,
            'content': message.content,
            'timestamp': str(message.timestamp)
        }

    commands = {
        'fetch_messages': fetch_messages,
        'new_message': new_message,
       
    }
    
    # Receive message from WebSocket
    def receive(self, text_data):
        # text_data_json = json.loads(text_data)
        # message = text_data_json["message"]
        data = json.loads(text_data)
        self.commands[data['command']](self, data)

    def send_chat_message(self, message):
        # Send message to room group
        async_to_sync(self.channel_layer.group_send)(
            self.room_group_name, {"type": "chat_message", "message": message}
        )

    # Receive message from room group
    def chat_message(self, event):
        message = event["message"]

        # Send message to WebSocket
        self.send(text_data=json.dumps(message))