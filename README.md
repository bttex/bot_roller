# Dice Roller Bot

Este é um bot de Discord simples que permite aos usuários rolar dados virtuais. Ele foi escrito em Python e utiliza a biblioteca discord.py. 

---


### **Requisitos:**

Python 3.8 ou superior

Biblioteca discord.py instalada (pip install discord.py)

---



### **Como usar:**

1.Crie um novo aplicativo no portal de desenvolvedores do [Discord]() ([https://discord.com/developers/applications](https://discord.com/developers/applications)).

2.Crie um novo bot e obtenha o token.

3.Substitua 'YOUR_BOT_TOKEN' no final do código pelo token do seu bot.

4.Adicione o bot ao seu servidor Discord.

5.Inicie o bot executando o arquivo Python.

**Comandos:**

Use o comando $rolar XDY para rolar dados virtuais, onde X é o número de rolagens e Y é o tipo de dado (4, 6, 8, 10, 12, 20, 100). Por exemplo, $rolar 3D6 rolará três dados de seis lados.

---



**Exemplo de Uso:**

``` python
$rolar 2D8
Rolando 2D8: [5, 3] (Total: 8)
```

**Notas:**

O bot só pode ser usado em canais de texto.

O bot não pode rolar dados com um número de rolagens maior que 100.

O bot não pode rolar dados com um tipo de dado diferente de 4, 6, 8, 10, 12, 20, ou 100.

Se você encontrar algum bug ou tiver alguma sugestão, abra um problema no GitHub ([https://github.com/bttex/bot_roller](https://github.com/bttex/bot_roller)).
