#Импортируем библиотеку vk_api
import vk_api

#Импортируем нужные классы.
from vk_api.longpoll import VkLongPoll, VkEventType

#https://www.blast.hk/threads/81201/

#Создаем токен в отдельной переменной.
token = '39e7dfe270e6428f1abe7bd9d4f040990838dbc3dc02488997c5b3f4c2baa0c3ba1ce120b10758a01f7fe'

#Подключаем токен и истанцируем longpoll
bh = vk_api.VkApi(token = token)
give = bh.get_api()
longpoll = VkLongPoll(bh)

def blasthack(id, text):
    """Функция для ответа"""
    bh.method('messages.send', {'user_id': id, 'message': text, 'random_id': 0})

for event in longpoll.listen():
    """ """
    if event.type == VkEventType.MESSAGE_NEW:
        """ """

        if event.to_me:
            """ """
            
            message = event.text.lower() #

            id = event.user_id           #

            if message == 'hellow':
                """ """
                blasthack(id, 'Hellow, i`m a bot.')

            elif message == 'how are you?':
                """ """
                blasthack(id, 'I`m fine, how are you?')

            else:
                """ """
                blasthack(id, 'I don`t understend you.')