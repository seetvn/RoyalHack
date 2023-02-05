import os
import discord
from discord.ext import commands
import time_logic as tl
import openai1 as gpt
import csv
import errors
#from keep_alive import keep_alive
dict={}


def run():
  intents = discord.Intents.default()
  intents.message_content = True
  client = commands.Bot(command_prefix='!', intents=intents)

  @client.event
  async def on_ready():
    print(f'Logged in as {client.user}')
    
    
  @client.command()
  async def tri(ctx):
    await client.get_channel(1071503612301299775).send("test")

  @client.command()
  async def ignore(ctx,*users):
    for user in users:
      dict[user]=True
      await ctx.channel.send(f"Will Ignore {user}\n!reinclude [user] to revert")
    print(dict)

  @client.command()
  async def reinclude(ctx,*users):
    for user in users:
      if dict.get(user,None)==True:
        dict[user]=False
        await ctx.channel.send(f"No Longer Ignoring {user}")
  
  @client.command()
  async def summarize(ctx, after, *before):
    channel = ctx.channel
    
    error_message = errors.before_after_errors(before, after)
    if error_message and error_message != "not error":
      await channel.send(error_message)
      return

    after = tl.create_datetime(after)
    if error_message == "not error":
      before = tl.datetime.datetime.now()
    before = tl.create_datetime(before[0])
    
    with open('messages.csv', 'w', newline='') as file:
      writer = csv.writer(file)
      async for message in channel.history(before=before, after=after):
        if message.author == client.user or "!summarize" in message.clean_content or dict.get(message.author.name,None)==True or "!ignore" in message.clean_content or "!reinclude" in message.clean_content:
          continue
        writer.writerow([message.author.name, message.clean_content])
        #await ctx.send(f"[{str(message.created_at)[11:16]}] {message.author.name}: {message.clean_content}")
    text=gpt.summ()
    after = after.strftime('%Y-%m-%d %H:%M')
    before = before.strftime('%Y-%m-%d %H:%M')
    await channel.send(f"TLDR [{after}|||{before}]{text}")
    await client.get_channel(1071503612301299775).send(f"TLDR [{after}|||{before}]{text}")

  #keep_alive()
  client.run(os.environ['DISCORD_BOT_SECRET'])
