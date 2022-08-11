from channels.generic.websocket import WebsocketConsumer
from asgiref.sync import async_to_sync 
import json


class TestConsumer(WebsocketConsumer):



    # this method is called with there is any incomming connections
    def connect(self):
        self.room_name = "test_consumers"
        self.room_group_name = 'test_consumers_group'
        async_to_sync(self.channel_layer.group_add)(
            self.room_group_name,self.channel_name
        )
        self.accept()
        #to send data from backend to frontend always use self.send() methode
        self.send(text_data=json.dumps({'status':'connected with django chanels'}))

    def receive(self, text_data):
        self.send(text_data=json.dumps({'status':'we got you'}))

    def disconnect(self, close_code):
        print('disconnected')

        # Called when the socket closes

    def send_notification(self , event):
        print("notification")
        print(event.get('value'))
        data = json.loads(event.get('value'))
        self.send(text_data=json.dumps({'payload': data}))
        print(event)
