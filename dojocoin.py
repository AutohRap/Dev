# Dojo Coin: Shuffle Party Point System

#Commands and Description:                                      How to use:

#1.?BANK shows personal member coin count                       [?BANK]
#2.?MBOARD (SK admin only) shows monthly leader board           [?MBOARD]
#3.?YBOARD (SK admin only) shows yearly leader board (Jan-Dec)  [?YBOARD]
#4.?CBOARD (SK admin only) shows career leader board            [?EBOARD]
#5.?COIN (S admin only) awards coins                            [?COIN value memberID]
#6.?GARN (S admin only) garnish coinss                          [?GARN value memberID]
#7.?TRANS transfer coins                                        [?TRANS value memberID]
#8.?POT send coins to Dojo Coin Bot for a jackpot               [?POT value]
#9.?SHOPOT view current pot count                               [?SHOPOT]
#10.?JPOT (S admin only) awards member Dojo coin Bot Jackpot    [?JPOT memberID]

#######################################################################################

#Dependencies:

import discord
from discord.ext.commands import bot
from discord.ext import commands
import asyncio
import time

#####################################################

#Definitions:

Client = discord.Client ()
client = commands.Bot (command_prefix = "?")
Mboard = []
Yboard = []
Cboard = []

#####################################################

#Event 1:

@client.event
async def on_ready():

#####################################################
    
    print ("Bot is discord ready!")

#####################################################

#Event 2:
    
@client.event
async def on_message(message):

#####################################################
    
    if message.content.upper().startswith ("?BANK"):
        if "498267433409445909" or "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
#            args = message.content.split (" ")
            file = print(open('coinboard.json').read())
         
            #args[0] = ?BANK
            #args[1] = hey
            #args[2] = there
            await client.send_message(message.channel, "<@%s>" % (userID))
            await client.send_message(message.channel, "%s" % (file))
#            await client.send_message(message.channel, "%s" % (" ".join(args[1:])))
            
            
            
            
#####################################################

    if message.content.upper().startswith ("?MBOARD"):
        if "498235850228891678" or "498236404199849996" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################

    if message.content.upper().startswith ("?YBOARD"):
        if "498235850228891678" or "498236404199849996" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################

    if message.content.upper().startswith ("CBOARD"):
        if "498235850228891678" or "498236404199849996" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################
            
    if message.content.upper().startswith ("?GARN"):
        if "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################

    if message.content.upper().startswith ("?GARN"):
        if "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")
            
######################################################

    if message.content.upper().startswith ("?TRANS"):
        if "498267433409445909" or "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")
            
######################################################
                                                                
    if message.content.upper().startswith ("?POT"):
        if "498267433409445909" or "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################
            
    if message.content.upper().startswith ("?SHOPOT"):
        if "498267433409445909" or "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")

######################################################
            
    if message.content.upper().startswith ("?JPOT"):
        if "498267433409445909" or "498235850228891678" in [role.id for role in message.author.roles]:
            userID = message.author.id
            await client.send_message(message.channel, "<@%s>" % (userID))
            #args = message.content.split (" ")
            #await client.send_message(message.channel, "%s" % (" ".join(args[1:]))
        else:
            await client.send_message(message.channel, "soooo.. this is awkward")
            
######################################################
            
                                       
            

            


client.run("NTA5NTU0MDI1NDQ0ODAyNTYy.DsQpRA.5WqqFnmwMarX3lPh4n5TWtadrNk")
