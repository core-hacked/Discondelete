import discord
import asyncio
import sys
import argparse
import re
import time

# Set your defaults below, or specify with the respective arguments
prefix = str("#DEL") 
token = str("")
heartbeat = int(86400)
serverpurge =str("#PS") 
nooutput = bool(True)
MessagesToDEL = int()
counter = int(0)

def has_numbers(inputString):
    return bool(re.search(r'\d', inputString))

class MyClient(discord.Client):
    async def delete_message_safe(self, message):
        try:
            await message.delete()
        except discord.errors.HTTPException as e:
            if e.status == 429:  # Rate limit error
                retry_after = e.retry_after  # Discord tells us how long to wait
                print(f"Rate limit hit. Retrying in {retry_after} seconds.")
                await asyncio.sleep(retry_after)  # Wait for the retry_after time before proceeding
            else:
                print(f"Error occurred: {e}")  # Handle other HTTP exceptions

    async def on_message(self, message):
        if(message.author != self.user):
            return
        
        channels = []
        containsnumbers = False
        
        if(message.content == serverpurge):
            channels = message.channel.guild.channels
        elif(prefix in message.content):  # Check if the prefix is present in the message
            tmpStrConv = message.content.replace(prefix, '')
            tmpStrConv = tmpStrConv.strip()
            containsnumbers = has_numbers(tmpStrConv)
            
            if containsnumbers:
                MessagesToDEL = int(str(tmpStrConv))
            channels.append(message.channel)
        else:
            return

        for channel in channels:
            if nooutput == False:
                print(channel)
            
            if containsnumbers:
                try:
                    async for mss in channel.history(limit=MessagesToDEL + 1):
                        if mss.author == self.user:
                            if nooutput == False:
                                print(mss.content)
                            try:
                                await self.delete_message_safe(mss)
                            except Exception as e:
                                if nooutput == False:
                                    print(f"Can't delete message due to: {e}")
                            await asyncio.sleep(2)  # Add a 2-second delay between each deletion to avoid rate limits
                except Exception as e:
                    if nooutput == False:
                        print(f"Can't read history due to: {e}")
            else:
                try:
                    async for mss in channel.history(limit=None):
                        if mss.author == self.user:
                            if nooutput == False:
                                print(mss.content)
                            try:
                                await self.delete_message_safe(mss)
                            except Exception as e:
                                if nooutput == False:
                                    print(f"Can't delete message due to: {e}")
                            await asyncio.sleep(2)  # Add a 2-second delay between each deletion to avoid rate limits
                except Exception as e:
                    if nooutput == False:
                        print(f"Can't read history due to: {e}")

# Create arguments
parser = argparse.ArgumentParser(description='')
parser.add_argument('-t', '--token', dest='token', type=str, help='Token to use with message purger')
parser.add_argument('-p', '--prefix', dest='prefix', type=str, help='Prefix to use with message purger')
parser.add_argument('-s', '--serverpurge', dest='serverpurge', type=str, help='Specify a prefix to use for Server Purge')
parser.add_argument('-b', '--heartbeat', dest='heartbeat', type=int, help='Heartbeat timeout to use')
parser.add_argument('-o', '--output', action='store_true', help='Enable console output of deleted messages (Good for debugging)')
args = parser.parse_args()

# Token
if args.token is not None:
    token = args.token

# Prefix
if args.prefix is not None:
    prefix = args.prefix
else:
    prefix = "#DEL"

# Serverpurge prefix
if args.serverpurge is not None:
    serverpurge = args.serverpurge
else:
    serverpurge = "#PS"

# Heartbeat
if args.heartbeat is not None:
    heartbeat = args.heartbeat
else:
    heartbeat = 86400

# Output
if args.output:
    nooutput = False

else:
    token = input("Please input a Token: ")
    # Prefix
    if args.prefix is not None:
        prefix = args.prefix
    else:
        prefix = input("Please input a prefix (leave blank for the default '#DEL'): ")
        if prefix == "":
            prefix = "#DEL"
    # Serverpurge prefix
    if args.serverpurge is not None:
        serverpurge = args.serverpurge
    else:
        serverpurge = input("Please input a server purge prefix (leave blank for the default '#PS'): ")
        if serverpurge == "":
            serverpurge = "#PS"
    # Heartbeat
    if args.heartbeat is not None:
        heartbeat = args.heartbeat
    else:
        heartbeat = input("Please input a heartbeat timeout (leave blank for the default 86400): ")
        if heartbeat == "":
            heartbeat = 86400
    # Output
    if args.output:
        nooutput = False
    else:
        nop = input("Do you want to log console output? (Y/N): ")
        if nop.lower() in ["", "n", "no"]:
            nooutput = True
        elif nop.lower() in ["y", "yes"]:
            nooutput = False

    print("\nTo delete all messages in one channel, type: " + prefix + " in Discord, \nor delete a set amount of messages by adding a number after the prefix\n")
    print("To delete all messages from the server type: " + serverpurge + " in Discord.")
    if sys.platform == "Darwin" or sys.platform == "darwin":
        print("\nTo stop the program, press " + u"\u2318" + " + C in the console.")
    else:
        print("\nTo stop the program, press CTRL + C in the console.")

# Run the self-bot and await prefix
client = MyClient(heartbeat_timeout=heartbeat, guild_subscriptions=False)
client.run(token)
