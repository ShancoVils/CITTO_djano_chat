# Импорт для работы с JSON
import json
from threading import Event 
# Импорт для асинхронного программирования
from channels.generic.websocket import AsyncWebsocketConsumer
# Импорт для работы с БД в асинхронном режиме
from channels.db import database_sync_to_async
# Импорт модели сообщений
from .models import Message
import redis
 
# Класс ChatConsumer
class ChatConsumer(AsyncWebsocketConsumer):
    
    # Метод подключения к WS
    async def connect(self):
        # Назначим пользователя в комнату
        self.room_name = self.scope['url_route']['kwargs']['room_name']
        self.room_group_name = self.room_name
        # Добавляем новую комнату
        await self.channel_layer.group_add(
            self.room_group_name,
            self.channel_name
        )
        print(self.room_group_name)
        print(self.channel_name)
        # Принимаем подключаем
        await self.accept()

    # def chat_message(self, event):
    #     redis_get = redis.Redis()
    #     message_info = redis_get.lrange(self.room_group_name, 0,-1)
    #     message_info = event['message_info']

    #     self.send(text_data=json.dumps({
    #             'message_info': message_info,
    #         }, ensure_ascii=False))

    

    # Метод для отключения пользователя
    async def disconnect(self, close_code):
        # Отключаем пользователя
        await self.channel_layer.group_discard(
            self.room_group_name,
            self.channel_name
        )
 
    # Декоратор для работы с БД в асинхронном режиме
    @database_sync_to_async
    # Функция для создания нового сообщения в БД
    def new_message(self, message, name_user):
        # Создаём сообщение в БД
        Message.objects.create(text=message, nickname = name_user)
 
    # Принимаем сообщение от пользователя
    async def receive(self, text_data=None, bytes_data=None):
        # Форматируем сообщение из JSON
        text_data_json = json.loads(text_data)
        # Получаем текст сообщения
        name_user = text_data_json['nickname']
        message = text_data_json['message']
        time_message = text_data_json['time_message']
        
        # Добавляем сообщение в БД 
        await self.new_message(message=message, name_user = name_user)
        
        # Отправляем сообщение 
        await self.channel_layer.group_send(
            self.room_group_name,
            {
                'type': 'chat_message',
                'nickname': name_user,
                'message': message,
                'time_message':time_message
            }
        )
        r = redis.Redis()
        message_info = "{0}: {1}".format(name_user,message)
        r.rpush(self.room_group_name, message_info)

    
    # Метод для отправки сообщения клиентам
    async def chat_message(self, event):
        # Получаем сообщение от receive
        nickname = event['nickname']
        message = event['message']
        time_message = event['time_message']
        # Отправляем сообщение клиентам
        await self.send(text_data=json.dumps({
            'nickname': nickname,
            'message': message,
            'time_message':time_message
        }, ensure_ascii=False))



