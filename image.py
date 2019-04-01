import sys
import os

from telethon import TelegramClient
from telethon.tl.functions.messages import GetFullChatRequest
from telethon.tl.functions.messages import GetHistoryRequest
from telethon.tl.functions.channels import GetChannelsRequest
from telethon.tl.functions.contacts import ResolveUsernameRequest
from telethon.tl.types import PeerUser, PeerChat, PeerChannel
import re
# These example values won't work. You must get your own api_id and
# api_hash from https://my.telegram.org, under API Development.
api_id = 11111  #number
api_hash = 'x'#string
phone = 'x'
client = TelegramClient('session_name', api_id, api_hash,update_workers=1, spawn_read_thread=False)
client.connect()

def callbackUpdate(update):
    channel_name = client.get_entity(PeerChannel(update.message.to_id.channel_id)).username
    if (update.message.message ==''):
        if (channel_name == 'bigpumpsignal'): #name of the telegram channel
            str_date='output'
            client.download_media(update.message,str_date)
            print("Image downloaded!")
            client.disconnect()

# If you already have a previous 'session_name.session' file, skip this.
#me = client.sign_in(phone=phone)
#me = client.sign_in(code=99494)  # Put whatever code you received here.

client.add_update_handler(callbackUpdate)
client.idle()