import discord
import random
import os
from dotenv import load_dotenv
import re

load_dotenv()


intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)


def roll_dice(number_of_rolls, dice_type, modifier=0):
    results = []
    for _ in range(number_of_rolls):
        results.append(random.randint(1, dice_type))
    total = sum(results) + modifier
    return results, total, modifier


@client.event
async def on_ready():
    print(f"Bot conectado como {client.user}")


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$rolar"):
        try:
            # Extrai a parte após $rolar
            roll_command = message.content.split("$rolar ")[1]

            # Usa regex para identificar o padrão de rolagem com possível modificador
            pattern = r"(\d+)D(\d+)([\+\-]\d+)?"
            match = re.match(pattern, roll_command, re.IGNORECASE)

            if not match:
                await message.channel.send(
                    "Comando inválido. Use o formato $rolar XDY ou $rolar XDY+Z, onde X é o número de rolagens, Y é o tipo de dado e Z é o modificador."
                )
                return

            num_rolls = int(match.group(1))
            dice_type = int(match.group(2))

            # Extrai o modificador se existir
            modifier = 0
            if match.group(3):
                modifier = int(
                    match.group(3)
                )  # O operador + ou - já está incluído na string

            if num_rolls > 0 and dice_type in [4, 6, 8, 10, 12, 20, 100]:
                results, total, mod = roll_dice(num_rolls, dice_type, modifier)

                # Formatação da mensagem de resposta com base no modificador
                if mod > 0:
                    mod_text = f"+{mod}"
                elif mod < 0:
                    mod_text = f"{mod}"
                else:
                    mod_text = ""

                await message.channel.send(
                    f"Rolando {num_rolls}D{dice_type}{mod_text}: {results} (Total: {total})"
                )
            else:
                await message.channel.send(
                    "Comando inválido. Use o formato $rolar XDY ou $rolar XDY+Z, onde X é o número de rolagens, Y é o tipo de dado (4, 6, 8, 10, 12, 20, 100) e Z é o modificador."
                )

        except Exception as e:
            await message.channel.send(
                f"Erro no comando. Certifique-se de usar o formato correto: $rolar XDY ou $rolar XDY+Z. Erro: {e}"
            )


# Substitua 'YOUR_BOT_TOKEN' pelo token do seu bot
client.run(os.getenv("TOKEN"))
