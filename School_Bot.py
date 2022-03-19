from lib2to3.pgen2 import grammar
import selenium
from selenium import webdriver
import time
import datetime
from datetime import date
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ActionChains
import schedule
import discord
import random
from discord import channel


intitaltime=time.time()
client = discord.Client()



opt = Options()
opt.add_experimental_option("prefs", { "profile.default_content_setting_values.media_stream_mic":2, 
    "profile.default_content_setting_values.media_stream_camera":2})

TOKEN = 'OTMxMzc0MjEwMzM5NzMzNTk1.YeDf0w.ZVdvTLqQE8MpspX9x1zY9adHYaY'
PATH = '/Users/dakshgupta/Desktop/My work/Python/School Classes/chromedriver'
driver = webdriver.Chrome(PATH)
URL = 'http://teams.microsoft.com'
TOKEN = 'OTMxMzc0MjEwMzM5NzMzNTk1.YeDf0w.ZVdvTLqQE8MpspX9x1zY9adHYaY'


emailid = '****'    #Enter the Mail ID for Microsoft Teams 
password = '****'   #Enter the Password for Microsoft Teams 

@client.event
async def on_ready():
    print('we have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
     username = str(message.author).split('#')[0]
     user_message = str(message.content)
     channel = str(message.channel.name)
     print(f'{username}: {user_message} ({channel})')
     
     if message.author == client.user:
         return

     if message.channel.name == 'online-classes':
         if user_message.lower() == 'lets get started':
            print("Trying to login:")
            driver.get("http://teams.microsoft.com")
            await message.channel.send(f'Opening website')
            driver.get(URL)
            time.sleep(2)



            email=driver.find_element_by_id("i0116")
            email.send_keys(emailid)
            print("EMAIL ID ENTERED")
            await message.channel.send(f'Entered email ID')
            x = 'done'
            time.sleep(1)
            enter=driver.find_element_by_id("idSIButton9")
            time.sleep(1)
            enter.click()
            time.sleep(1)


            passwd=driver.find_element_by_id("i0118")
            passwd.send_keys(password)
            print("PASSWORD ENTERED")
            await message.channel.send(f'Entered password')
            time.sleep(1)
            passbtn=driver.find_element_by_id("idSIButton9")
            passbtn.click()
            time.sleep(1)
            confirmbtn=driver.find_element_by_id("idSIButton9")
            confirmbtn.click()
            time.sleep(8)


            XIAgeneralbtn=driver.find_element_by_id('channel-19:efd35853a70b427fb7215495f331968b@thread.tacv2')
            XIAgeneralbtn.click()
            time.sleep(1)


            if driver.current_url=='https://teams.microsoft.com/_#/school/conversations/General?threadId=19:efd35853a70b427fb7215495f331968b@thread.tacv2&ctx=channel':
                await message.channel.send(f'Login successful')
                time.sleep(1)

            
            def mathschn():
                maths=driver.find_element_by_id('channel-19:19853b6c66554c16987199a45ca26e0a@thread.tacv2')
                maths.click()
                time.sleep(2)
                
            schedule.every().day.at("09:30").do(mathschn)
            await message.channel.send(f'Switching to maths channel')

            '''def mathjoin():
                mathsjoinbt=driver.find_element_by_id('m1642476357483')
                mathsjoinbt.click
                time.sleep(1)

            schedule.every().day.at('9:23').do(mathjoin)
            if schedule.every().day.at('9:23').do(mathjoin) == True:
                await message.channel.send(f'Joining Maths Class')'''


            

            
            

            while True:
                schedule.run_pending()


print('It took', time.time() - intitaltime , 'seconds to run this code')
client.run(TOKEN)
print('CODE COMPLETED')
