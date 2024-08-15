import discord
import random

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

def roll_dice(number_of_rolls, dice_type):
    results = []
    for _ in range(number_of_rolls):
        results.append(random.randint(1, dice_type))
    return results

@client.event
async def on_ready():
    print(f'Bot conectado como {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$rolar'):
        try:
            # Extrai a parte após $rolar
            roll_command = message.content.split('$rolar ')[1]
            # Divide em número de rolagens e tipo de dado
            num_rolls, dice_type = roll_command.split('D')
            num_rolls = int(num_rolls)
            dice_type = int(dice_type)

            if num_rolls > 0 and dice_type in [4, 6, 8, 10, 12, 20, 100]:
                results = roll_dice(num_rolls, dice_type)
                total = sum(results)
                await message.channel.send(f'Rolando {num_rolls}D{dice_type}: {results} (Total: {total})')
            else:
                await message.channel.send('Comando inválido. Use o formato $rolar XDY, onde X é o número de rolagens e Y é o tipo de dado (4, 6, 8, 10, 12, 20, 100).')

        except Exception as e:
            await message.channel.send('Erro no comando. Certifique-se de usar o formato correto: $rolar XDY.')

# Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
client.run('################################')

