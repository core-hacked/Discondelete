import discord
import asyncio
import sys
import argparse

# Set your defaults below, or specify with the respective arguments
prefix = str("#DEL") 
token = str("")
heartbeat = int(86400)
serverpurge =str("#PS") 

class MyClient(discord.Client):
    async def on_message(self, message):
        if(message.author!=self.user):
            return
        channels=[]
        if(message.content==serverpurge):
            channels=message.channel.guild.channels
        elif(message.content==prefix):
            channels.append(message.channel)
        else:
            return
        for channel in channels:
            print(channel)
            try:
                async for mss in channel.history(limit=None):
                # fetch all message, you might want to purge channel by channel to speed up if the server is old and big
                    if(mss.author==self.user):
                        print(mss.content)
                        try:
                            await mss.delete()
                        except:
                            print("Can't delete!\n") # this shouldn't happen unless you call purge multiple time
            except:
                print("Can't read history!\n")         

parser = argparse.ArgumentParser(description='')
parser.add_argument('-t','--token', dest='token', type=str, help='Token to use with message purger')
parser.add_argument('-p','--prefix', dest='prefix', type=str, help='Prefix to use with message purger')
parser.add_argument('-s','--serverpurge', dest='serverpurge', type=str, help='Specify a prefix to use for Server Purge')
parser.add_argument('-b','--heartbeat', dest='heartbeat', type=int, help='Heartbeat timeout to use')
args = parser.parse_args()

token = args.token
prefix = args.prefix
serverpurge = args.serverpurge
heartbeat = args.heartbeat

if token is not None:
    token = args.token
else:
    token = input("Please input a Token: ")
    prefix = input("Please input a prefix (leave blank for the default '#DEL'): ")
    heartbeat = input("Please input a heartbeat timeout (leave blank for the default 86400): ")
    serverpurge = input("Please input a server purge prefix (leave blank for the default '#PS'): ")
    if prefix is None:
        prefix="#DEL"
    if heartbeat is None:
        heartbeat = 86400
    if serverpurge is None:
        serverpurge = "#PS"

if prefix is None:
    prefix = "#DEL"
if serverpurge is None:
    serverpurge = "#PS"
if heartbeat is None:
    heartbeat = 86400


client=MyClient(heartbeat_timeout=heartbeat, guild_subscriptions=False)
client.run(token, bot=False)
