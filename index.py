#! /bin/python3

import json
import discord
import asyncio

client = discord.Client()


@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    if message.content.startswith('!test'):
        counter = 0
        tmp = await client.send_message(message.channel, 'Calculating...')
        async for log in client.logs_from(message.channel, limit=100):
            if log.author == message.author:
                counter += 1

        await client.edit_message(tmp, 'You have {} messages.'.format(counter))
    elif message.content.startswith('!sleep'):
        await asyncio.sleep(5)
        await client.send_message(message.channel, 'Done sleeping')

# client.run('NDkyMTMyMTk2NTUyMDE1ODcz.DoR9iQ.kKIhElV__Gal93bGIU3u-vKUBuQ')

with open('config.json', 'r') as jsonFile:
    config = json.load(jsonFile)
    client.run(config['token'])
