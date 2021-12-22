import discord
import asyncio
import sys
import argparse
import re
# Set your defaults below, or specify with the respective arguments
prefix = str("#DEL")
token = str("")
heartbeat = int(86400)
serverpurge = str("#PS")
nooutput = bool(True)


class MyClient(discord.Client):
    async def on_message(self, message):
        messages_to_delete = -2
        matches = pattern.match(message.content)
        if (message.author != self.user):
            return
        channels = []
        if (message.content == serverpurge):
            channels = message.channel.guild.channels
        elif (message.content == prefix):
            channels.append(message.channel)
        elif (matches):
            #if the user wants to delete X amount of messages
            messages_to_delete = int(matches.group(1))
            if messages_to_delete < 1:
                return
            channels.append(message.channel)
            #also delete the command message
            messages_to_delete += 1
        else:
            return
        for channel in channels:
            counter = 0
            try:
                async for mss in channel.history(limit=None):
                    # fetch all message, you might want to purge channel by channel to speed up if the server is old and big
                    if counter == messages_to_delete:
                        return
                    if (mss.author == self.user):

                        if nooutput == False:
                            print(mss.content)
                        try:
                            await mss.delete()
                            counter += 1
                        except Exception:
                            if nooutput == False:
                                print(
                                    "Can't delete!\n"
                                )  # this shouldn't happen unless you call purge multiple time
            except:
                # if args.nooutput==False:
                print("Can't read history!\n")
        print("DONE")


parser = argparse.ArgumentParser(description='')
parser.add_argument('-t',
                    '--token',
                    dest='token',
                    type=str,
                    help='Token to use with message purger')
parser.add_argument('-p',
                    '--prefix',
                    dest='prefix',
                    type=str,
                    help='Prefix to use with message purger')
parser.add_argument('-s',
                    '--serverpurge',
                    dest='serverpurge',
                    type=str,
                    help='Specify a prefix to use for Server Purge')
parser.add_argument('-b',
                    '--heartbeat',
                    dest='heartbeat',
                    type=int,
                    help='Heartbeat timeout to use')
parser.add_argument(
    '-o',
    '--output',
    action='store_true',
    help='Enable console output of deleted messages (Good for debugging)')
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
        serverpurge = "PS"

# Hearbeat
    if args.heartbeat is not None:
        heartbeat = args.heartbeat
    else:
        heartbeat = 86400

# output
    if args.output == True:
        nooutput = False

else:
    token = input("Please input a Token: ")
    # Prefix
    if args.prefix is not None:
        prefix = args.prefix
    else:
        prefix = input(
            "Please input a prefix (leave blank for the default '#DEL'): ")
        if prefix == "":
            prefix = "#DEL"
# Serverpurge prefix
    if args.serverpurge is not None:
        serverpurge = args.serverpurge
    else:
        serverpurge = input(
            "Please input a server purge prefix (leave blank for the default '#PS'): "
        )
        if serverpurge == "":
            serverpurge = "#PS"
# Heartbeat
    if args.heartbeat is not None:
        heartbeat = args.heartbeat
    else:
        heartbeat = input(
            "Please input a heartbeat timeout (leave blank for the default 86400): "
        )
        if heartbeat == "":
            heartbeat = 86400
# output
    if args.output == True:
        nooutput = False
    else:
        nop = input("Do you want to log console output? (Y/N): ")
        if nop == "" or nop == "n" or nop == "N" or nop == "No" or nop == "NO":
            nooutput = True
        elif nop == "y" or nop == "Y" or nop == "Yes" or nop == "YES":
            nooutput = False

# Run the self-bot and await prefix
#allow select number of messages to be deleted (eg #DEL 5)
pattern = re.compile(r"{} (\+d)".format(prefix))
client = MyClient(heartbeat_timeout=heartbeat, guild_subscriptions=False)
client.run(token, bot=False)
