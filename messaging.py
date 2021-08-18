#To send offline message or sms to farmer to notify him about intrusion

import time
from datetime import datetime
from twilio.rest import Client

#Credentials of twilio free account 
account_sid = "AC5aad119a940a53f1280daa307db06e0c"
auth_token = 'f6568a8c9df2c94f792c3d9a632162b4'
prov_ph_no = "+19402040142"
my_ph_no = "+919483926103"
client = Client(account_sid, auth_token)

#function to send sms
#sms the animal which is detected by ml model
#also the time of intrusion
def sendMessage(animal_name):
    now = datetime.now()
    cur_time = now.strftime("%H:%M:%S")
    cur_date = now.strftime("%d %B, %Y")
    cur_time_new = float(now.strftime("%H.%M"))
    print(cur_time_new)
    print("Animal - {} has entered your farm at {} on {}".format(animal_name, cur_time, cur_date))
    message = client.messages .create(
                    body =  "Animal - {} has entered your farm at {} on {}".format(animal_name, cur_time, cur_date),
                    from_ = prov_ph_no,
                    to =    my_ph_no)
    print(message.sid)


