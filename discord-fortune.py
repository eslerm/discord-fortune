#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Example Discord Bot

Author: Mark Esler
Date: 2022-02-28

Prints a fortune when "!fortune" is typed into a Discord channel.

Bot requires permission to read and make messages.

Requires fortune command to be installed.
"""

import discord
import subprocess

client = discord.Client()


@client.event
async def on_ready():
    print("We have logged in as {0.user}".format(client))


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("!fortune"):
        out = subprocess.getoutput("fortune")
        print(out)
        await message.channel.send(out)


client.run("secret bot token")
