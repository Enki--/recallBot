#! /bin/python3

import json
import asyncio
import discord
from tinydb import TinyDB, Query
from recallbotobjects import Member


client = discord.Client()
db = TinyDB('db.json')
membersList = []


@client.event
async def on_ready():
    for server in client.servers:
        for person in server.members:
            User = Query()
            if db.get(User.Name == person) is None:
                membersList.append(Member(str(person), server=server.name))
                db.insert(membersList[len(membersList)-1].toJSON())


@client.event
async def on_member_join(member):
    # need to test this
    membersList.append(Member(str(member.name), server=member.server.name))
    db.insert(membersList[len(membersList)-1].toJSON())


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


def main():
    with open('config.json', 'r') as jsonFile:
        config = json.load(jsonFile)
        client.run(config['token'])


if __name__ == "__main__":
    main()
