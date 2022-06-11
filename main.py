from keep_alive import keep_alive
import discord
import random
import os

client = discord.Client()

messages = ["Sla vai procurar saber, parece que sei de algo ?", 
"print('Testa ai') - Simples \U0001F923", "Talvez...", "StackOverflow ele sabe, eu não..",
"Ahhh Sabixão", "Sim com certeza \U0001F61C", "Pergunta pra ele 	\U0001F644"]

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('DevResponde!'):
        await message.channel.send(random.choice(messages))

    if message.content.startswith('D20!'):
        await message.channel.send(random.randint(1, 20))

    if message.content.startswith('Comandos!'):
        await message.channel.send("DevResponde! - Perguntas")
        await message.channel.send("D20! - Dado D20")

keep_alive()

client.run(os.getenv('TOKEN')
