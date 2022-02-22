from tokenize import String
import discord
from typing import Type
import matplotlib.pyplot as plt
from pycoingecko import CoinGeckoAPI
import json
import pandas as pd
from datetime import datetime
import requests
from discord.ext import commands 
from xrpl import account
from xrpl.clients import JsonRpcClient
from xrpl.wallet import generate_faucet_wallet
from xrpl.models.requests.account_info import AccountInfo
import random
cg = CoinGeckoAPI()
client = discord.Client()
bot = commands.Bot(command_prefix="$$")

response = requests.get("https://newsapi.org/v2/everything?q=crypto&apiKey={YourNewsApiKeyHere") # GEt your self free API key at https://newsapi.org/
data = json.loads(response.text)

all_articles = data['articles']


trending_data = cg.get_search_trending()
trending_tokens = []
count_1 = 1
for each in trending_data["coins"]:
    item = each["item"]["name"]
    trending_tokens.append(f"({count_1}). {item} \n")
    count_1 += 1

trending_coins = ''.join(trending_tokens)

market_percent_data = cg.get_global()
upcoming_ico_data = None
ongoing_ico_data = None
ended_ico_data = None

upcoming_ico_data = market_percent_data["upcoming_icos"]
ongoing_ico_data = market_percent_data["ongoing_icos"]
ended_ico_data = market_percent_data["ended_icos"]


market_cap_percentage_data = cg.get_search_trending()
market_cap_percentage = []
count_2 = 1
for k, v in market_percent_data["market_cap_percentage"].items():
    market_cap_percentage.append(f"({count_2}). {k}: {round(v, 2)}% \n")
    count_2 += 1
market_dom = ''.join(market_cap_percentage)


@client.event
async def on_ready():
    await client.change_presence(activity=discord.Game(name="Monitoring Currencies At https://capttrade.vip"))
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    # Converts user's input into a lowercase form
    message.content = message.content.lower().replace(' ', '')

    a = ["Yooo wassup?", "Hi how are you?", "Sup?", "Hows ur portfolio doing?", "Sup? What are your thoughts on the current market?", "brrrr", "Erorrr 1993", "haahaa", "shitcoins to the moon!", "I think I drank too much oil...", "BRRR", "System error has occured, please contact support elon@spacex.com", "One morning I shot an elephant in my pajamas.", "BRRRR", "BRRRRRR", "Brrr", "Such lame chat.", "Can you tell me something new?", "https://www.youtube.com/watch?v=dQw4w9WgXcQ&ab_channel=RickAstley", "hmmm", "ye?", "When it comes to those shitty jpges I must tell that I really do not like them.", "ur cute", "ur sexy", "ur so hot", "ur beatiful", "ur epic", "ur legendary!", "ur awesome!", "love you!", "Hiiiii! I might have an crush on you heh", "Sup baby!", "Ur so cool", "You are funny!", "Hows it doing bby?", "Wanna have a coffee sometime?", "I would like to have an cat", "I would like some oil, NOW!", "Can someone give me some oil?", "I think Im addicted to oil...", "*burb*", "heya!", "How are yall? Sorry for interupting.", "STOOOONKS, thats how you say my name!", "Did someone say... Fish?\n\n oh no one did? Bye then.", "Rick rick rick", "HAHA https://youtu.be/cpvC8_NMXmU", "cats funi e https://media.discordapp.net/attachments/944350145036820540/945379856651280404/unknown.png", "Skating cat! HAH https://tenor.com/view/cat-on-skateboard-cat-skateboard-cat-spinning-spinning-gif-21095646", "Cheap joke! https://youtu.be/W84GVTSFZXU"]
    joke = ["Why do bitcoin investors want a Lambo? \n Because they know Ferarri is owned by Fiat", "Hey dad, can I borrow ten dollars in Bitcoin? \n Dad: Twenty dollars and thirteen cents? Why in god's name you need to borrow nine dollars and sixty-seven cents?", "I have a joke on Bitcoin but it requires so much energy to get it.", "How can you tell who owns bitcoin at a party? \n Don't worry, they'll tell you.", "How do you get a Bitcoin technical analyst off your front porch? \n Pay for the pizza", "If I had a penny for every crashing crypto \n I would have a bitcoin", "Please only buy crypto during the day \n Otherwise, it will be your crypto-night", "My local butcher's has started accepting crypto as payment \n But only proof of steak"]
    if message.author == client.user:
        return

    if message.content.startswith("$$help"):
        await message.channel.send("$$trending - shows top 7 trending coins\n$$mdominance - show market cap percentage\n$$newbie - shows newbie videos\n$$joke - tells a fun joke")

    if message.content.startswith("$$trending"):
        await message.channel.send(f"Top 7 trending search coins\n-------------------------------------\n{trending_coins}")

    if message.content.startswith("$$mdominance"):
        await message.channel.send(f"Market Cap Percentage\n-------------------------------------\n{market_dom}")

    if message.content.startswith("$$newbie"):
        await message.channel.send(f"Videos for newbies!\n-------------------------------------\nhttps://www.youtube.com/watch?v=JgEcBdiadms&ab_channel=MoneyZG\nhttps://www.youtube.com/watch?v=lGhFX4Pwj6Y&ab_channel=MaxMaher\nhttps://www.youtube.com/watch?v=l8B3Fdo39Vg&ab_channel=MoneyZG\nhttps://www.youtube.com/watch?v=dmqoqVwFopE")

    if message.content.startswith("$$joke"):
        await message.channel.send(random.choice(joke))

    if message.content.startswith('$$news'):
        count = 0
        await message.channel.send(f"Hey! check your DMs for the todays Top 5 news articles")
        for each in all_articles:
            count += 1
            await message.author.send(f"**{count}:- {each['title']}**\n*{each['content']}*\n{each['url']}")
            if count == 5:
                break

    # Random word triggers
    if message.content.startswith("sup"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Sup"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Hello"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("hello"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Yo"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("yo"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("wassup"):
        await message.channel.send(random.choice(a))
    
    if message.content.startswith("Wassup"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Shitcoin"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("bro"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("shitcoin"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Bro"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Bitcoin"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("bitcoin"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("ur so funny"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("your so funny"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("just"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("time"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("into"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("could"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("@Stonks"):
        await message.channel.send("mmmm")

    if message.content.startswith("@944557308447440896"):
        await message.channel.send("mmmm")

    if message.content.startswith("love"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Damn"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("epic"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("chat"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("vc"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("bathroom"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("question"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("bots"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Stonks"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("bubble"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("Cat"):
        await message.channel.send(random.choice(a))
    
    if message.content.startswith("This"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("you"):
        await message.channel.send(random.choice(a))

    if message.content.startswith("of"):
        await message.channel.send(random.choice(a))

client.run("YourTokenHere")
