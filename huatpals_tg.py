# -*- coding: utf-8 -*-
"""
Created on Tue Feb 15 13:02:20 2022

@author: LEEbo
"""

from telethon import TelegramClient, events
import asyncio
import time

api_id = 'your api id here'
api_hash = 'your api hash here'
user = 'your tg username here'
phone_token = 'your phone number here'

message = '''
your message here
'''

async def main():
   async with TelegramClient(user, api_id, api_hash) as client:
      
      dialogs = await client.get_dialogs()
      # print(dialogs[0])
      
      while True:
          await client.send_message(dialogs[0], message)
          time.sleep(30.1)

      await client.run_until_disconnected()

if __name__ == '__main__':
    asyncio.run(main())