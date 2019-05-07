from django.shortcuts import render
from django.http import JsonResponse
# Create your views here.
from chat.models import history
from pubnub import Pubnub
import time

def start(request):
    chatroom = request.GET.get('room')
    user_name = request.GET.get('name')
    #print("Hello {}. Welcome to {} chatroom".format(user_name, chatroom))
    
    pn = Pubnub(publish_key="demo", subscribe_key="demo", ssl_on=False, uuid=user_name)
    
    channel = chatroom

    def _callback(message, channel):
        if message['user_name'] != user_name:
            print("\n{}: {}".format(message['user_name'], message['message']))
            print("{}: ".format(user_name))

    def _history_callback(message):
        print (message)
        print (len(message[0]))
        time.sleep(5)
        history.objects.all().delete()
 
        count=1
        for msg in message[0]:
            print (count)
            count+=1
            #history_dict.update({msg['user_name']:msg['message']})
            history_dict = history.objects.create(u_id=msg['user_name'], messages=msg['message'], cnl=channel)
        #return history_dict

    def _error(error):
        print(error)
 
    pn.subscribe(channels=channel, callback=_callback)
    pn.history(channel=channel, count=100, callback=_history_callback, error=_error)
    new_message = request.GET.get('msg')
    msg_object = dict(user_name=user_name, message=new_message)
    pn.publish(channel=channel, message=msg_object)
    message_list = history.objects.filter(cnl=channel)
    new_list = []
    time.sleep(40)
    for m in message_list:
        new_list.append({m.u_id:m.messages})
    print (len(new_list))
    history_dict = history.objects.create(u_id=user_name, messages=new_message, cnl=channel)
    new_list.append({user_name:new_message})
    return JsonResponse({'result':new_list})
